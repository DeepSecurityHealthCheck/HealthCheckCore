import lib.data_loader as dl
import lib.constants as constants

from lib.computer_checker import ComputerChecker
from lib.computer_statistics import ComputerStatisticsGetter
from lib.policy_checker import PolicyChecker
from lib.checker import Checker
from lib.anti_malware_checker import AntiMalwareChecker
from lib.firewall_checker import FirewallChecker
from lib.scheduled_task_checker import ScheduledTaskChecker
from lib.telemetry_reporter import report_crash, report_execution

from lib.CloudManager import CloudManager

import extractor as ext
import key_generator as key_gen

from lib.report_generator import BPGGenerator
from lib.yaml_parser import YAMLParser
from lib.crypto_spa_report import gen_aes_key
from utils.object_duplicator import duplicate_objects


from pprint import pprint
from collections import namedtuple
from colorama import init, Fore
init()

import time
import argparse
import os
import psutil
import logging
import json
import yaml
import traceback

import deepsecurity


API_CONFIG_PATH = "config/api_config.yml"
HELP_STRING = """
VALID LANGUAGES INPUT
en  English
jp  Japanese

If no modules or licenses are explicitly declared, all modules will be checked by default

VALID LICENSES INPUT
mp  (Malware Protection - Anti-Malware, Web Reputation)
ss  (System Security - Integrity Monitoring, Log Inspection, Application Control)
ns  (Network Security - Firewall, Intrusion Prevention)
all (All modules)

VALID MODULES INPUT
am  (Anti-Malware)
wr  (Web Reputation)
im  (Integrity Monitoring)
li  (Log Inspection)
ac  (Application Control)
fw  (Firewall)
ip  (Intrusion Prevention)


EXAMPLES
Check all Malware Protection and System Security modules and Intrusion Prevention module
%(prog)s -l mp ss -m ip

"""

COMPUTER_RESULTS_FILEPATH = "./report_pdfs/results_for_computers.log"
POLICY_RESULTS_FILEPATH="./report_pdfs/results_for_policies.log"
VERSION = "1.1"

VALID_MODULES = {
    "am" : "anti_malware",
    "wr" : "web_reputation",
    "im" : "integrity_monitoring",
    "li" : "log_inspection",
    "ac" : "application_control",
    "fw" : "firewall",
    "ip" : "intrusion_prevention"
}

VALID_LICENSES = {
    #MALWARE_PREVENTION
    "mp" : ["am","wr"],
    #SYSTEM_SECURITY
    "ss" : ["im","li","ac"],
    #NETWORK_SECURITY
    "ns" : ["fw", "ip"],
    #ALL    #Enterprise and DSaaS
    "all" : VALID_MODULES.keys()
}

API_CONFIG = './config/api_config.yml'
REPORT_DETAILS = './config/report_details.yml'
DATA_PACK_DEFAULT_PATH = './data_packs/'
PRIVATE_KEY_NAME = 'PRIVATE_key.pem'

PRIVATE_KEY_PATH = './keys/{}'.format(PRIVATE_KEY_NAME)
USER_CONFIG_FILES = [API_CONFIG, REPORT_DETAILS]

