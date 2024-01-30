# pyforeman.ComputeProfilesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_compute_profiles_id**](ComputeProfilesApi.md#delete_compute_profiles_id) | **DELETE** /compute_profiles/{id} | Delete a compute profile
[**get_compute_profiles**](ComputeProfilesApi.md#get_compute_profiles) | **GET** /compute_profiles | List of compute profiles
[**get_compute_profiles_id**](ComputeProfilesApi.md#get_compute_profiles_id) | **GET** /compute_profiles/{id} | Show a compute profile
[**post_compute_profiles**](ComputeProfilesApi.md#post_compute_profiles) | **POST** /compute_profiles | Create a compute profile
[**put_compute_profiles_id**](ComputeProfilesApi.md#put_compute_profiles_id) | **PUT** /compute_profiles/{id} | Update a compute profile


# **delete_compute_profiles_id**
> delete_compute_profiles_id(id, location_id=location_id, organization_id=organization_id)

Delete a compute profile



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeProfilesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a compute profile
    api_instance.delete_compute_profiles_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeProfilesApi->delete_compute_profiles_id: %s\n" % e)
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

# **get_compute_profiles**
> get_compute_profiles(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of compute profiles



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeProfilesApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of compute profiles
    api_instance.get_compute_profiles(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ComputeProfilesApi->get_compute_profiles: %s\n" % e)
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compute_profiles_id**
> get_compute_profiles_id(id, location_id=location_id, organization_id=organization_id)

Show a compute profile



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeProfilesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a compute profile
    api_instance.get_compute_profiles_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeProfilesApi->get_compute_profiles_id: %s\n" % e)
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

# **post_compute_profiles**
> post_compute_profiles(compute_profile_name, location_id=location_id, organization_id=organization_id)

Create a compute profile



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeProfilesApi()
compute_profile_name = 'compute_profile_name_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Create a compute profile
    api_instance.post_compute_profiles(compute_profile_name, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeProfilesApi->post_compute_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_profile_name** | **str**|  |
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

# **put_compute_profiles_id**
> put_compute_profiles_id(id, location_id=location_id, organization_id=organization_id, compute_profile_name=compute_profile_name)

Update a compute profile



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeProfilesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
compute_profile_name = 'compute_profile_name_example' # str |  (optional)

try:
    # Update a compute profile
    api_instance.put_compute_profiles_id(id, location_id=location_id, organization_id=organization_id, compute_profile_name=compute_profile_name)
except ApiException as e:
    print("Exception when calling ComputeProfilesApi->put_compute_profiles_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **compute_profile_name** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
