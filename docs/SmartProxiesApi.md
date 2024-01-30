# pyforeman.SmartProxiesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_smart_proxies_id**](SmartProxiesApi.md#delete_smart_proxies_id) | **DELETE** /smart_proxies/{id} | Delete a smart proxy
[**get_smart_proxies**](SmartProxiesApi.md#get_smart_proxies) | **GET** /smart_proxies | List all smart proxies
[**get_smart_proxies_id**](SmartProxiesApi.md#get_smart_proxies_id) | **GET** /smart_proxies/{id} | Show a smart proxy
[**post_smart_proxies**](SmartProxiesApi.md#post_smart_proxies) | **POST** /smart_proxies | Create a smart proxy
[**post_smart_proxies_id_import_subnets**](SmartProxiesApi.md#post_smart_proxies_id_import_subnets) | **POST** /smart_proxies/{id}/import_subnets | Import subnets from Smart proxy
[**put_smart_proxies_id**](SmartProxiesApi.md#put_smart_proxies_id) | **PUT** /smart_proxies/{id} | Update a smart proxy
[**put_smart_proxies_id_refresh**](SmartProxiesApi.md#put_smart_proxies_id_refresh) | **PUT** /smart_proxies/{id}/refresh | Refresh smart proxy features


# **delete_smart_proxies_id**
> delete_smart_proxies_id(id, location_id=location_id, organization_id=organization_id)

Delete a smart proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SmartProxiesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a smart proxy
    api_instance.delete_smart_proxies_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling SmartProxiesApi->delete_smart_proxies_id: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smart_proxies**
> get_smart_proxies(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page, include_status=include_status)

List all smart proxies



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SmartProxiesApi()
location_id = 8.14 # float | Scope by locations (optional)
organization_id = 8.14 # float | Scope by organizations (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)
include_status = true # bool | Flag to indicate whether to include status or not (optional)

try:
    # List all smart proxies
    api_instance.get_smart_proxies(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page, include_status=include_status)
except ApiException as e:
    print("Exception when calling SmartProxiesApi->get_smart_proxies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations | [optional]
 **organization_id** | **float**| Scope by organizations | [optional]
 **search** | **str**| filter results | [optional]
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional]
 **include_status** | **bool**| Flag to indicate whether to include status or not | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smart_proxies_id**
> get_smart_proxies_id(id, location_id=location_id, organization_id=organization_id, include_status=include_status, include_version=include_version)

Show a smart proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SmartProxiesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
include_status = true # bool | Flag to indicate whether to include status or not (optional)
include_version = true # bool | Flag to indicate whether to include version or not (optional)

try:
    # Show a smart proxy
    api_instance.get_smart_proxies_id(id, location_id=location_id, organization_id=organization_id, include_status=include_status, include_version=include_version)
except ApiException as e:
    print("Exception when calling SmartProxiesApi->get_smart_proxies_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **include_status** | **bool**| Flag to indicate whether to include status or not | [optional]
 **include_version** | **bool**| Flag to indicate whether to include version or not | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smart_proxies**
> post_smart_proxies(smart_proxy_name, smart_proxy_url, location_id=location_id, organization_id=organization_id, smart_proxy_location_ids=smart_proxy_location_ids, smart_proxy_organization_ids=smart_proxy_organization_ids, smart_proxy_download_policy=smart_proxy_download_policy, smart_proxy_http_proxy_id=smart_proxy_http_proxy_id)

Create a smart proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SmartProxiesApi()
smart_proxy_name = 'smart_proxy_name_example' # str |
smart_proxy_url = 'smart_proxy_url_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
smart_proxy_location_ids = ['smart_proxy_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
smart_proxy_organization_ids = ['smart_proxy_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)
smart_proxy_download_policy = 'smart_proxy_download_policy_example' # str | Download Policy of the capsule, must be one of on_demand, immediate, inherit, streamed (optional)
smart_proxy_http_proxy_id = 8.14 # float | Id of the HTTP proxy to use with alternate content sources (optional)

try:
    # Create a smart proxy
    api_instance.post_smart_proxies(smart_proxy_name, smart_proxy_url, location_id=location_id, organization_id=organization_id, smart_proxy_location_ids=smart_proxy_location_ids, smart_proxy_organization_ids=smart_proxy_organization_ids, smart_proxy_download_policy=smart_proxy_download_policy, smart_proxy_http_proxy_id=smart_proxy_http_proxy_id)
except ApiException as e:
    print("Exception when calling SmartProxiesApi->post_smart_proxies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_proxy_name** | **str**|  |
 **smart_proxy_url** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **smart_proxy_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **smart_proxy_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]
 **smart_proxy_download_policy** | **str**| Download Policy of the capsule, must be one of on_demand, immediate, inherit, streamed | [optional]
 **smart_proxy_http_proxy_id** | **float**| Id of the HTTP proxy to use with alternate content sources | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smart_proxies_id_import_subnets**
> post_smart_proxies_id_import_subnets(id, location_id=location_id, organization_id=organization_id)

Import subnets from Smart proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SmartProxiesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Import subnets from Smart proxy
    api_instance.post_smart_proxies_id_import_subnets(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling SmartProxiesApi->post_smart_proxies_id_import_subnets: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_smart_proxies_id**
> put_smart_proxies_id(id, location_id=location_id, organization_id=organization_id, smart_proxy_name=smart_proxy_name, smart_proxy_url=smart_proxy_url, smart_proxy_location_ids=smart_proxy_location_ids, smart_proxy_organization_ids=smart_proxy_organization_ids, smart_proxy_download_policy=smart_proxy_download_policy, smart_proxy_http_proxy_id=smart_proxy_http_proxy_id)

Update a smart proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SmartProxiesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
smart_proxy_name = 'smart_proxy_name_example' # str |  (optional)
smart_proxy_url = 'smart_proxy_url_example' # str |  (optional)
smart_proxy_location_ids = ['smart_proxy_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
smart_proxy_organization_ids = ['smart_proxy_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)
smart_proxy_download_policy = 'smart_proxy_download_policy_example' # str | Download Policy of the capsule, must be one of on_demand, immediate, inherit, streamed (optional)
smart_proxy_http_proxy_id = 8.14 # float | Id of the HTTP proxy to use with alternate content sources (optional)

try:
    # Update a smart proxy
    api_instance.put_smart_proxies_id(id, location_id=location_id, organization_id=organization_id, smart_proxy_name=smart_proxy_name, smart_proxy_url=smart_proxy_url, smart_proxy_location_ids=smart_proxy_location_ids, smart_proxy_organization_ids=smart_proxy_organization_ids, smart_proxy_download_policy=smart_proxy_download_policy, smart_proxy_http_proxy_id=smart_proxy_http_proxy_id)
except ApiException as e:
    print("Exception when calling SmartProxiesApi->put_smart_proxies_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **smart_proxy_name** | **str**|  | [optional]
 **smart_proxy_url** | **str**|  | [optional]
 **smart_proxy_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **smart_proxy_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]
 **smart_proxy_download_policy** | **str**| Download Policy of the capsule, must be one of on_demand, immediate, inherit, streamed | [optional]
 **smart_proxy_http_proxy_id** | **float**| Id of the HTTP proxy to use with alternate content sources | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_smart_proxies_id_refresh**
> put_smart_proxies_id_refresh(id, location_id=location_id, organization_id=organization_id)

Refresh smart proxy features



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SmartProxiesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Refresh smart proxy features
    api_instance.put_smart_proxies_id_refresh(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling SmartProxiesApi->put_smart_proxies_id_refresh: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
