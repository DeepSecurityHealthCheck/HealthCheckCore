# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 12.5.855
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class AdministratorRolesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_administrator_role(self, administratorrole, api_version, **kwargs):  # noqa: E501
        """Create an Administrator Role  # noqa: E501

        Create a new administrator role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_administrator_role(administratorrole, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Role administratorrole: The settings of the new administrator role. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_administrator_role_with_http_info(administratorrole, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_administrator_role_with_http_info(administratorrole, api_version, **kwargs)  # noqa: E501
            return data

    def create_administrator_role_with_http_info(self, administratorrole, api_version, **kwargs):  # noqa: E501
        """Create an Administrator Role  # noqa: E501

        Create a new administrator role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_administrator_role_with_http_info(administratorrole, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Role administratorrole: The settings of the new administrator role. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['administratorrole', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_administrator_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'administratorrole' is set
        if ('administratorrole' not in params or
                params['administratorrole'] is None):
            raise ValueError("Missing the required parameter `administratorrole` when calling `create_administrator_role`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_administrator_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'administratorrole' in params:
            body_params = params['administratorrole']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/roles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Role',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_administrator_role(self, role_id, api_version, **kwargs):  # noqa: E501
        """Delete an Administrator Role  # noqa: E501

        Delete an administrator role by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_administrator_role(role_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int role_id: The ID number of the administrator role to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_administrator_role_with_http_info(role_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_administrator_role_with_http_info(role_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_administrator_role_with_http_info(self, role_id, api_version, **kwargs):  # noqa: E501
        """Delete an Administrator Role  # noqa: E501

        Delete an administrator role by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_administrator_role_with_http_info(role_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int role_id: The ID number of the administrator role to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_administrator_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params or
                params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `delete_administrator_role`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_administrator_role`")  # noqa: E501

        if 'role_id' in params and not re.search('\\d+', str(params['role_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `role_id` when calling `delete_administrator_role`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role_id' in params:
            path_params['roleID'] = params['role_id']  # noqa: E501

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
            '/roles/{roleID}', 'DELETE',
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

    def describe_administrator_role(self, role_id, api_version, **kwargs):  # noqa: E501
        """Describe an Administrator Role  # noqa: E501

        Describe an administrator role by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_administrator_role(role_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int role_id: The ID number of the administrator role to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_administrator_role_with_http_info(role_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_administrator_role_with_http_info(role_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_administrator_role_with_http_info(self, role_id, api_version, **kwargs):  # noqa: E501
        """Describe an Administrator Role  # noqa: E501

        Describe an administrator role by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_administrator_role_with_http_info(role_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int role_id: The ID number of the administrator role to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_administrator_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params or
                params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `describe_administrator_role`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_administrator_role`")  # noqa: E501

        if 'role_id' in params and not re.search('\\d+', str(params['role_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `role_id` when calling `describe_administrator_role`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role_id' in params:
            path_params['roleID'] = params['role_id']  # noqa: E501

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
            '/roles/{roleID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Role',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_administrator_roles(self, api_version, **kwargs):  # noqa: E501
        """List Administrator Roles  # noqa: E501

        Lists all administrator roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_administrator_roles(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: AdministratorRoles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_administrator_roles_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_administrator_roles_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_administrator_roles_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List Administrator Roles  # noqa: E501

        Lists all administrator roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_administrator_roles_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: AdministratorRoles
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
                    " to method list_administrator_roles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_administrator_roles`")  # noqa: E501

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
            '/roles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdministratorRoles',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_administrator_role(self, role_id, administrator, api_version, **kwargs):  # noqa: E501
        """Modify an Administrator Role  # noqa: E501

        Modify an administrator role by ID. Any properties that have no value are not modified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_administrator_role(role_id, administrator, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int role_id: The ID number of the administrator role to modify. (required)
        :param Role administrator: The settings of the administrator role to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_administrator_role_with_http_info(role_id, administrator, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_administrator_role_with_http_info(role_id, administrator, api_version, **kwargs)  # noqa: E501
            return data

    def modify_administrator_role_with_http_info(self, role_id, administrator, api_version, **kwargs):  # noqa: E501
        """Modify an Administrator Role  # noqa: E501

        Modify an administrator role by ID. Any properties that have no value are not modified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_administrator_role_with_http_info(role_id, administrator, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int role_id: The ID number of the administrator role to modify. (required)
        :param Role administrator: The settings of the administrator role to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_id', 'administrator', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_administrator_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params or
                params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `modify_administrator_role`")  # noqa: E501
        # verify the required parameter 'administrator' is set
        if ('administrator' not in params or
                params['administrator'] is None):
            raise ValueError("Missing the required parameter `administrator` when calling `modify_administrator_role`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_administrator_role`")  # noqa: E501

        if 'role_id' in params and not re.search('\\d+', str(params['role_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `role_id` when calling `modify_administrator_role`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'role_id' in params:
            path_params['roleID'] = params['role_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'administrator' in params:
            body_params = params['administrator']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/roles/{roleID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Role',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_administrator_roles(self, api_version, **kwargs):  # noqa: E501
        """Search Administrator Roles  # noqa: E501

        Search for administrator roles using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_administrator_roles(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: AdministratorRoles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_administrator_roles_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_administrator_roles_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_administrator_roles_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search Administrator Roles  # noqa: E501

        Search for administrator roles using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_administrator_roles_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: AdministratorRoles
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
                    " to method search_administrator_roles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_administrator_roles`")  # noqa: E501

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
            '/roles/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AdministratorRoles',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
