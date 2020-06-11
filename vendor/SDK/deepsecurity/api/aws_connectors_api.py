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


class AWSConnectorsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_aws_connector(self, aws_connector, api_version, **kwargs):  # noqa: E501
        """Create an AWS Connector  # noqa: E501

        Create a new AWS Connector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_aws_connector(aws_connector, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AWSConnector aws_connector: The settings of the new AWS Connector. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AWSConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_aws_connector_with_http_info(aws_connector, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_aws_connector_with_http_info(aws_connector, api_version, **kwargs)  # noqa: E501
            return data

    def create_aws_connector_with_http_info(self, aws_connector, api_version, **kwargs):  # noqa: E501
        """Create an AWS Connector  # noqa: E501

        Create a new AWS Connector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_aws_connector_with_http_info(aws_connector, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AWSConnector aws_connector: The settings of the new AWS Connector. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AWSConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aws_connector', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_aws_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aws_connector' is set
        if ('aws_connector' not in params or
                params['aws_connector'] is None):
            raise ValueError("Missing the required parameter `aws_connector` when calling `create_aws_connector`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_aws_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'aws_connector' in params:
            body_params = params['aws_connector']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/awsconnectors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AWSConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_aws_connector(self, aws_connector_id, api_version, **kwargs):  # noqa: E501
        """Delete an AWS Connector  # noqa: E501

        Delete an existing AWS Connector by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_aws_connector(aws_connector_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int aws_connector_id: The ID number of the AWS Connector to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_aws_connector_with_http_info(aws_connector_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_aws_connector_with_http_info(aws_connector_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_aws_connector_with_http_info(self, aws_connector_id, api_version, **kwargs):  # noqa: E501
        """Delete an AWS Connector  # noqa: E501

        Delete an existing AWS Connector by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_aws_connector_with_http_info(aws_connector_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int aws_connector_id: The ID number of the AWS Connector to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aws_connector_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_aws_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aws_connector_id' is set
        if ('aws_connector_id' not in params or
                params['aws_connector_id'] is None):
            raise ValueError("Missing the required parameter `aws_connector_id` when calling `delete_aws_connector`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_aws_connector`")  # noqa: E501

        if 'aws_connector_id' in params and not re.search('\\d+', str(params['aws_connector_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `aws_connector_id` when calling `delete_aws_connector`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'aws_connector_id' in params:
            path_params['awsConnectorID'] = params['aws_connector_id']  # noqa: E501

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
            '/awsconnectors/{awsConnectorID}', 'DELETE',
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

    def describe_aws_connector(self, aws_connector_id, api_version, **kwargs):  # noqa: E501
        """Describe an existing AWS Connector  # noqa: E501

        Describe an AWS Connector by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_aws_connector(aws_connector_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int aws_connector_id: The ID number of the AWS Connector to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AWSConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_aws_connector_with_http_info(aws_connector_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_aws_connector_with_http_info(aws_connector_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_aws_connector_with_http_info(self, aws_connector_id, api_version, **kwargs):  # noqa: E501
        """Describe an existing AWS Connector  # noqa: E501

        Describe an AWS Connector by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_aws_connector_with_http_info(aws_connector_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int aws_connector_id: The ID number of the AWS Connector to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AWSConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aws_connector_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_aws_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aws_connector_id' is set
        if ('aws_connector_id' not in params or
                params['aws_connector_id'] is None):
            raise ValueError("Missing the required parameter `aws_connector_id` when calling `describe_aws_connector`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_aws_connector`")  # noqa: E501

        if 'aws_connector_id' in params and not re.search('\\d+', str(params['aws_connector_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `aws_connector_id` when calling `describe_aws_connector`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'aws_connector_id' in params:
            path_params['awsConnectorID'] = params['aws_connector_id']  # noqa: E501

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
            '/awsconnectors/{awsConnectorID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AWSConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_aws_connectors(self, api_version, **kwargs):  # noqa: E501
        """List AWS Connectors  # noqa: E501

        Lists all AWS Connectors.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_aws_connectors(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: AWSConnectors
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_aws_connectors_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_aws_connectors_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_aws_connectors_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List AWS Connectors  # noqa: E501

        Lists all AWS Connectors.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_aws_connectors_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: AWSConnectors
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
                    " to method list_aws_connectors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_aws_connectors`")  # noqa: E501

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
            '/awsconnectors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AWSConnectors',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_aws_connector(self, aws_connector_id, aws_connector, api_version, **kwargs):  # noqa: E501
        """Modify an AWS Connector  # noqa: E501

        Modify the specified AWS Connector by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_aws_connector(aws_connector_id, aws_connector, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int aws_connector_id: The ID number of the AWS Connector to modify. (required)
        :param AWSConnector aws_connector: The settings of the AWS Connector to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool sync: Immediately trigger a synchronization for the AWS Connector.
        :return: AWSConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_aws_connector_with_http_info(aws_connector_id, aws_connector, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_aws_connector_with_http_info(aws_connector_id, aws_connector, api_version, **kwargs)  # noqa: E501
            return data

    def modify_aws_connector_with_http_info(self, aws_connector_id, aws_connector, api_version, **kwargs):  # noqa: E501
        """Modify an AWS Connector  # noqa: E501

        Modify the specified AWS Connector by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_aws_connector_with_http_info(aws_connector_id, aws_connector, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int aws_connector_id: The ID number of the AWS Connector to modify. (required)
        :param AWSConnector aws_connector: The settings of the AWS Connector to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool sync: Immediately trigger a synchronization for the AWS Connector.
        :return: AWSConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['aws_connector_id', 'aws_connector', 'api_version', 'sync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_aws_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'aws_connector_id' is set
        if ('aws_connector_id' not in params or
                params['aws_connector_id'] is None):
            raise ValueError("Missing the required parameter `aws_connector_id` when calling `modify_aws_connector`")  # noqa: E501
        # verify the required parameter 'aws_connector' is set
        if ('aws_connector' not in params or
                params['aws_connector'] is None):
            raise ValueError("Missing the required parameter `aws_connector` when calling `modify_aws_connector`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_aws_connector`")  # noqa: E501

        if 'aws_connector_id' in params and not re.search('\\d+', str(params['aws_connector_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `aws_connector_id` when calling `modify_aws_connector`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'aws_connector_id' in params:
            path_params['awsConnectorID'] = params['aws_connector_id']  # noqa: E501

        query_params = []
        if 'sync' in params:
            query_params.append(('sync', params['sync']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'aws_connector' in params:
            body_params = params['aws_connector']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/awsconnectors/{awsConnectorID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AWSConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_aws_connectors(self, api_version, **kwargs):  # noqa: E501
        """Search AWS Connectors  # noqa: E501

        Search for AWS Connectors using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_aws_connectors(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: AWSConnectors
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_aws_connectors_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_aws_connectors_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_aws_connectors_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search AWS Connectors  # noqa: E501

        Search for AWS Connectors using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_aws_connectors_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: AWSConnectors
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
                    " to method search_aws_connectors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_aws_connectors`")  # noqa: E501

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
            '/awsconnectors/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AWSConnectors',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
