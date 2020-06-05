from lib.api_loader import Api_Loader
from multiprocessing.pool import ThreadPool
import time
import sys
import os
import binascii
import lib.constants as constants
from yaml import load, dump, safe_load


try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from colorama import init, Fore

from pprint import pprint
from prompt_toolkit import prompt

DEFAULT_YAML = '''
language: "en"
modules: "all"
customer_name: ""
customer_contacts:
    "Your name":
        title: ''
        email: ''
        phone: ''
partner_name: ""
partner_contacts:
    "":
        title: ''
        email: ''
        phone: ''
trend_contacts: 
    "Trend Engineer Name":
        title: ''
        email: ''
        phone: ''
'''.encode("UTF-8")
PARSED_YAML = safe_load(DEFAULT_YAML)

init(autoreset=True)

pool = ThreadPool(processes=1)


def threaded_fetch(func, desc):
    async_result = pool.apply_async(func)
    time_stepper(async_result, desc)
    return async_result.get()


def time_stepper(async_res, description):
    loop_counter = -1
    animation_index = 0
    animation_frames = ['|', '/', '-', '\\']

    sleep_time = 0.1
    seconds_to_warning = 60

    while True:
        if async_res.ready():
            print('\t...done')
            break
        loop_counter += 1
        msg = '\r{}  [{}]'.format(description, animation_frames[animation_index])
        if loop_counter * sleep_time > seconds_to_warning:
            msg += "\tTaking longer than normal, please wait..."
        sys.stdout.write(msg)
        time.sleep(sleep_time)
        animation_index = (animation_index + 1) % len(animation_frames)


def prettify_string(s):
    return "".join(s.replace("_", " ").capitalize())


def dive_into(d, recur=False):
    new_dict = {}
    for key, value in d.items():
        if type(value) == dict:
            ctrl = ""
            new_dict[key] = {}
            while ctrl not in ['n', 'no', 'NO', 'N']:
                # if recur:
                new_key = prompt("{}\n Name: ".format(prettify_string(key)))
                if new_key == "":
                    break

                base_key = list(value.keys())[0]
                new_dict[key][new_key] = dive_into(value[base_key], recur=True)
                if recur:
                    break

                ctrl = prompt("New entry? in {} [y/n]".format(prettify_string(key)))

            continue

        new_value = prompt("{} [{}]: ".format(prettify_string(key), value)) or value
        new_dict[key] = new_value

    return new_dict


def get_customer_info():
    cfg_folder = "customer_details_cache.yml"
    if not os.path.exists(cfg_folder):
        print(Fore.LIGHTGREEN_EX + "Please fill the required information about you and your company")
        try:
            report_details = load(DEFAULT_YAML, Loader=Loader)
        except Exception as e:
            print("Error on trying read yaml file {}".format("d"))
            print(e)
            sys.exit(1)

        new_cfg = dive_into(report_details)

        # Module and Language Validation ============
        if new_cfg["language"] not in constants.VALID_LANGUAGES.keys():
            new_cfg["language"] = constants.DEFAULT_LANGUAGE

        new_cfg["modules"] = new_cfg["modules"].split(" ")
        if "all" in new_cfg["modules"]:
            new_cfg["modules"] = constants.VALID_LICENSES["all"]
        else:
            filtered_input_modules = list(filter(lambda x:x in constants.VALID_MODULES.keys(), new_cfg["modules"]))
            if len(filtered_input_modules) == 0:
               new_cfg["modules"] = constants.VALID_LICENSES["all"]
            if len(filtered_input_modules) < len(new_cfg["modules"]):
                new_cfg["modules"] = filtered_input_modules
        pprint(new_cfg)

        # preventing bruteforce of customer info to match anonymous hash.
        new_cfg["random-padding0"] = binascii.hexlify(os.urandom(32))
        new_cfg["random-padding1"] = binascii.hexlify(os.urandom(32))
        new_cfg["random-padding2"] = binascii.hexlify(os.urandom(32))
        new_cfg["random-padding3"] = binascii.hexlify(os.urandom(32))

        if input("Is the above information correct? (n/Y)").lower() == "n":
            print("Exiting without saving, please rerun to reconfigure")
            exit(223)

        with open(cfg_folder, "w") as cfg:
            cfg.write(dump(new_cfg, Dumper=Dumper))

        print(Fore.GREEN + "New config saved on {}".format(cfg_folder))
    else:
        remove = input(Fore.BLUE + "Customer data already filled, remove and refill it? (y/N)")
        if remove.lower() == 'y':
            os.remove(cfg_folder)
            return get_customer_info()
        yml_cfg = open(cfg_folder, 'r').read()
        new_cfg = load(yml_cfg, Loader=Loader)

    return new_cfg


def get_info(include_am_configs=False, include_fw_configs=False):
    """
    Fetches the API and packages the returned SDK objects into a "data_pack"

    Args:
        arg_modules : List of ValidModules to be checked

    Returns:
        data_pack : Dict
    """

    api = Api_Loader()

    data_pack = {'customer_info': get_customer_info(),
                 'computers': threaded_fetch(api.request_computers, "Fetching Computers"),
                 'computer_groups': threaded_fetch(api.request_computer_groups, "Fetching Computer Groups"),
                 'policies': threaded_fetch(api.request_policies, "Fetching Policies"),
                 'scheduled_tasks': threaded_fetch(api.request_scheduled_tasks, "Fetching Scheduled Tasks"),
                 'host': api.api_config.host
                 }

    if include_am_configs:
        data_pack['am_config'] = threaded_fetch(api.request_anti_malware_configs, "Fetching AM Configs")
    if include_fw_configs:
        data_pack['stateful_configs'] = threaded_fetch(api.request_stateful_configs, "Fetching FW Configs")

    return data_pack
