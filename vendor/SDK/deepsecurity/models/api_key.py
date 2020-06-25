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


class ApiKey(object):
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
        'key_name': 'str',
        'description': 'str',
        'locale': 'str',
        'role_id': 'int',
        'time_zone': 'str',
        'active': 'bool',
        'created': 'int',
        'last_sign_in': 'int',
        'unlock_time': 'int',
        'unsuccessful_sign_in_attempts': 'int',
        'expiry_date': 'int',
        'secret_key': 'str',
        'service_account': 'bool',
        'id': 'int'
    }

    attribute_map = {
        'key_name': 'keyName',
        'description': 'description',
        'locale': 'locale',
        'role_id': 'roleID',
        'time_zone': 'timeZone',
        'active': 'active',
        'created': 'created',
        'last_sign_in': 'lastSignIn',
        'unlock_time': 'unlockTime',
        'unsuccessful_sign_in_attempts': 'unsuccessfulSignInAttempts',
        'expiry_date': 'expiryDate',
        'secret_key': 'secretKey',
        'service_account': 'serviceAccount',
        'id': 'ID'
    }

    def __init__(self, key_name=None, description=None, locale=None, role_id=None, time_zone=None, active=None, created=None, last_sign_in=None, unlock_time=None, unsuccessful_sign_in_attempts=None, expiry_date=None, secret_key=None, service_account=None, id=None):  # noqa: E501
        """ApiKey - a model defined in Swagger"""  # noqa: E501

        self._key_name = None
        self._description = None
        self._locale = None
        self._role_id = None
        self._time_zone = None
        self._active = None
        self._created = None
        self._last_sign_in = None
        self._unlock_time = None
        self._unsuccessful_sign_in_attempts = None
        self._expiry_date = None
        self._secret_key = None
        self._service_account = None
        self._id = None
        self.discriminator = None

        if key_name is not None:
            self.key_name = key_name
        if description is not None:
            self.description = description
        if locale is not None:
            self.locale = locale
        if role_id is not None:
            self.role_id = role_id
        if time_zone is not None:
            self.time_zone = time_zone
        if active is not None:
            self.active = active
        if created is not None:
            self.created = created
        if last_sign_in is not None:
            self.last_sign_in = last_sign_in
        if unlock_time is not None:
            self.unlock_time = unlock_time
        if unsuccessful_sign_in_attempts is not None:
            self.unsuccessful_sign_in_attempts = unsuccessful_sign_in_attempts
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if secret_key is not None:
            self.secret_key = secret_key
        if service_account is not None:
            self.service_account = service_account
        if id is not None:
            self.id = id

    @property
    def key_name(self):
        """Gets the key_name of this ApiKey.  # noqa: E501

        Display name of the APIKey. Searchable as String.  # noqa: E501

        :return: The key_name of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this ApiKey.

        Display name of the APIKey. Searchable as String.  # noqa: E501

        :param key_name: The key_name of this ApiKey.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def description(self):
        """Gets the description of this ApiKey.  # noqa: E501

        Description of the APIKey. Searchable as String.  # noqa: E501

        :return: The description of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiKey.

        Description of the APIKey. Searchable as String.  # noqa: E501

        :param description: The description of this ApiKey.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def locale(self):
        """Gets the locale of this ApiKey.  # noqa: E501

        Country and language for the APIKey.  # noqa: E501

        :return: The locale of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this ApiKey.

        Country and language for the APIKey.  # noqa: E501

        :param locale: The locale of this ApiKey.  # noqa: E501
        :type: str
        """
        allowed_values = ["en-US", "ja-JP"]  # noqa: E501
        if locale not in allowed_values:
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

    @property
    def role_id(self):
        """Gets the role_id of this ApiKey.  # noqa: E501

        ID of the role assigned to the APIKey. Searchable as Numeric.  # noqa: E501

        :return: The role_id of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this ApiKey.

        ID of the role assigned to the APIKey. Searchable as Numeric.  # noqa: E501

        :param role_id: The role_id of this ApiKey.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def time_zone(self):
        """Gets the time_zone of this ApiKey.  # noqa: E501

        Display name of the APIKey's time zone, e.g. America/New_York. Searchable as String.  # noqa: E501

        :return: The time_zone of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ApiKey.

        Display name of the APIKey's time zone, e.g. America/New_York. Searchable as String.  # noqa: E501

        :param time_zone: The time_zone of this ApiKey.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def active(self):
        """Gets the active of this ApiKey.  # noqa: E501

        If true, the APIKey can be used to authenticate. If false, the APIKey is locked out. Searchable as Boolean.  # noqa: E501

        :return: The active of this ApiKey.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ApiKey.

        If true, the APIKey can be used to authenticate. If false, the APIKey is locked out. Searchable as Boolean.  # noqa: E501

        :param active: The active of this ApiKey.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created(self):
        """Gets the created of this ApiKey.  # noqa: E501

        Timestamp of the APIKey's creation, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :return: The created of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApiKey.

        Timestamp of the APIKey's creation, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :param created: The created of this ApiKey.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def last_sign_in(self):
        """Gets the last_sign_in of this ApiKey.  # noqa: E501

        Timestamp of the APIKey's last successful authentication, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :return: The last_sign_in of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._last_sign_in

    @last_sign_in.setter
    def last_sign_in(self, last_sign_in):
        """Sets the last_sign_in of this ApiKey.

        Timestamp of the APIKey's last successful authentication, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :param last_sign_in: The last_sign_in of this ApiKey.  # noqa: E501
        :type: int
        """

        self._last_sign_in = last_sign_in

    @property
    def unlock_time(self):
        """Gets the unlock_time of this ApiKey.  # noqa: E501

        Timestamp of when a locked out APIKey will be unlocked, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :return: The unlock_time of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._unlock_time

    @unlock_time.setter
    def unlock_time(self, unlock_time):
        """Sets the unlock_time of this ApiKey.

        Timestamp of when a locked out APIKey will be unlocked, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :param unlock_time: The unlock_time of this ApiKey.  # noqa: E501
        :type: int
        """

        self._unlock_time = unlock_time

    @property
    def unsuccessful_sign_in_attempts(self):
        """Gets the unsuccessful_sign_in_attempts of this ApiKey.  # noqa: E501

        Number of unsuccessful authentication attempts made since the last successful authentication. Searchable as Numeric.  # noqa: E501

        :return: The unsuccessful_sign_in_attempts of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._unsuccessful_sign_in_attempts

    @unsuccessful_sign_in_attempts.setter
    def unsuccessful_sign_in_attempts(self, unsuccessful_sign_in_attempts):
        """Sets the unsuccessful_sign_in_attempts of this ApiKey.

        Number of unsuccessful authentication attempts made since the last successful authentication. Searchable as Numeric.  # noqa: E501

        :param unsuccessful_sign_in_attempts: The unsuccessful_sign_in_attempts of this ApiKey.  # noqa: E501
        :type: int
        """

        self._unsuccessful_sign_in_attempts = unsuccessful_sign_in_attempts

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ApiKey.  # noqa: E501

        Timestamp of the APIKey's expiry date, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :return: The expiry_date of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ApiKey.

        Timestamp of the APIKey's expiry date, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :param expiry_date: The expiry_date of this ApiKey.  # noqa: E501
        :type: int
        """

        self._expiry_date = expiry_date

    @property
    def secret_key(self):
        """Gets the secret_key of this ApiKey.  # noqa: E501

        Secret key used to authenticate API requests. Only returned when creating a new APIKey or regenerating the secret key.  # noqa: E501

        :return: The secret_key of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this ApiKey.

        Secret key used to authenticate API requests. Only returned when creating a new APIKey or regenerating the secret key.  # noqa: E501

        :param secret_key: The secret_key of this ApiKey.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def service_account(self):
        """Gets the service_account of this ApiKey.  # noqa: E501

        If true, the APIKey was created by the primary tenant (T0) to authenticate API calls against other tenants' databases. Searchable as Boolean.  # noqa: E501

        :return: The service_account of this ApiKey.  # noqa: E501
        :rtype: bool
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """Sets the service_account of this ApiKey.

        If true, the APIKey was created by the primary tenant (T0) to authenticate API calls against other tenants' databases. Searchable as Boolean.  # noqa: E501

        :param service_account: The service_account of this ApiKey.  # noqa: E501
        :type: bool
        """

        self._service_account = service_account

    @property
    def id(self):
        """Gets the id of this ApiKey.  # noqa: E501

        ID of the APIKey. Searchable as ID.  # noqa: E501

        :return: The id of this ApiKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiKey.

        ID of the APIKey. Searchable as ID.  # noqa: E501

        :param id: The id of this ApiKey.  # noqa: E501
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
        if issubclass(ApiKey, dict):
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
        if not isinstance(other, ApiKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
