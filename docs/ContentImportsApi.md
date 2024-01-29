# foreman.ContentImportsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_imports**](ContentImportsApi.md#get_content_imports) | **GET** /content_imports | List import histories
[**post_content_imports_library**](ContentImportsApi.md#post_content_imports_library) | **POST** /content_imports/library | Import a content view version to the library
[**post_content_imports_repository**](ContentImportsApi.md#post_content_imports_repository) | **POST** /content_imports/repository | Import a repository
[**post_content_imports_version**](ContentImportsApi.md#post_content_imports_version) | **POST** /content_imports/version | Import a content view version


# **get_content_imports**
> get_content_imports(content_view_version_id=content_view_version_id, content_view_id=content_view_id, organization_id=organization_id, id=id, type=type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List import histories

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentImportsApi(api_client)
    content_view_version_id = 3.4 # float | Content view version identifier (optional)
    content_view_id = 3.4 # float | Content view identifier (optional)
    organization_id = 3.4 # float | Organization identifier (optional)
    id = 3.4 # float | Content view version import history identifier (optional)
    type = 'type_example' # str | Import Types (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List import histories
        api_instance.get_content_imports(content_view_version_id=content_view_version_id, content_view_id=content_view_id, organization_id=organization_id, id=id, type=type, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ContentImportsApi->get_content_imports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_version_id** | **float**| Content view version identifier | [optional] 
 **content_view_id** | **float**| Content view identifier | [optional] 
 **organization_id** | **float**| Organization identifier | [optional] 
 **id** | **float**| Content view version import history identifier | [optional] 
 **type** | **str**| Import Types | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_imports_library**
> post_content_imports_library(organization_id, path)

Import a content view version to the library

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentImportsApi(api_client)
    organization_id = 3.4 # float | Organization identifier
    path = 'path_example' # str | Directory containing the exported Content View Version

    try:
        # Import a content view version to the library
        api_instance.post_content_imports_library(organization_id, path)
    except Exception as e:
        print("Exception when calling ContentImportsApi->post_content_imports_library: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier | 
 **path** | **str**| Directory containing the exported Content View Version | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_imports_repository**
> post_content_imports_repository(organization_id, path)

Import a repository

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentImportsApi(api_client)
    organization_id = 3.4 # float | Organization identifier
    path = 'path_example' # str | Directory containing the exported Content View Version

    try:
        # Import a repository
        api_instance.post_content_imports_repository(organization_id, path)
    except Exception as e:
        print("Exception when calling ContentImportsApi->post_content_imports_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier | 
 **path** | **str**| Directory containing the exported Content View Version | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_imports_version**
> post_content_imports_version(organization_id, path)

Import a content view version

### Example


```python
import time
import os
import foreman
from foreman.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = foreman.Configuration(
    host = "https://localhost:3000/api"
)


# Enter a context with an instance of the API client
with foreman.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = foreman.ContentImportsApi(api_client)
    organization_id = 3.4 # float | Organization identifier
    path = 'path_example' # str | Directory containing the exported Content View Version

    try:
        # Import a content view version
        api_instance.post_content_imports_version(organization_id, path)
    except Exception as e:
        print("Exception when calling ContentImportsApi->post_content_imports_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier | 
 **path** | **str**| Directory containing the exported Content View Version | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

