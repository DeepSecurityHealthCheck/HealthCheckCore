#Deep Security imports
from deepsecurity import AntiMalwareConfiguration
from deepsecurity import ScheduledTasks
from deepsecurity import ScheduledTask

#Python Imports
from enum import Enum
from collections import namedtuple
import os
from tqdm import tqdm
import logging

#Check Utils imports
from .check_utils import CheckItem as CheckItem
from .check_utils import Operator as op
from .check_utils import run_checklist as run_checklist

"""
 This module contains all necessary methods to check for best practices
conformity of the firewall module and other configurations.

This moudle **Should not interact with the API directly** but rather recieve
input which is returned by SDK calls.
"""

'''
firewall_stateful_checklist = [
    CheckItem(attr_path="deny_fragmented_packets_enabled",
        operator="EQUAL",
        operand=False,
        item_weight=1),

    CheckItem(attr_path="deny_packets_containing_cwr_or_ece_enabled",
        operator="EQUAL",
        operand=False,
        item_weight=1)

]
'''

class FirewallChecker(object):
    def __init__(self, dir_path, parser):
        file_path = os.path.join(dir_path,"firewall_configuration.yml")
        self.firewall_stateful_checklist = parser.load_module(file_path)['items']

    def check_firewall_configurations(self, config_list):

        """
        Checks if each FirewallConfiguration object in the list is in accordance
        with best practices

        Args:
            config: FirewallConfiguration list to check

        Returns:
            dict of type: {FirewallConfiguration.id:FirewallcheckResults}
        """
        config_dict = {}
        with tqdm(total=len(config_list), ascii=True, desc="Checking FW Configs") as pbar:
            for config in config_list:
                pbar.update(1)
                result = run_checklist(config, self.firewall_stateful_checklist, return_failures=True, logger=logging.getLogger())
                config_dict[config.id] = result
        return config_dict

#===============================================================================-
