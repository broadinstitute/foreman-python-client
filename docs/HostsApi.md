# pyforeman.HostsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_hosts_id**](HostsApi.md#delete_hosts_id) | **DELETE** /hosts/{id} | Delete a host
[**delete_hosts_id_status_type**](HostsApi.md#delete_hosts_id_status_type) | **DELETE** /hosts/{id}/status/{type} | Clear sub-status of host
[**get_hostgroups_hostgroup_id_hosts**](HostsApi.md#get_hostgroups_hostgroup_id_hosts) | **GET** /hostgroups/{hostgroup_id}/hosts | List all hosts for a host group
[**get_hosts**](HostsApi.md#get_hosts) | **GET** /hosts | List all hosts
[**get_hosts_id**](HostsApi.md#get_hosts_id) | **GET** /hosts/{id} | Show a host
[**get_hosts_id_enc**](HostsApi.md#get_hosts_id_enc) | **GET** /hosts/{id}/enc | Get ENC values of host
[**get_hosts_id_inherited_parameters**](HostsApi.md#get_hosts_id_inherited_parameters) | **GET** /hosts/{id}/inherited_parameters | Get all inherited parameters for a host
[**get_hosts_id_power**](HostsApi.md#get_hosts_id_power) | **GET** /hosts/{id}/power | Fetch the status of whether the host is powered on or not. Supported hosts are VMs and physical hosts with BMCs.
[**get_hosts_id_status_type**](HostsApi.md#get_hosts_id_status_type) | **GET** /hosts/{id}/status/{type} | Get status of host
[**get_hosts_id_template_kind**](HostsApi.md#get_hosts_id_template_kind) | **GET** /hosts/{id}/template/{kind} | Preview rendered provisioning template content
[**get_hosts_id_templates**](HostsApi.md#get_hosts_id_templates) | **GET** /hosts/{id}/templates | Get provisioning templates for the host
[**get_hosts_id_vm_compute_attributes**](HostsApi.md#get_hosts_id_vm_compute_attributes) | **GET** /hosts/{id}/vm_compute_attributes | Get vm attributes of host
[**get_locations_location_id_hosts**](HostsApi.md#get_locations_location_id_hosts) | **GET** /locations/{location_id}/hosts | List hosts per location
[**get_organizations_organization_id_hosts**](HostsApi.md#get_organizations_organization_id_hosts) | **GET** /organizations/{organization_id}/hosts | List hosts per organization
[**post_hosts**](HostsApi.md#post_hosts) | **POST** /hosts | Create a host
[**post_hosts_facts**](HostsApi.md#post_hosts_facts) | **POST** /hosts/facts | Upload facts for a host, creating the host if required
[**put_hosts_host_id_host_collections**](HostsApi.md#put_hosts_host_id_host_collections) | **PUT** /hosts/{host_id}/host_collections | Alter a host&#39;s host collections
[**put_hosts_id**](HostsApi.md#put_hosts_id) | **PUT** /hosts/{id} | Update a host
[**put_hosts_id_boot**](HostsApi.md#put_hosts_id_boot) | **PUT** /hosts/{id}/boot | Boot host from specified device
[**put_hosts_id_disassociate**](HostsApi.md#put_hosts_id_disassociate) | **PUT** /hosts/{id}/disassociate | Disassociate the host from a VM
[**put_hosts_id_power**](HostsApi.md#put_hosts_id_power) | **PUT** /hosts/{id}/power | Run a power operation on host
[**put_hosts_id_rebuild_config**](HostsApi.md#put_hosts_id_rebuild_config) | **PUT** /hosts/{id}/rebuild_config | Rebuild orchestration config


# **delete_hosts_id**
> delete_hosts_id(id, location_id=location_id, organization_id=organization_id)

Delete a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a host
    api_instance.delete_hosts_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->delete_hosts_id: %s\n" % e)
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

# **delete_hosts_id_status_type**
> delete_hosts_id_status_type(id, type, location_id=location_id, organization_id=organization_id)

Clear sub-status of host

Clears a host sub-status of a given type

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
type = 'type_example' # str | status type
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Clear sub-status of host
    api_instance.delete_hosts_id_status_type(id, type, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->delete_hosts_id_status_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **type** | **str**| status type  |
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

# **get_hostgroups_hostgroup_id_hosts**
> get_hostgroups_hostgroup_id_hosts(hostgroup_id, location_id, organization_id, thin=thin, include=include, search=search, order=order, page=page, per_page=per_page)

List all hosts for a host group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
location_id = 'location_id_example' # str | ID of location
organization_id = 'organization_id_example' # str | ID of organization
thin = true # bool | Only list ID and name of hosts (optional)
include = 'include_example' # str | Array of extra information types to include (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all hosts for a host group
    api_instance.get_hostgroups_hostgroup_id_hosts(hostgroup_id, location_id, organization_id, thin=thin, include=include, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling HostsApi->get_hostgroups_hostgroup_id_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostgroup_id** | **str**| ID of host group |
 **location_id** | **str**| ID of location |
 **organization_id** | **str**| ID of organization |
 **thin** | **bool**| Only list ID and name of hosts | [optional]
 **include** | **str**| Array of extra information types to include | [optional]
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

# **get_hosts**
> get_hosts(hostgroup_id, location_id, organization_id, thin=thin, include=include, search=search, order=order, page=page, per_page=per_page)

List all hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
location_id = 'location_id_example' # str | ID of location
organization_id = 'organization_id_example' # str | ID of organization
thin = true # bool | Only list ID and name of hosts (optional)
include = 'include_example' # str | Array of extra information types to include (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all hosts
    api_instance.get_hosts(hostgroup_id, location_id, organization_id, thin=thin, include=include, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostgroup_id** | **str**| ID of host group |
 **location_id** | **str**| ID of location |
 **organization_id** | **str**| ID of organization |
 **thin** | **bool**| Only list ID and name of hosts | [optional]
 **include** | **str**| Array of extra information types to include | [optional]
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

# **get_hosts_id**
> get_hosts_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)

Show a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
show_hidden_parameters = true # bool | Display hidden parameter values (optional)

try:
    # Show a host
    api_instance.get_hosts_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_id: %s\n" % e)
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

# **get_hosts_id_enc**
> get_hosts_id_enc(id, location_id=location_id, organization_id=organization_id)

Get ENC values of host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Get ENC values of host
    api_instance.get_hosts_id_enc(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_id_enc: %s\n" % e)
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

# **get_hosts_id_inherited_parameters**
> get_hosts_id_inherited_parameters(id, location_id=location_id, organization_id=organization_id)

Get all inherited parameters for a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Get all inherited parameters for a host
    api_instance.get_hosts_id_inherited_parameters(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_id_inherited_parameters: %s\n" % e)
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

# **get_hosts_id_power**
> get_hosts_id_power(id, location_id=location_id, organization_id=organization_id, timeout=timeout)

Fetch the status of whether the host is powered on or not. Supported hosts are VMs and physical hosts with BMCs.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
timeout = 'timeout_example' # str | Timeout to retrieve the power status of the host in seconds. Default is 3 seconds. (optional)

try:
    # Fetch the status of whether the host is powered on or not. Supported hosts are VMs and physical hosts with BMCs.
    api_instance.get_hosts_id_power(id, location_id=location_id, organization_id=organization_id, timeout=timeout)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_id_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **timeout** | **str**| Timeout to retrieve the power status of the host in seconds. Default is 3 seconds. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosts_id_status_type**
> get_hosts_id_status_type(id, type, location_id=location_id, organization_id=organization_id)

Get status of host

Returns string representing a host status of a given type

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
type = 'type_example' # str | status type, can be one of * global * configuration * build
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Get status of host
    api_instance.get_hosts_id_status_type(id, type, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_id_status_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **type** | **str**| status type, can be one of * global * configuration * build  |
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

# **get_hosts_id_template_kind**
> get_hosts_id_template_kind(id, kind, location_id=location_id, organization_id=organization_id)

Preview rendered provisioning template content



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
kind = 'kind_example' # str | Template kinds, available values: Bootdisk, PXELinux, PXEGrub, PXEGrub2, iPXE, provision, finish, script, user_data, ZTP, POAP, cloud-init, host_init_config, registration, kexec
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Preview rendered provisioning template content
    api_instance.get_hosts_id_template_kind(id, kind, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_id_template_kind: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **kind** | **str**| Template kinds, available values: Bootdisk, PXELinux, PXEGrub, PXEGrub2, iPXE, provision, finish, script, user_data, ZTP, POAP, cloud-init, host_init_config, registration, kexec |
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

# **get_hosts_id_templates**
> get_hosts_id_templates(id, location_id=location_id, organization_id=organization_id)

Get provisioning templates for the host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Get provisioning templates for the host
    api_instance.get_hosts_id_templates(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_id_templates: %s\n" % e)
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

# **get_hosts_id_vm_compute_attributes**
> get_hosts_id_vm_compute_attributes(id, location_id=location_id, organization_id=organization_id)

Get vm attributes of host

Return the host's compute attributes that can be used to create a clone of this VM

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Get vm attributes of host
    api_instance.get_hosts_id_vm_compute_attributes(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_id_vm_compute_attributes: %s\n" % e)
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

# **get_locations_location_id_hosts**
> get_locations_location_id_hosts(location_id, hostgroup_id, organization_id, thin=thin, include=include, search=search, order=order, page=page, per_page=per_page)

List hosts per location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
location_id = 'location_id_example' # str | ID of location
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
organization_id = 'organization_id_example' # str | ID of organization
thin = true # bool | Only list ID and name of hosts (optional)
include = 'include_example' # str | Array of extra information types to include (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List hosts per location
    api_instance.get_locations_location_id_hosts(location_id, hostgroup_id, organization_id, thin=thin, include=include, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling HostsApi->get_locations_location_id_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| ID of location |
 **hostgroup_id** | **str**| ID of host group |
 **organization_id** | **str**| ID of organization |
 **thin** | **bool**| Only list ID and name of hosts | [optional]
 **include** | **str**| Array of extra information types to include | [optional]
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

# **get_organizations_organization_id_hosts**
> get_organizations_organization_id_hosts(organization_id, hostgroup_id, location_id, thin=thin, include=include, search=search, order=order, page=page, per_page=per_page)

List hosts per organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
organization_id = 'organization_id_example' # str | ID of organization
hostgroup_id = 'hostgroup_id_example' # str | ID of host group
location_id = 'location_id_example' # str | ID of location
thin = true # bool | Only list ID and name of hosts (optional)
include = 'include_example' # str | Array of extra information types to include (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List hosts per organization
    api_instance.get_organizations_organization_id_hosts(organization_id, hostgroup_id, location_id, thin=thin, include=include, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling HostsApi->get_organizations_organization_id_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| ID of organization |
 **hostgroup_id** | **str**| ID of host group |
 **location_id** | **str**| ID of location |
 **thin** | **bool**| Only list ID and name of hosts | [optional]
 **include** | **str**| Array of extra information types to include | [optional]
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

# **post_hosts**
> post_hosts(host_name, host_location_id, host_organization_id, location_id=location_id, organization_id=organization_id, host_ip=host_ip, host_mac=host_mac, host_architecture_id=host_architecture_id, host_domain_id=host_domain_id, host_realm_id=host_realm_id, host_puppet_proxy_id=host_puppet_proxy_id, host_puppet_ca_proxy_id=host_puppet_ca_proxy_id, host_operatingsystem_id=host_operatingsystem_id, host_medium_id=host_medium_id, host_pxe_loader=host_pxe_loader, host_ptable_id=host_ptable_id, host_subnet_id=host_subnet_id, host_compute_resource_id=host_compute_resource_id, host_root_pass=host_root_pass, host_model_id=host_model_id, host_hostgroup_id=host_hostgroup_id, host_owner_id=host_owner_id, host_owner_type=host_owner_type, host_image_id=host_image_id, host_host_parameters_attributes=host_host_parameters_attributes, host_build=host_build, host_enabled=host_enabled, host_provision_method=host_provision_method, host_managed=host_managed, host_progress_report_id=host_progress_report_id, host_comment=host_comment, host_capabilities=host_capabilities, host_compute_profile_id=host_compute_profile_id, host_interfaces_attributes=host_interfaces_attributes, host_content_facet_attributes_content_view_id=host_content_facet_attributes_content_view_id, host_content_facet_attributes_lifecycle_environment_id=host_content_facet_attributes_lifecycle_environment_id, host_content_facet_attributes_content_source_id=host_content_facet_attributes_content_source_id, host_content_facet_attributes_kickstart_repository_id=host_content_facet_attributes_kickstart_repository_id, host_subscription_facet_attributes_release_version=host_subscription_facet_attributes_release_version, host_subscription_facet_attributes_autoheal=host_subscription_facet_attributes_autoheal, host_subscription_facet_attributes_purpose_usage=host_subscription_facet_attributes_purpose_usage, host_subscription_facet_attributes_purpose_role=host_subscription_facet_attributes_purpose_role, host_subscription_facet_attributes_purpose_addons=host_subscription_facet_attributes_purpose_addons, host_subscription_facet_attributes_service_level=host_subscription_facet_attributes_service_level, host_subscription_facet_attributes_hypervisor_guest_uuids=host_subscription_facet_attributes_hypervisor_guest_uuids, host_subscription_facet_attributes_installed_products_attributes=host_subscription_facet_attributes_installed_products_attributes, host_overwrite=host_overwrite)

Create a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
host_name = 'host_name_example' # str |
host_location_id = 8.14 # float |
host_organization_id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
host_ip = 'host_ip_example' # str | not required if using a subnet with DHCP proxy (optional)
host_mac = 'host_mac_example' # str | required for managed host that is bare metal, not required if it's a virtual machine (optional)
host_architecture_id = 8.14 # float | required if host is managed and value is not inherited from host group (optional)
host_domain_id = 8.14 # float | required if host is managed and value is not inherited from host group (optional)
host_realm_id = 8.14 # float |  (optional)
host_puppet_proxy_id = 8.14 # float | Puppet proxy ID (optional)
host_puppet_ca_proxy_id = 8.14 # float | Puppet CA proxy ID (optional)
host_operatingsystem_id = 8.14 # float | required if host is managed and value is not inherited from host group (optional)
host_medium_id = 'host_medium_id_example' # str | required if not imaged based provisioning and host is managed and value is not inherited from host group (optional)
host_pxe_loader = 'host_pxe_loader_example' # str | DHCP filename option (Grub2/PXELinux by default) (optional)
host_ptable_id = 8.14 # float | required if host is managed and custom partition has not been defined (optional)
host_subnet_id = 8.14 # float | required if host is managed and value is not inherited from host group (optional)
host_compute_resource_id = 8.14 # float | nil means host is bare metal (optional)
host_root_pass = 'host_root_pass_example' # str | required if host is managed and value is not inherited from host group or default password in settings (optional)
host_model_id = 8.14 # float |  (optional)
host_hostgroup_id = 8.14 # float |  (optional)
host_owner_id = 8.14 # float |  (optional)
host_owner_type = 'host_owner_type_example' # str | Host's owner type (optional)
host_image_id = 8.14 # float |  (optional)
host_host_parameters_attributes = ['host_host_parameters_attributes_example'] # list[str] | Host's parameters (array or indexed hash) (optional)
host_build = true # bool |  (optional)
host_enabled = true # bool | Include this host within Foreman reporting (optional)
host_provision_method = 'host_provision_method_example' # str | The method used to provision the host. (optional)
host_managed = true # bool | True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not (optional)
host_progress_report_id = 'host_progress_report_id_example' # str | UUID to track orchestration tasks status, GET /api/orchestration/:UUID/tasks (optional)
host_comment = 'host_comment_example' # str | Additional information about this host (optional)
host_capabilities = 'host_capabilities_example' # str |  (optional)
host_compute_profile_id = 8.14 # float |  (optional)
host_interfaces_attributes = ['host_interfaces_attributes_example'] # list[str] | Host's network interfaces. (optional)
host_content_facet_attributes_content_view_id = 8.14 # float |  (optional)
host_content_facet_attributes_lifecycle_environment_id = 8.14 # float |  (optional)
host_content_facet_attributes_content_source_id = 8.14 # float |  (optional)
host_content_facet_attributes_kickstart_repository_id = 8.14 # float | Repository Id associated with the kickstart repo used for provisioning (optional)
host_subscription_facet_attributes_release_version = 'host_subscription_facet_attributes_release_version_example' # str | Release version for this Host to use (7Server, 7.1, etc) (optional)
host_subscription_facet_attributes_autoheal = true # bool | Sets whether the Host will autoheal subscriptions upon checkin (optional)
host_subscription_facet_attributes_purpose_usage = 'host_subscription_facet_attributes_purpose_usage_example' # str | Sets the system purpose usage (optional)
host_subscription_facet_attributes_purpose_role = 'host_subscription_facet_attributes_purpose_role_example' # str | Sets the system purpose usage (optional)
host_subscription_facet_attributes_purpose_addons = ['host_subscription_facet_attributes_purpose_addons_example'] # list[str] | Sets the system add-ons (optional)
host_subscription_facet_attributes_service_level = 'host_subscription_facet_attributes_service_level_example' # str | Service level to be used for autoheal (optional)
host_subscription_facet_attributes_hypervisor_guest_uuids = ['host_subscription_facet_attributes_hypervisor_guest_uuids_example'] # list[str] | List of hypervisor guest uuids (optional)
host_subscription_facet_attributes_installed_products_attributes = ['host_subscription_facet_attributes_installed_products_attributes_example'] # list[str] | List of products installed on the host (optional)
host_overwrite = true # bool | Overwrite existing host (true by default) (optional)

try:
    # Create a host
    api_instance.post_hosts(host_name, host_location_id, host_organization_id, location_id=location_id, organization_id=organization_id, host_ip=host_ip, host_mac=host_mac, host_architecture_id=host_architecture_id, host_domain_id=host_domain_id, host_realm_id=host_realm_id, host_puppet_proxy_id=host_puppet_proxy_id, host_puppet_ca_proxy_id=host_puppet_ca_proxy_id, host_operatingsystem_id=host_operatingsystem_id, host_medium_id=host_medium_id, host_pxe_loader=host_pxe_loader, host_ptable_id=host_ptable_id, host_subnet_id=host_subnet_id, host_compute_resource_id=host_compute_resource_id, host_root_pass=host_root_pass, host_model_id=host_model_id, host_hostgroup_id=host_hostgroup_id, host_owner_id=host_owner_id, host_owner_type=host_owner_type, host_image_id=host_image_id, host_host_parameters_attributes=host_host_parameters_attributes, host_build=host_build, host_enabled=host_enabled, host_provision_method=host_provision_method, host_managed=host_managed, host_progress_report_id=host_progress_report_id, host_comment=host_comment, host_capabilities=host_capabilities, host_compute_profile_id=host_compute_profile_id, host_interfaces_attributes=host_interfaces_attributes, host_content_facet_attributes_content_view_id=host_content_facet_attributes_content_view_id, host_content_facet_attributes_lifecycle_environment_id=host_content_facet_attributes_lifecycle_environment_id, host_content_facet_attributes_content_source_id=host_content_facet_attributes_content_source_id, host_content_facet_attributes_kickstart_repository_id=host_content_facet_attributes_kickstart_repository_id, host_subscription_facet_attributes_release_version=host_subscription_facet_attributes_release_version, host_subscription_facet_attributes_autoheal=host_subscription_facet_attributes_autoheal, host_subscription_facet_attributes_purpose_usage=host_subscription_facet_attributes_purpose_usage, host_subscription_facet_attributes_purpose_role=host_subscription_facet_attributes_purpose_role, host_subscription_facet_attributes_purpose_addons=host_subscription_facet_attributes_purpose_addons, host_subscription_facet_attributes_service_level=host_subscription_facet_attributes_service_level, host_subscription_facet_attributes_hypervisor_guest_uuids=host_subscription_facet_attributes_hypervisor_guest_uuids, host_subscription_facet_attributes_installed_products_attributes=host_subscription_facet_attributes_installed_products_attributes, host_overwrite=host_overwrite)
except ApiException as e:
    print("Exception when calling HostsApi->post_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**|  |
 **host_location_id** | **float**|  |
 **host_organization_id** | **float**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **host_ip** | **str**| not required if using a subnet with DHCP proxy | [optional]
 **host_mac** | **str**| required for managed host that is bare metal, not required if it&#39;s a virtual machine | [optional]
 **host_architecture_id** | **float**| required if host is managed and value is not inherited from host group | [optional]
 **host_domain_id** | **float**| required if host is managed and value is not inherited from host group | [optional]
 **host_realm_id** | **float**|  | [optional]
 **host_puppet_proxy_id** | **float**| Puppet proxy ID | [optional]
 **host_puppet_ca_proxy_id** | **float**| Puppet CA proxy ID | [optional]
 **host_operatingsystem_id** | **float**| required if host is managed and value is not inherited from host group | [optional]
 **host_medium_id** | **str**| required if not imaged based provisioning and host is managed and value is not inherited from host group | [optional]
 **host_pxe_loader** | **str**| DHCP filename option (Grub2/PXELinux by default) | [optional]
 **host_ptable_id** | **float**| required if host is managed and custom partition has not been defined | [optional]
 **host_subnet_id** | **float**| required if host is managed and value is not inherited from host group | [optional]
 **host_compute_resource_id** | **float**| nil means host is bare metal | [optional]
 **host_root_pass** | **str**| required if host is managed and value is not inherited from host group or default password in settings | [optional]
 **host_model_id** | **float**|  | [optional]
 **host_hostgroup_id** | **float**|  | [optional]
 **host_owner_id** | **float**|  | [optional]
 **host_owner_type** | **str**| Host&#39;s owner type | [optional]
 **host_image_id** | **float**|  | [optional]
 **host_host_parameters_attributes** | [**list[str]**](str.md)| Host&#39;s parameters (array or indexed hash) | [optional]
 **host_build** | **bool**|  | [optional]
 **host_enabled** | **bool**| Include this host within Foreman reporting | [optional]
 **host_provision_method** | **str**| The method used to provision the host. | [optional]
 **host_managed** | **bool**| True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not | [optional]
 **host_progress_report_id** | **str**| UUID to track orchestration tasks status, GET /api/orchestration/:UUID/tasks | [optional]
 **host_comment** | **str**| Additional information about this host | [optional]
 **host_capabilities** | **str**|  | [optional]
 **host_compute_profile_id** | **float**|  | [optional]
 **host_interfaces_attributes** | [**list[str]**](str.md)| Host&#39;s network interfaces. | [optional]
 **host_content_facet_attributes_content_view_id** | **float**|  | [optional]
 **host_content_facet_attributes_lifecycle_environment_id** | **float**|  | [optional]
 **host_content_facet_attributes_content_source_id** | **float**|  | [optional]
 **host_content_facet_attributes_kickstart_repository_id** | **float**| Repository Id associated with the kickstart repo used for provisioning | [optional]
 **host_subscription_facet_attributes_release_version** | **str**| Release version for this Host to use (7Server, 7.1, etc) | [optional]
 **host_subscription_facet_attributes_autoheal** | **bool**| Sets whether the Host will autoheal subscriptions upon checkin | [optional]
 **host_subscription_facet_attributes_purpose_usage** | **str**| Sets the system purpose usage | [optional]
 **host_subscription_facet_attributes_purpose_role** | **str**| Sets the system purpose usage | [optional]
 **host_subscription_facet_attributes_purpose_addons** | [**list[str]**](str.md)| Sets the system add-ons | [optional]
 **host_subscription_facet_attributes_service_level** | **str**| Service level to be used for autoheal | [optional]
 **host_subscription_facet_attributes_hypervisor_guest_uuids** | [**list[str]**](str.md)| List of hypervisor guest uuids | [optional]
 **host_subscription_facet_attributes_installed_products_attributes** | [**list[str]**](str.md)| List of products installed on the host | [optional]
 **host_overwrite** | **bool**| Overwrite existing host (true by default) | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hosts_facts**
> post_hosts_facts(name, location_id=location_id, organization_id=organization_id, certname=certname, type=type)

Upload facts for a host, creating the host if required



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
name = 'name_example' # str | hostname of the host
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
certname = 'certname_example' # str | optional: certname of the host (optional)
type = 'type_example' # str | optional: the STI type of host to create (optional)

try:
    # Upload facts for a host, creating the host if required
    api_instance.post_hosts_facts(name, location_id=location_id, organization_id=organization_id, certname=certname, type=type)
except ApiException as e:
    print("Exception when calling HostsApi->post_hosts_facts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| hostname of the host |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **certname** | **str**| optional: certname of the host | [optional]
 **type** | **str**| optional: the STI type of host to create | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_host_id_host_collections**
> put_hosts_host_id_host_collections(host_id, host_collection_ids, location_id=location_id, organization_id=organization_id)

Alter a host's host collections



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
host_id = 8.14 # float | The id of the host to alter
host_collection_ids = ['host_collection_ids_example'] # list[str] | List of host collection ids to update
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Alter a host's host collections
    api_instance.put_hosts_host_id_host_collections(host_id, host_collection_ids, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->put_hosts_host_id_host_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| The id of the host to alter |
 **host_collection_ids** | [**list[str]**](str.md)| List of host collection ids to update |
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

# **put_hosts_id**
> put_hosts_id(id, location_id=location_id, organization_id=organization_id, host_name=host_name, host_location_id=host_location_id, host_organization_id=host_organization_id, host_ip=host_ip, host_mac=host_mac, host_architecture_id=host_architecture_id, host_domain_id=host_domain_id, host_realm_id=host_realm_id, host_puppet_proxy_id=host_puppet_proxy_id, host_puppet_ca_proxy_id=host_puppet_ca_proxy_id, host_operatingsystem_id=host_operatingsystem_id, host_medium_id=host_medium_id, host_pxe_loader=host_pxe_loader, host_ptable_id=host_ptable_id, host_subnet_id=host_subnet_id, host_compute_resource_id=host_compute_resource_id, host_root_pass=host_root_pass, host_model_id=host_model_id, host_hostgroup_id=host_hostgroup_id, host_owner_id=host_owner_id, host_owner_type=host_owner_type, host_image_id=host_image_id, host_host_parameters_attributes=host_host_parameters_attributes, host_build=host_build, host_enabled=host_enabled, host_provision_method=host_provision_method, host_managed=host_managed, host_progress_report_id=host_progress_report_id, host_comment=host_comment, host_capabilities=host_capabilities, host_compute_profile_id=host_compute_profile_id, host_interfaces_attributes=host_interfaces_attributes, host_content_facet_attributes_content_view_id=host_content_facet_attributes_content_view_id, host_content_facet_attributes_lifecycle_environment_id=host_content_facet_attributes_lifecycle_environment_id, host_content_facet_attributes_content_source_id=host_content_facet_attributes_content_source_id, host_content_facet_attributes_kickstart_repository_id=host_content_facet_attributes_kickstart_repository_id, host_subscription_facet_attributes_release_version=host_subscription_facet_attributes_release_version, host_subscription_facet_attributes_autoheal=host_subscription_facet_attributes_autoheal, host_subscription_facet_attributes_purpose_usage=host_subscription_facet_attributes_purpose_usage, host_subscription_facet_attributes_purpose_role=host_subscription_facet_attributes_purpose_role, host_subscription_facet_attributes_purpose_addons=host_subscription_facet_attributes_purpose_addons, host_subscription_facet_attributes_service_level=host_subscription_facet_attributes_service_level, host_subscription_facet_attributes_hypervisor_guest_uuids=host_subscription_facet_attributes_hypervisor_guest_uuids, host_subscription_facet_attributes_installed_products_attributes=host_subscription_facet_attributes_installed_products_attributes)

Update a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
host_name = 'host_name_example' # str |  (optional)
host_location_id = 8.14 # float |  (optional)
host_organization_id = 8.14 # float |  (optional)
host_ip = 'host_ip_example' # str | not required if using a subnet with DHCP proxy (optional)
host_mac = 'host_mac_example' # str | required for managed host that is bare metal, not required if it's a virtual machine (optional)
host_architecture_id = 8.14 # float | required if host is managed and value is not inherited from host group (optional)
host_domain_id = 8.14 # float | required if host is managed and value is not inherited from host group (optional)
host_realm_id = 8.14 # float |  (optional)
host_puppet_proxy_id = 8.14 # float | Puppet proxy ID (optional)
host_puppet_ca_proxy_id = 8.14 # float | Puppet CA proxy ID (optional)
host_operatingsystem_id = 8.14 # float | required if host is managed and value is not inherited from host group (optional)
host_medium_id = 'host_medium_id_example' # str | required if not imaged based provisioning and host is managed and value is not inherited from host group (optional)
host_pxe_loader = 'host_pxe_loader_example' # str | DHCP filename option (Grub2/PXELinux by default) (optional)
host_ptable_id = 8.14 # float | required if host is managed and custom partition has not been defined (optional)
host_subnet_id = 8.14 # float | required if host is managed and value is not inherited from host group (optional)
host_compute_resource_id = 8.14 # float | nil means host is bare metal (optional)
host_root_pass = 'host_root_pass_example' # str | required if host is managed and value is not inherited from host group or default password in settings (optional)
host_model_id = 8.14 # float |  (optional)
host_hostgroup_id = 8.14 # float |  (optional)
host_owner_id = 8.14 # float |  (optional)
host_owner_type = 'host_owner_type_example' # str | Host's owner type (optional)
host_image_id = 8.14 # float |  (optional)
host_host_parameters_attributes = ['host_host_parameters_attributes_example'] # list[str] | Host's parameters (array or indexed hash) (optional)
host_build = true # bool |  (optional)
host_enabled = true # bool | Include this host within Foreman reporting (optional)
host_provision_method = 'host_provision_method_example' # str | The method used to provision the host. (optional)
host_managed = true # bool | True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not (optional)
host_progress_report_id = 'host_progress_report_id_example' # str | UUID to track orchestration tasks status, GET /api/orchestration/:UUID/tasks (optional)
host_comment = 'host_comment_example' # str | Additional information about this host (optional)
host_capabilities = 'host_capabilities_example' # str |  (optional)
host_compute_profile_id = 8.14 # float |  (optional)
host_interfaces_attributes = ['host_interfaces_attributes_example'] # list[str] | Host's network interfaces. (optional)
host_content_facet_attributes_content_view_id = 8.14 # float |  (optional)
host_content_facet_attributes_lifecycle_environment_id = 8.14 # float |  (optional)
host_content_facet_attributes_content_source_id = 8.14 # float |  (optional)
host_content_facet_attributes_kickstart_repository_id = 8.14 # float | Repository Id associated with the kickstart repo used for provisioning (optional)
host_subscription_facet_attributes_release_version = 'host_subscription_facet_attributes_release_version_example' # str | Release version for this Host to use (7Server, 7.1, etc) (optional)
host_subscription_facet_attributes_autoheal = true # bool | Sets whether the Host will autoheal subscriptions upon checkin (optional)
host_subscription_facet_attributes_purpose_usage = 'host_subscription_facet_attributes_purpose_usage_example' # str | Sets the system purpose usage (optional)
host_subscription_facet_attributes_purpose_role = 'host_subscription_facet_attributes_purpose_role_example' # str | Sets the system purpose usage (optional)
host_subscription_facet_attributes_purpose_addons = ['host_subscription_facet_attributes_purpose_addons_example'] # list[str] | Sets the system add-ons (optional)
host_subscription_facet_attributes_service_level = 'host_subscription_facet_attributes_service_level_example' # str | Service level to be used for autoheal (optional)
host_subscription_facet_attributes_hypervisor_guest_uuids = ['host_subscription_facet_attributes_hypervisor_guest_uuids_example'] # list[str] | List of hypervisor guest uuids (optional)
host_subscription_facet_attributes_installed_products_attributes = ['host_subscription_facet_attributes_installed_products_attributes_example'] # list[str] | List of products installed on the host (optional)

try:
    # Update a host
    api_instance.put_hosts_id(id, location_id=location_id, organization_id=organization_id, host_name=host_name, host_location_id=host_location_id, host_organization_id=host_organization_id, host_ip=host_ip, host_mac=host_mac, host_architecture_id=host_architecture_id, host_domain_id=host_domain_id, host_realm_id=host_realm_id, host_puppet_proxy_id=host_puppet_proxy_id, host_puppet_ca_proxy_id=host_puppet_ca_proxy_id, host_operatingsystem_id=host_operatingsystem_id, host_medium_id=host_medium_id, host_pxe_loader=host_pxe_loader, host_ptable_id=host_ptable_id, host_subnet_id=host_subnet_id, host_compute_resource_id=host_compute_resource_id, host_root_pass=host_root_pass, host_model_id=host_model_id, host_hostgroup_id=host_hostgroup_id, host_owner_id=host_owner_id, host_owner_type=host_owner_type, host_image_id=host_image_id, host_host_parameters_attributes=host_host_parameters_attributes, host_build=host_build, host_enabled=host_enabled, host_provision_method=host_provision_method, host_managed=host_managed, host_progress_report_id=host_progress_report_id, host_comment=host_comment, host_capabilities=host_capabilities, host_compute_profile_id=host_compute_profile_id, host_interfaces_attributes=host_interfaces_attributes, host_content_facet_attributes_content_view_id=host_content_facet_attributes_content_view_id, host_content_facet_attributes_lifecycle_environment_id=host_content_facet_attributes_lifecycle_environment_id, host_content_facet_attributes_content_source_id=host_content_facet_attributes_content_source_id, host_content_facet_attributes_kickstart_repository_id=host_content_facet_attributes_kickstart_repository_id, host_subscription_facet_attributes_release_version=host_subscription_facet_attributes_release_version, host_subscription_facet_attributes_autoheal=host_subscription_facet_attributes_autoheal, host_subscription_facet_attributes_purpose_usage=host_subscription_facet_attributes_purpose_usage, host_subscription_facet_attributes_purpose_role=host_subscription_facet_attributes_purpose_role, host_subscription_facet_attributes_purpose_addons=host_subscription_facet_attributes_purpose_addons, host_subscription_facet_attributes_service_level=host_subscription_facet_attributes_service_level, host_subscription_facet_attributes_hypervisor_guest_uuids=host_subscription_facet_attributes_hypervisor_guest_uuids, host_subscription_facet_attributes_installed_products_attributes=host_subscription_facet_attributes_installed_products_attributes)
except ApiException as e:
    print("Exception when calling HostsApi->put_hosts_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **host_name** | **str**|  | [optional]
 **host_location_id** | **float**|  | [optional]
 **host_organization_id** | **float**|  | [optional]
 **host_ip** | **str**| not required if using a subnet with DHCP proxy | [optional]
 **host_mac** | **str**| required for managed host that is bare metal, not required if it&#39;s a virtual machine | [optional]
 **host_architecture_id** | **float**| required if host is managed and value is not inherited from host group | [optional]
 **host_domain_id** | **float**| required if host is managed and value is not inherited from host group | [optional]
 **host_realm_id** | **float**|  | [optional]
 **host_puppet_proxy_id** | **float**| Puppet proxy ID | [optional]
 **host_puppet_ca_proxy_id** | **float**| Puppet CA proxy ID | [optional]
 **host_operatingsystem_id** | **float**| required if host is managed and value is not inherited from host group | [optional]
 **host_medium_id** | **str**| required if not imaged based provisioning and host is managed and value is not inherited from host group | [optional]
 **host_pxe_loader** | **str**| DHCP filename option (Grub2/PXELinux by default) | [optional]
 **host_ptable_id** | **float**| required if host is managed and custom partition has not been defined | [optional]
 **host_subnet_id** | **float**| required if host is managed and value is not inherited from host group | [optional]
 **host_compute_resource_id** | **float**| nil means host is bare metal | [optional]
 **host_root_pass** | **str**| required if host is managed and value is not inherited from host group or default password in settings | [optional]
 **host_model_id** | **float**|  | [optional]
 **host_hostgroup_id** | **float**|  | [optional]
 **host_owner_id** | **float**|  | [optional]
 **host_owner_type** | **str**| Host&#39;s owner type | [optional]
 **host_image_id** | **float**|  | [optional]
 **host_host_parameters_attributes** | [**list[str]**](str.md)| Host&#39;s parameters (array or indexed hash) | [optional]
 **host_build** | **bool**|  | [optional]
 **host_enabled** | **bool**| Include this host within Foreman reporting | [optional]
 **host_provision_method** | **str**| The method used to provision the host. | [optional]
 **host_managed** | **bool**| True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not | [optional]
 **host_progress_report_id** | **str**| UUID to track orchestration tasks status, GET /api/orchestration/:UUID/tasks | [optional]
 **host_comment** | **str**| Additional information about this host | [optional]
 **host_capabilities** | **str**|  | [optional]
 **host_compute_profile_id** | **float**|  | [optional]
 **host_interfaces_attributes** | [**list[str]**](str.md)| Host&#39;s network interfaces. | [optional]
 **host_content_facet_attributes_content_view_id** | **float**|  | [optional]
 **host_content_facet_attributes_lifecycle_environment_id** | **float**|  | [optional]
 **host_content_facet_attributes_content_source_id** | **float**|  | [optional]
 **host_content_facet_attributes_kickstart_repository_id** | **float**| Repository Id associated with the kickstart repo used for provisioning | [optional]
 **host_subscription_facet_attributes_release_version** | **str**| Release version for this Host to use (7Server, 7.1, etc) | [optional]
 **host_subscription_facet_attributes_autoheal** | **bool**| Sets whether the Host will autoheal subscriptions upon checkin | [optional]
 **host_subscription_facet_attributes_purpose_usage** | **str**| Sets the system purpose usage | [optional]
 **host_subscription_facet_attributes_purpose_role** | **str**| Sets the system purpose usage | [optional]
 **host_subscription_facet_attributes_purpose_addons** | [**list[str]**](str.md)| Sets the system add-ons | [optional]
 **host_subscription_facet_attributes_service_level** | **str**| Service level to be used for autoheal | [optional]
 **host_subscription_facet_attributes_hypervisor_guest_uuids** | [**list[str]**](str.md)| List of hypervisor guest uuids | [optional]
 **host_subscription_facet_attributes_installed_products_attributes** | [**list[str]**](str.md)| List of products installed on the host | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_id_boot**
> put_hosts_id_boot(id, device, location_id=location_id, organization_id=organization_id)

Boot host from specified device



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
device = 'device_example' # str | boot device, valid devices are disk, cdrom, pxe, bios
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Boot host from specified device
    api_instance.put_hosts_id_boot(id, device, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->put_hosts_id_boot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **device** | **str**| boot device, valid devices are disk, cdrom, pxe, bios |
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

# **put_hosts_id_disassociate**
> put_hosts_id_disassociate(id, location_id=location_id, organization_id=organization_id)

Disassociate the host from a VM



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Disassociate the host from a VM
    api_instance.put_hosts_id_disassociate(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->put_hosts_id_disassociate: %s\n" % e)
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

# **put_hosts_id_power**
> put_hosts_id_power(id, power_action, location_id=location_id, organization_id=organization_id)

Run a power operation on host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
power_action = 'power_action_example' # str | power action, valid actions are (on/start), (off/stop), (soft/reboot), (cycle/reset), (state/status)
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Run a power operation on host
    api_instance.put_hosts_id_power(id, power_action, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsApi->put_hosts_id_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **power_action** | **str**| power action, valid actions are (on/start), (off/stop), (soft/reboot), (cycle/reset), (state/status) |
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

# **put_hosts_id_rebuild_config**
> put_hosts_id_rebuild_config(id, location_id=location_id, organization_id=organization_id, only=only)

Rebuild orchestration config



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
only = ['only_example'] # list[str] | Limit rebuild steps, valid steps are DHCP, DNS, TFTP, Content_Host_Status, Refresh_Content_Host_Status (optional)

try:
    # Rebuild orchestration config
    api_instance.put_hosts_id_rebuild_config(id, location_id=location_id, organization_id=organization_id, only=only)
except ApiException as e:
    print("Exception when calling HostsApi->put_hosts_id_rebuild_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **only** | [**list[str]**](str.md)| Limit rebuild steps, valid steps are DHCP, DNS, TFTP, Content_Host_Status, Refresh_Content_Host_Status | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
