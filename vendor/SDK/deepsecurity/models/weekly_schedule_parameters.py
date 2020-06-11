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


class WeeklyScheduleParameters(object):
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
        'start_time': 'int',
        'interval': 'int',
        'days': 'list[str]'
    }

    attribute_map = {
        'start_time': 'startTime',
        'interval': 'interval',
        'days': 'days'
    }

    def __init__(self, start_time=None, interval=None, days=None):  # noqa: E501
        """WeeklyScheduleParameters - a model defined in Swagger"""  # noqa: E501

        self._start_time = None
        self._interval = None
        self._days = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if interval is not None:
            self.interval = interval
        if days is not None:
            self.days = days

    @property
    def start_time(self):
        """Gets the start_time of this WeeklyScheduleParameters.  # noqa: E501

        Date/Time when the task should run.  # noqa: E501

        :return: The start_time of this WeeklyScheduleParameters.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WeeklyScheduleParameters.

        Date/Time when the task should run.  # noqa: E501

        :param start_time: The start_time of this WeeklyScheduleParameters.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def interval(self):
        """Gets the interval of this WeeklyScheduleParameters.  # noqa: E501

        Number of weeks between recurrences.  # noqa: E501

        :return: The interval of this WeeklyScheduleParameters.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this WeeklyScheduleParameters.

        Number of weeks between recurrences.  # noqa: E501

        :param interval: The interval of this WeeklyScheduleParameters.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def days(self):
        """Gets the days of this WeeklyScheduleParameters.  # noqa: E501

        Days of the week when the scheduled task will run.  # noqa: E501

        :return: The days of this WeeklyScheduleParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this WeeklyScheduleParameters.

        Days of the week when the scheduled task will run.  # noqa: E501

        :param days: The days of this WeeklyScheduleParameters.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]  # noqa: E501
        if not set(days).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `days` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(days) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._days = days

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
        if issubclass(WeeklyScheduleParameters, dict):
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
        if not isinstance(other, WeeklyScheduleParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

