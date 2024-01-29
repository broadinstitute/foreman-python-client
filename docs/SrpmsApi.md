# foreman.SrpmsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repositories_repository_id_srpms_id**](SrpmsApi.md#get_repositories_repository_id_srpms_id) | **GET** /repositories/{repository_id}/srpms/{id} | Show SRPM details
[**get_srpms**](SrpmsApi.md#get_srpms) | **GET** /srpms | List srpms
[**get_srpms_compare**](SrpmsApi.md#get_srpms_compare) | **GET** /srpms/compare | List srpms
[**get_srpms_id**](SrpmsApi.md#get_srpms_id) | **GET** /srpms/{id} | Show SRPM details


# **get_repositories_repository_id_srpms_id**
> get_repositories_repository_id_srpms_id(repository_id, id, organization_id=organization_id)

Show SRPM details

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
    api_instance = foreman.SrpmsApi(api_client)
    repository_id = 3.4 # float | repository identifier
    id = 'id_example' # str | :a_resource identifier
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Show SRPM details
        api_instance.get_repositories_repository_id_srpms_id(repository_id, id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling SrpmsApi->get_repositories_repository_id_srpms_id: %s\n" % e)
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

# **get_srpms**
> get_srpms(organization_id=organization_id, repository_id=repository_id, environment_id=environment_id, content_view_version_id=content_view_version_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List srpms

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
    api_instance = foreman.SrpmsApi(api_client)
    organization_id = 3.4 # float | Organization identifier (optional)
    repository_id = 3.4 # float | Repository identifier (optional)
    environment_id = 3.4 # float | Environment identifier (optional)
    content_view_version_id = 3.4 # float | Content View Version identifier (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List srpms
        api_instance.get_srpms(organization_id=organization_id, repository_id=repository_id, environment_id=environment_id, content_view_version_id=content_view_version_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling SrpmsApi->get_srpms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier | [optional] 
 **repository_id** | **float**| Repository identifier | [optional] 
 **environment_id** | **float**| Environment identifier | [optional] 
 **content_view_version_id** | **float**| Content View Version identifier | [optional] 
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

# **get_srpms_compare**
> get_srpms_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)

List srpms

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
    api_instance = foreman.SrpmsApi(api_client)
    content_view_version_ids = ['content_view_version_ids_example'] # List[str] | content view versions to compare (optional)
    repository_id = 3.4 # float | Library repository id to restrict comparisons to (optional)
    restrict_comparison = 'restrict_comparison_example' # str | Return same, different or all results (optional)

    try:
        # List srpms
        api_instance.get_srpms_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)
    except Exception as e:
        print("Exception when calling SrpmsApi->get_srpms_compare: %s\n" % e)
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

# **get_srpms_id**
> get_srpms_id(id, repository_id, organization_id=organization_id)

Show SRPM details

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
    api_instance = foreman.SrpmsApi(api_client)
    id = 'id_example' # str | :a_resource identifier
    repository_id = 3.4 # float | repository identifier
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Show SRPM details
        api_instance.get_srpms_id(id, repository_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling SrpmsApi->get_srpms_id: %s\n" % e)
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

