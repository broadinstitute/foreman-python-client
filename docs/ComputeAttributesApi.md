# pyforeman.ComputeAttributesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compute_attributes_id**](ComputeAttributesApi.md#get_compute_attributes_id) | **GET** /compute_attributes/{id} | Show a compute attributes set
[**get_compute_profiles_compute_profile_id_compute_attributes**](ComputeAttributesApi.md#get_compute_profiles_compute_profile_id_compute_attributes) | **GET** /compute_profiles/{compute_profile_id}/compute_attributes | List of compute attributes for compute profile
[**get_compute_profiles_compute_profile_id_compute_attributes_id**](ComputeAttributesApi.md#get_compute_profiles_compute_profile_id_compute_attributes_id) | **GET** /compute_profiles/{compute_profile_id}/compute_attributes/{id} | Show a compute attributes set
[**get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes**](ComputeAttributesApi.md#get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes) | **GET** /compute_profiles/{compute_profile_id}/compute_resources/{compute_resource_id}/compute_attributes | List of compute attributes for provided compute profile and compute resource
[**get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id**](ComputeAttributesApi.md#get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id) | **GET** /compute_profiles/{compute_profile_id}/compute_resources/{compute_resource_id}/compute_attributes/{id} | Show a compute attributes set
[**get_compute_resources_compute_resource_id_compute_attributes**](ComputeAttributesApi.md#get_compute_resources_compute_resource_id_compute_attributes) | **GET** /compute_resources/{compute_resource_id}/compute_attributes | List of compute attributes for compute resource
[**get_compute_resources_compute_resource_id_compute_attributes_id**](ComputeAttributesApi.md#get_compute_resources_compute_resource_id_compute_attributes_id) | **GET** /compute_resources/{compute_resource_id}/compute_attributes/{id} | Show a compute attributes set
[**get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes**](ComputeAttributesApi.md#get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes) | **GET** /compute_resources/{compute_resource_id}/compute_profiles/{compute_profile_id}/compute_attributes | List of compute attributes for provided compute profile and compute resource
[**get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id**](ComputeAttributesApi.md#get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id) | **GET** /compute_resources/{compute_resource_id}/compute_profiles/{compute_profile_id}/compute_attributes/{id} | Show a compute attributes set
[**post_compute_attributes**](ComputeAttributesApi.md#post_compute_attributes) | **POST** /compute_attributes | Create a compute attributes set
[**post_compute_profiles_compute_profile_id_compute_attributes**](ComputeAttributesApi.md#post_compute_profiles_compute_profile_id_compute_attributes) | **POST** /compute_profiles/{compute_profile_id}/compute_attributes | Create a compute attributes set
[**post_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes**](ComputeAttributesApi.md#post_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes) | **POST** /compute_profiles/{compute_profile_id}/compute_resources/{compute_resource_id}/compute_attributes | Create a compute attributes set
[**post_compute_resources_compute_resource_id_compute_attributes**](ComputeAttributesApi.md#post_compute_resources_compute_resource_id_compute_attributes) | **POST** /compute_resources/{compute_resource_id}/compute_attributes | Create a compute attributes set
[**post_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes**](ComputeAttributesApi.md#post_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes) | **POST** /compute_resources/{compute_resource_id}/compute_profiles/{compute_profile_id}/compute_attributes | Create a compute attributes set
[**put_compute_attributes_id**](ComputeAttributesApi.md#put_compute_attributes_id) | **PUT** /compute_attributes/{id} | Update a compute attributes set
[**put_compute_profiles_compute_profile_id_compute_attributes_id**](ComputeAttributesApi.md#put_compute_profiles_compute_profile_id_compute_attributes_id) | **PUT** /compute_profiles/{compute_profile_id}/compute_attributes/{id} | Update a compute attributes set
[**put_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id**](ComputeAttributesApi.md#put_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id) | **PUT** /compute_profiles/{compute_profile_id}/compute_resources/{compute_resource_id}/compute_attributes/{id} | Update a compute attributes set
[**put_compute_resources_compute_resource_id_compute_attributes_id**](ComputeAttributesApi.md#put_compute_resources_compute_resource_id_compute_attributes_id) | **PUT** /compute_resources/{compute_resource_id}/compute_attributes/{id} | Update a compute attributes set
[**put_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id**](ComputeAttributesApi.md#put_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id) | **PUT** /compute_resources/{compute_resource_id}/compute_profiles/{compute_profile_id}/compute_attributes/{id} | Update a compute attributes set


# **get_compute_attributes_id**
> get_compute_attributes_id(id, location_id=location_id, organization_id=organization_id)

Show a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a compute attributes set
    api_instance.get_compute_attributes_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
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

# **get_compute_profiles_compute_profile_id_compute_attributes**
> get_compute_profiles_compute_profile_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of compute attributes for compute profile



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str | ID of compute profile
compute_resource_id = 'compute_resource_id_example' # str | ID of compute_resource
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of compute attributes for compute profile
    api_instance.get_compute_profiles_compute_profile_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_profiles_compute_profile_id_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**| ID of compute profile |
 **compute_resource_id** | **str**| ID of compute_resource |
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

# **get_compute_profiles_compute_profile_id_compute_attributes_id**
> get_compute_profiles_compute_profile_id_compute_attributes_id(compute_profile_id, id, location_id=location_id, organization_id=organization_id)

Show a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 8.14 # float |
id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a compute attributes set
    api_instance.get_compute_profiles_compute_profile_id_compute_attributes_id(compute_profile_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_profiles_compute_profile_id_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **float**|  |
 **id** | **float**|  |
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

# **get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes**
> get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of compute attributes for provided compute profile and compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str | ID of compute profile
compute_resource_id = 'compute_resource_id_example' # str | ID of compute_resource
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of compute attributes for provided compute profile and compute resource
    api_instance.get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**| ID of compute profile |
 **compute_resource_id** | **str**| ID of compute_resource |
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

# **get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id**
> get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id(compute_profile_id, compute_resource_id, id, location_id=location_id, organization_id=organization_id)

Show a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 8.14 # float |
compute_resource_id = 8.14 # float |
id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a compute attributes set
    api_instance.get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id(compute_profile_id, compute_resource_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **float**|  |
 **compute_resource_id** | **float**|  |
 **id** | **float**|  |
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

# **get_compute_resources_compute_resource_id_compute_attributes**
> get_compute_resources_compute_resource_id_compute_attributes(compute_resource_id, compute_profile_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of compute attributes for compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_resource_id = 'compute_resource_id_example' # str | ID of compute_resource
compute_profile_id = 'compute_profile_id_example' # str | ID of compute profile
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of compute attributes for compute resource
    api_instance.get_compute_resources_compute_resource_id_compute_attributes(compute_resource_id, compute_profile_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_resources_compute_resource_id_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **str**| ID of compute_resource |
 **compute_profile_id** | **str**| ID of compute profile |
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

# **get_compute_resources_compute_resource_id_compute_attributes_id**
> get_compute_resources_compute_resource_id_compute_attributes_id(compute_resource_id, id, location_id=location_id, organization_id=organization_id)

Show a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_resource_id = 8.14 # float |
id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a compute attributes set
    api_instance.get_compute_resources_compute_resource_id_compute_attributes_id(compute_resource_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_resources_compute_resource_id_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **float**|  |
 **id** | **float**|  |
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

# **get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes**
> get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of compute attributes for provided compute profile and compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str | ID of compute profile
compute_resource_id = 'compute_resource_id_example' # str | ID of compute_resource
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of compute attributes for provided compute profile and compute resource
    api_instance.get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**| ID of compute profile |
 **compute_resource_id** | **str**| ID of compute_resource |
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

# **get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id**
> get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id(compute_resource_id, compute_profile_id, id, location_id=location_id, organization_id=organization_id)

Show a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_resource_id = 8.14 # float |
compute_profile_id = 8.14 # float |
id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a compute attributes set
    api_instance.get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id(compute_resource_id, compute_profile_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->get_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **float**|  |
 **compute_profile_id** | **float**|  |
 **id** | **float**|  |
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

# **post_compute_attributes**
> post_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)

Create a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str |
compute_resource_id = 'compute_resource_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Create a compute attributes set
    api_instance.post_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->post_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**|  |
 **compute_resource_id** | **str**|  |
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

# **post_compute_profiles_compute_profile_id_compute_attributes**
> post_compute_profiles_compute_profile_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)

Create a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str |
compute_resource_id = 'compute_resource_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Create a compute attributes set
    api_instance.post_compute_profiles_compute_profile_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->post_compute_profiles_compute_profile_id_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**|  |
 **compute_resource_id** | **str**|  |
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

# **post_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes**
> post_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)

Create a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str |
compute_resource_id = 'compute_resource_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Create a compute attributes set
    api_instance.post_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->post_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**|  |
 **compute_resource_id** | **str**|  |
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

# **post_compute_resources_compute_resource_id_compute_attributes**
> post_compute_resources_compute_resource_id_compute_attributes(compute_resource_id, compute_profile_id, location_id=location_id, organization_id=organization_id)

Create a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_resource_id = 'compute_resource_id_example' # str |
compute_profile_id = 'compute_profile_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Create a compute attributes set
    api_instance.post_compute_resources_compute_resource_id_compute_attributes(compute_resource_id, compute_profile_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->post_compute_resources_compute_resource_id_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **str**|  |
 **compute_profile_id** | **str**|  |
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

# **post_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes**
> post_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)

Create a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str |
compute_resource_id = 'compute_resource_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Create a compute attributes set
    api_instance.post_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes(compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->post_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**|  |
 **compute_resource_id** | **str**|  |
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

# **put_compute_attributes_id**
> put_compute_attributes_id(id, compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)

Update a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
id = 'id_example' # str |
compute_profile_id = 'compute_profile_id_example' # str |
compute_resource_id = 'compute_resource_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Update a compute attributes set
    api_instance.put_compute_attributes_id(id, compute_profile_id, compute_resource_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->put_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **compute_profile_id** | **str**|  |
 **compute_resource_id** | **str**|  |
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

# **put_compute_profiles_compute_profile_id_compute_attributes_id**
> put_compute_profiles_compute_profile_id_compute_attributes_id(compute_profile_id, id, compute_resource_id, location_id=location_id, organization_id=organization_id)

Update a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str |
id = 'id_example' # str |
compute_resource_id = 'compute_resource_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Update a compute attributes set
    api_instance.put_compute_profiles_compute_profile_id_compute_attributes_id(compute_profile_id, id, compute_resource_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->put_compute_profiles_compute_profile_id_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**|  |
 **id** | **str**|  |
 **compute_resource_id** | **str**|  |
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

# **put_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id**
> put_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id(compute_profile_id, compute_resource_id, id, location_id=location_id, organization_id=organization_id)

Update a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str |
compute_resource_id = 'compute_resource_id_example' # str |
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Update a compute attributes set
    api_instance.put_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id(compute_profile_id, compute_resource_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->put_compute_profiles_compute_profile_id_compute_resources_compute_resource_id_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**|  |
 **compute_resource_id** | **str**|  |
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

# **put_compute_resources_compute_resource_id_compute_attributes_id**
> put_compute_resources_compute_resource_id_compute_attributes_id(compute_resource_id, id, compute_profile_id, location_id=location_id, organization_id=organization_id)

Update a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_resource_id = 'compute_resource_id_example' # str |
id = 'id_example' # str |
compute_profile_id = 'compute_profile_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Update a compute attributes set
    api_instance.put_compute_resources_compute_resource_id_compute_attributes_id(compute_resource_id, id, compute_profile_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->put_compute_resources_compute_resource_id_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_id** | **str**|  |
 **id** | **str**|  |
 **compute_profile_id** | **str**|  |
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

# **put_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id**
> put_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id(compute_profile_id, compute_resource_id, id, location_id=location_id, organization_id=organization_id)

Update a compute attributes set



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeAttributesApi()
compute_profile_id = 'compute_profile_id_example' # str |
compute_resource_id = 'compute_resource_id_example' # str |
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Update a compute attributes set
    api_instance.put_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id(compute_profile_id, compute_resource_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeAttributesApi->put_compute_resources_compute_resource_id_compute_profiles_compute_profile_id_compute_attributes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_id** | **str**|  |
 **compute_resource_id** | **str**|  |
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
