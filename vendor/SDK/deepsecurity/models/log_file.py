# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 12.5.969
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LogFile(object):
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
        'location': 'str',
        'format': 'str'
    }

    attribute_map = {
        'location': 'location',
        'format': 'format'
    }

    def __init__(self, location=None, format=None):  # noqa: E501
        """LogFile - a model defined in Swagger"""  # noqa: E501

        self._location = None
        self._format = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if format is not None:
            self.format = format

    @property
    def location(self):
        """Gets the location of this LogFile.  # noqa: E501

        File path of the log file.  # noqa: E501

        :return: The location of this LogFile.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this LogFile.

        File path of the log file.  # noqa: E501

        :param location: The location of this LogFile.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def format(self):
        """Gets the format of this LogFile.  # noqa: E501

        Structure of the data in the log file. The application that generates the log file defines the structure of the data.  # noqa: E501

        :return: The format of this LogFile.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this LogFile.

        Structure of the data in the log file. The application that generates the log file defines the structure of the data.  # noqa: E501

        :param format: The format of this LogFile.  # noqa: E501
        :type: str
        """
        allowed_values = ["syslog", "snort-full", "snort-fast", "apache", "iis", "squid", "nmapg", "mysql-log", "postgresql-log", "dbj-multilog", "eventlog", "single-line-text-log"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

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
        if issubclass(LogFile, dict):
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
        if not isinstance(other, LogFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

