# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 12.5.855
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from deepsecurity.models.computer_module_status import ComputerModuleStatus  # noqa: F401,E501


class IntegrityMonitoringComputerExtension(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'state': 'str',
        'module_status': 'ComputerModuleStatus',
        'last_integrity_scan': 'int',
        'last_baseline_created': 'int',
        'rule_ids': 'list[int]'
    }

    attribute_map = {
        'state': 'state',
        'module_status': 'moduleStatus',
        'last_integrity_scan': 'lastIntegrityScan',
        'last_baseline_created': 'lastBaselineCreated',
        'rule_ids': 'ruleIDs'
    }

    def __init__(self, state=None, module_status=None, last_integrity_scan=None, last_baseline_created=None, rule_ids=None):  # noqa: E501
        """IntegrityMonitoringComputerExtension - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._module_status = None
        self._last_integrity_scan = None
        self._last_baseline_created = None
        self._rule_ids = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if module_status is not None:
            self.module_status = module_status
        if last_integrity_scan is not None:
            self.last_integrity_scan = last_integrity_scan
        if last_baseline_created is not None:
            self.last_baseline_created = last_baseline_created
        if rule_ids is not None:
            self.rule_ids = rule_ids

    @property
    def state(self):
        """Gets the state of this IntegrityMonitoringComputerExtension.  # noqa: E501

        Module state.  # noqa: E501

        :return: The state of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IntegrityMonitoringComputerExtension.

        Module state.  # noqa: E501

        :param state: The state of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :type: str
        """
        allowed_values = ["inherited", "real-time", "on", "off"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def module_status(self):
        """Gets the module_status of this IntegrityMonitoringComputerExtension.  # noqa: E501


        :return: The module_status of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :rtype: ComputerModuleStatus
        """
        return self._module_status

    @module_status.setter
    def module_status(self, module_status):
        """Sets the module_status of this IntegrityMonitoringComputerExtension.


        :param module_status: The module_status of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :type: ComputerModuleStatus
        """

        self._module_status = module_status

    @property
    def last_integrity_scan(self):
        """Gets the last_integrity_scan of this IntegrityMonitoringComputerExtension.  # noqa: E501

        Timestamp of the last full scan for integrity, in milliseconds since epoch.  # noqa: E501

        :return: The last_integrity_scan of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :rtype: int
        """
        return self._last_integrity_scan

    @last_integrity_scan.setter
    def last_integrity_scan(self, last_integrity_scan):
        """Sets the last_integrity_scan of this IntegrityMonitoringComputerExtension.

        Timestamp of the last full scan for integrity, in milliseconds since epoch.  # noqa: E501

        :param last_integrity_scan: The last_integrity_scan of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :type: int
        """

        self._last_integrity_scan = last_integrity_scan

    @property
    def last_baseline_created(self):
        """Gets the last_baseline_created of this IntegrityMonitoringComputerExtension.  # noqa: E501

        Timestamp of the last integrity baseline, in milliseconds since epoch.  # noqa: E501

        :return: The last_baseline_created of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :rtype: int
        """
        return self._last_baseline_created

    @last_baseline_created.setter
    def last_baseline_created(self, last_baseline_created):
        """Sets the last_baseline_created of this IntegrityMonitoringComputerExtension.

        Timestamp of the last integrity baseline, in milliseconds since epoch.  # noqa: E501

        :param last_baseline_created: The last_baseline_created of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :type: int
        """

        self._last_baseline_created = last_baseline_created

    @property
    def rule_ids(self):
        """Gets the rule_ids of this IntegrityMonitoringComputerExtension.  # noqa: E501

        IDs of the assigned Integrity Monitoring rules.  # noqa: E501

        :return: The rule_ids of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :rtype: list[int]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this IntegrityMonitoringComputerExtension.

        IDs of the assigned Integrity Monitoring rules.  # noqa: E501

        :param rule_ids: The rule_ids of this IntegrityMonitoringComputerExtension.  # noqa: E501
        :type: list[int]
        """

        self._rule_ids = rule_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IntegrityMonitoringComputerExtension, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IntegrityMonitoringComputerExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

