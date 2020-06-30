# Manipulate dir files
import os
import glob
from tqdm import tqdm
from .check_utils import run_checklist
from .check_utils import CheckResult
from .yaml_parser import YAMLParser
from deepsecurity import Computer
from pprint import pprint


class ComputerChecker(object):
    """
    Attributes:
        parser: instance of YAMLParser
        base_path: path to the YAML with checklists
        checklist: Lists of CheckItems built from the YAML files
        module_results: Dict of { module_name: CheckResult } containing the MODULE'S average of all computers
        computer_results: Dict of {computer_id : { module_name : CheckResult } }

    """

    def __init__(self, checker ,computer_list=None, modules_to_check=None ,computers_group = None, am_results = None, fw_results = None):
        """
        ComputerCheck constructor.

        Args:
            yParser: YAMLParser instance
            path: Path to the analysis template

            computer_list: List of computers to be checked. if this arg is not None, the __init__ will run check_computers
            modules_to_check: List of module names to be checked
            am_results: list of all anti-malware analysis
            fw_results: list of all firewall analysis
            computer_groupss: Dict of all computer groups {id:{"name":computer_groups.name}}
        Raises:

        Returns:
        """

        self.checker = checker
        self.checklists = self.checker.build_checklists_dict(path="computer_config")

        self.environment_issues = []
        self.module_results = {}
        self.module_results['total'] = CheckResult(0,0,[])
        self.used_policies = {}
        #Increment 'deployed' in the big for loopself.

        ## COMBAK: set "valid" as a parameter
        self.computer_results = {}

        """
        Computer group dict. Each ComputerGroup will store the sum of CheckResults
        for each computer in a new group_check_results attribute
        """
        self.computer_groups = {group.id:{"name":group.name} for group in computers_group.computer_groups}
        self.computer_groups_ordered = ()

        for module_name in modules_to_check:
            self.module_results[module_name] = CheckResult(0,0,[])
        if computer_list != None:
            self.check_computers(computer_list, am_results, fw_results)

    def check_computers(self, computer_list, am_results = None, fw_results = None):
        """
        Runs all checklists for each computer. Stores the dict of computers and
        the checkresults for each checklist in self.computer_results

        Args:
            computer_list: list of all computers objects
            am_results: list of all anti-malware analysis
            fw_results: list of all firewall analysis

        Raises:
            -
        Returns:
            -
        """


        """
        Callbacks functions for checker, lambda is used to be more compact and faster.
        but you can used def instead
        """
        self.computer_results = {}
        self.num_computers = len(computer_list)

        callback_functions = {}
        callback_functions['per_module'] = []
        callback_functions['before_exit'] = []

        inc_env_issues      = lambda x: self.__inc_env_issues(x['result'].failed_items)
        inc_module_average  = lambda x: self.__inc_average(x['result'], x['module_name'])

        callback_functions['per_module'].append(inc_env_issues)
        callback_functions['per_module'].append(inc_module_average)

        options = {
            "keyName": "host_name"
        }

        

        managed_computers = list(filter(lambda x: x.agent_finger_print != None or x.appliance_finger_print != None,computer_list))

        with tqdm(total=len(managed_computers), ascii=True, desc="Checking Managed Computers") as pbar:

            for computer in managed_computers:
                pbar.update(1)
                self.computer_results[computer.id] = self.checker.generic_check(computer, self.checklists, options, callback_functions, am_results, fw_results)
                self.used_policies.setdefault(computer.policy_id, None)

                #IN CASE NO EXISTING COMPUTER GROUP
                if computer.group_id not in self.computer_groups:
                    continue
                self.computer_groups[computer.group_id].setdefault('results', {})
                self.computer_groups[computer.group_id].setdefault('total', CheckResult(0,0,[]))

                self.computer_groups[computer.group_id]['total'] += self.computer_results[computer.id]['total']
                self.computer_groups[computer.group_id]['results'][computer.id] = self.computer_results[computer.id]


        # Filtering unused computers group
        # We cant change dict using iterators, thats why we get a list of keys
        for group_id in list(self.computer_groups.keys()):
            if not self.computer_groups[group_id].get('results', None):
                del self.computer_groups[group_id]
        # There is a better way to do this, but we goota boot fast

        self.environment_issues = list(set(self.environment_issues))

    def __inc_average(self, inc, module_name):
        """
        Increment average of a given module

        Args:
            ChecResult for increment
            Key name for increment

        Raises:

        Returns:
        """
        self.module_results[module_name] += inc
        self.module_results['total'] += inc

    def __inc_env_issues(self, failed_items):
        """
        Incresse environment issues
        Args:
            Failed items on run_checklist
        Raises: -
        Returns: -
        """
        self.environment_issues += failed_items

    def get_average(self, raw=False):
        """
        Get method for module_results

        Args:
        Raises:

        Returns:
            module_results dictionary as
            { module_name: CheckResult }
        """
        return self.module_results['total'] if not raw else self.module_results


    def get_environment_issues(self):
        """
        Returns all environment issues in a list of checkItems

        Args: -
        Raises: -
        Returns:
            [CheckItems]
        """
        return self.environment_issues

    def get_used_policies(self):
        """
        Return a dictionary of used policies by the computers
        Args:
        Return: Dictionary of policies
        """
        return self.used_policies

    def get_bundle(self):
        """
        Returns all the raw data collected from the computer_checker

        Args: -
        Raises: -
        Returns:
            dictionary with all analysis results
        """
        return {
            "computers_average_conformity" : self.get_average().conformity_rate,
            "module_results":self.module_results,
            "issues": self.environment_issues,
            "computer_results" : self.computer_results,
            "computer_groups"  : self.computer_groups
        }
