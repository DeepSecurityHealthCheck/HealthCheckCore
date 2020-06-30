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


class RulesetRights(object):
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
        'can_create_new_rulesets': 'bool',
        'can_delete_rulesets': 'bool',
        'can_edit_ruleset_properties': 'bool',
        'can_view_rulesets': 'bool'
    }

    attribute_map = {
        'can_create_new_rulesets': 'canCreateNewRulesets',
        'can_delete_rulesets': 'canDeleteRulesets',
        'can_edit_ruleset_properties': 'canEditRulesetProperties',
        'can_view_rulesets': 'canViewRulesets'
    }

    def __init__(self, can_create_new_rulesets=None, can_delete_rulesets=None, can_edit_ruleset_properties=None, can_view_rulesets=None):  # noqa: E501
        """RulesetRights - a model defined in Swagger"""  # noqa: E501

        self._can_create_new_rulesets = None
        self._can_delete_rulesets = None
        self._can_edit_ruleset_properties = None
        self._can_view_rulesets = None
        self.discriminator = None

        if can_create_new_rulesets is not None:
            self.can_create_new_rulesets = can_create_new_rulesets
        if can_delete_rulesets is not None:
            self.can_delete_rulesets = can_delete_rulesets
        if can_edit_ruleset_properties is not None:
            self.can_edit_ruleset_properties = can_edit_ruleset_properties
        if can_view_rulesets is not None:
            self.can_view_rulesets = can_view_rulesets

    @property
    def can_create_new_rulesets(self):
        """Gets the can_create_new_rulesets of this RulesetRights.  # noqa: E501

        Right to create new rulesets.  # noqa: E501

        :return: The can_create_new_rulesets of this RulesetRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_new_rulesets

    @can_create_new_rulesets.setter
    def can_create_new_rulesets(self, can_create_new_rulesets):
        """Sets the can_create_new_rulesets of this RulesetRights.

        Right to create new rulesets.  # noqa: E501

        :param can_create_new_rulesets: The can_create_new_rulesets of this RulesetRights.  # noqa: E501
        :type: bool
        """

        self._can_create_new_rulesets = can_create_new_rulesets

    @property
    def can_delete_rulesets(self):
        """Gets the can_delete_rulesets of this RulesetRights.  # noqa: E501

        Right to delete rulesets.  # noqa: E501

        :return: The can_delete_rulesets of this RulesetRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_rulesets

    @can_delete_rulesets.setter
    def can_delete_rulesets(self, can_delete_rulesets):
        """Sets the can_delete_rulesets of this RulesetRights.

        Right to delete rulesets.  # noqa: E501

        :param can_delete_rulesets: The can_delete_rulesets of this RulesetRights.  # noqa: E501
        :type: bool
        """

        self._can_delete_rulesets = can_delete_rulesets

    @property
    def can_edit_ruleset_properties(self):
        """Gets the can_edit_ruleset_properties of this RulesetRights.  # noqa: E501

        Right to edit ruleset properties.  # noqa: E501

        :return: The can_edit_ruleset_properties of this RulesetRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_ruleset_properties

    @can_edit_ruleset_properties.setter
    def can_edit_ruleset_properties(self, can_edit_ruleset_properties):
        """Sets the can_edit_ruleset_properties of this RulesetRights.

        Right to edit ruleset properties.  # noqa: E501

        :param can_edit_ruleset_properties: The can_edit_ruleset_properties of this RulesetRights.  # noqa: E501
        :type: bool
        """

        self._can_edit_ruleset_properties = can_edit_ruleset_properties

    @property
    def can_view_rulesets(self):
        """Gets the can_view_rulesets of this RulesetRights.  # noqa: E501

        Right to view rulesets.  # noqa: E501

        :return: The can_view_rulesets of this RulesetRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_view_rulesets

    @can_view_rulesets.setter
    def can_view_rulesets(self, can_view_rulesets):
        """Sets the can_view_rulesets of this RulesetRights.

        Right to view rulesets.  # noqa: E501

        :param can_view_rulesets: The can_view_rulesets of this RulesetRights.  # noqa: E501
        :type: bool
        """

        self._can_view_rulesets = can_view_rulesets

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
        if issubclass(RulesetRights, dict):
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
        if not isinstance(other, RulesetRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

