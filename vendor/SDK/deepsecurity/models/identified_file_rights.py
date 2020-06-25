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


class IdentifiedFileRights(object):
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
        'can_delete_identified_files': 'bool',
        'can_download_identified_files': 'bool',
        'can_restore_identified_files': 'bool',
        'can_submit_identified_files': 'bool'
    }

    attribute_map = {
        'can_delete_identified_files': 'canDeleteIdentifiedFiles',
        'can_download_identified_files': 'canDownloadIdentifiedFiles',
        'can_restore_identified_files': 'canRestoreIdentifiedFiles',
        'can_submit_identified_files': 'canSubmitIdentifiedFiles'
    }

    def __init__(self, can_delete_identified_files=None, can_download_identified_files=None, can_restore_identified_files=None, can_submit_identified_files=None):  # noqa: E501
        """IdentifiedFileRights - a model defined in Swagger"""  # noqa: E501

        self._can_delete_identified_files = None
        self._can_download_identified_files = None
        self._can_restore_identified_files = None
        self._can_submit_identified_files = None
        self.discriminator = None

        if can_delete_identified_files is not None:
            self.can_delete_identified_files = can_delete_identified_files
        if can_download_identified_files is not None:
            self.can_download_identified_files = can_download_identified_files
        if can_restore_identified_files is not None:
            self.can_restore_identified_files = can_restore_identified_files
        if can_submit_identified_files is not None:
            self.can_submit_identified_files = can_submit_identified_files

    @property
    def can_delete_identified_files(self):
        """Gets the can_delete_identified_files of this IdentifiedFileRights.  # noqa: E501

        Right to delete identified files.  # noqa: E501

        :return: The can_delete_identified_files of this IdentifiedFileRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_identified_files

    @can_delete_identified_files.setter
    def can_delete_identified_files(self, can_delete_identified_files):
        """Sets the can_delete_identified_files of this IdentifiedFileRights.

        Right to delete identified files.  # noqa: E501

        :param can_delete_identified_files: The can_delete_identified_files of this IdentifiedFileRights.  # noqa: E501
        :type: bool
        """

        self._can_delete_identified_files = can_delete_identified_files

    @property
    def can_download_identified_files(self):
        """Gets the can_download_identified_files of this IdentifiedFileRights.  # noqa: E501

        Right to download identified files.  # noqa: E501

        :return: The can_download_identified_files of this IdentifiedFileRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_download_identified_files

    @can_download_identified_files.setter
    def can_download_identified_files(self, can_download_identified_files):
        """Sets the can_download_identified_files of this IdentifiedFileRights.

        Right to download identified files.  # noqa: E501

        :param can_download_identified_files: The can_download_identified_files of this IdentifiedFileRights.  # noqa: E501
        :type: bool
        """

        self._can_download_identified_files = can_download_identified_files

    @property
    def can_restore_identified_files(self):
        """Gets the can_restore_identified_files of this IdentifiedFileRights.  # noqa: E501

        Right to restore identified files.  # noqa: E501

        :return: The can_restore_identified_files of this IdentifiedFileRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_restore_identified_files

    @can_restore_identified_files.setter
    def can_restore_identified_files(self, can_restore_identified_files):
        """Sets the can_restore_identified_files of this IdentifiedFileRights.

        Right to restore identified files.  # noqa: E501

        :param can_restore_identified_files: The can_restore_identified_files of this IdentifiedFileRights.  # noqa: E501
        :type: bool
        """

        self._can_restore_identified_files = can_restore_identified_files

    @property
    def can_submit_identified_files(self):
        """Gets the can_submit_identified_files of this IdentifiedFileRights.  # noqa: E501

        Right to submit identified files to Deep Discovery Analyzer.  # noqa: E501

        :return: The can_submit_identified_files of this IdentifiedFileRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_submit_identified_files

    @can_submit_identified_files.setter
    def can_submit_identified_files(self, can_submit_identified_files):
        """Sets the can_submit_identified_files of this IdentifiedFileRights.

        Right to submit identified files to Deep Discovery Analyzer.  # noqa: E501

        :param can_submit_identified_files: The can_submit_identified_files of this IdentifiedFileRights.  # noqa: E501
        :type: bool
        """

        self._can_submit_identified_files = can_submit_identified_files

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
        if issubclass(IdentifiedFileRights, dict):
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
        if not isinstance(other, IdentifiedFileRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