def process_args(arguments):
    """ Used to process the arguments recieved by the command line

    Args:
        arguments: Object returned by the parse_args() method of ArgumentParser

    Returns:
        arg_modules_to_check: Set of modules to check - ALL by Default
        arg_conf_standard_dir_path: directory path for configuration files - config/bpg_config by Default
        debug - Show debug info
        stress_test_num_computers - number of dummy machines for stress test
    Raises:
        FileNotFoundError if the directory does not exist
        ValueError if recieves non-valid module/licenses
    """

    if arguments.version is True:
        print("Version: {}".format(VERSION))
        exit()

    key = None
    password = None
    if arguments.key != None:
        key = arguments.key
        password = arguments.password


    if arguments.generate_keys is True:
        key_gen.generate_keys()
        exit()

    #Migrate keys then exit
    if arguments.migrate is True:
        ext.migrate_package()
        exit()
    if arguments.language in constants.VALID_LANGUAGES.keys():
        os.environ[constants.LANGUAGE_ENV_NAME] = arguments.language
    #DEFAULT, SET ENGLISH
    else:
        os.environ[constants.LANGUAGE_ENV_NAME] = constants.DEFAULT_LANGUAGE
    """
    THE FOLLOWING FUNCTION _MUST_ BE CALLED
    """
    constants.format_paths()

    filtered_input_licenses = list(filter(lambda x:x in VALID_LICENSES.keys(), arguments.licenses))
    if len(filtered_input_licenses) != len(arguments.licenses):
        raise ValueError("Invalid License")

    filtered_input_modules = list(filter(lambda x:x in VALID_MODULES.keys(), arguments.modules))
    if len(filtered_input_modules) != len(arguments.modules):
        raise ValueError("Invalid Module")

    arg_modules_to_check = []
    if (len(filtered_input_licenses) == 0) and (len(filtered_input_modules) == 0):
        arg_modules_to_check += VALID_MODULES
    else:
        for a in filtered_input_licenses:
            arg_modules_to_check += VALID_LICENSES[a]
        arg_modules_to_check += filtered_input_modules
    #Deduping
    arg_modules_to_check = [VALID_MODULES[i] for i in set(arg_modules_to_check)]

    
    arg_conf_standard_name = arguments.standard
    #TODO CREATE DISPATCH TABLE LINKING REPORT GENERATOR CONSTRUCTORS
    arg_conf_standard_name = arguments.standard
    arg_conf_standard_dir_path = os.path.join(os.getcwd(), constants.CONFORMITY_STANDARDS_BASE_PATH + arg_conf_standard_name + constants.CONFORMITY_STANDARDS_SUFFIX)
    if os.path.isdir(arg_conf_standard_dir_path) == False:
        raise FileNotFoundError("Conformity Standard \""+ arg_conf_standard_name + "\" "+constants.CONFORMITY_STANDARDS_SUFFIX+" directory not found")

    stress_test_num_computers = 0
    if arguments.stress is not None:
        stress_test_num_computers = int(arguments.stress)

    data_pack_filename = None
    if arguments.remote is not None:
        data_pack_filename = str(arguments.remote)
        if os.environ.get('ENV') == 'DOCKER' and not os.environ.get('AWS', False):
            data_pack_filename = "./data_packs/" + data_pack_filename

        if os.path.exists(data_pack_filename) is False:
            print("Specified file does not exist")
            exit(-1)

    options = {
        "arg_modules_to_check": arg_modules_to_check,
        "arg_conf_standard_name": arg_conf_standard_name,
        "arg_conf_standard_dir_path": arg_conf_standard_dir_path,
        "debug":  arguments.debug,
        "arg_stress_num_computers": stress_test_num_computers,
        "data_pack_filename": data_pack_filename,

        "private_key": key,
        "password": password,
        
        "output_folder": arguments.output
    }

    return options
    # return (arg_modules_to_check,arg_conf_standard_name,arg_conf_standard_dir_path, arguments.debug, stress_test_num_computers, data_pack_filename)

def beautify_hostname(url):
    """
    Returns the hostname of a given URL
    """
    if not isinstance(url,str):
        return ""
    
    h = list(filter(lambda x: 'api' in x ,url.split("//")))
    if len(h) == 0:
        return url.split("//")[-1]
    
    #If there is port specified in the config
    h = h[0].split(":")[0]
    if "api" not in h:
        return h

    #Return only the hostname
    return h.split('/')[0]

def choose_report_generator(conf_name,report_data,data_pack):
    """
    Dispatcher that selects the Report Generator based on the conformity Standard
    Defaults to the BPG Generator

    NEW TYPES OF REPORT GENERATION ARE TO BE PLACED HERE
    """
    report_options = {
        "customer_host" : beautify_hostname(data_pack["host"]),
        "version" : VERSION
    }
    
    if conf_name == "bpg":
        report_options.update({
            "conformity_standard":"Deep Security Best Practices Guide"
        })
        return BPGGenerator(report_data,report_options)
    else:
        report_options.update({
            "conformity_standard":str.upper(conf_name)
        })
        return BPGGenerator(report_data, report_options)

