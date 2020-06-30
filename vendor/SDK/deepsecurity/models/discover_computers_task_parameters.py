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


class DiscoverComputersTaskParameters(object):
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
        'discovery_type': 'str',
        'ip': 'str',
        'scan_discovered_computers': 'bool',
        'resolve_ips': 'bool',
        'computer_group_id': 'int',
        'ipmask': 'str',
        'iprange_low': 'str',
        'iprange_high': 'str'
    }

    attribute_map = {
        'discovery_type': 'discoveryType',
        'ip': 'ip',
        'scan_discovered_computers': 'scanDiscoveredComputers',
        'resolve_ips': 'resolveIPs',
        'computer_group_id': 'computerGroupID',
        'ipmask': 'ipmask',
        'iprange_low': 'iprangeLow',
        'iprange_high': 'iprangeHigh'
    }

    def __init__(self, discovery_type=None, ip=None, scan_discovered_computers=None, resolve_ips=None, computer_group_id=None, ipmask=None, iprange_low=None, iprange_high=None):  # noqa: E501
        """DiscoverComputersTaskParameters - a model defined in Swagger"""  # noqa: E501

        self._discovery_type = None
        self._ip = None
        self._scan_discovered_computers = None
        self._resolve_ips = None
        self._computer_group_id = None
        self._ipmask = None
        self._iprange_low = None
        self._iprange_high = None
        self.discriminator = None

        if discovery_type is not None:
            self.discovery_type = discovery_type
        if ip is not None:
            self.ip = ip
        if scan_discovered_computers is not None:
            self.scan_discovered_computers = scan_discovered_computers
        if resolve_ips is not None:
            self.resolve_ips = resolve_ips
        if computer_group_id is not None:
            self.computer_group_id = computer_group_id
        if ipmask is not None:
            self.ipmask = ipmask
        if iprange_low is not None:
            self.iprange_low = iprange_low
        if iprange_high is not None:
            self.iprange_high = iprange_high

    @property
    def discovery_type(self):
        """Gets the discovery_type of this DiscoverComputersTaskParameters.  # noqa: E501

        Discovery type. Default \"masked-ip\".  # noqa: E501

        :return: The discovery_type of this DiscoverComputersTaskParameters.  # noqa: E501
        :rtype: str
        """
        return self._discovery_type

    @discovery_type.setter
    def discovery_type(self, discovery_type):
        """Sets the discovery_type of this DiscoverComputersTaskParameters.

        Discovery type. Default \"masked-ip\".  # noqa: E501

        :param discovery_type: The discovery_type of this DiscoverComputersTaskParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["range", "masked-ip"]  # noqa: E501
        if discovery_type not in allowed_values:
            raise ValueError(
                "Invalid value for `discovery_type` ({0}), must be one of {1}"  # noqa: E501
                .format(discovery_type, allowed_values)
            )

        self._discovery_type = discovery_type

    @property
    def ip(self):
        """Gets the ip of this DiscoverComputersTaskParameters.  # noqa: E501

        IP address for masked-ip search.  # noqa: E501

        :return: The ip of this DiscoverComputersTaskParameters.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DiscoverComputersTaskParameters.

        IP address for masked-ip search.  # noqa: E501

        :param ip: The ip of this DiscoverComputersTaskParameters.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def scan_discovered_computers(self):
        """Gets the scan_discovered_computers of this DiscoverComputersTaskParameters.  # noqa: E501

        Automatically perform a port scan of discovered computers. Default false. Set true to enable.  # noqa: E501

        :return: The scan_discovered_computers of this DiscoverComputersTaskParameters.  # noqa: E501
        :rtype: bool
        """
        return self._scan_discovered_computers

    @scan_discovered_computers.setter
    def scan_discovered_computers(self, scan_discovered_computers):
        """Sets the scan_discovered_computers of this DiscoverComputersTaskParameters.

        Automatically perform a port scan of discovered computers. Default false. Set true to enable.  # noqa: E501

        :param scan_discovered_computers: The scan_discovered_computers of this DiscoverComputersTaskParameters.  # noqa: E501
        :type: bool
        """

        self._scan_discovered_computers = scan_discovered_computers

    @property
    def resolve_ips(self):
        """Gets the resolve_ips of this DiscoverComputersTaskParameters.  # noqa: E501

        Automatically resolve IPs to hostnames. Default true. Set false to disable.  # noqa: E501

        :return: The resolve_ips of this DiscoverComputersTaskParameters.  # noqa: E501
        :rtype: bool
        """
        return self._resolve_ips

    @resolve_ips.setter
    def resolve_ips(self, resolve_ips):
        """Sets the resolve_ips of this DiscoverComputersTaskParameters.

        Automatically resolve IPs to hostnames. Default true. Set false to disable.  # noqa: E501

        :param resolve_ips: The resolve_ips of this DiscoverComputersTaskParameters.  # noqa: E501
        :type: bool
        """

        self._resolve_ips = resolve_ips

    @property
    def computer_group_id(self):
        """Gets the computer_group_id of this DiscoverComputersTaskParameters.  # noqa: E501

        ID of computer group that discovered computers will be added to, or null for no group.  # noqa: E501

        :return: The computer_group_id of this DiscoverComputersTaskParameters.  # noqa: E501
        :rtype: int
        """
        return self._computer_group_id

    @computer_group_id.setter
    def computer_group_id(self, computer_group_id):
        """Sets the computer_group_id of this DiscoverComputersTaskParameters.

        ID of computer group that discovered computers will be added to, or null for no group.  # noqa: E501

        :param computer_group_id: The computer_group_id of this DiscoverComputersTaskParameters.  # noqa: E501
        :type: int
        """

        self._computer_group_id = computer_group_id

    @property
    def ipmask(self):
        """Gets the ipmask of this DiscoverComputersTaskParameters.  # noqa: E501


        :return: The ipmask of this DiscoverComputersTaskParameters.  # noqa: E501
        :rtype: str
        """
        return self._ipmask

    @ipmask.setter
    def ipmask(self, ipmask):
        """Sets the ipmask of this DiscoverComputersTaskParameters.


        :param ipmask: The ipmask of this DiscoverComputersTaskParameters.  # noqa: E501
        :type: str
        """

        self._ipmask = ipmask

    @property
    def iprange_low(self):
        """Gets the iprange_low of this DiscoverComputersTaskParameters.  # noqa: E501


        :return: The iprange_low of this DiscoverComputersTaskParameters.  # noqa: E501
        :rtype: str
        """
        return self._iprange_low

    @iprange_low.setter
    def iprange_low(self, iprange_low):
        """Sets the iprange_low of this DiscoverComputersTaskParameters.


        :param iprange_low: The iprange_low of this DiscoverComputersTaskParameters.  # noqa: E501
        :type: str
        """

        self._iprange_low = iprange_low

    @property
    def iprange_high(self):
        """Gets the iprange_high of this DiscoverComputersTaskParameters.  # noqa: E501


        :return: The iprange_high of this DiscoverComputersTaskParameters.  # noqa: E501
        :rtype: str
        """
        return self._iprange_high

    @iprange_high.setter
    def iprange_high(self, iprange_high):
        """Sets the iprange_high of this DiscoverComputersTaskParameters.


        :param iprange_high: The iprange_high of this DiscoverComputersTaskParameters.  # noqa: E501
        :type: str
        """

        self._iprange_high = iprange_high

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
        if issubclass(DiscoverComputersTaskParameters, dict):
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
        if not isinstance(other, DiscoverComputersTaskParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

