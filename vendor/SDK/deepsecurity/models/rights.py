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

from deepsecurity.models.anti_malware_rights import AntiMalwareRights  # noqa: F401,E501
from deepsecurity.models.application_control_rights import ApplicationControlRights  # noqa: F401,E501
from deepsecurity.models.aws_marketplace_rights import AwsMarketplaceRights  # noqa: F401,E501
from deepsecurity.models.firewall_rights import FirewallRights  # noqa: F401,E501
from deepsecurity.models.hosted_service_rights import HostedServiceRights  # noqa: F401,E501
from deepsecurity.models.integrity_monitoring_rights import IntegrityMonitoringRights  # noqa: F401,E501
from deepsecurity.models.intrusion_prevention_rights import IntrusionPreventionRights  # noqa: F401,E501
from deepsecurity.models.log_inspection_rights import LogInspectionRights  # noqa: F401,E501
from deepsecurity.models.platform_rights import PlatformRights  # noqa: F401,E501
from deepsecurity.models.sensing_mode_rights import SensingModeRights  # noqa: F401,E501
from deepsecurity.models.web_reputation_rights import WebReputationRights  # noqa: F401,E501


class Rights(object):
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
        'platform_rights': 'PlatformRights',
        'anti_malware_rights': 'AntiMalwareRights',
        'web_reputation_rights': 'WebReputationRights',
        'sensing_mode_rights': 'SensingModeRights',
        'firewall_rights': 'FirewallRights',
        'intrusion_prevention_rights': 'IntrusionPreventionRights',
        'integrity_monitoring_rights': 'IntegrityMonitoringRights',
        'log_inspection_rights': 'LogInspectionRights',
        'application_control_rights': 'ApplicationControlRights',
        'hosted_service_rights': 'HostedServiceRights',
        'awsmarketplace_rights': 'AwsMarketplaceRights'
    }

    attribute_map = {
        'platform_rights': 'platformRights',
        'anti_malware_rights': 'antiMalwareRights',
        'web_reputation_rights': 'webReputationRights',
        'sensing_mode_rights': 'sensingModeRights',
        'firewall_rights': 'firewallRights',
        'intrusion_prevention_rights': 'intrusionPreventionRights',
        'integrity_monitoring_rights': 'integrityMonitoringRights',
        'log_inspection_rights': 'logInspectionRights',
        'application_control_rights': 'applicationControlRights',
        'hosted_service_rights': 'hostedServiceRights',
        'awsmarketplace_rights': 'awsmarketplaceRights'
    }

    def __init__(self, platform_rights=None, anti_malware_rights=None, web_reputation_rights=None, sensing_mode_rights=None, firewall_rights=None, intrusion_prevention_rights=None, integrity_monitoring_rights=None, log_inspection_rights=None, application_control_rights=None, hosted_service_rights=None, awsmarketplace_rights=None):  # noqa: E501
        """Rights - a model defined in Swagger"""  # noqa: E501

        self._platform_rights = None
        self._anti_malware_rights = None
        self._web_reputation_rights = None
        self._sensing_mode_rights = None
        self._firewall_rights = None
        self._intrusion_prevention_rights = None
        self._integrity_monitoring_rights = None
        self._log_inspection_rights = None
        self._application_control_rights = None
        self._hosted_service_rights = None
        self._awsmarketplace_rights = None
        self.discriminator = None

        if platform_rights is not None:
            self.platform_rights = platform_rights
        if anti_malware_rights is not None:
            self.anti_malware_rights = anti_malware_rights
        if web_reputation_rights is not None:
            self.web_reputation_rights = web_reputation_rights
        if sensing_mode_rights is not None:
            self.sensing_mode_rights = sensing_mode_rights
        if firewall_rights is not None:
            self.firewall_rights = firewall_rights
        if intrusion_prevention_rights is not None:
            self.intrusion_prevention_rights = intrusion_prevention_rights
        if integrity_monitoring_rights is not None:
            self.integrity_monitoring_rights = integrity_monitoring_rights
        if log_inspection_rights is not None:
            self.log_inspection_rights = log_inspection_rights
        if application_control_rights is not None:
            self.application_control_rights = application_control_rights
        if hosted_service_rights is not None:
            self.hosted_service_rights = hosted_service_rights
        if awsmarketplace_rights is not None:
            self.awsmarketplace_rights = awsmarketplace_rights

    @property
    def platform_rights(self):
        """Gets the platform_rights of this Rights.  # noqa: E501

        Platform rights.  # noqa: E501

        :return: The platform_rights of this Rights.  # noqa: E501
        :rtype: PlatformRights
        """
        return self._platform_rights

    @platform_rights.setter
    def platform_rights(self, platform_rights):
        """Sets the platform_rights of this Rights.

        Platform rights.  # noqa: E501

        :param platform_rights: The platform_rights of this Rights.  # noqa: E501
        :type: PlatformRights
        """

        self._platform_rights = platform_rights

    @property
    def anti_malware_rights(self):
        """Gets the anti_malware_rights of this Rights.  # noqa: E501

        Anti-Malware rights.  # noqa: E501

        :return: The anti_malware_rights of this Rights.  # noqa: E501
        :rtype: AntiMalwareRights
        """
        return self._anti_malware_rights

    @anti_malware_rights.setter
    def anti_malware_rights(self, anti_malware_rights):
        """Sets the anti_malware_rights of this Rights.

        Anti-Malware rights.  # noqa: E501

        :param anti_malware_rights: The anti_malware_rights of this Rights.  # noqa: E501
        :type: AntiMalwareRights
        """

        self._anti_malware_rights = anti_malware_rights

    @property
    def web_reputation_rights(self):
        """Gets the web_reputation_rights of this Rights.  # noqa: E501

        Web Reputation rights.  # noqa: E501

        :return: The web_reputation_rights of this Rights.  # noqa: E501
        :rtype: WebReputationRights
        """
        return self._web_reputation_rights

    @web_reputation_rights.setter
    def web_reputation_rights(self, web_reputation_rights):
        """Sets the web_reputation_rights of this Rights.

        Web Reputation rights.  # noqa: E501

        :param web_reputation_rights: The web_reputation_rights of this Rights.  # noqa: E501
        :type: WebReputationRights
        """

        self._web_reputation_rights = web_reputation_rights

    @property
    def sensing_mode_rights(self):
        """Gets the sensing_mode_rights of this Rights.  # noqa: E501

        Activity Monitoring rights.  # noqa: E501

        :return: The sensing_mode_rights of this Rights.  # noqa: E501
        :rtype: SensingModeRights
        """
        return self._sensing_mode_rights

    @sensing_mode_rights.setter
    def sensing_mode_rights(self, sensing_mode_rights):
        """Sets the sensing_mode_rights of this Rights.

        Activity Monitoring rights.  # noqa: E501

        :param sensing_mode_rights: The sensing_mode_rights of this Rights.  # noqa: E501
        :type: SensingModeRights
        """

        self._sensing_mode_rights = sensing_mode_rights

    @property
    def firewall_rights(self):
        """Gets the firewall_rights of this Rights.  # noqa: E501

        Firewall rights.  # noqa: E501

        :return: The firewall_rights of this Rights.  # noqa: E501
        :rtype: FirewallRights
        """
        return self._firewall_rights

    @firewall_rights.setter
    def firewall_rights(self, firewall_rights):
        """Sets the firewall_rights of this Rights.

        Firewall rights.  # noqa: E501

        :param firewall_rights: The firewall_rights of this Rights.  # noqa: E501
        :type: FirewallRights
        """

        self._firewall_rights = firewall_rights

    @property
    def intrusion_prevention_rights(self):
        """Gets the intrusion_prevention_rights of this Rights.  # noqa: E501

        Intrusion Prevention rights.  # noqa: E501

        :return: The intrusion_prevention_rights of this Rights.  # noqa: E501
        :rtype: IntrusionPreventionRights
        """
        return self._intrusion_prevention_rights

    @intrusion_prevention_rights.setter
    def intrusion_prevention_rights(self, intrusion_prevention_rights):
        """Sets the intrusion_prevention_rights of this Rights.

        Intrusion Prevention rights.  # noqa: E501

        :param intrusion_prevention_rights: The intrusion_prevention_rights of this Rights.  # noqa: E501
        :type: IntrusionPreventionRights
        """

        self._intrusion_prevention_rights = intrusion_prevention_rights

    @property
    def integrity_monitoring_rights(self):
        """Gets the integrity_monitoring_rights of this Rights.  # noqa: E501

        Integrity Monitoring rights.  # noqa: E501

        :return: The integrity_monitoring_rights of this Rights.  # noqa: E501
        :rtype: IntegrityMonitoringRights
        """
        return self._integrity_monitoring_rights

    @integrity_monitoring_rights.setter
    def integrity_monitoring_rights(self, integrity_monitoring_rights):
        """Sets the integrity_monitoring_rights of this Rights.

        Integrity Monitoring rights.  # noqa: E501

        :param integrity_monitoring_rights: The integrity_monitoring_rights of this Rights.  # noqa: E501
        :type: IntegrityMonitoringRights
        """

        self._integrity_monitoring_rights = integrity_monitoring_rights

    @property
    def log_inspection_rights(self):
        """Gets the log_inspection_rights of this Rights.  # noqa: E501

        Log Inspection rights.  # noqa: E501

        :return: The log_inspection_rights of this Rights.  # noqa: E501
        :rtype: LogInspectionRights
        """
        return self._log_inspection_rights

    @log_inspection_rights.setter
    def log_inspection_rights(self, log_inspection_rights):
        """Sets the log_inspection_rights of this Rights.

        Log Inspection rights.  # noqa: E501

        :param log_inspection_rights: The log_inspection_rights of this Rights.  # noqa: E501
        :type: LogInspectionRights
        """

        self._log_inspection_rights = log_inspection_rights

    @property
    def application_control_rights(self):
        """Gets the application_control_rights of this Rights.  # noqa: E501

        Application Control rights.  # noqa: E501

        :return: The application_control_rights of this Rights.  # noqa: E501
        :rtype: ApplicationControlRights
        """
        return self._application_control_rights

    @application_control_rights.setter
    def application_control_rights(self, application_control_rights):
        """Sets the application_control_rights of this Rights.

        Application Control rights.  # noqa: E501

        :param application_control_rights: The application_control_rights of this Rights.  # noqa: E501
        :type: ApplicationControlRights
        """

        self._application_control_rights = application_control_rights

    @property
    def hosted_service_rights(self):
        """Gets the hosted_service_rights of this Rights.  # noqa: E501

        Hosted Service rights.  # noqa: E501

        :return: The hosted_service_rights of this Rights.  # noqa: E501
        :rtype: HostedServiceRights
        """
        return self._hosted_service_rights

    @hosted_service_rights.setter
    def hosted_service_rights(self, hosted_service_rights):
        """Sets the hosted_service_rights of this Rights.

        Hosted Service rights.  # noqa: E501

        :param hosted_service_rights: The hosted_service_rights of this Rights.  # noqa: E501
        :type: HostedServiceRights
        """

        self._hosted_service_rights = hosted_service_rights

    @property
    def awsmarketplace_rights(self):
        """Gets the awsmarketplace_rights of this Rights.  # noqa: E501


        :return: The awsmarketplace_rights of this Rights.  # noqa: E501
        :rtype: AwsMarketplaceRights
        """
        return self._awsmarketplace_rights

    @awsmarketplace_rights.setter
    def awsmarketplace_rights(self, awsmarketplace_rights):
        """Sets the awsmarketplace_rights of this Rights.


        :param awsmarketplace_rights: The awsmarketplace_rights of this Rights.  # noqa: E501
        :type: AwsMarketplaceRights
        """

        self._awsmarketplace_rights = awsmarketplace_rights

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
        if issubclass(Rights, dict):
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
        if not isinstance(other, Rights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
