# foreman.ModuleStreamsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_view_filters_content_view_filter_id_module_streams**](ModuleStreamsApi.md#get_content_view_filters_content_view_filter_id_module_streams) | **GET** /content_view_filters/{content_view_filter_id}/module_streams | List module_streams
[**get_content_views_content_view_id_filters_filter_id_module_streams**](ModuleStreamsApi.md#get_content_views_content_view_id_filters_filter_id_module_streams) | **GET** /content_views/{content_view_id}/filters/{filter_id}/module_streams | List module_streams
[**get_module_streams**](ModuleStreamsApi.md#get_module_streams) | **GET** /module_streams | List module_streams
[**get_module_streams_compare**](ModuleStreamsApi.md#get_module_streams_compare) | **GET** /module_streams/compare | List module_streams
[**get_module_streams_id**](ModuleStreamsApi.md#get_module_streams_id) | **GET** /module_streams/{id} | Show a module stream
[**get_repositories_repository_id_module_streams**](ModuleStreamsApi.md#get_repositories_repository_id_module_streams) | **GET** /repositories/{repository_id}/module_streams | List module_streams
[**get_repositories_repository_id_module_streams_id**](ModuleStreamsApi.md#get_repositories_repository_id_module_streams_id) | **GET** /repositories/{repository_id}/module_streams/{id} | Show a module stream


# **get_content_view_filters_content_view_filter_id_module_streams**
> get_content_view_filters_content_view_filter_id_module_streams(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_ids=host_ids, name_stream_only=name_stream_only)

List module_streams

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
    api_instance = foreman.ModuleStreamsApi(api_client)
    content_view_filter_id = 3.4 # float | content view filter identifier
    repository_id = 3.4 # float | repository identifier
    organization_id = 3.4 # float | organization identifier (optional)
    content_view_version_id = 3.4 # float | content view version identifier (optional)
    content_view_filter_rule_id = 3.4 # float | content view filter rule identifier (optional)
    environment_id = 3.4 # float | environment identifier (optional)
    ids = ['ids_example'] # List[str] | ids to filter content by (optional)
    include_filter_ids = True # bool | Includes associated content view filter ids in response (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
    host_ids = ['host_ids_example'] # List[str] | List of host id to list available module streams for (optional)
    name_stream_only = True # bool | Return name and stream information only) (optional)

    try:
        # List module_streams
        api_instance.get_content_view_filters_content_view_filter_id_module_streams(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_ids=host_ids, name_stream_only=name_stream_only)
    except Exception as e:
        print("Exception when calling ModuleStreamsApi->get_content_view_filters_content_view_filter_id_module_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| content view filter identifier | 
 **repository_id** | **float**| repository identifier | 
 **organization_id** | **float**| organization identifier | [optional] 
 **content_view_version_id** | **float**| content view version identifier | [optional] 
 **content_view_filter_rule_id** | **float**| content view filter rule identifier | [optional] 
 **environment_id** | **float**| environment identifier | [optional] 
 **ids** | [**List[str]**](str.md)| ids to filter content by | [optional] 
 **include_filter_ids** | **bool**| Includes associated content view filter ids in response | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 
 **host_ids** | [**List[str]**](str.md)| List of host id to list available module streams for | [optional] 
 **name_stream_only** | **bool**| Return name and stream information only) | [optional] 

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

# **get_content_views_content_view_id_filters_filter_id_module_streams**
> get_content_views_content_view_id_filters_filter_id_module_streams(content_view_id, filter_id, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_ids=host_ids, name_stream_only=name_stream_only)

List module_streams

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
    api_instance = foreman.ModuleStreamsApi(api_client)
    content_view_id = 3.4 # float | 
    filter_id = 3.4 # float | 
    content_view_filter_id = 3.4 # float | content view filter identifier
    repository_id = 3.4 # float | repository identifier
    organization_id = 3.4 # float | organization identifier (optional)
    content_view_version_id = 3.4 # float | content view version identifier (optional)
    content_view_filter_rule_id = 3.4 # float | content view filter rule identifier (optional)
    environment_id = 3.4 # float | environment identifier (optional)
    ids = ['ids_example'] # List[str] | ids to filter content by (optional)
    include_filter_ids = True # bool | Includes associated content view filter ids in response (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
    host_ids = ['host_ids_example'] # List[str] | List of host id to list available module streams for (optional)
    name_stream_only = True # bool | Return name and stream information only) (optional)

    try:
        # List module_streams
        api_instance.get_content_views_content_view_id_filters_filter_id_module_streams(content_view_id, filter_id, content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_ids=host_ids, name_stream_only=name_stream_only)
    except Exception as e:
        print("Exception when calling ModuleStreamsApi->get_content_views_content_view_id_filters_filter_id_module_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**|  | 
 **filter_id** | **float**|  | 
 **content_view_filter_id** | **float**| content view filter identifier | 
 **repository_id** | **float**| repository identifier | 
 **organization_id** | **float**| organization identifier | [optional] 
 **content_view_version_id** | **float**| content view version identifier | [optional] 
 **content_view_filter_rule_id** | **float**| content view filter rule identifier | [optional] 
 **environment_id** | **float**| environment identifier | [optional] 
 **ids** | [**List[str]**](str.md)| ids to filter content by | [optional] 
 **include_filter_ids** | **bool**| Includes associated content view filter ids in response | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 
 **host_ids** | [**List[str]**](str.md)| List of host id to list available module streams for | [optional] 
 **name_stream_only** | **bool**| Return name and stream information only) | [optional] 

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

# **get_module_streams**
> get_module_streams(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_ids=host_ids, name_stream_only=name_stream_only)

List module_streams

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
    api_instance = foreman.ModuleStreamsApi(api_client)
    content_view_filter_id = 3.4 # float | content view filter identifier
    repository_id = 3.4 # float | repository identifier
    organization_id = 3.4 # float | organization identifier (optional)
    content_view_version_id = 3.4 # float | content view version identifier (optional)
    content_view_filter_rule_id = 3.4 # float | content view filter rule identifier (optional)
    environment_id = 3.4 # float | environment identifier (optional)
    ids = ['ids_example'] # List[str] | ids to filter content by (optional)
    include_filter_ids = True # bool | Includes associated content view filter ids in response (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
    host_ids = ['host_ids_example'] # List[str] | List of host id to list available module streams for (optional)
    name_stream_only = True # bool | Return name and stream information only) (optional)

    try:
        # List module_streams
        api_instance.get_module_streams(content_view_filter_id, repository_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_ids=host_ids, name_stream_only=name_stream_only)
    except Exception as e:
        print("Exception when calling ModuleStreamsApi->get_module_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_filter_id** | **float**| content view filter identifier | 
 **repository_id** | **float**| repository identifier | 
 **organization_id** | **float**| organization identifier | [optional] 
 **content_view_version_id** | **float**| content view version identifier | [optional] 
 **content_view_filter_rule_id** | **float**| content view filter rule identifier | [optional] 
 **environment_id** | **float**| environment identifier | [optional] 
 **ids** | [**List[str]**](str.md)| ids to filter content by | [optional] 
 **include_filter_ids** | **bool**| Includes associated content view filter ids in response | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 
 **host_ids** | [**List[str]**](str.md)| List of host id to list available module streams for | [optional] 
 **name_stream_only** | **bool**| Return name and stream information only) | [optional] 

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

# **get_module_streams_compare**
> get_module_streams_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)

List module_streams

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
    api_instance = foreman.ModuleStreamsApi(api_client)
    content_view_version_ids = ['content_view_version_ids_example'] # List[str] | content view versions to compare (optional)
    repository_id = 3.4 # float | Library repository id to restrict comparisons to (optional)
    restrict_comparison = 'restrict_comparison_example' # str | Return same, different or all results (optional)

    try:
        # List module_streams
        api_instance.get_module_streams_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)
    except Exception as e:
        print("Exception when calling ModuleStreamsApi->get_module_streams_compare: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_version_ids** | [**List[str]**](str.md)| content view versions to compare | [optional] 
 **repository_id** | **float**| Library repository id to restrict comparisons to | [optional] 
 **restrict_comparison** | **str**| Return same, different or all results | [optional] 

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

# **get_module_streams_id**
> get_module_streams_id(id, repository_id, organization_id=organization_id)

Show a module stream

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
    api_instance = foreman.ModuleStreamsApi(api_client)
    id = 'id_example' # str | :a_resource identifier
    repository_id = 3.4 # float | repository identifier
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Show a module stream
        api_instance.get_module_streams_id(id, repository_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ModuleStreamsApi->get_module_streams_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| :a_resource identifier | 
 **repository_id** | **float**| repository identifier | 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **get_repositories_repository_id_module_streams**
> get_repositories_repository_id_module_streams(repository_id, content_view_filter_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_ids=host_ids, name_stream_only=name_stream_only)

List module_streams

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
    api_instance = foreman.ModuleStreamsApi(api_client)
    repository_id = 3.4 # float | repository identifier
    content_view_filter_id = 3.4 # float | content view filter identifier
    organization_id = 3.4 # float | organization identifier (optional)
    content_view_version_id = 3.4 # float | content view version identifier (optional)
    content_view_filter_rule_id = 3.4 # float | content view filter rule identifier (optional)
    environment_id = 3.4 # float | environment identifier (optional)
    ids = ['ids_example'] # List[str] | ids to filter content by (optional)
    include_filter_ids = True # bool | Includes associated content view filter ids in response (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
    host_ids = ['host_ids_example'] # List[str] | List of host id to list available module streams for (optional)
    name_stream_only = True # bool | Return name and stream information only) (optional)

    try:
        # List module_streams
        api_instance.get_repositories_repository_id_module_streams(repository_id, content_view_filter_id, organization_id=organization_id, content_view_version_id=content_view_version_id, content_view_filter_rule_id=content_view_filter_rule_id, environment_id=environment_id, ids=ids, include_filter_ids=include_filter_ids, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_ids=host_ids, name_stream_only=name_stream_only)
    except Exception as e:
        print("Exception when calling ModuleStreamsApi->get_repositories_repository_id_module_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| repository identifier | 
 **content_view_filter_id** | **float**| content view filter identifier | 
 **organization_id** | **float**| organization identifier | [optional] 
 **content_view_version_id** | **float**| content view version identifier | [optional] 
 **content_view_filter_rule_id** | **float**| content view filter rule identifier | [optional] 
 **environment_id** | **float**| environment identifier | [optional] 
 **ids** | [**List[str]**](str.md)| ids to filter content by | [optional] 
 **include_filter_ids** | **bool**| Includes associated content view filter ids in response | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 
 **host_ids** | [**List[str]**](str.md)| List of host id to list available module streams for | [optional] 
 **name_stream_only** | **bool**| Return name and stream information only) | [optional] 

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

# **get_repositories_repository_id_module_streams_id**
> get_repositories_repository_id_module_streams_id(repository_id, id, organization_id=organization_id)

Show a module stream

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
    api_instance = foreman.ModuleStreamsApi(api_client)
    repository_id = 3.4 # float | repository identifier
    id = 'id_example' # str | :a_resource identifier
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Show a module stream
        api_instance.get_repositories_repository_id_module_streams_id(repository_id, id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ModuleStreamsApi->get_repositories_repository_id_module_streams_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **float**| repository identifier | 
 **id** | **str**| :a_resource identifier | 
 **organization_id** | **float**| organization identifier | [optional] 

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

