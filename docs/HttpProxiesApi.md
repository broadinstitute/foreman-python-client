# pyforeman.HttpProxiesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_http_proxies_id**](HttpProxiesApi.md#delete_http_proxies_id) | **DELETE** /http_proxies/{id} | Delete an HTTP Proxy
[**get_http_proxies**](HttpProxiesApi.md#get_http_proxies) | **GET** /http_proxies | List of HTTP Proxies
[**get_http_proxies_id**](HttpProxiesApi.md#get_http_proxies_id) | **GET** /http_proxies/{id} | Show an HTTP Proxy
[**post_http_proxies**](HttpProxiesApi.md#post_http_proxies) | **POST** /http_proxies | Create an HTTP Proxy
[**put_http_proxies_id**](HttpProxiesApi.md#put_http_proxies_id) | **PUT** /http_proxies/{id} | Update an HTTP Proxy


# **delete_http_proxies_id**
> delete_http_proxies_id(id, location_id=location_id, organization_id=organization_id)

Delete an HTTP Proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HttpProxiesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete an HTTP Proxy
    api_instance.delete_http_proxies_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HttpProxiesApi->delete_http_proxies_id: %s\n" % e)
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

# **get_http_proxies**
> get_http_proxies(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of HTTP Proxies



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HttpProxiesApi()
location_id = 8.14 # float | Scope by locations (optional)
organization_id = 8.14 # float | Scope by organizations (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of HTTP Proxies
    api_instance.get_http_proxies(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling HttpProxiesApi->get_http_proxies: %s\n" % e)
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

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_proxies_id**
> get_http_proxies_id(id, location_id=location_id, organization_id=organization_id)

Show an HTTP Proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HttpProxiesApi()
id = 'id_example' # str | Identifier of the HTTP Proxy
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show an HTTP Proxy
    api_instance.get_http_proxies_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HttpProxiesApi->get_http_proxies_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the HTTP Proxy |
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

# **post_http_proxies**
> post_http_proxies(http_proxy_name, http_proxy_url, location_id=location_id, organization_id=organization_id, http_proxy_username=http_proxy_username, http_proxy_password=http_proxy_password, http_proxy_location_ids=http_proxy_location_ids, http_proxy_organization_ids=http_proxy_organization_ids)

Create an HTTP Proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HttpProxiesApi()
http_proxy_name = 'http_proxy_name_example' # str | The HTTP Proxy name
http_proxy_url = 'http_proxy_url_example' # str | URL of the HTTP Proxy
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
http_proxy_username = 'http_proxy_username_example' # str | Username used to authenticate with the HTTP Proxy (optional)
http_proxy_password = 'http_proxy_password_example' # str | Password used to authenticate with the HTTP Proxy (optional)
http_proxy_location_ids = ['http_proxy_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
http_proxy_organization_ids = ['http_proxy_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Create an HTTP Proxy
    api_instance.post_http_proxies(http_proxy_name, http_proxy_url, location_id=location_id, organization_id=organization_id, http_proxy_username=http_proxy_username, http_proxy_password=http_proxy_password, http_proxy_location_ids=http_proxy_location_ids, http_proxy_organization_ids=http_proxy_organization_ids)
except ApiException as e:
    print("Exception when calling HttpProxiesApi->post_http_proxies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_proxy_name** | **str**| The HTTP Proxy name |
 **http_proxy_url** | **str**| URL of the HTTP Proxy |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **http_proxy_username** | **str**| Username used to authenticate with the HTTP Proxy | [optional]
 **http_proxy_password** | **str**| Password used to authenticate with the HTTP Proxy | [optional]
 **http_proxy_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **http_proxy_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_http_proxies_id**
> put_http_proxies_id(id, location_id=location_id, organization_id=organization_id, http_proxy_name=http_proxy_name, http_proxy_url=http_proxy_url, http_proxy_username=http_proxy_username, http_proxy_password=http_proxy_password, http_proxy_location_ids=http_proxy_location_ids, http_proxy_organization_ids=http_proxy_organization_ids)

Update an HTTP Proxy



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HttpProxiesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
http_proxy_name = 'http_proxy_name_example' # str | The HTTP Proxy name (optional)
http_proxy_url = 'http_proxy_url_example' # str | URL of the HTTP Proxy (optional)
http_proxy_username = 'http_proxy_username_example' # str | Username used to authenticate with the HTTP Proxy (optional)
http_proxy_password = 'http_proxy_password_example' # str | Password used to authenticate with the HTTP Proxy (optional)
http_proxy_location_ids = ['http_proxy_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
http_proxy_organization_ids = ['http_proxy_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Update an HTTP Proxy
    api_instance.put_http_proxies_id(id, location_id=location_id, organization_id=organization_id, http_proxy_name=http_proxy_name, http_proxy_url=http_proxy_url, http_proxy_username=http_proxy_username, http_proxy_password=http_proxy_password, http_proxy_location_ids=http_proxy_location_ids, http_proxy_organization_ids=http_proxy_organization_ids)
except ApiException as e:
    print("Exception when calling HttpProxiesApi->put_http_proxies_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **http_proxy_name** | **str**| The HTTP Proxy name | [optional]
 **http_proxy_url** | **str**| URL of the HTTP Proxy | [optional]
 **http_proxy_username** | **str**| Username used to authenticate with the HTTP Proxy | [optional]
 **http_proxy_password** | **str**| Password used to authenticate with the HTTP Proxy | [optional]
 **http_proxy_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **http_proxy_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