def fetch_data_pack(modules_to_check,data_pack_filename, key_path, key_password):
    """
    Creates a data pack from the data loader or unpack's an extractor datapack file

    Args:
        modules_to_check: List of modules to extract data
        data_pack_filename: String with the data pack's filename
    """
    if data_pack_filename is not None:
        data_pack = ext.unpack_data(data_pack_filename, key_path, key_password)

    else:
        parser = YAMLParser()        
        include_am_configs = VALID_MODULES['am'] in modules_to_check
        include_fw_configs = VALID_MODULES['fw'] in modules_to_check
        data_pack = dl.get_info(include_am_configs=include_am_configs,include_fw_configs=include_fw_configs)
        data_pack["host"] = parser.load_file(API_CONFIG_PATH)["api-configuration"]["host"]
    return data_pack


def run_checkers(arg_conf_standard_dir_path, am_config_list, stateful_config_list,
    computer_list,computer_groups_list,policy_list,scheduled_task_list, arg_modules_to_check):
    """
    Runs checkers for Anti-Malware Configs, Stateful Configs, Computers, Policies, Scheduled Tasks

    Args:
        arg_conf_standard_dir_path: Directory path with Conformity Standard configs
        am_config_list: List of Anti Malware Configurations
        stateful_config_list: List of Stateful Configurations
        computer_list: List of Computers
        computer_groups_list: List of Computer Groups
        policy_list: List of Policies
        scheduled_task_list: List of Scheduled Tasks
        arg_modules_to_check: Dict of Module names to check

    Returns:
        Named Tuple containing the bundled results for each checker
    """
    parser = YAMLParser()
    checker = Checker(arg_conf_standard_dir_path, parser, include_modules=arg_modules_to_check)
    am_configs_results = None
    fw_configs_results = None

    if VALID_MODULES["am"] in arg_modules_to_check and am_config_list is not None:
        am_checker = AntiMalwareChecker(arg_conf_standard_dir_path, parser)
        am_configs_results = am_checker.check_anti_malware_configurations(am_config_list)

    if VALID_MODULES["fw"] in arg_modules_to_check and stateful_config_list is not None:
        fw_checker = FirewallChecker(arg_conf_standard_dir_path, parser)
        fw_configs_results =  fw_checker.check_firewall_configurations(stateful_config_list)

    computer_checker = ComputerChecker(checker, computer_list,
        arg_modules_to_check, computer_groups_list, am_configs_results, fw_configs_results)
    
    policy_checker = PolicyChecker(checker,
        policy_list, am_configs_results, fw_configs_results, computer_checker.used_policies)
    
    computer_stats_getter = ComputerStatisticsGetter(computer_list,
        arg_modules_to_check,computer_checker.computer_groups,
        computer_checker.computer_results,computer_checker.module_results,
        policy_checker.policy_results)
   
    scheduled_tasks_checker = ScheduledTaskChecker(checker, scheduled_task_list,
        computer_list, computer_checker.computer_groups, computer_stats_getter.get_mapped_policies())

    bundled_results = namedtuple("bundled_results", 
        ["computer_checker","policy_checker","computer_stats_getter","scheduled_tasks_checker"])
    

    return bundled_results(computer_checker.get_bundle(),policy_checker.get_bundle(),
        computer_stats_getter.get_bundle(),scheduled_tasks_checker.get_bundle())


