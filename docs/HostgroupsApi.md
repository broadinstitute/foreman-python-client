# pyforeman.HostgroupsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_hostgroups_id**](HostgroupsApi.md#delete_hostgroups_id) | **DELETE** /hostgroups/{id} | Delete a host group
[**get_hostgroups**](HostgroupsApi.md#get_hostgroups) | **GET** /hostgroups | List all host groups
[**get_hostgroups_id**](HostgroupsApi.md#get_hostgroups_id) | **GET** /hostgroups/{id} | Show a host group
[**get_locations_location_id_hostgroups**](HostgroupsApi.md#get_locations_location_id_hostgroups) | **GET** /locations/{location_id}/hostgroups | List all host groups per location
[**get_organizations_organization_id_hostgroups**](HostgroupsApi.md#get_organizations_organization_id_hostgroups) | **GET** /organizations/{organization_id}/hostgroups | List all host groups per organization
[**post_hostgroups**](HostgroupsApi.md#post_hostgroups) | **POST** /hostgroups | Create a host group
[**post_hostgroups_id_clone**](HostgroupsApi.md#post_hostgroups_id_clone) | **POST** /hostgroups/{id}/clone | Clone a host group
[**put_hostgroups_id**](HostgroupsApi.md#put_hostgroups_id) | **PUT** /hostgroups/{id} | Update a host group
[**put_hostgroups_id_rebuild_config**](HostgroupsApi.md#put_hostgroups_id_rebuild_config) | **PUT** /hostgroups/{id}/rebuild_config | Rebuild orchestration config


# **delete_hostgroups_id**
> delete_hostgroups_id(id, location_id=location_id, organization_id=organization_id)

Delete a host group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a host group
    api_instance.delete_hostgroups_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostgroupsApi->delete_hostgroups_id: %s\n" % e)
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

# **get_hostgroups**
> get_hostgroups(location_id, organization_id, search=search, order=order, page=page, per_page=per_page, include=include)

List all host groups



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)
include = ['include_example'] # list[str] | Array of extra information types to include (optional)

try:
    # List all host groups
    api_instance.get_hostgroups(location_id, organization_id, search=search, order=order, page=page, per_page=per_page, include=include)
except ApiException as e:
    print("Exception when calling HostgroupsApi->get_hostgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations |
 **organization_id** | **float**| Scope by organizations |
 **search** | **str**| filter results | [optional]
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional]
 **include** | [**list[str]**](str.md)| Array of extra information types to include | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostgroups_id**
> get_hostgroups_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)

Show a host group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
show_hidden_parameters = true # bool | Display hidden parameter values (optional)

try:
    # Show a host group
    api_instance.get_hostgroups_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)
except ApiException as e:
    print("Exception when calling HostgroupsApi->get_hostgroups_id: %s\n" % e)
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

# **get_locations_location_id_hostgroups**
> get_locations_location_id_hostgroups(location_id, organization_id, search=search, order=order, page=page, per_page=per_page, include=include)

List all host groups per location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)
include = ['include_example'] # list[str] | Array of extra information types to include (optional)

try:
    # List all host groups per location
    api_instance.get_locations_location_id_hostgroups(location_id, organization_id, search=search, order=order, page=page, per_page=per_page, include=include)
except ApiException as e:
    print("Exception when calling HostgroupsApi->get_locations_location_id_hostgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations |
 **organization_id** | **float**| Scope by organizations |
 **search** | **str**| filter results | [optional]
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional]
 **include** | [**list[str]**](str.md)| Array of extra information types to include | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_hostgroups**
> get_organizations_organization_id_hostgroups(organization_id, location_id, search=search, order=order, page=page, per_page=per_page, include=include)

List all host groups per organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
organization_id = 8.14 # float | Scope by organizations
location_id = 8.14 # float | Scope by locations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)
include = ['include_example'] # list[str] | Array of extra information types to include (optional)

try:
    # List all host groups per organization
    api_instance.get_organizations_organization_id_hostgroups(organization_id, location_id, search=search, order=order, page=page, per_page=per_page, include=include)
except ApiException as e:
    print("Exception when calling HostgroupsApi->get_organizations_organization_id_hostgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations |
 **location_id** | **float**| Scope by locations |
 **search** | **str**| filter results | [optional]
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional]
 **include** | [**list[str]**](str.md)| Array of extra information types to include | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hostgroups**
> post_hostgroups(hostgroup_name, location_id=location_id, organization_id=organization_id, hostgroup_description=hostgroup_description, hostgroup_parent_id=hostgroup_parent_id, hostgroup_compute_profile_id=hostgroup_compute_profile_id, hostgroup_compute_resource_id=hostgroup_compute_resource_id, hostgroup_operatingsystem_id=hostgroup_operatingsystem_id, hostgroup_architecture_id=hostgroup_architecture_id, hostgroup_pxe_loader=hostgroup_pxe_loader, hostgroup_medium_id=hostgroup_medium_id, hostgroup_ptable_id=hostgroup_ptable_id, hostgroup_subnet_id=hostgroup_subnet_id, hostgroup_subnet6_id=hostgroup_subnet6_id, hostgroup_domain_id=hostgroup_domain_id, hostgroup_realm_id=hostgroup_realm_id, hostgroup_group_parameters_attributes=hostgroup_group_parameters_attributes, hostgroup_puppet_proxy_id=hostgroup_puppet_proxy_id, hostgroup_puppet_ca_proxy_id=hostgroup_puppet_ca_proxy_id, hostgroup_root_pass=hostgroup_root_pass, hostgroup_location_ids=hostgroup_location_ids, hostgroup_organization_ids=hostgroup_organization_ids, hostgroup_content_source_id=hostgroup_content_source_id, hostgroup_content_view_id=hostgroup_content_view_id, hostgroup_lifecycle_environment_id=hostgroup_lifecycle_environment_id, hostgroup_kickstart_repository_id=hostgroup_kickstart_repository_id)

Create a host group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
hostgroup_name = 'hostgroup_name_example' # str | Name of the host group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
hostgroup_description = 'hostgroup_description_example' # str | Host group description (optional)
hostgroup_parent_id = 8.14 # float | Parent ID of the host group (optional)
hostgroup_compute_profile_id = 8.14 # float | Compute profile ID (optional)
hostgroup_compute_resource_id = 8.14 # float | Compute resource ID (optional)
hostgroup_operatingsystem_id = 8.14 # float | Operating system ID (optional)
hostgroup_architecture_id = 8.14 # float | Architecture ID (optional)
hostgroup_pxe_loader = 'hostgroup_pxe_loader_example' # str | DHCP filename option (Grub2/PXELinux by default) (optional)
hostgroup_medium_id = 8.14 # float | Media ID (optional)
hostgroup_ptable_id = 8.14 # float | Partition table ID (optional)
hostgroup_subnet_id = 8.14 # float | Subnet ID (optional)
hostgroup_subnet6_id = 8.14 # float | Subnet IPv6 ID (optional)
hostgroup_domain_id = 8.14 # float | Domain ID (optional)
hostgroup_realm_id = 8.14 # float | Realm ID (optional)
hostgroup_group_parameters_attributes = ['hostgroup_group_parameters_attributes_example'] # list[str] | Array of parameters (optional)
hostgroup_puppet_proxy_id = 8.14 # float | Puppet proxy ID (optional)
hostgroup_puppet_ca_proxy_id = 8.14 # float | Puppet CA proxy ID (optional)
hostgroup_root_pass = 'hostgroup_root_pass_example' # str | Root password on provisioned hosts (optional)
hostgroup_location_ids = ['hostgroup_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
hostgroup_organization_ids = ['hostgroup_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)
hostgroup_content_source_id = 8.14 # float | Content source ID (optional)
hostgroup_content_view_id = 8.14 # float | Content view ID (optional)
hostgroup_lifecycle_environment_id = 8.14 # float | Lifecycle environment ID (optional)
hostgroup_kickstart_repository_id = 8.14 # float | Kickstart repository ID (optional)

try:
    # Create a host group
    api_instance.post_hostgroups(hostgroup_name, location_id=location_id, organization_id=organization_id, hostgroup_description=hostgroup_description, hostgroup_parent_id=hostgroup_parent_id, hostgroup_compute_profile_id=hostgroup_compute_profile_id, hostgroup_compute_resource_id=hostgroup_compute_resource_id, hostgroup_operatingsystem_id=hostgroup_operatingsystem_id, hostgroup_architecture_id=hostgroup_architecture_id, hostgroup_pxe_loader=hostgroup_pxe_loader, hostgroup_medium_id=hostgroup_medium_id, hostgroup_ptable_id=hostgroup_ptable_id, hostgroup_subnet_id=hostgroup_subnet_id, hostgroup_subnet6_id=hostgroup_subnet6_id, hostgroup_domain_id=hostgroup_domain_id, hostgroup_realm_id=hostgroup_realm_id, hostgroup_group_parameters_attributes=hostgroup_group_parameters_attributes, hostgroup_puppet_proxy_id=hostgroup_puppet_proxy_id, hostgroup_puppet_ca_proxy_id=hostgroup_puppet_ca_proxy_id, hostgroup_root_pass=hostgroup_root_pass, hostgroup_location_ids=hostgroup_location_ids, hostgroup_organization_ids=hostgroup_organization_ids, hostgroup_content_source_id=hostgroup_content_source_id, hostgroup_content_view_id=hostgroup_content_view_id, hostgroup_lifecycle_environment_id=hostgroup_lifecycle_environment_id, hostgroup_kickstart_repository_id=hostgroup_kickstart_repository_id)
except ApiException as e:
    print("Exception when calling HostgroupsApi->post_hostgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostgroup_name** | **str**| Name of the host group |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **hostgroup_description** | **str**| Host group description | [optional]
 **hostgroup_parent_id** | **float**| Parent ID of the host group | [optional]
 **hostgroup_compute_profile_id** | **float**| Compute profile ID | [optional]
 **hostgroup_compute_resource_id** | **float**| Compute resource ID | [optional]
 **hostgroup_operatingsystem_id** | **float**| Operating system ID | [optional]
 **hostgroup_architecture_id** | **float**| Architecture ID | [optional]
 **hostgroup_pxe_loader** | **str**| DHCP filename option (Grub2/PXELinux by default) | [optional]
 **hostgroup_medium_id** | **float**| Media ID | [optional]
 **hostgroup_ptable_id** | **float**| Partition table ID | [optional]
 **hostgroup_subnet_id** | **float**| Subnet ID | [optional]
 **hostgroup_subnet6_id** | **float**| Subnet IPv6 ID | [optional]
 **hostgroup_domain_id** | **float**| Domain ID | [optional]
 **hostgroup_realm_id** | **float**| Realm ID | [optional]
 **hostgroup_group_parameters_attributes** | [**list[str]**](str.md)| Array of parameters | [optional]
 **hostgroup_puppet_proxy_id** | **float**| Puppet proxy ID | [optional]
 **hostgroup_puppet_ca_proxy_id** | **float**| Puppet CA proxy ID | [optional]
 **hostgroup_root_pass** | **str**| Root password on provisioned hosts | [optional]
 **hostgroup_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **hostgroup_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]
 **hostgroup_content_source_id** | **float**| Content source ID | [optional]
 **hostgroup_content_view_id** | **float**| Content view ID | [optional]
 **hostgroup_lifecycle_environment_id** | **float**| Lifecycle environment ID | [optional]
 **hostgroup_kickstart_repository_id** | **float**| Kickstart repository ID | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hostgroups_id_clone**
> post_hostgroups_id_clone(id, name, location_id=location_id, organization_id=organization_id)

Clone a host group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
id = 8.14 # float |
name = 'name_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Clone a host group
    api_instance.post_hostgroups_id_clone(id, name, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostgroupsApi->post_hostgroups_id_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **name** | **str**|  |
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

# **put_hostgroups_id**
> put_hostgroups_id(id, location_id=location_id, organization_id=organization_id, hostgroup_name=hostgroup_name, hostgroup_description=hostgroup_description, hostgroup_parent_id=hostgroup_parent_id, hostgroup_compute_profile_id=hostgroup_compute_profile_id, hostgroup_compute_resource_id=hostgroup_compute_resource_id, hostgroup_operatingsystem_id=hostgroup_operatingsystem_id, hostgroup_architecture_id=hostgroup_architecture_id, hostgroup_pxe_loader=hostgroup_pxe_loader, hostgroup_medium_id=hostgroup_medium_id, hostgroup_ptable_id=hostgroup_ptable_id, hostgroup_subnet_id=hostgroup_subnet_id, hostgroup_subnet6_id=hostgroup_subnet6_id, hostgroup_domain_id=hostgroup_domain_id, hostgroup_realm_id=hostgroup_realm_id, hostgroup_group_parameters_attributes=hostgroup_group_parameters_attributes, hostgroup_puppet_proxy_id=hostgroup_puppet_proxy_id, hostgroup_puppet_ca_proxy_id=hostgroup_puppet_ca_proxy_id, hostgroup_root_pass=hostgroup_root_pass, hostgroup_location_ids=hostgroup_location_ids, hostgroup_organization_ids=hostgroup_organization_ids, hostgroup_content_source_id=hostgroup_content_source_id, hostgroup_content_view_id=hostgroup_content_view_id, hostgroup_lifecycle_environment_id=hostgroup_lifecycle_environment_id, hostgroup_kickstart_repository_id=hostgroup_kickstart_repository_id)

Update a host group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
hostgroup_name = 'hostgroup_name_example' # str | Name of the host group (optional)
hostgroup_description = 'hostgroup_description_example' # str | Host group description (optional)
hostgroup_parent_id = 8.14 # float | Parent ID of the host group (optional)
hostgroup_compute_profile_id = 8.14 # float | Compute profile ID (optional)
hostgroup_compute_resource_id = 8.14 # float | Compute resource ID (optional)
hostgroup_operatingsystem_id = 8.14 # float | Operating system ID (optional)
hostgroup_architecture_id = 8.14 # float | Architecture ID (optional)
hostgroup_pxe_loader = 'hostgroup_pxe_loader_example' # str | DHCP filename option (Grub2/PXELinux by default) (optional)
hostgroup_medium_id = 8.14 # float | Media ID (optional)
hostgroup_ptable_id = 8.14 # float | Partition table ID (optional)
hostgroup_subnet_id = 8.14 # float | Subnet ID (optional)
hostgroup_subnet6_id = 8.14 # float | Subnet IPv6 ID (optional)
hostgroup_domain_id = 8.14 # float | Domain ID (optional)
hostgroup_realm_id = 8.14 # float | Realm ID (optional)
hostgroup_group_parameters_attributes = ['hostgroup_group_parameters_attributes_example'] # list[str] | Array of parameters (optional)
hostgroup_puppet_proxy_id = 8.14 # float | Puppet proxy ID (optional)
hostgroup_puppet_ca_proxy_id = 8.14 # float | Puppet CA proxy ID (optional)
hostgroup_root_pass = 'hostgroup_root_pass_example' # str | Root password on provisioned hosts (optional)
hostgroup_location_ids = ['hostgroup_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
hostgroup_organization_ids = ['hostgroup_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)
hostgroup_content_source_id = 8.14 # float | Content source ID (optional)
hostgroup_content_view_id = 8.14 # float | Content view ID (optional)
hostgroup_lifecycle_environment_id = 8.14 # float | Lifecycle environment ID (optional)
hostgroup_kickstart_repository_id = 8.14 # float | Kickstart repository ID (optional)

try:
    # Update a host group
    api_instance.put_hostgroups_id(id, location_id=location_id, organization_id=organization_id, hostgroup_name=hostgroup_name, hostgroup_description=hostgroup_description, hostgroup_parent_id=hostgroup_parent_id, hostgroup_compute_profile_id=hostgroup_compute_profile_id, hostgroup_compute_resource_id=hostgroup_compute_resource_id, hostgroup_operatingsystem_id=hostgroup_operatingsystem_id, hostgroup_architecture_id=hostgroup_architecture_id, hostgroup_pxe_loader=hostgroup_pxe_loader, hostgroup_medium_id=hostgroup_medium_id, hostgroup_ptable_id=hostgroup_ptable_id, hostgroup_subnet_id=hostgroup_subnet_id, hostgroup_subnet6_id=hostgroup_subnet6_id, hostgroup_domain_id=hostgroup_domain_id, hostgroup_realm_id=hostgroup_realm_id, hostgroup_group_parameters_attributes=hostgroup_group_parameters_attributes, hostgroup_puppet_proxy_id=hostgroup_puppet_proxy_id, hostgroup_puppet_ca_proxy_id=hostgroup_puppet_ca_proxy_id, hostgroup_root_pass=hostgroup_root_pass, hostgroup_location_ids=hostgroup_location_ids, hostgroup_organization_ids=hostgroup_organization_ids, hostgroup_content_source_id=hostgroup_content_source_id, hostgroup_content_view_id=hostgroup_content_view_id, hostgroup_lifecycle_environment_id=hostgroup_lifecycle_environment_id, hostgroup_kickstart_repository_id=hostgroup_kickstart_repository_id)
except ApiException as e:
    print("Exception when calling HostgroupsApi->put_hostgroups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **hostgroup_name** | **str**| Name of the host group | [optional]
 **hostgroup_description** | **str**| Host group description | [optional]
 **hostgroup_parent_id** | **float**| Parent ID of the host group | [optional]
 **hostgroup_compute_profile_id** | **float**| Compute profile ID | [optional]
 **hostgroup_compute_resource_id** | **float**| Compute resource ID | [optional]
 **hostgroup_operatingsystem_id** | **float**| Operating system ID | [optional]
 **hostgroup_architecture_id** | **float**| Architecture ID | [optional]
 **hostgroup_pxe_loader** | **str**| DHCP filename option (Grub2/PXELinux by default) | [optional]
 **hostgroup_medium_id** | **float**| Media ID | [optional]
 **hostgroup_ptable_id** | **float**| Partition table ID | [optional]
 **hostgroup_subnet_id** | **float**| Subnet ID | [optional]
 **hostgroup_subnet6_id** | **float**| Subnet IPv6 ID | [optional]
 **hostgroup_domain_id** | **float**| Domain ID | [optional]
 **hostgroup_realm_id** | **float**| Realm ID | [optional]
 **hostgroup_group_parameters_attributes** | [**list[str]**](str.md)| Array of parameters | [optional]
 **hostgroup_puppet_proxy_id** | **float**| Puppet proxy ID | [optional]
 **hostgroup_puppet_ca_proxy_id** | **float**| Puppet CA proxy ID | [optional]
 **hostgroup_root_pass** | **str**| Root password on provisioned hosts | [optional]
 **hostgroup_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **hostgroup_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]
 **hostgroup_content_source_id** | **float**| Content source ID | [optional]
 **hostgroup_content_view_id** | **float**| Content view ID | [optional]
 **hostgroup_lifecycle_environment_id** | **float**| Lifecycle environment ID | [optional]
 **hostgroup_kickstart_repository_id** | **float**| Kickstart repository ID | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hostgroups_id_rebuild_config**
> put_hostgroups_id_rebuild_config(id, location_id=location_id, organization_id=organization_id, only=only, children_hosts=children_hosts)

Rebuild orchestration config



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostgroupsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
only = ['only_example'] # list[str] | Limit rebuild steps, valid steps are DHCP, DNS, TFTP, Content_Host_Status, Refresh_Content_Host_Status (optional)
children_hosts = true # bool | Operate on child hostgroup hosts (optional)

try:
    # Rebuild orchestration config
    api_instance.put_hostgroups_id_rebuild_config(id, location_id=location_id, organization_id=organization_id, only=only, children_hosts=children_hosts)
except ApiException as e:
    print("Exception when calling HostgroupsApi->put_hostgroups_id_rebuild_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **only** | [**list[str]**](str.md)| Limit rebuild steps, valid steps are DHCP, DNS, TFTP, Content_Host_Status, Refresh_Content_Host_Status | [optional]
 **children_hosts** | **bool**| Operate on child hostgroup hosts | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
