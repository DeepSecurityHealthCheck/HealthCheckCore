from .check_utils import run_checklist
from .check_utils import CheckResult

from tqdm import tqdm

"""
    This class is used to analyse policies configurations that are retrieved by API
    this need receive a checker module that are used to analyse the checklists
"""


class PolicyChecker(object):
    """
    Attributes:
        checker: Checker class instance for use generic checker
        checklists: Checklist built on checker
        policy_results: Each policy analysed organized as { id: results}
        policies_average: Avegare of all the policies
        policies_num: Number of policies
        scan_dict: Dicionary with all policies used that need be analyzed
    """
    def __init__(self, checker, policies = None, am_results = None, fw_results = None, scan_dict = {}):
        """
        Policy checker constructor.

        Args:
            checker: Checker instance
            policies: raw policies objects retrieved by API!
            am_results: list of all anti-malware analysis
            fw_results: list of all firewall analysis
            scan_dict: Dicionary with all policies used that need be analyzed
        Raises:

        Returns:
        """
        self.checker = checker
        self.checklists = checker.build_checklists_dict(path="policies_config")
        self.policy_results = {}
        self.policies_average = CheckResult(0,0,[])
        self.policies_num = 0
        self.scan_dict = scan_dict
        if policies != None:
            self.policies_checker(policies, am_results, fw_results)


    def policies_checker(self, policies, am_results = None, fw_results = None):
        self.policy_results = {}
        self.policies_num = len(policies)
        callbacks = {"before_exit": []}
        inc_average = lambda x: self.__inc_average(x['analyse_result']['total'])
        callbacks['before_exit'].append(inc_average)

        options = {
            "keyName": "name"
        }
        with tqdm(total=self.policies_num, ascii=True, desc="Checking Policies configs") as pbar:
            for policy in policies:
                pbar.update(1)
                if policy.id in self.scan_dict:
                    self.policy_results[policy.id] = self.checker.generic_check(policy, self.checklists, options,callbacks, am_results=am_results, fw_results=fw_results)

        self.policy_results_ordered = sorted(self.policy_results.items(), key=lambda v: v[1]['total'].curr_score)


    def get_ordered_policy_results(self):
        return self.policy_results_ordered


    def get_policy_results_by_range(self, start=0, until=0):
        until = max(min(len(self.policy_results_ordered),until),0)
        start = max(min(len(self.policy_results_ordered),start),0)
#        if until > len(self.policies_rezasults_ordered) or until - start < 0:
#            raise IndexError("Invalid start or end size!")

        return self.policy_results_ordered[start:until]

    def __inc_average(self, average):
        self.policies_average += average

    def get_average(self):
        """
        Args:
        Raises:

        Returns:

        """
        return self.policies_average

    def get_bundle(self):
        """
        Returns all the raw data collected from the computer_checker

        Args: -
        Raises: -
        Returns:
            dictionary with all analysis results
        """
        return {
            "policies_average_conformity" : self.get_average().conformity_rate,
            "top_ten_worst_policies": self.get_policy_results_by_range(until=10),
            "policies_results":self.policy_results
        }