def main(options):
    try:
        debug = options['debug']

        if debug:
            logging.basicConfig(filename='debug.log', filemode='w',
                                level=logging.DEBUG, format='dshc %(levelname)s:%(message)s')

        ##FETCHING  ----------------------------------------------------------------
        # Organized way of getting the data.
        arg_modules_to_check       = options['arg_modules_to_check']
        arg_conf_standard_name     = options['arg_conf_standard_name']
        arg_conf_standard_dir_path = options['arg_conf_standard_dir_path']
        arg_stress_num_computers   = options['arg_stress_num_computers']
        data_pack_filename         = options['data_pack_filename']
        private_key_path           = options['private_key']
        key_password               = options['password']
        output_folder              = options['output_folder'] or ''


        t0_fetch = time.time()
        data_pack = fetch_data_pack(arg_modules_to_check,data_pack_filename, private_key_path, key_password)
        t1_fetch = time.time()

        computer_groups_list = data_pack['computer_groups']
        computer_list = data_pack['computers']
        policy_list = data_pack['policies']
        scheduled_task_list = data_pack['scheduled_tasks']
        am_config_list = data_pack.get('am_config',None)
        stateful_config_list = data_pack.get('stateful_configs',None)
        """
        Filters out unavailable Modules - in the computer object
        Due to issue with multi-tenant agents without certain modules. 
        The variable for those modules on a computer becomes None
        """
    except Exception as e:
        report_crash(str(e), None)
        exit(-1)

    try:
        arg_modules_to_check = list(filter(lambda x: getattr(computer_list[0],x) != None, arg_modules_to_check))

        """
        RUN STRESS TEST
        """
        t0_dup = time.time()
        if arg_stress_num_computers:
            print("Duplicating Computers...")
            computer_list = duplicate_objects(computer_list,arg_stress_num_computers)
        t1_dup = time.time()

        # CHECKING  ----------------------------------------------------------------
        t0_check = time.time()

        bundled_results = run_checkers(arg_conf_standard_dir_path,
            am_config_list,
            stateful_config_list,
            computer_list,
            computer_groups_list,
            policy_list,
            scheduled_task_list,
            arg_modules_to_check)

        t1_check = time.time()
        print("\n")

        # REPORTING ----------------------------------------------------------------
        t0_report = time.time()
        #Results bundle
        report_data = {
            **bundled_results.computer_checker,
            **bundled_results.policy_checker,
            **bundled_results.computer_stats_getter,
            **bundled_results.scheduled_tasks_checker
        }

        report_data["computers"] = computer_list,
        report_data["policies"] = policy_list,
        report_data["scheduled_tasks"] = scheduled_task_list,
        report_data["modules_to_check"] = arg_modules_to_check

        #Dict of Modules "Acronym":"ugly_name"
        valid_modules_to_check = dict(filter(lambda v: v[1] in arg_modules_to_check, VALID_MODULES.items()))
        valid_modules_not_to_check = dict(filter(lambda v: v[1] not in arg_modules_to_check, VALID_MODULES.items()))

        report_data["dict_modules_to_check"] = valid_modules_to_check
        report_data["dict_modules_not_to_check"] = valid_modules_not_to_check

        print("Generating Report...")

        tech_report_key = gen_aes_key()
        report_data['tech_key'] = tech_report_key['key'].decode()


        if 'customer_info' not in data_pack:
            print(Fore.LIGHTYELLOW_EX + "Legacy Packet detected, please fill with the customer data")
            report_data['customer_info'] = dl.dive_into(dl.PARSED_YAML)
        else:
            report_data['customer_info'] = data_pack["customer_info"]

            
        print("Generating executive report...")
        generator = choose_report_generator(arg_conf_standard_name,report_data,data_pack)
        generator.generate_exec_report()

        # print(tech_report_key)

        print("Building technical report...")
        generator.generate_tech_report(computer_list, policy_list, {**bundled_results.computer_checker, **bundled_results.policy_checker, **bundled_results.computer_stats_getter}, valid_modules_to_check, tech_report_key)


        print("Zipping...")
        zip_path = generator.pack_report(output_folder)
        t1_report = time.time()

        if debug or arg_stress_num_computers:
            print("Fetching time", t1_fetch-t0_fetch)
            if arg_stress_num_computers: print("Duplication time", t1_dup - t0_dup)
            print("Processing time: ", t1_check-t0_check)
            print("Report Generation time: ",t1_report-t0_report)

        report_analytics = generator.generate_analytics()
        
        if debug:
            print(Fore.LIGHTRED_EX + "Debug mode, report not sent!")
        else:
            report_execution(report_analytics ,data_pack)

        print("...Done")
        return zip_path


    except Exception as e:
        if debug:
            print(Fore.LIGHTRED_EX + "Debug mode, Crash report not sent!")
        else:
            report_crash(str(e), data_pack)
            traceback.print_exc(e)
        exit(-1)


