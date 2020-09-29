# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.186
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class PolicyIntegrityMonitoringRuleAssignmentsRecommendationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_integrity_monitoring_rule_ids_to_policy(self, policy_id, api_version, **kwargs):  # noqa: E501
        """Add Integrity Monitoring Rule IDs  # noqa: E501

        Assign integrity monitoring rule IDs to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_integrity_monitoring_rule_ids_to_policy(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param RuleIDs integrity_monitoring_rule_ids: The ID numbers of the integrity monitoring rules to add.
        :param bool overrides: Return only rule IDs assigned directly to the current policy.
        :return: IntegrityMonitoringAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_integrity_monitoring_rule_ids_to_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.add_integrity_monitoring_rule_ids_to_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
            return data

    def add_integrity_monitoring_rule_ids_to_policy_with_http_info(self, policy_id, api_version, **kwargs):  # noqa: E501
        """Add Integrity Monitoring Rule IDs  # noqa: E501

        Assign integrity monitoring rule IDs to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_integrity_monitoring_rule_ids_to_policy_with_http_info(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param RuleIDs integrity_monitoring_rule_ids: The ID numbers of the integrity monitoring rules to add.
        :param bool overrides: Return only rule IDs assigned directly to the current policy.
        :return: IntegrityMonitoringAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'api_version', 'integrity_monitoring_rule_ids', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_integrity_monitoring_rule_ids_to_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `add_integrity_monitoring_rule_ids_to_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `add_integrity_monitoring_rule_ids_to_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `add_integrity_monitoring_rule_ids_to_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'integrity_monitoring_rule_ids' in params:
            body_params = params['integrity_monitoring_rule_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/integritymonitoring/assignments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrityMonitoringAssignments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_integrity_monitoring_rule_ids_on_policy(self, policy_id, api_version, **kwargs):  # noqa: E501
        """List Integrity Monitoring Rule IDs  # noqa: E501

        Lists all integrity monitoring rule IDs assigned to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_integrity_monitoring_rule_ids_on_policy(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Return only rule IDs assigned directly to the current policy.
        :return: IntegrityMonitoringAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_integrity_monitoring_rule_ids_on_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_integrity_monitoring_rule_ids_on_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
            return data

    def list_integrity_monitoring_rule_ids_on_policy_with_http_info(self, policy_id, api_version, **kwargs):  # noqa: E501
        """List Integrity Monitoring Rule IDs  # noqa: E501

        Lists all integrity monitoring rule IDs assigned to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_integrity_monitoring_rule_ids_on_policy_with_http_info(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Return only rule IDs assigned directly to the current policy.
        :return: IntegrityMonitoringAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_integrity_monitoring_rule_ids_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `list_integrity_monitoring_rule_ids_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_integrity_monitoring_rule_ids_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `list_integrity_monitoring_rule_ids_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/integritymonitoring/assignments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrityMonitoringAssignments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_integrity_monitoring_rule_id_from_policy(self, policy_id, integrity_monitoring_rule_id, api_version, **kwargs):  # noqa: E501
        """Remove an Integrity Monitoring Rule ID  # noqa: E501

        Unassign an integrity monitoring rule ID from a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_integrity_monitoring_rule_id_from_policy(policy_id, integrity_monitoring_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int integrity_monitoring_rule_id: The ID number of the integrity monitoring rule to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Return only rule IDs assigned directly to the current policy.
        :return: IntegrityMonitoringAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_integrity_monitoring_rule_id_from_policy_with_http_info(policy_id, integrity_monitoring_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_integrity_monitoring_rule_id_from_policy_with_http_info(policy_id, integrity_monitoring_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def remove_integrity_monitoring_rule_id_from_policy_with_http_info(self, policy_id, integrity_monitoring_rule_id, api_version, **kwargs):  # noqa: E501
        """Remove an Integrity Monitoring Rule ID  # noqa: E501

        Unassign an integrity monitoring rule ID from a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_integrity_monitoring_rule_id_from_policy_with_http_info(policy_id, integrity_monitoring_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int integrity_monitoring_rule_id: The ID number of the integrity monitoring rule to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Return only rule IDs assigned directly to the current policy.
        :return: IntegrityMonitoringAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'integrity_monitoring_rule_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_integrity_monitoring_rule_id_from_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `remove_integrity_monitoring_rule_id_from_policy`")  # noqa: E501
        # verify the required parameter 'integrity_monitoring_rule_id' is set
        if ('integrity_monitoring_rule_id' not in params or
                params['integrity_monitoring_rule_id'] is None):
            raise ValueError("Missing the required parameter `integrity_monitoring_rule_id` when calling `remove_integrity_monitoring_rule_id_from_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `remove_integrity_monitoring_rule_id_from_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `remove_integrity_monitoring_rule_id_from_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'integrity_monitoring_rule_id' in params and not re.search('\\d+', str(params['integrity_monitoring_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `integrity_monitoring_rule_id` when calling `remove_integrity_monitoring_rule_id_from_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'integrity_monitoring_rule_id' in params:
            path_params['integrityMonitoringRuleID'] = params['integrity_monitoring_rule_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/integritymonitoring/assignments/{integrityMonitoringRuleID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrityMonitoringAssignments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_integrity_monitoring_rule_ids_on_policy(self, policy_id, api_version, **kwargs):  # noqa: E501
        """Set Integrity Monitoring Rule IDs  # noqa: E501

        Set integrity monitoring rule IDs assigned to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_integrity_monitoring_rule_ids_on_policy(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param RuleIDs integrity_monitoring_rule_ids: The ID numbers of the integrity monitoring rules to set.
        :param bool overrides: Return only rule IDs assigned directly to the current policy.
        :return: IntegrityMonitoringAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_integrity_monitoring_rule_ids_on_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.set_integrity_monitoring_rule_ids_on_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
            return data

    def set_integrity_monitoring_rule_ids_on_policy_with_http_info(self, policy_id, api_version, **kwargs):  # noqa: E501
        """Set Integrity Monitoring Rule IDs  # noqa: E501

        Set integrity monitoring rule IDs assigned to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_integrity_monitoring_rule_ids_on_policy_with_http_info(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param RuleIDs integrity_monitoring_rule_ids: The ID numbers of the integrity monitoring rules to set.
        :param bool overrides: Return only rule IDs assigned directly to the current policy.
        :return: IntegrityMonitoringAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'api_version', 'integrity_monitoring_rule_ids', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_integrity_monitoring_rule_ids_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `set_integrity_monitoring_rule_ids_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `set_integrity_monitoring_rule_ids_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `set_integrity_monitoring_rule_ids_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'integrity_monitoring_rule_ids' in params:
            body_params = params['integrity_monitoring_rule_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/integritymonitoring/assignments', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrityMonitoringAssignments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
