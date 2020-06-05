# Manipulate dir files
import yaml
import sys

# Local libs
from .check_utils import CheckItem

class YAMLParser():
    """
    Class used to load and parse YAML files, both generic or by DS Module
    """


    def __init__(self, threshold_min = 1, threshold_max = 10):
        """
        Sets the minimum and maximum weight thresholds used to load checklists
        Check items with weights not within the thresholds are not loaded
        """
        self.threshold_min = threshold_min if threshold_min >= 1 else 1
        self.threshold_max = threshold_max if threshold_max <= 10 else 10


    def load_module(self, path, swap = None, verbose = False):
        """
        Hold YAML for all the modules

        It receives the path where there is the yaml file,
        check the encoding and load the file. If it has more than one level,
        it verifies in deep by the swapself.

        Args:
            path: Path to the module's YAML file eg.: config/bpg_config/computer_config/anti_malware.yml
            swap: Sub-Title to access within the file. Used for the Anti-Malware exclusively
                eg.: config/bpg_config/anti_malware_configuration.yml scheduled_scan
            verbose: Boolean, return the YAML file's title and description with the list of check items
        Returns:
            checklist: a list of CheckItems
            (CheckList, title): If title
        """
        self.configs = {}
        with open(path, "r", encoding = 'utf-8') as config_file_descriptor:
            config_file = yaml.safe_load(config_file_descriptor.read())
            try:
                keyName = config_file['title']
                if swap != None:
                    self.configs[keyName] = config_file[keyName][swap]
                else:
                    self.configs[keyName] = config_file[keyName]
                
                if verbose:
                    return {
                        "items": self.__create_checklist(),
                        "title": config_file['title'],
                        "description": config_file.get('description', None)
                    }
                else:
                    return {
                        "items": self.__create_checklist()
                    }
            except TypeError:
                return None
            # self.configs[keyName]
            # self.configs[config_file['title']] = config_file[config_file['title']][swap] if swap != None else config_file[config_file['title']]


    def load_file(self, path, only_title = False):
        """
        It receives the path where there is the yaml file,
        check the encoding and load the file.

        Args:
            path: File's path
            only_title: Return only the yaml dict's title

        Returns:
            yaml_dict : Contents of the file as a dict
        """
        yaml_dict = {}
        try:
            with open(path, "r", encoding = 'utf-8') as cfg_fd:
                yaml_dict = yaml.safe_load(cfg_fd.read())
        except OSError as e:
            return False


        return yaml_dict if not only_title else yaml_dict['title']

    def __create_checklist(self):
        """
        Create a dictionary with the module keys and their respective CheckItems

        Returns:
            the final list, to be used by the checkers
        """
        checklist = []

        # Code Refactoring
        for module_checklist in self.configs.values():
            try:
                for attr_path, value in module_checklist.items():
                    if (value['weight'] >= self.threshold_min and value['weight'] <= self.threshold_max):
                        checklist.append(CheckItem(attr_path=attr_path,
                                                    operator=value['operator'],
                                                    operand=value['operand'],
                                                    item_weight=value['weight'],
                                                    description=value['description']
                                        ))
                    elif value['weight'] == 0: continue
                    else:
                        print("An invalid threshold value was selected, \
                        please choose a number between {0} and {1} in {2} found {3}".                                                                                                                           format (self.threshold_min, self.threshold_max, value['description']['failure_item'], value['weight']))
            except:
                continue
        return checklist
