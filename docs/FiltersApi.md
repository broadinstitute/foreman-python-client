# foreman.FiltersApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_filters_id**](FiltersApi.md#delete_filters_id) | **DELETE** /filters/{id} | Delete a filter
[**get_filters**](FiltersApi.md#get_filters) | **GET** /filters | List all filters
[**get_filters_id**](FiltersApi.md#get_filters_id) | **GET** /filters/{id} | Show a filter
[**post_filters**](FiltersApi.md#post_filters) | **POST** /filters | Create a filter
[**put_filters_id**](FiltersApi.md#put_filters_id) | **PUT** /filters/{id} | Update a filter


# **delete_filters_id**
> delete_filters_id(id, location_id=location_id, organization_id=organization_id)

Delete a filter

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
    api_instance = foreman.FiltersApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a filter
        api_instance.delete_filters_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling FiltersApi->delete_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **get_filters**
> get_filters(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all filters

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
    api_instance = foreman.FiltersApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all filters
        api_instance.get_filters(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling FiltersApi->get_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **search** | **str**| filter results | [optional] 
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional] 

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

# **get_filters_id**
> get_filters_id(id, location_id=location_id, organization_id=organization_id)

Show a filter

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
    api_instance = foreman.FiltersApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show a filter
        api_instance.get_filters_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling FiltersApi->get_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 

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

# **post_filters**
> post_filters(filter_role_id, location_id=location_id, organization_id=organization_id, filter_search=filter_search, filter_override=filter_override, filter_permission_ids=filter_permission_ids, filter_organization_ids=filter_organization_ids, filter_location_ids=filter_location_ids)

Create a filter

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
    api_instance = foreman.FiltersApi(api_client)
    filter_role_id = 'filter_role_id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    filter_search = 'filter_search_example' # str |  (optional)
    filter_override = True # bool |  (optional)
    filter_permission_ids = ['filter_permission_ids_example'] # List[str] |  (optional)
    filter_organization_ids = ['filter_organization_ids_example'] # List[str] |  (optional)
    filter_location_ids = ['filter_location_ids_example'] # List[str] |  (optional)

    try:
        # Create a filter
        api_instance.post_filters(filter_role_id, location_id=location_id, organization_id=organization_id, filter_search=filter_search, filter_override=filter_override, filter_permission_ids=filter_permission_ids, filter_organization_ids=filter_organization_ids, filter_location_ids=filter_location_ids)
    except Exception as e:
        print("Exception when calling FiltersApi->post_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_role_id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **filter_search** | **str**|  | [optional] 
 **filter_override** | **bool**|  | [optional] 
 **filter_permission_ids** | [**List[str]**](str.md)|  | [optional] 
 **filter_organization_ids** | [**List[str]**](str.md)|  | [optional] 
 **filter_location_ids** | [**List[str]**](str.md)|  | [optional] 

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

# **put_filters_id**
> put_filters_id(id, location_id=location_id, organization_id=organization_id, filter_role_id=filter_role_id, filter_search=filter_search, filter_override=filter_override, filter_permission_ids=filter_permission_ids, filter_organization_ids=filter_organization_ids, filter_location_ids=filter_location_ids)

Update a filter

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
    api_instance = foreman.FiltersApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    filter_role_id = 'filter_role_id_example' # str |  (optional)
    filter_search = 'filter_search_example' # str |  (optional)
    filter_override = True # bool |  (optional)
    filter_permission_ids = ['filter_permission_ids_example'] # List[str] |  (optional)
    filter_organization_ids = ['filter_organization_ids_example'] # List[str] |  (optional)
    filter_location_ids = ['filter_location_ids_example'] # List[str] |  (optional)

    try:
        # Update a filter
        api_instance.put_filters_id(id, location_id=location_id, organization_id=organization_id, filter_role_id=filter_role_id, filter_search=filter_search, filter_override=filter_override, filter_permission_ids=filter_permission_ids, filter_organization_ids=filter_organization_ids, filter_location_ids=filter_location_ids)
    except Exception as e:
        print("Exception when calling FiltersApi->put_filters_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **filter_role_id** | **str**|  | [optional] 
 **filter_search** | **str**|  | [optional] 
 **filter_override** | **bool**|  | [optional] 
 **filter_permission_ids** | [**List[str]**](str.md)|  | [optional] 
 **filter_organization_ids** | [**List[str]**](str.md)|  | [optional] 
 **filter_location_ids** | [**List[str]**](str.md)|  | [optional] 

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

