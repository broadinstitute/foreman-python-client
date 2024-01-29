# foreman.RolesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_roles_id**](RolesApi.md#delete_roles_id) | **DELETE** /roles/{id} | Delete a role
[**get_roles**](RolesApi.md#get_roles) | **GET** /roles | List all roles
[**get_roles_id**](RolesApi.md#get_roles_id) | **GET** /roles/{id} | Show a role
[**post_roles**](RolesApi.md#post_roles) | **POST** /roles | Create a role
[**post_roles_id_clone**](RolesApi.md#post_roles_id_clone) | **POST** /roles/{id}/clone | Clone a role
[**put_roles_id**](RolesApi.md#put_roles_id) | **PUT** /roles/{id} | Update a role


# **delete_roles_id**
> delete_roles_id(id, location_id=location_id, organization_id=organization_id)

Delete a role

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
    api_instance = foreman.RolesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a role
        api_instance.delete_roles_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RolesApi->delete_roles_id: %s\n" % e)
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

# **get_roles**
> get_roles(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all roles

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
    api_instance = foreman.RolesApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all roles
        api_instance.get_roles(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling RolesApi->get_roles: %s\n" % e)
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

# **get_roles_id**
> get_roles_id(id, location_id=location_id, organization_id=organization_id, description=description)

Show a role

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
    api_instance = foreman.RolesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    description = 'description_example' # str |  (optional)

    try:
        # Show a role
        api_instance.get_roles_id(id, location_id=location_id, organization_id=organization_id, description=description)
    except Exception as e:
        print("Exception when calling RolesApi->get_roles_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **description** | **str**|  | [optional] 

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

# **post_roles**
> post_roles(role_name, location_id=location_id, organization_id=organization_id, role_description=role_description, role_location_ids=role_location_ids, role_organization_ids=role_organization_ids)

Create a role

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
    api_instance = foreman.RolesApi(api_client)
    role_name = 'role_name_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    role_description = 'role_description_example' # str | Role description (optional)
    role_location_ids = ['role_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    role_organization_ids = ['role_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Create a role
        api_instance.post_roles(role_name, location_id=location_id, organization_id=organization_id, role_description=role_description, role_location_ids=role_location_ids, role_organization_ids=role_organization_ids)
    except Exception as e:
        print("Exception when calling RolesApi->post_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **role_description** | **str**| Role description | [optional] 
 **role_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **role_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

# **post_roles_id_clone**
> post_roles_id_clone(id, location_id=location_id, organization_id=organization_id, role_name=role_name, role_description=role_description, role_location_ids=role_location_ids, role_organization_ids=role_organization_ids)

Clone a role

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
    api_instance = foreman.RolesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    role_name = 'role_name_example' # str |  (optional)
    role_description = 'role_description_example' # str | Role description (optional)
    role_location_ids = ['role_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    role_organization_ids = ['role_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Clone a role
        api_instance.post_roles_id_clone(id, location_id=location_id, organization_id=organization_id, role_name=role_name, role_description=role_description, role_location_ids=role_location_ids, role_organization_ids=role_organization_ids)
    except Exception as e:
        print("Exception when calling RolesApi->post_roles_id_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **role_name** | **str**|  | [optional] 
 **role_description** | **str**| Role description | [optional] 
 **role_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **role_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

# **put_roles_id**
> put_roles_id(id, location_id=location_id, organization_id=organization_id, role_name=role_name, role_description=role_description, role_location_ids=role_location_ids, role_organization_ids=role_organization_ids)

Update a role

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
    api_instance = foreman.RolesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    role_name = 'role_name_example' # str |  (optional)
    role_description = 'role_description_example' # str | Role description (optional)
    role_location_ids = ['role_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    role_organization_ids = ['role_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Update a role
        api_instance.put_roles_id(id, location_id=location_id, organization_id=organization_id, role_name=role_name, role_description=role_description, role_location_ids=role_location_ids, role_organization_ids=role_organization_ids)
    except Exception as e:
        print("Exception when calling RolesApi->put_roles_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **role_name** | **str**|  | [optional] 
 **role_description** | **str**| Role description | [optional] 
 **role_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **role_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

