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


class Component(object):
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
        'name': 'str',
        'for_use_by': 'str',
        'platform': 'str',
        'version': 'str',
        'latest': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'for_use_by': 'forUseBy',
        'platform': 'platform',
        'version': 'version',
        'latest': 'latest'
    }

    def __init__(self, name=None, for_use_by=None, platform=None, version=None, latest=None):  # noqa: E501
        """Component - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._for_use_by = None
        self._platform = None
        self._version = None
        self._latest = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if for_use_by is not None:
            self.for_use_by = for_use_by
        if platform is not None:
            self.platform = platform
        if version is not None:
            self.version = version
        if latest is not None:
            self.latest = latest

    @property
    def name(self):
        """Gets the name of this Component.  # noqa: E501

        Name of the component.  # noqa: E501

        :return: The name of this Component.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Component.

        Name of the component.  # noqa: E501

        :param name: The name of this Component.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def for_use_by(self):
        """Gets the for_use_by of this Component.  # noqa: E501

        Name and version of the component consumer.  # noqa: E501

        :return: The for_use_by of this Component.  # noqa: E501
        :rtype: str
        """
        return self._for_use_by

    @for_use_by.setter
    def for_use_by(self, for_use_by):
        """Sets the for_use_by of this Component.

        Name and version of the component consumer.  # noqa: E501

        :param for_use_by: The for_use_by of this Component.  # noqa: E501
        :type: str
        """

        self._for_use_by = for_use_by

    @property
    def platform(self):
        """Gets the platform of this Component.  # noqa: E501

        Platform of the component.  # noqa: E501

        :return: The platform of this Component.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Component.

        Platform of the component.  # noqa: E501

        :param platform: The platform of this Component.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def version(self):
        """Gets the version of this Component.  # noqa: E501

        Version of the component.  # noqa: E501

        :return: The version of this Component.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Component.

        Version of the component.  # noqa: E501

        :param version: The version of this Component.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def latest(self):
        """Gets the latest of this Component.  # noqa: E501

        True if the component is the latest version.  # noqa: E501

        :return: The latest of this Component.  # noqa: E501
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this Component.

        True if the component is the latest version.  # noqa: E501

        :param latest: The latest of this Component.  # noqa: E501
        :type: bool
        """

        self._latest = latest

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
        if issubclass(Component, dict):
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
        if not isinstance(other, Component):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

