# Manipulate dir files
import os
import glob
from tqdm import tqdm
from .check_utils import run_checklist
from .check_utils import CheckResult
from .yaml_parser import YAMLParser
from deepsecurity import Computer
from pprint import pprint


class ScheduledTaskChecker(object):


    def __init__(self, checker, scheduled_tasks, computers, computer_groups, policies_mapped):

        """
        ScheduledTask constructor.

        Args:
            checker: GenericChecker instance
            path: Path to the analysis template
            computers: List of all computers in the environment
            computer_groups: Dict of all computer groups and their respective computers {id:{"name": ..., "results": {computer_id:...}... , "total":CheckResult}}
            policies_mapped: Dict of all policies in use and their respective computers {id:{"name": ..., "results": {computer_id:...}... , "total":CheckResult}}
        Raises:

        Returns:
        """
        self.checker = checker
        self.checklists = self.checker.build_checklists_dict(path="scheduled_tasks_config",force_include_module=True)
        self.scheduled_tasks_results={}

        self.computers = computers
        self.computer_groups = computer_groups
        self.policies_mapped = policies_mapped

        self.check_scheduled_tasks(scheduled_tasks)

    def check_scheduled_tasks(self, scheduled_tasks):
        """
        #Loads all checklists in the "conformity_standards/<selected standard>/scheduled_tasks_config
        #Runs checks for all scheduled_tasks according to the Checklist of the same type 
        """
        options = {
            "keyName": "name"
        }
            
        for task_type in self.checklists.keys():
            
            self.scheduled_tasks_results.setdefault(task_type,{"enabled_tasks":{}})
            
            task_type_has_computer_filter = False  
            #Task HAS Computer Filter 
            if task_type not in ["synchronize-vcenter","synchronize-directory","synchronize-cloud-account",
            "run-script","send-alert-summary","discover-computers" ] :
                task_type_has_computer_filter = True
                self.scheduled_tasks_results[task_type]["computers_in_filter"] = []

            #Get all ENABLED tasks of the current Type
            filtered_tasks = list(filter(lambda x:x.type==task_type and x.enabled , scheduled_tasks))
            
            for task in filtered_tasks:
                self.scheduled_tasks_results[task_type]["enabled_tasks"][task.id] = self.checker.generic_check(task,{task_type:self.checklists[task_type]},options)
                if not task_type_has_computer_filter:
                    pass

                #Scheduled task is in conformity,  
                if self.scheduled_tasks_results[task_type]["enabled_tasks"][task.id]["total"].conformity_rate == 100:                 
                    computer_filter = self._get_computer_filter_from_task(task, task_type)
                    self.scheduled_tasks_results[task_type]["computers_in_filter"] += self._get_computers_in_filter(computer_filter)

            self.scheduled_tasks_results[task_type]["computers_in_filter"] = list(set(self.scheduled_tasks_results[task_type]["computers_in_filter"]))
            self.scheduled_tasks_results[task_type]["checklist_description"] = self.checklists[task_type].description

    def _get_computer_filter_from_task(self,task, task_type):
        """
        gets the instance of ComputerFilter inside an instance of ScheduledTask by a given type
        args:
            task: Instance of ScheduledTask
            task_type: String that gives the type of Scheduled Task - Consult the API docs
        returns:
            instance of ComputerFilter, if the task has a 'task_type'_task_parameters attribute
        raises:

        """
        mod_type = task_type.replace("-","_")
        try:
            task_params = getattr(task,mod_type+"_task_parameters")
            return task_params.computer_filter
        except:
            return None

    def _get_computers_in_filter(self,computer_filter):
        """
        Gets the list of computer ids being covered by a given computer_filter

        args:
            computer_filter: Instance of ComputerFilter
        
        returns: List of ints, empty list if no computer is being covered
        """
        if computer_filter.type == "computer":
            return [computer_filter.computer_id]
        elif computer_filter.type == "all-computers":
            return list(c.id for c in self.computers)
        elif computer_filter.type == "computers-in-group" or computer_filter.type == "computers-in-group-or-subgroup":
            try: #Group populated by computers
                return list(self.computer_groups[computer_filter.computer_group_id]["results"].keys())
            except:
                return []
        elif computer_filter.type == "computers-using-policy" or computer_filter.type == "computers-using-policy-or-subpolicy":    
            try: #A Policy being used by computers
                return list(self.policies_mapped[computer_filter.policy_id]["results"].keys())
            except:
                return []
        else:
            return []

    def get_bundle(self):
        """
        Returns all the raw data collected from the computer_checker

        Args: -
        Raises: -
        Returns:
        A dict of type 
        {scheduled_task_type_string : {
            enabled_tasks {
                scheduled_task_id : {
                    "name of Check List for that type of scheduled task ": CheckResult
                    "total": CheckResult
                },
                
                ....
            }
            "checklist_description" : Description of the checklist
            #List of computer IDs affected by that task type - only exists if the task type has a ComputerFilter 
            "computer_in_filter": [] 
        ....,
        }
        """
        return {
            "scheduled_tasks_results" :  self.scheduled_tasks_results
        }
