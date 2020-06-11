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


class HourlyScheduleParameters(object):
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
        'minutes_past_the_hour': 'str'
    }

    attribute_map = {
        'minutes_past_the_hour': 'minutesPastTheHour'
    }

    def __init__(self, minutes_past_the_hour=None):  # noqa: E501
        """HourlyScheduleParameters - a model defined in Swagger"""  # noqa: E501

        self._minutes_past_the_hour = None
        self.discriminator = None

        if minutes_past_the_hour is not None:
            self.minutes_past_the_hour = minutes_past_the_hour

    @property
    def minutes_past_the_hour(self):
        """Gets the minutes_past_the_hour of this HourlyScheduleParameters.  # noqa: E501

        Minutes past the hour when the task should run.  # noqa: E501

        :return: The minutes_past_the_hour of this HourlyScheduleParameters.  # noqa: E501
        :rtype: str
        """
        return self._minutes_past_the_hour

    @minutes_past_the_hour.setter
    def minutes_past_the_hour(self, minutes_past_the_hour):
        """Sets the minutes_past_the_hour of this HourlyScheduleParameters.

        Minutes past the hour when the task should run.  # noqa: E501

        :param minutes_past_the_hour: The minutes_past_the_hour of this HourlyScheduleParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["0", "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]  # noqa: E501
        if minutes_past_the_hour not in allowed_values:
            raise ValueError(
                "Invalid value for `minutes_past_the_hour` ({0}), must be one of {1}"  # noqa: E501
                .format(minutes_past_the_hour, allowed_values)
            )

        self._minutes_past_the_hour = minutes_past_the_hour

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
        if issubclass(HourlyScheduleParameters, dict):
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
        if not isinstance(other, HourlyScheduleParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

