# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from deepsecurity.models.policy_module_status import PolicyModuleStatus  # noqa: F401,E501
from deepsecurity.models.stateful_configuration_assignments import StatefulConfigurationAssignments  # noqa: F401,E501


class FirewallPolicyExtension(object):
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
        'module_status': 'PolicyModuleStatus',
        'global_stateful_configuration_id': 'int',
        'stateful_configuration_assignments': 'StatefulConfigurationAssignments',
        'rule_ids': 'list[int]'
    }

    attribute_map = {
        'state': 'state',
        'module_status': 'moduleStatus',
        'global_stateful_configuration_id': 'globalStatefulConfigurationID',
        'stateful_configuration_assignments': 'statefulConfigurationAssignments',
        'rule_ids': 'ruleIDs'
    }

    def __init__(self, state=None, module_status=None, global_stateful_configuration_id=None, stateful_configuration_assignments=None, rule_ids=None):  # noqa: E501
        """FirewallPolicyExtension - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._module_status = None
        self._global_stateful_configuration_id = None
        self._stateful_configuration_assignments = None
        self._rule_ids = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if module_status is not None:
            self.module_status = module_status
        if global_stateful_configuration_id is not None:
            self.global_stateful_configuration_id = global_stateful_configuration_id
        if stateful_configuration_assignments is not None:
            self.stateful_configuration_assignments = stateful_configuration_assignments
        if rule_ids is not None:
            self.rule_ids = rule_ids

    @property
    def state(self):
        """Gets the state of this FirewallPolicyExtension.  # noqa: E501

        Module state.  # noqa: E501

        :return: The state of this FirewallPolicyExtension.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FirewallPolicyExtension.

        Module state.  # noqa: E501

        :param state: The state of this FirewallPolicyExtension.  # noqa: E501
        :type: str
        """
        allowed_values = ["inherited", "on", "off"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def module_status(self):
        """Gets the module_status of this FirewallPolicyExtension.  # noqa: E501


        :return: The module_status of this FirewallPolicyExtension.  # noqa: E501
        :rtype: PolicyModuleStatus
        """
        return self._module_status

    @module_status.setter
    def module_status(self, module_status):
        """Sets the module_status of this FirewallPolicyExtension.


        :param module_status: The module_status of this FirewallPolicyExtension.  # noqa: E501
        :type: PolicyModuleStatus
        """

        self._module_status = module_status

    @property
    def global_stateful_configuration_id(self):
        """Gets the global_stateful_configuration_id of this FirewallPolicyExtension.  # noqa: E501

        ID of the Global Stateful Configuration.  # noqa: E501

        :return: The global_stateful_configuration_id of this FirewallPolicyExtension.  # noqa: E501
        :rtype: int
        """
        return self._global_stateful_configuration_id

    @global_stateful_configuration_id.setter
    def global_stateful_configuration_id(self, global_stateful_configuration_id):
        """Sets the global_stateful_configuration_id of this FirewallPolicyExtension.

        ID of the Global Stateful Configuration.  # noqa: E501

        :param global_stateful_configuration_id: The global_stateful_configuration_id of this FirewallPolicyExtension.  # noqa: E501
        :type: int
        """

        self._global_stateful_configuration_id = global_stateful_configuration_id

    @property
    def stateful_configuration_assignments(self):
        """Gets the stateful_configuration_assignments of this FirewallPolicyExtension.  # noqa: E501

        IDs of the interface-specific Stateful Configuration assignments.  # noqa: E501

        :return: The stateful_configuration_assignments of this FirewallPolicyExtension.  # noqa: E501
        :rtype: StatefulConfigurationAssignments
        """
        return self._stateful_configuration_assignments

    @stateful_configuration_assignments.setter
    def stateful_configuration_assignments(self, stateful_configuration_assignments):
        """Sets the stateful_configuration_assignments of this FirewallPolicyExtension.

        IDs of the interface-specific Stateful Configuration assignments.  # noqa: E501

        :param stateful_configuration_assignments: The stateful_configuration_assignments of this FirewallPolicyExtension.  # noqa: E501
        :type: StatefulConfigurationAssignments
        """

        self._stateful_configuration_assignments = stateful_configuration_assignments

    @property
    def rule_ids(self):
        """Gets the rule_ids of this FirewallPolicyExtension.  # noqa: E501

        IDs of the assigned firewall rules.  # noqa: E501

        :return: The rule_ids of this FirewallPolicyExtension.  # noqa: E501
        :rtype: list[int]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this FirewallPolicyExtension.

        IDs of the assigned firewall rules.  # noqa: E501

        :param rule_ids: The rule_ids of this FirewallPolicyExtension.  # noqa: E501
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
        if issubclass(FirewallPolicyExtension, dict):
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
        if not isinstance(other, FirewallPolicyExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

