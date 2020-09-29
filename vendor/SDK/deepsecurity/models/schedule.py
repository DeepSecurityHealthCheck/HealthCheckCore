# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.186
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Schedule(object):
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
        'description': 'str',
        'hours_of_week': 'list[bool]',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'hours_of_week': 'hoursOfWeek',
        'id': 'ID'
    }

    def __init__(self, name=None, description=None, hours_of_week=None, id=None):  # noqa: E501
        """Schedule - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._hours_of_week = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if hours_of_week is not None:
            self.hours_of_week = hours_of_week
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this Schedule.  # noqa: E501

        Display name of the Schedule. Searchable as String.  # noqa: E501

        :return: The name of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Schedule.

        Display name of the Schedule. Searchable as String.  # noqa: E501

        :param name: The name of this Schedule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Schedule.  # noqa: E501

        Description of the Schedule. Searchable as String.  # noqa: E501

        :return: The description of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Schedule.

        Description of the Schedule. Searchable as String.  # noqa: E501

        :param description: The description of this Schedule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hours_of_week(self):
        """Gets the hours_of_week of this Schedule.  # noqa: E501

        An array of 168 boolean values representing each hour in the week starting Sunday at 0:00. A value of 'true' marks the given hour as 'on'.  # noqa: E501

        :return: The hours_of_week of this Schedule.  # noqa: E501
        :rtype: list[bool]
        """
        return self._hours_of_week

    @hours_of_week.setter
    def hours_of_week(self, hours_of_week):
        """Sets the hours_of_week of this Schedule.

        An array of 168 boolean values representing each hour in the week starting Sunday at 0:00. A value of 'true' marks the given hour as 'on'.  # noqa: E501

        :param hours_of_week: The hours_of_week of this Schedule.  # noqa: E501
        :type: list[bool]
        """

        self._hours_of_week = hours_of_week

    @property
    def id(self):
        """Gets the id of this Schedule.  # noqa: E501

        ID of the Schedule. Searchable as ID.  # noqa: E501

        :return: The id of this Schedule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Schedule.

        ID of the Schedule. Searchable as ID.  # noqa: E501

        :param id: The id of this Schedule.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(Schedule, dict):
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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

