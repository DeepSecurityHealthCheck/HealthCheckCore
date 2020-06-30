# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class InterfaceTypesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_interface_type(self, policy_id, api_version, **kwargs):  # noqa: E501
        """Create an Interface Type  # noqa: E501

        Create a new interface type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_interface_type(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param InterfaceType interface_types: The settings of the new interface type.
        :return: InterfaceType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_interface_type_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_interface_type_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
            return data

    def create_interface_type_with_http_info(self, policy_id, api_version, **kwargs):  # noqa: E501
        """Create an Interface Type  # noqa: E501

        Create a new interface type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_interface_type_with_http_info(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param InterfaceType interface_types: The settings of the new interface type.
        :return: InterfaceType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'api_version', 'interface_types']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_interface_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `create_interface_type`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_interface_type`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `create_interface_type`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interface_types' in params:
            body_params = params['interface_types']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/interfacetypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InterfaceType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_interface_type(self, policy_id, interface_type_id, api_version, **kwargs):  # noqa: E501
        """Delete an Interface Type  # noqa: E501

        Delete an interface type by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_interface_type(policy_id, interface_type_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int interface_type_id: The ID number of the interface type to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_interface_type_with_http_info(policy_id, interface_type_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_interface_type_with_http_info(policy_id, interface_type_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_interface_type_with_http_info(self, policy_id, interface_type_id, api_version, **kwargs):  # noqa: E501
        """Delete an Interface Type  # noqa: E501

        Delete an interface type by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_interface_type_with_http_info(policy_id, interface_type_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int interface_type_id: The ID number of the interface type to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'interface_type_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_interface_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `delete_interface_type`")  # noqa: E501
        # verify the required parameter 'interface_type_id' is set
        if ('interface_type_id' not in params or
                params['interface_type_id'] is None):
            raise ValueError("Missing the required parameter `interface_type_id` when calling `delete_interface_type`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_interface_type`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `delete_interface_type`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'interface_type_id' in params and not re.search('\\d+', str(params['interface_type_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `interface_type_id` when calling `delete_interface_type`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'interface_type_id' in params:
            path_params['interfaceTypeID'] = params['interface_type_id']  # noqa: E501

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
            '/policies/{policyID}/interfacetypes/{interfaceTypeID}', 'DELETE',
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

    def describe_interface_type(self, policy_id, interface_type_id, api_version, **kwargs):  # noqa: E501
        """Describe an Interface Type  # noqa: E501

        Describe an interface type by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_interface_type(policy_id, interface_type_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int interface_type_id: The ID number of the interface type to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: InterfaceType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_interface_type_with_http_info(policy_id, interface_type_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_interface_type_with_http_info(policy_id, interface_type_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_interface_type_with_http_info(self, policy_id, interface_type_id, api_version, **kwargs):  # noqa: E501
        """Describe an Interface Type  # noqa: E501

        Describe an interface type by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_interface_type_with_http_info(policy_id, interface_type_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int interface_type_id: The ID number of the interface type to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: InterfaceType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'interface_type_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_interface_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `describe_interface_type`")  # noqa: E501
        # verify the required parameter 'interface_type_id' is set
        if ('interface_type_id' not in params or
                params['interface_type_id'] is None):
            raise ValueError("Missing the required parameter `interface_type_id` when calling `describe_interface_type`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_interface_type`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `describe_interface_type`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'interface_type_id' in params and not re.search('\\d+', str(params['interface_type_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `interface_type_id` when calling `describe_interface_type`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'interface_type_id' in params:
            path_params['interfaceTypeID'] = params['interface_type_id']  # noqa: E501

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
            '/policies/{policyID}/interfacetypes/{interfaceTypeID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InterfaceType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_interface_types(self, policy_id, api_version, **kwargs):  # noqa: E501
        """List Interface Types  # noqa: E501

        Lists all interface types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_interface_types(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :return: InterfaceTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_interface_types_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_interface_types_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
            return data

    def list_interface_types_with_http_info(self, policy_id, api_version, **kwargs):  # noqa: E501
        """List Interface Types  # noqa: E501

        Lists all interface types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_interface_types_with_http_info(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :return: InterfaceTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_interface_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `list_interface_types`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_interface_types`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `list_interface_types`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501

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
            '/policies/{policyID}/interfacetypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InterfaceTypes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_interface_type(self, policy_id, interface_type_id, interface_type, api_version, **kwargs):  # noqa: E501
        """Modify an Interface Type  # noqa: E501

        Modify an interface type by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_interface_type(policy_id, interface_type_id, interface_type, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int interface_type_id: The ID number of the interface type to modify. (required)
        :param InterfaceType interface_type: The settings of the interface type to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: InterfaceType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_interface_type_with_http_info(policy_id, interface_type_id, interface_type, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_interface_type_with_http_info(policy_id, interface_type_id, interface_type, api_version, **kwargs)  # noqa: E501
            return data

    def modify_interface_type_with_http_info(self, policy_id, interface_type_id, interface_type, api_version, **kwargs):  # noqa: E501
        """Modify an Interface Type  # noqa: E501

        Modify an interface type by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_interface_type_with_http_info(policy_id, interface_type_id, interface_type, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int interface_type_id: The ID number of the interface type to modify. (required)
        :param InterfaceType interface_type: The settings of the interface type to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: InterfaceType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'interface_type_id', 'interface_type', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_interface_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `modify_interface_type`")  # noqa: E501
        # verify the required parameter 'interface_type_id' is set
        if ('interface_type_id' not in params or
                params['interface_type_id'] is None):
            raise ValueError("Missing the required parameter `interface_type_id` when calling `modify_interface_type`")  # noqa: E501
        # verify the required parameter 'interface_type' is set
        if ('interface_type' not in params or
                params['interface_type'] is None):
            raise ValueError("Missing the required parameter `interface_type` when calling `modify_interface_type`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_interface_type`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `modify_interface_type`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'interface_type_id' in params and not re.search('\\d+', str(params['interface_type_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `interface_type_id` when calling `modify_interface_type`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'interface_type_id' in params:
            path_params['interfaceTypeID'] = params['interface_type_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'interface_type' in params:
            body_params = params['interface_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/interfacetypes/{interfaceTypeID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InterfaceType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_interface_types(self, policy_id, api_version, **kwargs):  # noqa: E501
        """Search Interface Types  # noqa: E501

        Search for interface types using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_interface_types(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: InterfaceTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_interface_types_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_interface_types_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
            return data

    def search_interface_types_with_http_info(self, policy_id, api_version, **kwargs):  # noqa: E501
        """Search Interface Types  # noqa: E501

        Search for interface types using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_interface_types_with_http_info(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: InterfaceTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'api_version', 'search_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_interface_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `search_interface_types`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_interface_types`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `search_interface_types`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501

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
            '/policies/{policyID}/interfacetypes/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InterfaceTypes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
