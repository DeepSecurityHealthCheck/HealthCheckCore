import os
import glob
from types import SimpleNamespace # Used to avoid error on checking states
import logging
#import os.path(os.getcwd).data_loader as dl
from .check_utils import CheckResult, run_checklist, CheckList

"""

"""

class Checker(object):
    """
    Attributes:
        parser: instance of YAMLParser
        base_path: path to the YAML with checklists
        include_modules: List of module names to be checked. e.g ["anti_malware","intrusion_prevention"] 
    """
    def __init__(self, path, parser, include_modules):
        """
        Checker constructor.
        Args:
            path: Path for the YAML with the checklists
            parser: Instace of YAMLParser
            config_path: A depth path for join with the template path
        """
        self.parser = parser
        self.base_path = path
        self.include_modules = include_modules

    def build_checklists_dict(self, path, force_include_module=False):
        """
        Build a dict of checklists with the information provided in constructor
        Args: 
            path
            force_include_module: Bool, to include a module even when is not in
                the 'included modules' - To be used by scheduled tasks
        Raises:
            IndexError if wrong key is sent on exclude_modules

        Returns:
            A checklist as {module_name: CheckItem}
        """
        self.checklists = {}
        self.checklist_path = os.path.join(self.base_path, path + "/*.yml")

        self.path_modules = glob.glob(self.checklist_path)

        for path in self.path_modules:
            module_response = self.parser.load_module(path, verbose=True)
            if module_response['title'] in self.include_modules or force_include_module:
                self.checklists[module_response["title"]] = CheckList(items=module_response["items"],title=module_response["title"],description=module_response["description"])

        return self.checklists


    def generic_check(self, target, checklists, options, functions = {}, am_results = None, fw_results = None):
        """
        Generic checker that can be customized, with this function you can send
        options that configure how a given analyse will display(keyName).
        Also you can send callback_functions that run per module or before exit

        Args:
            target: computer/policy object that will be used to extract information
            checklists: Dictionary of type {'key':CheckList}
            options: options for analyse, for now only {'keyName': <name>}
            functions: A dictionary with a list of functions that will be executed per module
                       or before exit analysis
            am_results: am_results for correlation analysis
            fw_results: fw_results for correlation analysis
            
        """

        callbacks_per_module = functions.get('per_module', None)
        callbacks_before_exit = functions.get('before_exit', None)
        analyse_result = {}

        analyse_result['total'] = CheckResult(0,0,[])
        analyse_result[options['keyName']] = getattr(target, options['keyName'])
    

        State = SimpleNamespace(state='on') # Schedule task dont have this attr

        for module_name, check_list in checklists.items():

            result = run_checklist(target, check_list.items, return_failures = True, logger=logging.getLogger())

            analyse_result[module_name] = result
                
            if module_name == 'anti_malware':
                self.anti_malware_correlation(target, analyse_result, am_results)

            elif module_name == 'firewall':
                self.firewall_correlation(target, analyse_result, fw_results)
        
            if getattr(target, module_name, State).state == 'off':
                result.curr_score = 0
                result.conformity_rate = 0

            """
            Its execute each callback function provided per module analysis
            """
            if callbacks_per_module != None:
                for f in callbacks_per_module:
                    f({'result': result, 'module_name': module_name, 'analyse_result': analyse_result})

            analyse_result['total'] += result
            
        if callbacks_before_exit != None:
            for f in callbacks_before_exit:
                f({'analyse_result': analyse_result})

        return analyse_result


    def anti_malware_correlation(self, target, obj, am_results):
        """
        Correlates the AM Config ids assigned to a computer with the
        Check Results for the AM Configs, present in the am_results

        Args:
            target: Computer SDK instance
            am_results: Dict of {AM_Config_ID : AntiMalwareCheckResults}
        Returns:
            -

        Raises:
            -

        """
        # Correlation with analysis of Anti-Malware & Firewall configs
        scan_configuration_ids = { "manual"     :target.anti_malware.manual_scan_configuration_id,
                                   "scheduled"  :target.anti_malware.scheduled_scan_configuration_id,
                                   "real_time"  :target.anti_malware.real_time_scan_configuration_id}

        # Uses key name to find attr in AntiMalware class and ID as value
        for attr_name, scan_id in scan_configuration_ids.items():

            #Mostly for rule id 0 (no rule), but you never know...
            if not scan_id in am_results.keys():
                continue

            am_result = getattr(am_results[scan_id], attr_name)
            if am_result == None:
                got_str = "real-time" if am_results[scan_id].real_time != None else "manual/scheduled"
                logging.error("AM scan type mismatch: computer id: {}\tscan id: {}\tgot: {}\texpected: {}".format(target.id,scan_id,got_str,attr_name))
                continue
            obj['anti_malware'] += am_result


    def firewall_correlation(self, target, obj, fw_results):
        """
        Correlates the Firewall Stateful Configuration ids assigned to a
        computer (both globally and by interface) with the Check Results for
         the Stateful Configs, present in the fw_results

        Args:
            target: Computer SDK instance
            am_results: Dict of {Stateful_Configuration : CheckResult}
            obj: CheckResult of the target
        Returns:
            -

        Raises:
            -

        """
        global_firewall_id = target.firewall.global_stateful_configuration_id
        fw_configuration_total = CheckResult(0,0,list())

        #Each computer may or may not have a global stateful configuration
        #The global is the 'default' config for the interfaces
        if global_firewall_id != None:
            fw_configuration_total += fw_results[global_firewall_id]

        #Each interface however may be assigned with a different stateful
        #configuration
        if target.firewall.stateful_configuration_assignments != None:
            for interface_rule in target.firewall.stateful_configuration_assignments.stateful_configuration_assignments:
                fw_configuration_total += fw_results[interface_rule.stateful_configuration_id]

        obj['firewall'] += fw_configuration_total
