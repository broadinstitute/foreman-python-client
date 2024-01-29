# pyforeman.LocationsApi

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
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LocationsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a location
    api_instance.delete_locations_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations**
> get_locations(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all locations



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LocationsApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all locations
    api_instance.get_locations(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations_id**
> get_locations_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)

Show a location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LocationsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
show_hidden_parameters = true # bool | Display hidden parameter values (optional)

try:
    # Show a location
    api_instance.get_locations_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)
except ApiException as e:
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_locations**
> post_locations(location_name, location_id=location_id, organization_id=organization_id, location_description=location_description, location_user_ids=location_user_ids, location_smart_proxy_ids=location_smart_proxy_ids, location_compute_resource_ids=location_compute_resource_ids, location_medium_ids=location_medium_ids, location_ptable_ids=location_ptable_ids, location_provisioning_template_ids=location_provisioning_template_ids, location_domain_ids=location_domain_ids, location_realm_ids=location_realm_ids, location_hostgroup_ids=location_hostgroup_ids, location_environment_ids=location_environment_ids, location_subnet_ids=location_subnet_ids, location_parent_id=location_parent_id, location_ignore_types=location_ignore_types, location_organization_ids=location_organization_ids)

Create a location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LocationsApi()
location_name = 'location_name_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
location_description = 'location_description_example' # str |  (optional)
location_user_ids = ['location_user_ids_example'] # list[str] | User IDs (optional)
location_smart_proxy_ids = ['location_smart_proxy_ids_example'] # list[str] | Smart proxy IDs (optional)
location_compute_resource_ids = ['location_compute_resource_ids_example'] # list[str] | Compute resource IDs (optional)
location_medium_ids = ['location_medium_ids_example'] # list[str] | Medium IDs (optional)
location_ptable_ids = ['location_ptable_ids_example'] # list[str] | Partition template IDs (optional)
location_provisioning_template_ids = ['location_provisioning_template_ids_example'] # list[str] | Provisioning template IDs (optional)
location_domain_ids = ['location_domain_ids_example'] # list[str] | Domain IDs (optional)
location_realm_ids = ['location_realm_ids_example'] # list[str] | Realm IDs (optional)
location_hostgroup_ids = ['location_hostgroup_ids_example'] # list[str] | Host group IDs (optional)
location_environment_ids = ['location_environment_ids_example'] # list[str] | Environment IDs (optional)
location_subnet_ids = ['location_subnet_ids_example'] # list[str] | Subnet IDs (optional)
location_parent_id = 8.14 # float | Parent ID (optional)
location_ignore_types = ['location_ignore_types_example'] # list[str] | List of resources types that will be automatically associated (optional)
location_organization_ids = ['location_organization_ids_example'] # list[str] | Associated organization IDs (optional)

try:
    # Create a location
    api_instance.post_locations(location_name, location_id=location_id, organization_id=organization_id, location_description=location_description, location_user_ids=location_user_ids, location_smart_proxy_ids=location_smart_proxy_ids, location_compute_resource_ids=location_compute_resource_ids, location_medium_ids=location_medium_ids, location_ptable_ids=location_ptable_ids, location_provisioning_template_ids=location_provisioning_template_ids, location_domain_ids=location_domain_ids, location_realm_ids=location_realm_ids, location_hostgroup_ids=location_hostgroup_ids, location_environment_ids=location_environment_ids, location_subnet_ids=location_subnet_ids, location_parent_id=location_parent_id, location_ignore_types=location_ignore_types, location_organization_ids=location_organization_ids)
