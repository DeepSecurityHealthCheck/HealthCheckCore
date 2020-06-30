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


class VcloudVMVirtualMachineSummary(object):
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
        'cloud_provider': 'str',
        'operating_system': 'str',
        'instance_id': 'str',
        'type': 'str',
        'state': 'str',
        'ip_address': 'str',
        'dns_name': 'str'
    }

    attribute_map = {
        'cloud_provider': 'cloudProvider',
        'operating_system': 'operatingSystem',
        'instance_id': 'instanceID',
        'type': 'type',
        'state': 'state',
        'ip_address': 'IPAddress',
        'dns_name': 'DNSName'
    }

    def __init__(self, cloud_provider=None, operating_system=None, instance_id=None, type=None, state=None, ip_address=None, dns_name=None):  # noqa: E501
        """VcloudVMVirtualMachineSummary - a model defined in Swagger"""  # noqa: E501

        self._cloud_provider = None
        self._operating_system = None
        self._instance_id = None
        self._type = None
        self._state = None
        self._ip_address = None
        self._dns_name = None
        self.discriminator = None

        if cloud_provider is not None:
            self.cloud_provider = cloud_provider
        if operating_system is not None:
            self.operating_system = operating_system
        if instance_id is not None:
            self.instance_id = instance_id
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if ip_address is not None:
            self.ip_address = ip_address
        if dns_name is not None:
            self.dns_name = dns_name

    @property
    def cloud_provider(self):
        """Gets the cloud_provider of this VcloudVMVirtualMachineSummary.  # noqa: E501

        Cloud provider: \"vCloud\".  # noqa: E501

        :return: The cloud_provider of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, cloud_provider):
        """Sets the cloud_provider of this VcloudVMVirtualMachineSummary.

        Cloud provider: \"vCloud\".  # noqa: E501

        :param cloud_provider: The cloud_provider of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._cloud_provider = cloud_provider

    @property
    def operating_system(self):
        """Gets the operating_system of this VcloudVMVirtualMachineSummary.  # noqa: E501

        Operating system, for example: \"Microsoft Windows Server 2012 (64-bit)\". Searchable as String.  # noqa: E501

        :return: The operating_system of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this VcloudVMVirtualMachineSummary.

        Operating system, for example: \"Microsoft Windows Server 2012 (64-bit)\". Searchable as String.  # noqa: E501

        :param operating_system: The operating_system of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

    @property
    def instance_id(self):
        """Gets the instance_id of this VcloudVMVirtualMachineSummary.  # noqa: E501

        Instance ID. Searchable as String.  # noqa: E501

        :return: The instance_id of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this VcloudVMVirtualMachineSummary.

        Instance ID. Searchable as String.  # noqa: E501

        :param instance_id: The instance_id of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this VcloudVMVirtualMachineSummary.  # noqa: E501

        Hardware type. Searchable as String.  # noqa: E501

        :return: The type of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VcloudVMVirtualMachineSummary.

        Hardware type. Searchable as String.  # noqa: E501

        :param type: The type of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def state(self):
        """Gets the state of this VcloudVMVirtualMachineSummary.  # noqa: E501

        Power state, for example: \"Powered On\".  # noqa: E501

        :return: The state of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VcloudVMVirtualMachineSummary.

        Power state, for example: \"Powered On\".  # noqa: E501

        :param state: The state of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def ip_address(self):
        """Gets the ip_address of this VcloudVMVirtualMachineSummary.  # noqa: E501


        :return: The ip_address of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this VcloudVMVirtualMachineSummary.


        :param ip_address: The ip_address of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def dns_name(self):
        """Gets the dns_name of this VcloudVMVirtualMachineSummary.  # noqa: E501


        :return: The dns_name of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this VcloudVMVirtualMachineSummary.


        :param dns_name: The dns_name of this VcloudVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._dns_name = dns_name

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
        if issubclass(VcloudVMVirtualMachineSummary, dict):
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
        if not isinstance(other, VcloudVMVirtualMachineSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

