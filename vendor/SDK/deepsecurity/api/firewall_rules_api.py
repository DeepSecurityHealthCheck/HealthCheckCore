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


class FirewallRulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_firewall_rule(self, firewall_rule, api_version, **kwargs):  # noqa: E501
        """Create a Firewall Rule  # noqa: E501

        Create a new firewall rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_firewall_rule(firewall_rule, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FirewallRule firewall_rule: The settings of the new firewall rule. (required)
        :param str api_version: The version of the api being called. (required)
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_firewall_rule_with_http_info(firewall_rule, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_firewall_rule_with_http_info(firewall_rule, api_version, **kwargs)  # noqa: E501
            return data

    def create_firewall_rule_with_http_info(self, firewall_rule, api_version, **kwargs):  # noqa: E501
        """Create a Firewall Rule  # noqa: E501

        Create a new firewall rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_firewall_rule_with_http_info(firewall_rule, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FirewallRule firewall_rule: The settings of the new firewall rule. (required)
        :param str api_version: The version of the api being called. (required)
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['firewall_rule', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_firewall_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'firewall_rule' is set
        if ('firewall_rule' not in params or
                params['firewall_rule'] is None):
            raise ValueError("Missing the required parameter `firewall_rule` when calling `create_firewall_rule`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_firewall_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'firewall_rule' in params:
            body_params = params['firewall_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/firewallrules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_firewall_rule(self, firewall_rule_id, api_version, **kwargs):  # noqa: E501
        """Delete a Firewall Rule  # noqa: E501

        Delete a firewall rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_firewall_rule(firewall_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int firewall_rule_id: The ID number of the firewall rule to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_firewall_rule_with_http_info(firewall_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_firewall_rule_with_http_info(firewall_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_firewall_rule_with_http_info(self, firewall_rule_id, api_version, **kwargs):  # noqa: E501
        """Delete a Firewall Rule  # noqa: E501

        Delete a firewall rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_firewall_rule_with_http_info(firewall_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int firewall_rule_id: The ID number of the firewall rule to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['firewall_rule_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_firewall_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'firewall_rule_id' is set
        if ('firewall_rule_id' not in params or
                params['firewall_rule_id'] is None):
            raise ValueError("Missing the required parameter `firewall_rule_id` when calling `delete_firewall_rule`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_firewall_rule`")  # noqa: E501

        if 'firewall_rule_id' in params and not re.search('\\d+', str(params['firewall_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `firewall_rule_id` when calling `delete_firewall_rule`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in params:
            path_params['firewallRuleID'] = params['firewall_rule_id']  # noqa: E501

        query_params = []

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
            '/firewallrules/{firewallRuleID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_firewall_rule(self, firewall_rule_id, api_version, **kwargs):  # noqa: E501
        """Describe a Firewall Rule  # noqa: E501

        Describe a firewall rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_firewall_rule(firewall_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int firewall_rule_id: The ID number of the firewall rule to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_firewall_rule_with_http_info(firewall_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_firewall_rule_with_http_info(firewall_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_firewall_rule_with_http_info(self, firewall_rule_id, api_version, **kwargs):  # noqa: E501
        """Describe a Firewall Rule  # noqa: E501

        Describe a firewall rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_firewall_rule_with_http_info(firewall_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int firewall_rule_id: The ID number of the firewall rule to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['firewall_rule_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_firewall_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'firewall_rule_id' is set
        if ('firewall_rule_id' not in params or
                params['firewall_rule_id'] is None):
            raise ValueError("Missing the required parameter `firewall_rule_id` when calling `describe_firewall_rule`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_firewall_rule`")  # noqa: E501

        if 'firewall_rule_id' in params and not re.search('\\d+', str(params['firewall_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `firewall_rule_id` when calling `describe_firewall_rule`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in params:
            path_params['firewallRuleID'] = params['firewall_rule_id']  # noqa: E501

        query_params = []

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
            '/firewallrules/{firewallRuleID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_firewall_rules(self, api_version, **kwargs):  # noqa: E501
        """List Firewall Rules  # noqa: E501

        Lists all firewall rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_firewall_rules(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: FirewallRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_firewall_rules_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_firewall_rules_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_firewall_rules_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List Firewall Rules  # noqa: E501

        Lists all firewall rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_firewall_rules_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: FirewallRules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_firewall_rules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_firewall_rules`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/firewallrules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRules',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_firewall_rule(self, firewall_rule_id, firewall_rules, api_version, **kwargs):  # noqa: E501
        """Modify a Firewall Rule  # noqa: E501

        Modify a firewall rule by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_firewall_rule(firewall_rule_id, firewall_rules, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int firewall_rule_id: The ID number of the firewall rule to modify. (required)
        :param FirewallRule firewall_rules: The settings of the firewall rule to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_firewall_rule_with_http_info(firewall_rule_id, firewall_rules, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_firewall_rule_with_http_info(firewall_rule_id, firewall_rules, api_version, **kwargs)  # noqa: E501
            return data

    def modify_firewall_rule_with_http_info(self, firewall_rule_id, firewall_rules, api_version, **kwargs):  # noqa: E501
        """Modify a Firewall Rule  # noqa: E501

        Modify a firewall rule by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_firewall_rule_with_http_info(firewall_rule_id, firewall_rules, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int firewall_rule_id: The ID number of the firewall rule to modify. (required)
        :param FirewallRule firewall_rules: The settings of the firewall rule to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['firewall_rule_id', 'firewall_rules', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_firewall_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'firewall_rule_id' is set
        if ('firewall_rule_id' not in params or
                params['firewall_rule_id'] is None):
            raise ValueError("Missing the required parameter `firewall_rule_id` when calling `modify_firewall_rule`")  # noqa: E501
        # verify the required parameter 'firewall_rules' is set
        if ('firewall_rules' not in params or
                params['firewall_rules'] is None):
            raise ValueError("Missing the required parameter `firewall_rules` when calling `modify_firewall_rule`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_firewall_rule`")  # noqa: E501

        if 'firewall_rule_id' in params and not re.search('\\d+', str(params['firewall_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `firewall_rule_id` when calling `modify_firewall_rule`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'firewall_rule_id' in params:
            path_params['firewallRuleID'] = params['firewall_rule_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'firewall_rules' in params:
            body_params = params['firewall_rules']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/firewallrules/{firewallRuleID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_firewall_rules(self, api_version, **kwargs):  # noqa: E501
        """Search Firewall Rules  # noqa: E501

        Search for firewall rules using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_firewall_rules(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: FirewallRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_firewall_rules_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_firewall_rules_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_firewall_rules_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search Firewall Rules  # noqa: E501

        Search for firewall rules using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_firewall_rules_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: FirewallRules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'search_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_firewall_rules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_firewall_rules`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_filter' in params:
            body_params = params['search_filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/firewallrules/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRules',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
