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

from deepsecurity.models.policy_module_status import PolicyModuleStatus  # noqa: F401,E501


class ApplicationControlPolicyExtension(object):
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
        'block_unrecognized': 'bool',
        'ruleset_id': 'int'
    }

    attribute_map = {
        'state': 'state',
        'module_status': 'moduleStatus',
        'block_unrecognized': 'blockUnrecognized',
        'ruleset_id': 'rulesetID'
    }

    def __init__(self, state=None, module_status=None, block_unrecognized=None, ruleset_id=None):  # noqa: E501
        """ApplicationControlPolicyExtension - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._module_status = None
        self._block_unrecognized = None
        self._ruleset_id = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if module_status is not None:
            self.module_status = module_status
        if block_unrecognized is not None:
            self.block_unrecognized = block_unrecognized
        if ruleset_id is not None:
            self.ruleset_id = ruleset_id

    @property
    def state(self):
        """Gets the state of this ApplicationControlPolicyExtension.  # noqa: E501

        Module state.  # noqa: E501

        :return: The state of this ApplicationControlPolicyExtension.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ApplicationControlPolicyExtension.

        Module state.  # noqa: E501

        :param state: The state of this ApplicationControlPolicyExtension.  # noqa: E501
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
        """Gets the module_status of this ApplicationControlPolicyExtension.  # noqa: E501


        :return: The module_status of this ApplicationControlPolicyExtension.  # noqa: E501
        :rtype: PolicyModuleStatus
        """
        return self._module_status

    @module_status.setter
    def module_status(self, module_status):
        """Sets the module_status of this ApplicationControlPolicyExtension.


        :param module_status: The module_status of this ApplicationControlPolicyExtension.  # noqa: E501
        :type: PolicyModuleStatus
        """

        self._module_status = module_status

    @property
    def block_unrecognized(self):
        """Gets the block_unrecognized of this ApplicationControlPolicyExtension.  # noqa: E501

        Block unrecognized software until it is explicitly allowed.  # noqa: E501

        :return: The block_unrecognized of this ApplicationControlPolicyExtension.  # noqa: E501
        :rtype: bool
        """
        return self._block_unrecognized

    @block_unrecognized.setter
    def block_unrecognized(self, block_unrecognized):
        """Sets the block_unrecognized of this ApplicationControlPolicyExtension.

        Block unrecognized software until it is explicitly allowed.  # noqa: E501

        :param block_unrecognized: The block_unrecognized of this ApplicationControlPolicyExtension.  # noqa: E501
        :type: bool
        """

        self._block_unrecognized = block_unrecognized

    @property
    def ruleset_id(self):
        """Gets the ruleset_id of this ApplicationControlPolicyExtension.  # noqa: E501

        ID of the shared whitelist ruleset.  # noqa: E501

        :return: The ruleset_id of this ApplicationControlPolicyExtension.  # noqa: E501
        :rtype: int
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        """Sets the ruleset_id of this ApplicationControlPolicyExtension.

        ID of the shared whitelist ruleset.  # noqa: E501

        :param ruleset_id: The ruleset_id of this ApplicationControlPolicyExtension.  # noqa: E501
        :type: int
        """

        self._ruleset_id = ruleset_id

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
        if issubclass(ApplicationControlPolicyExtension, dict):
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
        if not isinstance(other, ApplicationControlPolicyExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

