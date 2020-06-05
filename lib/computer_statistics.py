# Manipulate dir files
import os
import glob
import logging
from tqdm import tqdm
from .check_utils import run_checklist
from .check_utils import CheckResult
from .yaml_parser import YAMLParser
from deepsecurity import Computer
from pprint import pprint


def inc_count_and_percentage(dict_to_inc=None,key=None,increment=0,max_items=0):
    """
    Increments the count and percentage to a dict of type
    {'key':{'count':0,'percentage':0}}

    Args:
        dict_to_inc: Dictionary in question
        key:
        increment: Amount to increment
        max_items: Max number of items
    Raises:

    Returns:
    """
    if dict_to_inc == None:
        raise TypeError("dict is None")
    
    dict_to_inc.setdefault(key, {"count":0,"percentage":0})
    dict_to_inc[key]["count"] += increment

    for v in dict_to_inc.values():
        if max_items == 0:
            v["percentage"] = 0
        else:
            v["percentage"] = 100 * ( v["count"]/max_items )

class DeploymentScenario():
    """
    Class used to store Information for the computers in a given
    Deployment Scenario
    """
    def __init__(self, name):
        self.name = name
        self.status_count = {
            'inactive' : 0,
            'active': 0,
            'warning': 0,
            'error': 0,
            'not-supported': 0
        }
        self.num_computers_scenario = 0
        self.num_managed_computers = 0
        self.environment_percentage = 0
        self.result = CheckResult(0,0,[])

    def to_dict(self):
        return{
            "name":self.name,
            "status_count":self.status_count,
            "num_computers_scenario":self.num_computers_scenario,
            "environment_percentage":self.environment_percentage,
            "result":self.result
        }

    def inc_status_count(self, computer, result=None):
        """
        Increment count of computers with a given status
        """

        #Sanity check against invalid status key


        if computer.agent_finger_print is not None or computer.appliance_finger_print is not None:
            self.num_managed_computers += 1

        if computer.computer_status.agent_status is None:
            computer.computer_status.agent_status = computer.computer_status.appliance_status
        # if computer.computer_status.agent_status not in self.status_count.keys():
        #     logging.error("Unknown agent status: computer id: {} agent status '{}'".format(
        #         computer.id,computer.computer_status.agent_status))
        #     return

        # #Sanity check against unmanaged computer with active status
        # if computer.computer_status.agent_status != 'inactive' and computer.agent_finger_print == None:
        #     logging.error("Unmanaged computer not inactive: computer id: {} agent status '{}'".format(
        #         computer.id,computer.computer_status.agent_status))
        #     return
            
        self.status_count[computer.computer_status.agent_status] += 1
        self.num_computers_scenario += 1
        if result is not None:
            self.result += result

    def set_environment_percentage(self, num_computers):
        """
        Sets the percentage that the deployment scenario represents on the
        environment, using the total number of computers
        """
        self.environment_percentage = round(100 * (self.num_computers_scenario / num_computers),1)

    def __str__(self):
        x = str(self.name) + "\n"
        x += str("Status Count{}".format(self.status_count)) + "\n"
        x += str("Total in scenario " + str(self.num_computers_scenario)) + " : " + str(self.environment_percentage) + " % of env\n"
        x += str("Conf Rating " + str(self.result.conformity_rate)) + "\n"
        return x


    def __iadd__(self,other):
        self.num_computers_scenario += other.num_computers_scenario
        self.environment_percentage += other.environment_percentage

        for k in self.status_count.keys():
            self.status_count[k] += other.status_count[k]

        self.result += other.result
        return self
#===============================================================================



