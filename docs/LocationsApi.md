# foreman.LocationsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_locations_id**](LocationsApi.md#delete_locations_id) | **DELETE** /locations/{id} | Delete a location
[**get_locations**](LocationsApi.md#get_locations) | **GET** /locations | List all locations
[**get_locations_id**](LocationsApi.md#get_locations_id) | **GET** /locations/{id} | Show a location
[**post_locations**](LocationsApi.md#post_locations) | **POST** /locations | Create a location
[**put_locations_id**](LocationsApi.md#put_locations_id) | **PUT** /locations/{id} | Update a location


# **delete_locations_id**
> delete_locations_id(id, location_id=location_id, organization_id=organization_id)

Delete a location

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
    api_instance = foreman.LocationsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a location
        api_instance.delete_locations_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling LocationsApi->delete_locations_id: %s\n" % e)
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

# **get_locations**
> get_locations(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all locations

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
    api_instance = foreman.LocationsApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all locations
        api_instance.get_locations(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling LocationsApi->get_locations: %s\n" % e)
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

# **get_locations_id**
> get_locations_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)

Show a location

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
    api_instance = foreman.LocationsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    show_hidden_parameters = True # bool | Display hidden parameter values (optional)

    try:
        # Show a location
        api_instance.get_locations_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)
    except Exception as e:
        print("Exception when calling LocationsApi->get_locations_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **show_hidden_parameters** | **bool**| Display hidden parameter values | [optional] 

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

# **post_locations**
> post_locations(location_name, location_id=location_id, organization_id=organization_id, location_description=location_description, location_user_ids=location_user_ids, location_smart_proxy_ids=location_smart_proxy_ids, location_compute_resource_ids=location_compute_resource_ids, location_medium_ids=location_medium_ids, location_ptable_ids=location_ptable_ids, location_provisioning_template_ids=location_provisioning_template_ids, location_domain_ids=location_domain_ids, location_realm_ids=location_realm_ids, location_hostgroup_ids=location_hostgroup_ids, location_environment_ids=location_environment_ids, location_subnet_ids=location_subnet_ids, location_parent_id=location_parent_id, location_ignore_types=location_ignore_types, location_organization_ids=location_organization_ids)

Create a location

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
    api_instance = foreman.LocationsApi(api_client)
    location_name = 'location_name_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    location_description = 'location_description_example' # str |  (optional)
    location_user_ids = ['location_user_ids_example'] # List[str] | User IDs (optional)
    location_smart_proxy_ids = ['location_smart_proxy_ids_example'] # List[str] | Smart proxy IDs (optional)
    location_compute_resource_ids = ['location_compute_resource_ids_example'] # List[str] | Compute resource IDs (optional)
    location_medium_ids = ['location_medium_ids_example'] # List[str] | Medium IDs (optional)
    location_ptable_ids = ['location_ptable_ids_example'] # List[str] | Partition template IDs (optional)
    location_provisioning_template_ids = ['location_provisioning_template_ids_example'] # List[str] | Provisioning template IDs (optional)
    location_domain_ids = ['location_domain_ids_example'] # List[str] | Domain IDs (optional)
    location_realm_ids = ['location_realm_ids_example'] # List[str] | Realm IDs (optional)
    location_hostgroup_ids = ['location_hostgroup_ids_example'] # List[str] | Host group IDs (optional)
    location_environment_ids = ['location_environment_ids_example'] # List[str] | Environment IDs (optional)
    location_subnet_ids = ['location_subnet_ids_example'] # List[str] | Subnet IDs (optional)
    location_parent_id = 3.4 # float | Parent ID (optional)
    location_ignore_types = ['location_ignore_types_example'] # List[str] | List of resources types that will be automatically associated (optional)
    location_organization_ids = ['location_organization_ids_example'] # List[str] | Associated organization IDs (optional)

    try:
        # Create a location
        api_instance.post_locations(location_name, location_id=location_id, organization_id=organization_id, location_description=location_description, location_user_ids=location_user_ids, location_smart_proxy_ids=location_smart_proxy_ids, location_compute_resource_ids=location_compute_resource_ids, location_medium_ids=location_medium_ids, location_ptable_ids=location_ptable_ids, location_provisioning_template_ids=location_provisioning_template_ids, location_domain_ids=location_domain_ids, location_realm_ids=location_realm_ids, location_hostgroup_ids=location_hostgroup_ids, location_environment_ids=location_environment_ids, location_subnet_ids=location_subnet_ids, location_parent_id=location_parent_id, location_ignore_types=location_ignore_types, location_organization_ids=location_organization_ids)
    except Exception as e:
        print("Exception when calling LocationsApi->post_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **location_description** | **str**|  | [optional] 
 **location_user_ids** | [**List[str]**](str.md)| User IDs | [optional] 
 **location_smart_proxy_ids** | [**List[str]**](str.md)| Smart proxy IDs | [optional] 
 **location_compute_resource_ids** | [**List[str]**](str.md)| Compute resource IDs | [optional] 
 **location_medium_ids** | [**List[str]**](str.md)| Medium IDs | [optional] 
 **location_ptable_ids** | [**List[str]**](str.md)| Partition template IDs | [optional] 
 **location_provisioning_template_ids** | [**List[str]**](str.md)| Provisioning template IDs | [optional] 
 **location_domain_ids** | [**List[str]**](str.md)| Domain IDs | [optional] 
 **location_realm_ids** | [**List[str]**](str.md)| Realm IDs | [optional] 
 **location_hostgroup_ids** | [**List[str]**](str.md)| Host group IDs | [optional] 
 **location_environment_ids** | [**List[str]**](str.md)| Environment IDs | [optional] 
 **location_subnet_ids** | [**List[str]**](str.md)| Subnet IDs | [optional] 
 **location_parent_id** | **float**| Parent ID | [optional] 
 **location_ignore_types** | [**List[str]**](str.md)| List of resources types that will be automatically associated | [optional] 
 **location_organization_ids** | [**List[str]**](str.md)| Associated organization IDs | [optional] 

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

# **put_locations_id**
> put_locations_id(id, location_id=location_id, organization_id=organization_id, location_name=location_name, location_description=location_description, location_user_ids=location_user_ids, location_smart_proxy_ids=location_smart_proxy_ids, location_compute_resource_ids=location_compute_resource_ids, location_medium_ids=location_medium_ids, location_ptable_ids=location_ptable_ids, location_provisioning_template_ids=location_provisioning_template_ids, location_domain_ids=location_domain_ids, location_realm_ids=location_realm_ids, location_hostgroup_ids=location_hostgroup_ids, location_environment_ids=location_environment_ids, location_subnet_ids=location_subnet_ids, location_parent_id=location_parent_id, location_ignore_types=location_ignore_types, location_organization_ids=location_organization_ids)

Update a location

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
    api_instance = foreman.LocationsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    location_name = 'location_name_example' # str |  (optional)
    location_description = 'location_description_example' # str |  (optional)
    location_user_ids = ['location_user_ids_example'] # List[str] | User IDs (optional)
    location_smart_proxy_ids = ['location_smart_proxy_ids_example'] # List[str] | Smart proxy IDs (optional)
    location_compute_resource_ids = ['location_compute_resource_ids_example'] # List[str] | Compute resource IDs (optional)
    location_medium_ids = ['location_medium_ids_example'] # List[str] | Medium IDs (optional)
    location_ptable_ids = ['location_ptable_ids_example'] # List[str] | Partition template IDs (optional)
    location_provisioning_template_ids = ['location_provisioning_template_ids_example'] # List[str] | Provisioning template IDs (optional)
    location_domain_ids = ['location_domain_ids_example'] # List[str] | Domain IDs (optional)
    location_realm_ids = ['location_realm_ids_example'] # List[str] | Realm IDs (optional)
    location_hostgroup_ids = ['location_hostgroup_ids_example'] # List[str] | Host group IDs (optional)
    location_environment_ids = ['location_environment_ids_example'] # List[str] | Environment IDs (optional)
    location_subnet_ids = ['location_subnet_ids_example'] # List[str] | Subnet IDs (optional)
    location_parent_id = 3.4 # float | Parent ID (optional)
    location_ignore_types = ['location_ignore_types_example'] # List[str] | List of resources types that will be automatically associated (optional)
    location_organization_ids = ['location_organization_ids_example'] # List[str] | Associated organization IDs (optional)

    try:
        # Update a location
        api_instance.put_locations_id(id, location_id=location_id, organization_id=organization_id, location_name=location_name, location_description=location_description, location_user_ids=location_user_ids, location_smart_proxy_ids=location_smart_proxy_ids, location_compute_resource_ids=location_compute_resource_ids, location_medium_ids=location_medium_ids, location_ptable_ids=location_ptable_ids, location_provisioning_template_ids=location_provisioning_template_ids, location_domain_ids=location_domain_ids, location_realm_ids=location_realm_ids, location_hostgroup_ids=location_hostgroup_ids, location_environment_ids=location_environment_ids, location_subnet_ids=location_subnet_ids, location_parent_id=location_parent_id, location_ignore_types=location_ignore_types, location_organization_ids=location_organization_ids)
    except Exception as e:
        print("Exception when calling LocationsApi->put_locations_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **location_name** | **str**|  | [optional] 
 **location_description** | **str**|  | [optional] 
 **location_user_ids** | [**List[str]**](str.md)| User IDs | [optional] 
 **location_smart_proxy_ids** | [**List[str]**](str.md)| Smart proxy IDs | [optional] 
 **location_compute_resource_ids** | [**List[str]**](str.md)| Compute resource IDs | [optional] 
 **location_medium_ids** | [**List[str]**](str.md)| Medium IDs | [optional] 
 **location_ptable_ids** | [**List[str]**](str.md)| Partition template IDs | [optional] 
 **location_provisioning_template_ids** | [**List[str]**](str.md)| Provisioning template IDs | [optional] 
 **location_domain_ids** | [**List[str]**](str.md)| Domain IDs | [optional] 
 **location_realm_ids** | [**List[str]**](str.md)| Realm IDs | [optional] 
 **location_hostgroup_ids** | [**List[str]**](str.md)| Host group IDs | [optional] 
 **location_environment_ids** | [**List[str]**](str.md)| Environment IDs | [optional] 
 **location_subnet_ids** | [**List[str]**](str.md)| Subnet IDs | [optional] 
 **location_parent_id** | **float**| Parent ID | [optional] 
 **location_ignore_types** | [**List[str]**](str.md)| List of resources types that will be automatically associated | [optional] 
 **location_organization_ids** | [**List[str]**](str.md)| Associated organization IDs | [optional] 

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

