import deepsecurity
import sys, warnings
import urllib3
#TODO REMOVE THIS IMPORT
from lib.yaml_parser import YAMLParser
from colorama import init, Fore
import yaml
import os
init(autoreset=True)

class Api_Loader(object):
    """docstring for Api_Loader."""
    def __init__(self):
        self.api_config = deepsecurity.Configuration()
        self.api_version = ''

        self.API_CONFIG_PATH = "config/api_config.yml"
        self.MAX_RETRY_ERROR_MSG = "ERROR: Failed to establish connection - Make sure the hostname is correct"
        self.MAX_ITEMS_PER_PAGE = 1000 #Up To 5000

        expand_options = deepsecurity.Expand()
        expand_options.add(
            # deepsecurity.Expand.anti_malware,
            # deepsecurity.Expand.application_control,
            # deepsecurity.Expand.firewall,
            # deepsecurity.Expand.web_reputation,
            # deepsecurity.Expand.log_inspection,
            # deepsecurity.Expand.integrity_monitoring,
            # deepsecurity.Expand.intrusion_prevention,
            # deepsecurity.Expand.computer_settings,
            # deepsecurity.Expand.computer_status,
            # deepsecurity.Expand.ec2_virtual_machine_summary,
            # deepsecurity.Expand.azure_arm_virtual_machine_summary,
            # deepsecurity.Expand.azure_vm_virtual_machine_summary,
            # deepsecurity.Expand.gcp_virtual_machine_summary
            deepsecurity.Expand.all
        )
        self.COMPUTER_EXPAND = expand_options.list()


        search_criteria = deepsecurity.SearchCriteria()
        search_criteria.id_value = 0
        search_criteria.id_test = "greater-than"
        self.SEARCH_FILTER = deepsecurity.SearchFilter(max_items=self.MAX_ITEMS_PER_PAGE, search_criteria=search_criteria)

        #Turns off warnings unless specified
        if not sys.warnoptions:
    	       warnings.simplefilter("ignore")


        file_config = dict()

        try:
            with open(self.API_CONFIG_PATH, "r", encoding = 'utf-8') as cfg_fd:
                file_config = yaml.safe_load(cfg_fd.read())

            if file_config is None:
                file_config = dict()


        
            self.api_config.host = file_config["host"]
            self.api_config.api_key['api-secret-key'] = file_config["api-secret-key"]
            self.api_version = file_config["api-version"]

            if not "https://" in self.api_config.host:
                self.api_config.host = "https://"+self.api_config.host
        except Exception as e:
            print(Fore.LIGHTRED_EX + "Error while loading the config/api_config.yml file, resetting it...")
            try:
                os.makedirs("config")
            except Exception as e:
                pass

        try:
            if "host" not in file_config or file_config["host"] == "https://<Your DSM Hostname or IP>:<DSM Port>/api" or \
                "api-secret-key" not in file_config or file_config["api-secret-key"] == "" or "api-version" not in file_config:
                print(Fore.LIGHTRED_EX+"CONFIG FILE NOT SET!")
                print("{}Insert the DSM host (link) following this example {}[{}https://{}<Your DSM Hostname or IP>{}:{}<DSM Port if on-premise>{}/api{}]".
                format(Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX,Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX,Fore.LIGHTWHITE_EX,Fore.LIGHTRED_EX,Fore.LIGHTMAGENTA_EX,Fore.LIGHTWHITE_EX))
                self.api_config.host = input("Inset the DSM Host: ").rstrip().lstrip()
                file_config["host"] = self.api_config.host
                if self.api_config.host == "":
                    raise TypeError("Empty Host Configuration is NOT VALID")

                print(Fore.LIGHTCYAN_EX + "Insert the secret key for the API (Check the documentation if lost)")
                self.api_config.api_key['api-secret-key'] = input("Inset the Api Secret key: ").rstrip().lstrip()
                file_config["api-secret-key"] = self.api_config.api_key['api-secret-key']
                if self.api_config.api_key['api-secret-key'] == "":
                    raise TypeError("Empty key Configuration is NOT VALID")

                self.api_version = "v1"
                file_config["api-version"] = self.api_version

                print(Fore.LIGHTGREEN_EX + "Saving to config/api_config.yml (you can modify the info here)")
                try:
                    with open(self.API_CONFIG_PATH, "w+") as config:
                        yaml.dump(file_config,config, default_flow_style=False)
                except Exception as e:
                    print("Could not save configs to file, you will have to type them again later")
        
        except Exception as e:
            raise IOError("Corrupted api_config, please re download the file: " + str(e))

        
        if self.api_config.host is None or self.api_config.api_key is None or self.api_version is None:
            raise TypeError( ("API Configuration values on {} are NOT VALID".format(self.API_CONFIG_PATH)))


    def request_computers(self):
        """Returns a list with all computers in the DS environment"""

        computers_list = []
        api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(self.api_config))
        try:
            while True:
                paged_response = api_instance.search_computers(self.api_version,
                    expand=self.COMPUTER_EXPAND, overrides=False, search_filter=self.SEARCH_FILTER)
                computers_list+=paged_response.computers
                last_id = computers_list[-1].id
                self.SEARCH_FILTER.search_criteria.id_value = last_id

                if len(paged_response.computers) != self.SEARCH_FILTER.max_items:
                    break

        except deepsecurity.rest.ApiException as e:
            self.handle_api_exception(e,"COMPUTERS")
        except urllib3.exceptions.MaxRetryError as e:
            raise Exception(self.MAX_RETRY_ERROR_MSG)
        except urllib3.exceptions.LocationParseError:
            raise TypeError( ("API Configuration values on {} are NOT VALID".format(self.API_CONFIG_PATH)))
        except Exception as e:
            raise Exception("Generic connection error!" + str(e) + "Generic connection error!")
        
        self.SEARCH_FILTER.search_criteria.id_value = 0 #Reset the Search Criteria
        return computers_list

    def request_computer_per_id(self, comp_id):
        """Returns a unique computer in the DS environment"""
        api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(self.api_config))
        try:
            api_response = api_instance.describe_computer(comp_id, self.api_version, 
            expand=self.COMPUTER_EXPAND, overrides=False)
        except deepsecurity.rest.ApiException as e:
            self.handle_api_exception(e,"COMPUTERS")
        except urllib3.exceptions.MaxRetryError as e:
            raise Exception(self.MAX_RETRY_ERROR_MSG)
        except urllib3.exceptions.LocationParseError:
            raise TypeError( ("API Configuration values on {} are NOT VALID".format(self.API_CONFIG_PATH)))
        return api_response

    def request_computer_groups(self):
        api_instance = deepsecurity.ComputerGroupsApi(deepsecurity.ApiClient(self.api_config))
        try:
            api_response = api_instance.list_computer_groups(self.api_version)
        except deepsecurity.rest.ApiException as e:
            self.handle_api_exception(e,"COMPUTERS")
        except urllib3.exceptions.MaxRetryError as e:
            raise Exception(self.MAX_RETRY_ERROR_MSG)
        except urllib3.exceptions.LocationParseError:
            raise TypeError( ("API Configuration values on {} are NOT VALID".format(self.API_CONFIG_PATH)))
        except Exception as e:
            raise Exception("Generic connection error!" + str(e) + "Generic connection error!")
        return api_response


    def request_policies(self):
        """Returns a list of all policies in the DS environment"""
        api_instance = deepsecurity.PoliciesApi(deepsecurity.ApiClient(self.api_config))
        try:
            api_response = api_instance.list_policies(self.api_version, overrides=False)
        except deepsecurity.rest.ApiException as e:
            self.handle_api_exception(e,"POLICIES")
        except urllib3.exceptions.MaxRetryError as e:
            raise Exception(self.MAX_RETRY_ERROR_MSG)            
        except urllib3.exceptions.LocationParseError:
            raise TypeError( ("API Configuration values on {} are NOT VALID".format(self.API_CONFIG_PATH)))
        except Exception as e:
            raise Exception("Generic connection error!" + str(e) + "Generic connection error!")
        #return {item.id : item for item in api_response.policies}
        return api_response.policies

    def request_anti_malware_configs(self):
        """Returns list of all anti-malware configs in the DS environment """
        api_instance = deepsecurity.AntiMalwareConfigurationsApi(deepsecurity.ApiClient(self.api_config))
        try:
            api_response = api_instance.list_anti_malwares(self.api_version)
        except deepsecurity.rest.ApiException as e:
            self.handle_api_exception(e, "ANTI-MALWARE CONFIGURATIONS")
        except urllib3.exceptions.MaxRetryError as e:
            raise Exception(self.MAX_RETRY_ERROR_MSG)
        except urllib3.exceptions.LocationParseError:
            raise TypeError( ("API Configuration values on {} are NOT VALID".format(self.API_CONFIG_PATH)))
        return api_response.anti_malware_configurations
        #return {item.id : item for item in api_response.anti_malware_configurations}

    def request_stateful_configs(self):
        """Returns a list of all firewall stateful configs in the DS environment """
        api_instance = deepsecurity.StatefulConfigurationsApi(deepsecurity.ApiClient(self.api_config))
        try:
            api_response = api_instance.list_stateful_configurations(self.api_version)
        except deepsecurity.rest.ApiException as e:
            self.handle_api_exception(e,"STATEFUL CONFIGURATIONS")
        except urllib3.exceptions.MaxRetryError as e:
            raise Exception(self.MAX_RETRY_ERROR_MSG)
        except urllib3.exceptions.LocationParseError:
            raise TypeError( ("API Configuration values on {} are NOT VALID".format(self.API_CONFIG_PATH)))
        return api_response.stateful_configurations

    def request_scheduled_tasks(self):
        """Returns a list with all scheduled tasks in the DS environment"""
        api_instance = deepsecurity.ScheduledTasksApi(deepsecurity.ApiClient(self.api_config))
        try:
            api_response = api_instance.list_scheduled_tasks(self.api_version)
        except deepsecurity.rest.ApiException as e:
            self.handle_api_exception(e)
        except urllib3.exceptions.MaxRetryError as e:
            raise Exception(self.MAX_RETRY_ERROR_MSG)            
        except urllib3.exceptions.LocationParseError:
            raise TypeError( ("API Configuration values on {} are NOT VALID".format(self.API_CONFIG_PATH)))
        except Exception as e:
            raise Exception("Generic connection error!" + str(e) + "Generic connection error!")
        return api_response.scheduled_tasks


    def handle_api_exception(self,e,resource_name = "RESOURCE"):
        exception_str=str(e)
        if e.status == 401:
            exception_str = "ERROR 401: UNKNOWN API KEY - Please make sure that the API Key is correct "
        elif e.status == 403:
            exception_str = "ERROR 403: UNAUTHORIZED ACCESS TO {} - Please allow VIEW access for the key's role".format(resource_name.upper()),
        elif e.status == 404:
            exception_str = "ERROR 404: API NOT FOUND - Please make sure the host address is correct and ends with /api"
        raise Exception(exception_str) from e
