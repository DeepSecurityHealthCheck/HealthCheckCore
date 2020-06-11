# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 12.5.969
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class ComputerLogInspectionRuleAssignmentsRecommendationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_log_inspection_rule_ids_to_computer(self, computer_id, api_version, **kwargs):  # noqa: E501
        """Add Log Inspection Rule IDs  # noqa: E501

        Assign log inspection rule IDs to a computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_log_inspection_rule_ids_to_computer(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer. (required)
        :param str api_version: The version of the api being called. (required)
        :param RuleIDs log_inspection_rule_ids: The ID numbers of the log inspection rules to add.
        :param bool overrides: Return only rule IDs assigned directly to the current computer.
        :return: LogInspectionAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_log_inspection_rule_ids_to_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.add_log_inspection_rule_ids_to_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
            return data

    def add_log_inspection_rule_ids_to_computer_with_http_info(self, computer_id, api_version, **kwargs):  # noqa: E501
        """Add Log Inspection Rule IDs  # noqa: E501

        Assign log inspection rule IDs to a computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_log_inspection_rule_ids_to_computer_with_http_info(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer. (required)
        :param str api_version: The version of the api being called. (required)
        :param RuleIDs log_inspection_rule_ids: The ID numbers of the log inspection rules to add.
        :param bool overrides: Return only rule IDs assigned directly to the current computer.
        :return: LogInspectionAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_id', 'api_version', 'log_inspection_rule_ids', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_log_inspection_rule_ids_to_computer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_id' is set
        if ('computer_id' not in params or
                params['computer_id'] is None):
            raise ValueError("Missing the required parameter `computer_id` when calling `add_log_inspection_rule_ids_to_computer`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `add_log_inspection_rule_ids_to_computer`")  # noqa: E501

        if 'computer_id' in params and not re.search('\\d+', str(params['computer_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_id` when calling `add_log_inspection_rule_ids_to_computer`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_id' in params:
            path_params['computerID'] = params['computer_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'log_inspection_rule_ids' in params:
            body_params = params['log_inspection_rule_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computers/{computerID}/loginspection/assignments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogInspectionAssignments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_log_inspection_rule_ids_on_computer(self, computer_id, api_version, **kwargs):  # noqa: E501
        """List Log Inspection Rule IDs  # noqa: E501

        Lists all log inspection rule IDs assigned to a computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_log_inspection_rule_ids_on_computer(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Return only rule IDs assigned directly to the current computer.
        :return: LogInspectionAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_log_inspection_rule_ids_on_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_log_inspection_rule_ids_on_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
            return data

    def list_log_inspection_rule_ids_on_computer_with_http_info(self, computer_id, api_version, **kwargs):  # noqa: E501
        """List Log Inspection Rule IDs  # noqa: E501

        Lists all log inspection rule IDs assigned to a computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_log_inspection_rule_ids_on_computer_with_http_info(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Return only rule IDs assigned directly to the current computer.
        :return: LogInspectionAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_log_inspection_rule_ids_on_computer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_id' is set
        if ('computer_id' not in params or
                params['computer_id'] is None):
            raise ValueError("Missing the required parameter `computer_id` when calling `list_log_inspection_rule_ids_on_computer`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_log_inspection_rule_ids_on_computer`")  # noqa: E501

        if 'computer_id' in params and not re.search('\\d+', str(params['computer_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_id` when calling `list_log_inspection_rule_ids_on_computer`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_id' in params:
            path_params['computerID'] = params['computer_id']  # noqa: E501

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
            '/computers/{computerID}/loginspection/assignments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogInspectionAssignments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_log_inspection_rule_id_from_computer(self, computer_id, log_inspection_rule_id, api_version, **kwargs):  # noqa: E501
        """Remove a Log Inspection Rule ID  # noqa: E501

        Unassign a log inspection rule ID from a computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_log_inspection_rule_id_from_computer(computer_id, log_inspection_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer. (required)
        :param int log_inspection_rule_id: The ID number of the log inspection rule to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Return only rule IDs assigned directly to the current computer.
        :return: LogInspectionAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_log_inspection_rule_id_from_computer_with_http_info(computer_id, log_inspection_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_log_inspection_rule_id_from_computer_with_http_info(computer_id, log_inspection_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def remove_log_inspection_rule_id_from_computer_with_http_info(self, computer_id, log_inspection_rule_id, api_version, **kwargs):  # noqa: E501
        """Remove a Log Inspection Rule ID  # noqa: E501

        Unassign a log inspection rule ID from a computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_log_inspection_rule_id_from_computer_with_http_info(computer_id, log_inspection_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer. (required)
        :param int log_inspection_rule_id: The ID number of the log inspection rule to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Return only rule IDs assigned directly to the current computer.
        :return: LogInspectionAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_id', 'log_inspection_rule_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_log_inspection_rule_id_from_computer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_id' is set
        if ('computer_id' not in params or
                params['computer_id'] is None):
            raise ValueError("Missing the required parameter `computer_id` when calling `remove_log_inspection_rule_id_from_computer`")  # noqa: E501
        # verify the required parameter 'log_inspection_rule_id' is set
        if ('log_inspection_rule_id' not in params or
                params['log_inspection_rule_id'] is None):
            raise ValueError("Missing the required parameter `log_inspection_rule_id` when calling `remove_log_inspection_rule_id_from_computer`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `remove_log_inspection_rule_id_from_computer`")  # noqa: E501

        if 'computer_id' in params and not re.search('\\d+', str(params['computer_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_id` when calling `remove_log_inspection_rule_id_from_computer`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'log_inspection_rule_id' in params and not re.search('\\d+', str(params['log_inspection_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `log_inspection_rule_id` when calling `remove_log_inspection_rule_id_from_computer`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_id' in params:
            path_params['computerID'] = params['computer_id']  # noqa: E501
        if 'log_inspection_rule_id' in params:
            path_params['logInspectionRuleID'] = params['log_inspection_rule_id']  # noqa: E501

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
            '/computers/{computerID}/loginspection/assignments/{logInspectionRuleID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogInspectionAssignments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_log_inspection_rule_ids_on_computer(self, computer_id, api_version, **kwargs):  # noqa: E501
        """Set Log Inspection Rule IDs  # noqa: E501

        Set log inspection rule IDs assigned to a computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_log_inspection_rule_ids_on_computer(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer. (required)
        :param str api_version: The version of the api being called. (required)
        :param RuleIDs log_inspection_rule_ids: The ID numbers of the log inspection rules to set.
        :param bool overrides: Return only rule IDs assigned directly to the current computer.
        :return: LogInspectionAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_log_inspection_rule_ids_on_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.set_log_inspection_rule_ids_on_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
            return data

    def set_log_inspection_rule_ids_on_computer_with_http_info(self, computer_id, api_version, **kwargs):  # noqa: E501
        """Set Log Inspection Rule IDs  # noqa: E501

        Set log inspection rule IDs assigned to a computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_log_inspection_rule_ids_on_computer_with_http_info(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer. (required)
        :param str api_version: The version of the api being called. (required)
        :param RuleIDs log_inspection_rule_ids: The ID numbers of the log inspection rules to set.
        :param bool overrides: Return only rule IDs assigned directly to the current computer.
        :return: LogInspectionAssignments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_id', 'api_version', 'log_inspection_rule_ids', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_log_inspection_rule_ids_on_computer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_id' is set
        if ('computer_id' not in params or
                params['computer_id'] is None):
            raise ValueError("Missing the required parameter `computer_id` when calling `set_log_inspection_rule_ids_on_computer`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `set_log_inspection_rule_ids_on_computer`")  # noqa: E501

        if 'computer_id' in params and not re.search('\\d+', str(params['computer_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_id` when calling `set_log_inspection_rule_ids_on_computer`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_id' in params:
            path_params['computerID'] = params['computer_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'log_inspection_rule_ids' in params:
            body_params = params['log_inspection_rule_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computers/{computerID}/loginspection/assignments', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LogInspectionAssignments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
