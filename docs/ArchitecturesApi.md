# pyforeman.ArchitecturesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_architectures_id**](ArchitecturesApi.md#delete_architectures_id) | **DELETE** /architectures/{id} | Delete an architecture
[**get_architectures**](ArchitecturesApi.md#get_architectures) | **GET** /architectures | List all architectures
[**get_architectures_id**](ArchitecturesApi.md#get_architectures_id) | **GET** /architectures/{id} | Show an architecture
[**get_operatingsystems_operatingsystem_id_architectures**](ArchitecturesApi.md#get_operatingsystems_operatingsystem_id_architectures) | **GET** /operatingsystems/{operatingsystem_id}/architectures | List all architectures for operating system
[**post_architectures**](ArchitecturesApi.md#post_architectures) | **POST** /architectures | Create an architecture
[**put_architectures_id**](ArchitecturesApi.md#put_architectures_id) | **PUT** /architectures/{id} | Update an architecture


# **delete_architectures_id**
> delete_architectures_id(id, location_id=location_id, organization_id=organization_id)

Delete an architecture



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ArchitecturesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete an architecture
    api_instance.delete_architectures_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ArchitecturesApi->delete_architectures_id: %s\n" % e)
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

# **get_architectures**
> get_architectures(operatingsystem_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all architectures



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ArchitecturesApi()
operatingsystem_id = 8.14 # float | ID of operating system
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all architectures
    api_instance.get_architectures(operatingsystem_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ArchitecturesApi->get_architectures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system |
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_architectures_id**
> get_architectures_id(id, location_id=location_id, organization_id=organization_id)

Show an architecture



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ArchitecturesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show an architecture
    api_instance.get_architectures_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ArchitecturesApi->get_architectures_id: %s\n" % e)
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

# **get_operatingsystems_operatingsystem_id_architectures**
> get_operatingsystems_operatingsystem_id_architectures(operatingsystem_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all architectures for operating system



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ArchitecturesApi()
operatingsystem_id = 8.14 # float | ID of operating system
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all architectures for operating system
    api_instance.get_operatingsystems_operatingsystem_id_architectures(operatingsystem_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ArchitecturesApi->get_operatingsystems_operatingsystem_id_architectures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system |
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_architectures**
> post_architectures(architecture_name, location_id=location_id, organization_id=organization_id, architecture_operatingsystem_ids=architecture_operatingsystem_ids)

Create an architecture



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ArchitecturesApi()
architecture_name = 'architecture_name_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
architecture_operatingsystem_ids = ['architecture_operatingsystem_ids_example'] # list[str] | Operating system IDs (optional)

try:
    # Create an architecture
    api_instance.post_architectures(architecture_name, location_id=location_id, organization_id=organization_id, architecture_operatingsystem_ids=architecture_operatingsystem_ids)
except ApiException as e:
    print("Exception when calling ArchitecturesApi->post_architectures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architecture_name** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **architecture_operatingsystem_ids** | [**list[str]**](str.md)| Operating system IDs | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_architectures_id**
> put_architectures_id(id, location_id=location_id, organization_id=organization_id, architecture_name=architecture_name, architecture_operatingsystem_ids=architecture_operatingsystem_ids)

Update an architecture



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ArchitecturesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
architecture_name = 'architecture_name_example' # str |  (optional)
architecture_operatingsystem_ids = ['architecture_operatingsystem_ids_example'] # list[str] | Operating system IDs (optional)

try:
    # Update an architecture
    api_instance.put_architectures_id(id, location_id=location_id, organization_id=organization_id, architecture_name=architecture_name, architecture_operatingsystem_ids=architecture_operatingsystem_ids)
except ApiException as e:
    print("Exception when calling ArchitecturesApi->put_architectures_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **architecture_name** | **str**|  | [optional]
 **architecture_operatingsystem_ids** | [**list[str]**](str.md)| Operating system IDs | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