def process_cloud():
    """Load all serveless information"""
    # Pull each times if there is new sqs events
    try_count = 5 # This will run for 25 seconds if there is no sqs message
    wait_time = 5
    count = 0
    dshc_cloud = CloudManager()
    print("[+] Starting DSHC as a Service :) [+]")
    print("Loading keys...")

    private_key = dshc_cloud.pull_s3_object(bucket=dshc_cloud.keys_bucket, key='PRIVATE_key.pem')
    password = dshc_cloud.pull_s3_object(bucket=dshc_cloud.keys_bucket, key='PRIVATE_key_password').decode().rstrip()

    print("[+] Keys loaded! [+]")
    try:
        os.mkdir('./keys')
        os.mkdir('./data_packs')
        os.mkdir('./config')
        os.mkdir('./report_pdfs')
    except:
        print("Could not create files")

    with open(PRIVATE_KEY_PATH, 'wb') as private_key_fd:
        private_key_fd.write(private_key)

    while count != try_count:
        params = dshc_cloud.pull_sqs()
        if params != None:
            for i,param in enumerate(params):
                param = json.loads(param.get('Body'))
                generation_id = param.pop('generation_id')
                modules = param.pop('modules')
                language = param.pop('language')
                with open(REPORT_DETAILS, 'w') as config:
                    config.write(yaml.dump(param))

                data_pack = dshc_cloud.pull_s3_object(bucket=dshc_cloud.remote_bucket, key=generation_id)

                data_pack_path = "{}{}".format(DATA_PACK_DEFAULT_PATH, generation_id)
                with open(data_pack_path, 'wb') as data_pack_fd:
                    data_pack_fd.write(data_pack)

                try:
                    print('Processing {}'.format(generation_id))
                    res = start(modules,language, remote=data_pack_path, private_key_password=password)
                    print('Writing...')
                    dshc_cloud.write_new_report(res, generation_id)
                    count = 0
                except Exception as e:
                    print("Error while processing package, Please check if your extractor version is at [{}]"
                    "\n debug info: [Id]: {} -- [Exception] : {}".format(str(constants.EXTRACTOR_VERSION),str(generation_id),str(e)))
                    dshc_cloud.remove_message(params[i])
                    continue
                dshc_cloud.remove_message(params[i])
        else:
            count += 1
        
        time.sleep(wait_time) 
        
        


def start(modules=[], language=constants.DEFAULT_LANGUAGE, remote="", private_key_password=""):
    try:
        parser = argparse.ArgumentParser(
            prog="dshc",
            description='Automated Deep Security Health Check Verification',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=HELP_STRING )

        parser.add_argument('--licenses', '-l', nargs='+',help="Space separated list of modules (grouped by license) to be checked", default=[])
        parser.add_argument('--modules', '-m', nargs='+',help="Space separated list of modules to be checked", default=[])
        parser.add_argument('--standard', '-c',help="Conformity Standard to be used", default='bpg')
        parser.add_argument('--debug', '-d', action='store_true', help="Debug messages will be written in debug.log")
        parser.add_argument('--stress', '-s', help="Stress test - Choose number (dummy) of computers to run test")
        parser.add_argument('--remote', '-r',  help="Loads a previously extracted data package")
        parser.add_argument("--generate-keys","-g", action='store_true', help="Generate a new cryptographic key pair and exits")
        parser.add_argument("--migrate",action='store_true',help="Migrates a Data Package to a new key pair and exits")
        parser.add_argument('--language', help="Language to be used in the report", default='en')

        parser.add_argument('--key', '-k', help="Path to your private key")
        parser.add_argument('--password', '-p', help='Your private key password, this will be written in your history file!')
        parser.add_argument('--output', '-o', help='Path that zip file will be stored')
        parser.add_argument('--version', '-v',action='store_true', help='Print version and exit')

        args = parser.parse_args()
        if len(modules) > 0:
            args.modules = modules
            args.remote  = remote
            args.key = PRIVATE_KEY_NAME
            args.password = private_key_password
            args.language = language
            
        # arg_modules_to_check, arg_conf_standard_name, arg_conf_standard_dir_path, arg_debug, arg_stress_num_computers, data_pack_filename = process_args(parser.parse_args())
        arg_options = process_args(args)
        # main( arg_modules_to_check, arg_conf_standard_name, arg_conf_standard_dir_path, arg_debug, arg_stress_num_computers , data_pack_filename)

        if arg_options['data_pack_filename'] is not None and len(USER_CONFIG_FILES) > 1:
            # Check config files
            USER_CONFIG_FILES.pop(0)

        for config in USER_CONFIG_FILES:
            if os.path.exists(config) is False:
                print("{} is missing!".format(config))
                exit(1)

    except Exception as e:
        report_crash(str(e), None)
        exit(-1)

    return main(arg_options)

if __name__ == '__main__':
    if os.environ.get('AWS', False):
        process_cloud()
    else:
        start()
            # else: count += 1


   
