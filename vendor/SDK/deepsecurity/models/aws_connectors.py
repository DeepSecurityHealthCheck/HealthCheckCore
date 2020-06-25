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

from deepsecurity.models.aws_connector import AWSConnector  # noqa: F401,E501


class AWSConnectors(object):
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
        'aws_connectors': 'list[AWSConnector]'
    }

    attribute_map = {
        'aws_connectors': 'awsConnectors'
    }

    def __init__(self, aws_connectors=None):  # noqa: E501
        """AWSConnectors - a model defined in Swagger"""  # noqa: E501

        self._aws_connectors = None
        self.discriminator = None

        if aws_connectors is not None:
            self.aws_connectors = aws_connectors

    @property
    def aws_connectors(self):
        """Gets the aws_connectors of this AWSConnectors.  # noqa: E501


        :return: The aws_connectors of this AWSConnectors.  # noqa: E501
        :rtype: list[AWSConnector]
        """
        return self._aws_connectors

    @aws_connectors.setter
    def aws_connectors(self, aws_connectors):
        """Sets the aws_connectors of this AWSConnectors.


        :param aws_connectors: The aws_connectors of this AWSConnectors.  # noqa: E501
        :type: list[AWSConnector]
        """

        self._aws_connectors = aws_connectors

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
        if issubclass(AWSConnectors, dict):
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
        if not isinstance(other, AWSConnectors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