except ApiException as e:
    print("Exception when calling LocationsApi->post_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_name** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **location_description** | **str**|  | [optional]
 **location_user_ids** | [**list[str]**](str.md)| User IDs | [optional]
 **location_smart_proxy_ids** | [**list[str]**](str.md)| Smart proxy IDs | [optional]
 **location_compute_resource_ids** | [**list[str]**](str.md)| Compute resource IDs | [optional]
 **location_medium_ids** | [**list[str]**](str.md)| Medium IDs | [optional]
 **location_ptable_ids** | [**list[str]**](str.md)| Partition template IDs | [optional]
 **location_provisioning_template_ids** | [**list[str]**](str.md)| Provisioning template IDs | [optional]
 **location_domain_ids** | [**list[str]**](str.md)| Domain IDs | [optional]
 **location_realm_ids** | [**list[str]**](str.md)| Realm IDs | [optional]
 **location_hostgroup_ids** | [**list[str]**](str.md)| Host group IDs | [optional]
 **location_environment_ids** | [**list[str]**](str.md)| Environment IDs | [optional]
 **location_subnet_ids** | [**list[str]**](str.md)| Subnet IDs | [optional]
 **location_parent_id** | **float**| Parent ID | [optional]
 **location_ignore_types** | [**list[str]**](str.md)| List of resources types that will be automatically associated | [optional]
 **location_organization_ids** | [**list[str]**](str.md)| Associated organization IDs | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_locations_id**
> put_locations_id(id, location_id=location_id, organization_id=organization_id, location_name=location_name, location_description=location_description, location_user_ids=location_user_ids, location_smart_proxy_ids=location_smart_proxy_ids, location_compute_resource_ids=location_compute_resource_ids, location_medium_ids=location_medium_ids, location_ptable_ids=location_ptable_ids, location_provisioning_template_ids=location_provisioning_template_ids, location_domain_ids=location_domain_ids, location_realm_ids=location_realm_ids, location_hostgroup_ids=location_hostgroup_ids, location_environment_ids=location_environment_ids, location_subnet_ids=location_subnet_ids, location_parent_id=location_parent_id, location_ignore_types=location_ignore_types, location_organization_ids=location_organization_ids)

Update a location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LocationsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
location_name = 'location_name_example' # str |  (optional)
location_description = 'location_description_example' # str |  (optional)
location_user_ids = ['location_user_ids_example'] # list[str] | User IDs (optional)
location_smart_proxy_ids = ['location_smart_proxy_ids_example'] # list[str] | Smart proxy IDs (optional)
location_compute_resource_ids = ['location_compute_resource_ids_example'] # list[str] | Compute resource IDs (optional)
location_medium_ids = ['location_medium_ids_example'] # list[str] | Medium IDs (optional)
location_ptable_ids = ['location_ptable_ids_example'] # list[str] | Partition template IDs (optional)
location_provisioning_template_ids = ['location_provisioning_template_ids_example'] # list[str] | Provisioning template IDs (optional)
location_domain_ids = ['location_domain_ids_example'] # list[str] | Domain IDs (optional)
location_realm_ids = ['location_realm_ids_example'] # list[str] | Realm IDs (optional)
location_hostgroup_ids = ['location_hostgroup_ids_example'] # list[str] | Host group IDs (optional)
location_environment_ids = ['location_environment_ids_example'] # list[str] | Environment IDs (optional)
location_subnet_ids = ['location_subnet_ids_example'] # list[str] | Subnet IDs (optional)
location_parent_id = 8.14 # float | Parent ID (optional)
location_ignore_types = ['location_ignore_types_example'] # list[str] | List of resources types that will be automatically associated (optional)
location_organization_ids = ['location_organization_ids_example'] # list[str] | Associated organization IDs (optional)

try:
    # Update a location
    api_instance.put_locations_id(id, location_id=location_id, organization_id=organization_id, location_name=location_name, location_description=location_description, location_user_ids=location_user_ids, location_smart_proxy_ids=location_smart_proxy_ids, location_compute_resource_ids=location_compute_resource_ids, location_medium_ids=location_medium_ids, location_ptable_ids=location_ptable_ids, location_provisioning_template_ids=location_provisioning_template_ids, location_domain_ids=location_domain_ids, location_realm_ids=location_realm_ids, location_hostgroup_ids=location_hostgroup_ids, location_environment_ids=location_environment_ids, location_subnet_ids=location_subnet_ids, location_parent_id=location_parent_id, location_ignore_types=location_ignore_types, location_organization_ids=location_organization_ids)
except ApiException as e:
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
 **location_user_ids** | [**list[str]**](str.md)| User IDs | [optional]
 **location_smart_proxy_ids** | [**list[str]**](str.md)| Smart proxy IDs | [optional]
 **location_compute_resource_ids** | [**list[str]**](str.md)| Compute resource IDs | [optional]
 **location_medium_ids** | [**list[str]**](str.md)| Medium IDs | [optional]
 **location_ptable_ids** | [**list[str]**](str.md)| Partition template IDs | [optional]
 **location_provisioning_template_ids** | [**list[str]**](str.md)| Provisioning template IDs | [optional]
 **location_domain_ids** | [**list[str]**](str.md)| Domain IDs | [optional]
 **location_realm_ids** | [**list[str]**](str.md)| Realm IDs | [optional]
 **location_hostgroup_ids** | [**list[str]**](str.md)| Host group IDs | [optional]
 **location_environment_ids** | [**list[str]**](str.md)| Environment IDs | [optional]
 **location_subnet_ids** | [**list[str]**](str.md)| Subnet IDs | [optional]
 **location_parent_id** | **float**| Parent ID | [optional]
 **location_ignore_types** | [**list[str]**](str.md)| List of resources types that will be automatically associated | [optional]
 **location_organization_ids** | [**list[str]**](str.md)| Associated organization IDs | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