#===============================================================================
class ComputerStatisticsGetter(object):

    def __init__(self,computer_list, modules_to_check , computer_groups, computer_results, module_results, policies_results):
        if computer_list is None:
            raise TypeError("computer_list is of type None")

        #Number of computers (managed and unmanaged)
        self.num_computers = len(computer_list)
        self.managed_computer_list = list(filter(lambda x: x.agent_finger_print is not None or x.appliance_finger_print is not None,computer_list))
        #Number of deployed Agents
        self.num_managed_computers = len(self.managed_computer_list)
        self.unmanaged_computer_list = list(filter(lambda x: x.agent_finger_print is None and x.appliance_finger_print is None,computer_list))
        self.num_unmanaged_computers = len(self.unmanaged_computer_list)

        #Sanity Checking
        if(self.num_managed_computers+self.num_unmanaged_computers != self.num_computers):
            err_str = "# of Agents: {} + # of Unmanaged: {} != # of total {} ".format(self.num_managed_computers,self.num_unmanaged_computers,self.num_computers)
            logging.error(err_str)
            raise ArithmeticError(err_str)

        self.computer_results = computer_results
        self.computer_groups = computer_groups
        self.module_results = module_results
        self.modules_to_check = modules_to_check
        self.agent_deployment_scenarios = {
            'aws': DeploymentScenario("AWS"),
            'azure':DeploymentScenario("Azure"),
            'gcp':DeploymentScenario("GCP"),
            'on-premise':DeploymentScenario("On-Premise"),
            #Total is to be incremented after populating the other scenarios
        }
        self.overall_agent_deployment = DeploymentScenario("Total")

        self.fully_conformant_modules_count = {}
        self.agent_operating_system = {}
        self.agent_release = {}

        #Dictionary of policies ids
        self.module_deployment_count={}
        #tuple list as [(computer_id, CheckResult)]
        self.policies_results = policies_results
        self.mapped_policies = {}
        self.get_computer_statistics()
       

    def get_computer_statistics(self):
        """
        Raises:

        Returns:
        """

        """
        Computer group dict. Each ComputerGroup will store the sum of CheckResults
        for each computer in a new group_check_results attribute
        """
        self.computer_results_ordered = sorted(self.computer_results.items(), key=lambda v: v[1]['total'].curr_score)
        self.computer_groups_ordered = sorted(self.computer_groups.items(), key=lambda v: v[1]['total'].curr_score)

        for module_name in self.modules_to_check:
            self.module_deployment_count[module_name] = 0
            self.fully_conformant_modules_count[module_name] = 0

        with tqdm(total=self.num_computers, ascii=True, desc="Calculating Computer Statistics") as pbar:            
            for managed_computer in self.managed_computer_list:
                pbar.update(1)

                inc_count_and_percentage(dict_to_inc=self.agent_operating_system,key=managed_computer.platform,
                    increment=1,max_items=self.num_managed_computers)
                self.__inc_agent_release(managed_computer.agent_version)
                self.__inc_agent_deployment_scenario(managed_computer, self.computer_results[managed_computer.id]['total'])

                ### TODO: Increment module deployment
                for module_name in self.modules_to_check:
                    #Module deployment
                    if getattr(managed_computer, module_name)._state != 'off':
                        self.module_deployment_count[module_name] += 1
                    #Fully Compliant
                    if self.computer_results[managed_computer.id][module_name].max_score == self.computer_results[managed_computer.id][module_name].curr_score:
                        self.fully_conformant_modules_count[module_name] += 1
                
                if managed_computer.policy_id in self.policies_results: # sanity check
                    self.mapped_policies.setdefault(managed_computer.policy_id, {
                        'name': self.policies_results[managed_computer.policy_id]['name'],
                        'computers_using': [],
                        'total': self.policies_results[managed_computer.policy_id]['total']
                    })

                    self.mapped_policies[managed_computer.policy_id]['computers_using'].append(managed_computer.id) #= computer.id #self.computer_results[computer.id]['total']
            
            for unmanaged_computer in self.unmanaged_computer_list:
                pbar.update(1)
                self.__inc_agent_deployment_scenario(unmanaged_computer, None)

            for value in self.agent_deployment_scenarios.values():
                value.set_environment_percentage(self.num_computers)
                self.overall_agent_deployment += value

        # That way we dont lost the capability to fast search using computer_id :setdefault)
        #print(computer_groups.items())

        #sort_function_group = lambda v: v[1]['total'] if v[1].get('results', None) else 0
        #print(computer_groups_ordered)

    def __inc_agent_deployment_scenario(self,computer, result=None):
        """
        Increment deployment scenerario counter
        Args:
            computer for extract scenario, Check Result for the computer
        Raises: -
        Returns: -
        """
        scenario_key='on-premise'
        try:
            if computer.azure_arm_virtual_machine_summary or computer.azure_vm_virtual_machine_summary:
                #azure
                scenario_key='azure'
            elif computer.ec2_virtual_machine_summary :
                #aws
                scenario_key='aws'
            elif computer.gcp_virtual_machine_summary:
                #gcp
                scenario_key='gcp'
        except Exception as e:
            print("Some of the scenario_keys were not available: {}".format(str(e)))
        self.agent_deployment_scenarios[scenario_key].inc_status_count(computer,result)


    def __inc_agent_release(self,agent_version):
        """
        Increment agent release getting only the first 3 values
        Args:
            self.agent_release dict
            agent_version to be truncated
        """
        agent_version = '.'.join(agent_version.split('.')[:-1])
        inc_count_and_percentage(self.agent_release,agent_version,1,self.num_managed_computers)


    def get_items_by_range(self,ordered_list ,start = 0, until = 0):
        """
        Return a specific range (slice) on a ordered list
        Args:
            ordered_list: Source of the items
            start: Where to start
            Until: Where to stop
        Raises:
            IndexError if wrong start/until was sent

        Returns:
            tuple list as [(computer_id, CheckResult)]
        """
        until = max(min(len(ordered_list),until),0)
        start = max(min(len(ordered_list),start),0)
        #if until > len(computers_results) or until - start < 0:
            #raise IndexError("Invalid start or end size!")

        return ordered_list[start:until]



    def get_mapped_policies(self):
        return self.mapped_policies

    def get_bundle(self):
        return {
            "agent_deployment_scenarios":self.agent_deployment_scenarios,
            "overall_agent_deployment":self.overall_agent_deployment,
            "agent_operating_system":self.agent_operating_system,
            "agent_release":self.agent_release,
            "num_computers": self.num_computers,
            "num_managed_computers": self.num_managed_computers,
            "module_deployment_count":self.module_deployment_count,
            "fully_compliant_modules_count": self.fully_conformant_modules_count,
            "least_conforming_computers": self.get_items_by_range(self.computer_results_ordered,until=20),
            "top_ten_computers_groups": self.get_items_by_range(self.computer_groups_ordered,until=10),
            "mapped_policies": self.mapped_policies
        }
