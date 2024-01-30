# pyforeman.ComputeResourcesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_compute_resources_id**](ComputeResourcesApi.md#delete_compute_resources_id) | **DELETE** /compute_resources/{id} | Delete a compute resource
[**delete_compute_resources_id_available_virtual_machines_vm_id**](ComputeResourcesApi.md#delete_compute_resources_id_available_virtual_machines_vm_id) | **DELETE** /compute_resources/{id}/available_virtual_machines/{vm_id} | Delete a Virtual Machine
[**get_compute_resources**](ComputeResourcesApi.md#get_compute_resources) | **GET** /compute_resources | List all compute resources
[**get_compute_resources_id**](ComputeResourcesApi.md#get_compute_resources_id) | **GET** /compute_resources/{id} | Show a compute resource
[**get_compute_resources_id_available_clusters**](ComputeResourcesApi.md#get_compute_resources_id_available_clusters) | **GET** /compute_resources/{id}/available_clusters | List available clusters for a compute resource
[**get_compute_resources_id_available_clusters_cluster_id_available_networks**](ComputeResourcesApi.md#get_compute_resources_id_available_clusters_cluster_id_available_networks) | **GET** /compute_resources/{id}/available_clusters/{cluster_id}/available_networks | List available networks for a compute resource cluster
[**get_compute_resources_id_available_clusters_cluster_id_available_resource_pools**](ComputeResourcesApi.md#get_compute_resources_id_available_clusters_cluster_id_available_resource_pools) | **GET** /compute_resources/{id}/available_clusters/{cluster_id}/available_resource_pools | List resource pools for a compute resource cluster
[**get_compute_resources_id_available_clusters_cluster_id_available_storage_domains**](ComputeResourcesApi.md#get_compute_resources_id_available_clusters_cluster_id_available_storage_domains) | **GET** /compute_resources/{id}/available_clusters/{cluster_id}/available_storage_domains | List storage domains for a compute resource
[**get_compute_resources_id_available_clusters_cluster_id_available_storage_pods**](ComputeResourcesApi.md#get_compute_resources_id_available_clusters_cluster_id_available_storage_pods) | **GET** /compute_resources/{id}/available_clusters/{cluster_id}/available_storage_pods | List storage pods for a compute resource
[**get_compute_resources_id_available_flavors**](ComputeResourcesApi.md#get_compute_resources_id_available_flavors) | **GET** /compute_resources/{id}/available_flavors | List available flavors for a compute resource
[**get_compute_resources_id_available_folders**](ComputeResourcesApi.md#get_compute_resources_id_available_folders) | **GET** /compute_resources/{id}/available_folders | List available folders for a compute resource
[**get_compute_resources_id_available_images**](ComputeResourcesApi.md#get_compute_resources_id_available_images) | **GET** /compute_resources/{id}/available_images | List available images for a compute resource
[**get_compute_resources_id_available_networks**](ComputeResourcesApi.md#get_compute_resources_id_available_networks) | **GET** /compute_resources/{id}/available_networks | List available networks for a compute resource
[**get_compute_resources_id_available_security_groups**](ComputeResourcesApi.md#get_compute_resources_id_available_security_groups) | **GET** /compute_resources/{id}/available_security_groups | List available security groups for a compute resource
[**get_compute_resources_id_available_storage_domains**](ComputeResourcesApi.md#get_compute_resources_id_available_storage_domains) | **GET** /compute_resources/{id}/available_storage_domains | List storage domains for a compute resource
[**get_compute_resources_id_available_storage_domains_storage_domain**](ComputeResourcesApi.md#get_compute_resources_id_available_storage_domains_storage_domain) | **GET** /compute_resources/{id}/available_storage_domains/{storage_domain} | List attributes for a given storage domain
[**get_compute_resources_id_available_storage_pods**](ComputeResourcesApi.md#get_compute_resources_id_available_storage_pods) | **GET** /compute_resources/{id}/available_storage_pods | List storage pods for a compute resource
[**get_compute_resources_id_available_storage_pods_storage_pod**](ComputeResourcesApi.md#get_compute_resources_id_available_storage_pods_storage_pod) | **GET** /compute_resources/{id}/available_storage_pods/{storage_pod} | List attributes for a given storage pod
[**get_compute_resources_id_available_virtual_machines**](ComputeResourcesApi.md#get_compute_resources_id_available_virtual_machines) | **GET** /compute_resources/{id}/available_virtual_machines | List available virtual machines for a compute resource
[**get_compute_resources_id_available_virtual_machines_vm_id**](ComputeResourcesApi.md#get_compute_resources_id_available_virtual_machines_vm_id) | **GET** /compute_resources/{id}/available_virtual_machines/{vm_id} | Show a virtual machine
[**get_compute_resources_id_available_vnic_profiles**](ComputeResourcesApi.md#get_compute_resources_id_available_vnic_profiles) | **GET** /compute_resources/{id}/available_vnic_profiles | List available vnic profiles for a compute resource, for oVirt only
[**get_compute_resources_id_available_zones**](ComputeResourcesApi.md#get_compute_resources_id_available_zones) | **GET** /compute_resources/{id}/available_zones | List available zone for a compute resource
[**get_compute_resources_id_storage_domains_storage_domain_id**](ComputeResourcesApi.md#get_compute_resources_id_storage_domains_storage_domain_id) | **GET** /compute_resources/{id}/storage_domains/{storage_domain_id} | List attributes for a given storage domain
[**get_compute_resources_id_storage_pods_storage_pod_id**](ComputeResourcesApi.md#get_compute_resources_id_storage_pods_storage_pod_id) | **GET** /compute_resources/{id}/storage_pods/{storage_pod_id} | List attributes for a given storage pod
[**post_compute_resources**](ComputeResourcesApi.md#post_compute_resources) | **POST** /compute_resources | Create a compute resource
[**put_compute_resources_id**](ComputeResourcesApi.md#put_compute_resources_id) | **PUT** /compute_resources/{id} | Update a compute resource
[**put_compute_resources_id_associate_vm_id**](ComputeResourcesApi.md#put_compute_resources_id_associate_vm_id) | **PUT** /compute_resources/{id}/associate/{vm_id} | Associate VMs to Hosts
[**put_compute_resources_id_available_virtual_machines_vm_id_power**](ComputeResourcesApi.md#put_compute_resources_id_available_virtual_machines_vm_id_power) | **PUT** /compute_resources/{id}/available_virtual_machines/{vm_id}/power | Power a Virtual Machine
[**put_compute_resources_id_refresh_cache**](ComputeResourcesApi.md#put_compute_resources_id_refresh_cache) | **PUT** /compute_resources/{id}/refresh_cache | Refresh Compute Resource Cache


# **delete_compute_resources_id**
> delete_compute_resources_id(id, location_id=location_id, organization_id=organization_id)

Delete a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a compute resource
    api_instance.delete_compute_resources_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->delete_compute_resources_id: %s\n" % e)
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

# **delete_compute_resources_id_available_virtual_machines_vm_id**
> delete_compute_resources_id_available_virtual_machines_vm_id(id, vm_id, location_id=location_id, organization_id=organization_id)

Delete a Virtual Machine



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
vm_id = 'vm_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a Virtual Machine
    api_instance.delete_compute_resources_id_available_virtual_machines_vm_id(id, vm_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->delete_compute_resources_id_available_virtual_machines_vm_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **vm_id** | **str**|  |
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

# **get_compute_resources**
> get_compute_resources(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all compute resources



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
location_id = 8.14 # float | Scope by locations (optional)
organization_id = 8.14 # float | Scope by organizations (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all compute resources
    api_instance.get_compute_resources(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources: %s\n" % e)
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

# **get_compute_resources_id**
> get_compute_resources_id(id, location_id=location_id, organization_id=organization_id)

Show a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a compute resource
    api_instance.get_compute_resources_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id: %s\n" % e)
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

# **get_compute_resources_id_available_clusters**
> get_compute_resources_id_available_clusters(id, location_id=location_id, organization_id=organization_id)

List available clusters for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available clusters for a compute resource
    api_instance.get_compute_resources_id_available_clusters(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_clusters: %s\n" % e)
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

# **get_compute_resources_id_available_clusters_cluster_id_available_networks**
> get_compute_resources_id_available_clusters_cluster_id_available_networks(id, cluster_id, location_id=location_id, organization_id=organization_id)

List available networks for a compute resource cluster



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
cluster_id = 'cluster_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available networks for a compute resource cluster
    api_instance.get_compute_resources_id_available_clusters_cluster_id_available_networks(id, cluster_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_clusters_cluster_id_available_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **cluster_id** | **str**|  |
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

# **get_compute_resources_id_available_clusters_cluster_id_available_resource_pools**
> get_compute_resources_id_available_clusters_cluster_id_available_resource_pools(id, cluster_id, location_id=location_id, organization_id=organization_id)

List resource pools for a compute resource cluster



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
cluster_id = 'cluster_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List resource pools for a compute resource cluster
    api_instance.get_compute_resources_id_available_clusters_cluster_id_available_resource_pools(id, cluster_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_clusters_cluster_id_available_resource_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **cluster_id** | **str**|  |
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

# **get_compute_resources_id_available_clusters_cluster_id_available_storage_domains**
> get_compute_resources_id_available_clusters_cluster_id_available_storage_domains(id, cluster_id, storage_domain, location_id=location_id, organization_id=organization_id)

List storage domains for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
cluster_id = 'cluster_id_example' # str |
storage_domain = 'storage_domain_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List storage domains for a compute resource
    api_instance.get_compute_resources_id_available_clusters_cluster_id_available_storage_domains(id, cluster_id, storage_domain, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_clusters_cluster_id_available_storage_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **cluster_id** | **str**|  |
 **storage_domain** | **str**|  |
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

# **get_compute_resources_id_available_clusters_cluster_id_available_storage_pods**
> get_compute_resources_id_available_clusters_cluster_id_available_storage_pods(id, cluster_id, storage_pod, location_id=location_id, organization_id=organization_id)

List storage pods for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
cluster_id = 'cluster_id_example' # str |
storage_pod = 'storage_pod_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List storage pods for a compute resource
    api_instance.get_compute_resources_id_available_clusters_cluster_id_available_storage_pods(id, cluster_id, storage_pod, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_clusters_cluster_id_available_storage_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **cluster_id** | **str**|  |
 **storage_pod** | **str**|  |
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

# **get_compute_resources_id_available_flavors**
> get_compute_resources_id_available_flavors(id, location_id=location_id, organization_id=organization_id)

List available flavors for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available flavors for a compute resource
    api_instance.get_compute_resources_id_available_flavors(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_flavors: %s\n" % e)
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

# **get_compute_resources_id_available_folders**
> get_compute_resources_id_available_folders(id, location_id=location_id, organization_id=organization_id)

List available folders for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available folders for a compute resource
    api_instance.get_compute_resources_id_available_folders(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_folders: %s\n" % e)
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

# **get_compute_resources_id_available_images**
> get_compute_resources_id_available_images(id, location_id=location_id, organization_id=organization_id)

List available images for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available images for a compute resource
    api_instance.get_compute_resources_id_available_images(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_images: %s\n" % e)
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

# **get_compute_resources_id_available_networks**
> get_compute_resources_id_available_networks(id, cluster_id, location_id=location_id, organization_id=organization_id)

List available networks for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
cluster_id = 'cluster_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available networks for a compute resource
    api_instance.get_compute_resources_id_available_networks(id, cluster_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **cluster_id** | **str**|  |
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

# **get_compute_resources_id_available_security_groups**
> get_compute_resources_id_available_security_groups(id, location_id=location_id, organization_id=organization_id)

List available security groups for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available security groups for a compute resource
    api_instance.get_compute_resources_id_available_security_groups(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_security_groups: %s\n" % e)
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

# **get_compute_resources_id_available_storage_domains**
> get_compute_resources_id_available_storage_domains(id, cluster_id, storage_domain, location_id=location_id, organization_id=organization_id)

List storage domains for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
cluster_id = 'cluster_id_example' # str |
storage_domain = 'storage_domain_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List storage domains for a compute resource
    api_instance.get_compute_resources_id_available_storage_domains(id, cluster_id, storage_domain, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_storage_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **cluster_id** | **str**|  |
 **storage_domain** | **str**|  |
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

# **get_compute_resources_id_available_storage_domains_storage_domain**
> get_compute_resources_id_available_storage_domains_storage_domain(id, storage_domain, cluster_id, location_id=location_id, organization_id=organization_id)

List attributes for a given storage domain



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
storage_domain = 'storage_domain_example' # str |
cluster_id = 'cluster_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List attributes for a given storage domain
    api_instance.get_compute_resources_id_available_storage_domains_storage_domain(id, storage_domain, cluster_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_storage_domains_storage_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **storage_domain** | **str**|  |
 **cluster_id** | **str**|  |
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

# **get_compute_resources_id_available_storage_pods**
> get_compute_resources_id_available_storage_pods(id, cluster_id, storage_pod, location_id=location_id, organization_id=organization_id)

List storage pods for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
cluster_id = 'cluster_id_example' # str |
storage_pod = 'storage_pod_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List storage pods for a compute resource
    api_instance.get_compute_resources_id_available_storage_pods(id, cluster_id, storage_pod, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_storage_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **cluster_id** | **str**|  |
 **storage_pod** | **str**|  |
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

# **get_compute_resources_id_available_storage_pods_storage_pod**
> get_compute_resources_id_available_storage_pods_storage_pod(id, storage_pod, cluster_id, location_id=location_id, organization_id=organization_id)

List attributes for a given storage pod



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
storage_pod = 'storage_pod_example' # str |
cluster_id = 'cluster_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List attributes for a given storage pod
    api_instance.get_compute_resources_id_available_storage_pods_storage_pod(id, storage_pod, cluster_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_storage_pods_storage_pod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **storage_pod** | **str**|  |
 **cluster_id** | **str**|  |
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

# **get_compute_resources_id_available_virtual_machines**
> get_compute_resources_id_available_virtual_machines(id, location_id=location_id, organization_id=organization_id)

List available virtual machines for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available virtual machines for a compute resource
    api_instance.get_compute_resources_id_available_virtual_machines(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_virtual_machines: %s\n" % e)
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

# **get_compute_resources_id_available_virtual_machines_vm_id**
> get_compute_resources_id_available_virtual_machines_vm_id(id, vm_id, location_id=location_id, organization_id=organization_id)

Show a virtual machine



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
vm_id = 'vm_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a virtual machine
    api_instance.get_compute_resources_id_available_virtual_machines_vm_id(id, vm_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_virtual_machines_vm_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **vm_id** | **str**|  |
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

# **get_compute_resources_id_available_vnic_profiles**
> get_compute_resources_id_available_vnic_profiles(id, location_id=location_id, organization_id=organization_id)

List available vnic profiles for a compute resource, for oVirt only



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available vnic profiles for a compute resource, for oVirt only
    api_instance.get_compute_resources_id_available_vnic_profiles(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_vnic_profiles: %s\n" % e)
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

# **get_compute_resources_id_available_zones**
> get_compute_resources_id_available_zones(id, location_id=location_id, organization_id=organization_id)

List available zone for a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available zone for a compute resource
    api_instance.get_compute_resources_id_available_zones(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_available_zones: %s\n" % e)
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

# **get_compute_resources_id_storage_domains_storage_domain_id**
> get_compute_resources_id_storage_domains_storage_domain_id(id, storage_domain_id, location_id=location_id, organization_id=organization_id)

List attributes for a given storage domain



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
storage_domain_id = 'storage_domain_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List attributes for a given storage domain
    api_instance.get_compute_resources_id_storage_domains_storage_domain_id(id, storage_domain_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_storage_domains_storage_domain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **storage_domain_id** | **str**|  |
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

# **get_compute_resources_id_storage_pods_storage_pod_id**
> get_compute_resources_id_storage_pods_storage_pod_id(id, storage_pod_id, location_id=location_id, organization_id=organization_id)

List attributes for a given storage pod



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
storage_pod_id = 'storage_pod_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List attributes for a given storage pod
    api_instance.get_compute_resources_id_storage_pods_storage_pod_id(id, storage_pod_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->get_compute_resources_id_storage_pods_storage_pod_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **storage_pod_id** | **str**|  |
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

# **post_compute_resources**
> post_compute_resources(compute_resource_name, location_id=location_id, organization_id=organization_id, compute_resource_provider=compute_resource_provider, compute_resource_url=compute_resource_url, compute_resource_description=compute_resource_description, compute_resource_user=compute_resource_user, compute_resource_password=compute_resource_password, compute_resource_datacenter=compute_resource_datacenter, compute_resource_ovirt_quota=compute_resource_ovirt_quota, compute_resource_public_key=compute_resource_public_key, compute_resource_region=compute_resource_region, compute_resource_tenant=compute_resource_tenant, compute_resource_domain=compute_resource_domain, compute_resource_project_domain_name=compute_resource_project_domain_name, compute_resource_project_domain_id=compute_resource_project_domain_id, compute_resource_server=compute_resource_server, compute_resource_set_console_password=compute_resource_set_console_password, compute_resource_display_type=compute_resource_display_type, compute_resource_keyboard_layout=compute_resource_keyboard_layout, compute_resource_caching_enabled=compute_resource_caching_enabled, compute_resource_location_ids=compute_resource_location_ids, compute_resource_organization_ids=compute_resource_organization_ids)

Create a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
compute_resource_name = 'compute_resource_name_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
compute_resource_provider = 'compute_resource_provider_example' # str | Providers include  (optional)
compute_resource_url = 'compute_resource_url_example' # str | URL for Libvirt, oVirt and OpenStack (optional)
compute_resource_description = 'compute_resource_description_example' # str |  (optional)
compute_resource_user = 'compute_resource_user_example' # str | Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2. (optional)
compute_resource_password = 'compute_resource_password_example' # str | Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2 (optional)
compute_resource_datacenter = 'compute_resource_datacenter_example' # str | for oVirt, VMware Datacenter (optional)
compute_resource_ovirt_quota = 'compute_resource_ovirt_quota_example' # str | for oVirt only, ID or Name of quota to use (optional)
compute_resource_public_key = 'compute_resource_public_key_example' # str | for oVirt only (optional)
compute_resource_region = 'compute_resource_region_example' # str | for AzureRm eg. 'eastus' and for EC2 only. Use 'us-gov-west-1' for EC2 GovCloud region (optional)
compute_resource_tenant = 'compute_resource_tenant_example' # str | for OpenStack and AzureRm only (optional)
compute_resource_domain = 'compute_resource_domain_example' # str | for OpenStack (v3) only (optional)
compute_resource_project_domain_name = 'compute_resource_project_domain_name_example' # str | for OpenStack (v3) only (optional)
compute_resource_project_domain_id = 'compute_resource_project_domain_id_example' # str | for OpenStack (v3) only (optional)
compute_resource_server = 'compute_resource_server_example' # str | for VMware (optional)
compute_resource_set_console_password = true # bool | for Libvirt and VMware only (optional)
compute_resource_display_type = 'compute_resource_display_type_example' # str | for Libvirt and oVirt only (optional)
compute_resource_keyboard_layout = 'compute_resource_keyboard_layout_example' # str | for oVirt only (optional)
compute_resource_caching_enabled = true # bool | enable caching, for VMware only (optional)
compute_resource_location_ids = ['compute_resource_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
compute_resource_organization_ids = ['compute_resource_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Create a compute resource
    api_instance.post_compute_resources(compute_resource_name, location_id=location_id, organization_id=organization_id, compute_resource_provider=compute_resource_provider, compute_resource_url=compute_resource_url, compute_resource_description=compute_resource_description, compute_resource_user=compute_resource_user, compute_resource_password=compute_resource_password, compute_resource_datacenter=compute_resource_datacenter, compute_resource_ovirt_quota=compute_resource_ovirt_quota, compute_resource_public_key=compute_resource_public_key, compute_resource_region=compute_resource_region, compute_resource_tenant=compute_resource_tenant, compute_resource_domain=compute_resource_domain, compute_resource_project_domain_name=compute_resource_project_domain_name, compute_resource_project_domain_id=compute_resource_project_domain_id, compute_resource_server=compute_resource_server, compute_resource_set_console_password=compute_resource_set_console_password, compute_resource_display_type=compute_resource_display_type, compute_resource_keyboard_layout=compute_resource_keyboard_layout, compute_resource_caching_enabled=compute_resource_caching_enabled, compute_resource_location_ids=compute_resource_location_ids, compute_resource_organization_ids=compute_resource_organization_ids)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->post_compute_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_resource_name** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **compute_resource_provider** | **str**| Providers include  | [optional]
 **compute_resource_url** | **str**| URL for Libvirt, oVirt and OpenStack | [optional]
 **compute_resource_description** | **str**|  | [optional]
 **compute_resource_user** | **str**| Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2. | [optional]
 **compute_resource_password** | **str**| Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2 | [optional]
 **compute_resource_datacenter** | **str**| for oVirt, VMware Datacenter | [optional]
 **compute_resource_ovirt_quota** | **str**| for oVirt only, ID or Name of quota to use | [optional]
 **compute_resource_public_key** | **str**| for oVirt only | [optional]
 **compute_resource_region** | **str**| for AzureRm eg. &#39;eastus&#39; and for EC2 only. Use &#39;us-gov-west-1&#39; for EC2 GovCloud region | [optional]
 **compute_resource_tenant** | **str**| for OpenStack and AzureRm only | [optional]
 **compute_resource_domain** | **str**| for OpenStack (v3) only | [optional]
 **compute_resource_project_domain_name** | **str**| for OpenStack (v3) only | [optional]
 **compute_resource_project_domain_id** | **str**| for OpenStack (v3) only | [optional]
 **compute_resource_server** | **str**| for VMware | [optional]
 **compute_resource_set_console_password** | **bool**| for Libvirt and VMware only | [optional]
 **compute_resource_display_type** | **str**| for Libvirt and oVirt only | [optional]
 **compute_resource_keyboard_layout** | **str**| for oVirt only | [optional]
 **compute_resource_caching_enabled** | **bool**| enable caching, for VMware only | [optional]
 **compute_resource_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **compute_resource_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_compute_resources_id**
> put_compute_resources_id(id, location_id=location_id, organization_id=organization_id, compute_resource_name=compute_resource_name, compute_resource_provider=compute_resource_provider, compute_resource_url=compute_resource_url, compute_resource_description=compute_resource_description, compute_resource_user=compute_resource_user, compute_resource_password=compute_resource_password, compute_resource_datacenter=compute_resource_datacenter, compute_resource_ovirt_quota=compute_resource_ovirt_quota, compute_resource_public_key=compute_resource_public_key, compute_resource_region=compute_resource_region, compute_resource_tenant=compute_resource_tenant, compute_resource_domain=compute_resource_domain, compute_resource_project_domain_name=compute_resource_project_domain_name, compute_resource_project_domain_id=compute_resource_project_domain_id, compute_resource_server=compute_resource_server, compute_resource_set_console_password=compute_resource_set_console_password, compute_resource_display_type=compute_resource_display_type, compute_resource_keyboard_layout=compute_resource_keyboard_layout, compute_resource_caching_enabled=compute_resource_caching_enabled, compute_resource_location_ids=compute_resource_location_ids, compute_resource_organization_ids=compute_resource_organization_ids)

Update a compute resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
compute_resource_name = 'compute_resource_name_example' # str |  (optional)
compute_resource_provider = 'compute_resource_provider_example' # str | Providers include  (optional)
compute_resource_url = 'compute_resource_url_example' # str | URL for Libvirt, oVirt and OpenStack (optional)
compute_resource_description = 'compute_resource_description_example' # str |  (optional)
compute_resource_user = 'compute_resource_user_example' # str | Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2. (optional)
compute_resource_password = 'compute_resource_password_example' # str | Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2 (optional)
compute_resource_datacenter = 'compute_resource_datacenter_example' # str | for oVirt, VMware Datacenter (optional)
compute_resource_ovirt_quota = 'compute_resource_ovirt_quota_example' # str | for oVirt only, ID or Name of quota to use (optional)
compute_resource_public_key = 'compute_resource_public_key_example' # str | for oVirt only (optional)
compute_resource_region = 'compute_resource_region_example' # str | for AzureRm eg. 'eastus' and for EC2 only. Use 'us-gov-west-1' for EC2 GovCloud region (optional)
compute_resource_tenant = 'compute_resource_tenant_example' # str | for OpenStack and AzureRm only (optional)
compute_resource_domain = 'compute_resource_domain_example' # str | for OpenStack (v3) only (optional)
compute_resource_project_domain_name = 'compute_resource_project_domain_name_example' # str | for OpenStack (v3) only (optional)
compute_resource_project_domain_id = 'compute_resource_project_domain_id_example' # str | for OpenStack (v3) only (optional)
compute_resource_server = 'compute_resource_server_example' # str | for VMware (optional)
compute_resource_set_console_password = true # bool | for Libvirt and VMware only (optional)
compute_resource_display_type = 'compute_resource_display_type_example' # str | for Libvirt and oVirt only (optional)
compute_resource_keyboard_layout = 'compute_resource_keyboard_layout_example' # str | for oVirt only (optional)
compute_resource_caching_enabled = true # bool | enable caching, for VMware only (optional)
compute_resource_location_ids = ['compute_resource_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
compute_resource_organization_ids = ['compute_resource_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Update a compute resource
    api_instance.put_compute_resources_id(id, location_id=location_id, organization_id=organization_id, compute_resource_name=compute_resource_name, compute_resource_provider=compute_resource_provider, compute_resource_url=compute_resource_url, compute_resource_description=compute_resource_description, compute_resource_user=compute_resource_user, compute_resource_password=compute_resource_password, compute_resource_datacenter=compute_resource_datacenter, compute_resource_ovirt_quota=compute_resource_ovirt_quota, compute_resource_public_key=compute_resource_public_key, compute_resource_region=compute_resource_region, compute_resource_tenant=compute_resource_tenant, compute_resource_domain=compute_resource_domain, compute_resource_project_domain_name=compute_resource_project_domain_name, compute_resource_project_domain_id=compute_resource_project_domain_id, compute_resource_server=compute_resource_server, compute_resource_set_console_password=compute_resource_set_console_password, compute_resource_display_type=compute_resource_display_type, compute_resource_keyboard_layout=compute_resource_keyboard_layout, compute_resource_caching_enabled=compute_resource_caching_enabled, compute_resource_location_ids=compute_resource_location_ids, compute_resource_organization_ids=compute_resource_organization_ids)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->put_compute_resources_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **compute_resource_name** | **str**|  | [optional]
 **compute_resource_provider** | **str**| Providers include  | [optional]
 **compute_resource_url** | **str**| URL for Libvirt, oVirt and OpenStack | [optional]
 **compute_resource_description** | **str**|  | [optional]
 **compute_resource_user** | **str**| Username for oVirt, EC2, VMware, OpenStack. Access Key for EC2. | [optional]
 **compute_resource_password** | **str**| Password for oVirt, EC2, VMware, OpenStack. Secret key for EC2 | [optional]
 **compute_resource_datacenter** | **str**| for oVirt, VMware Datacenter | [optional]
 **compute_resource_ovirt_quota** | **str**| for oVirt only, ID or Name of quota to use | [optional]
 **compute_resource_public_key** | **str**| for oVirt only | [optional]
 **compute_resource_region** | **str**| for AzureRm eg. &#39;eastus&#39; and for EC2 only. Use &#39;us-gov-west-1&#39; for EC2 GovCloud region | [optional]
 **compute_resource_tenant** | **str**| for OpenStack and AzureRm only | [optional]
 **compute_resource_domain** | **str**| for OpenStack (v3) only | [optional]
 **compute_resource_project_domain_name** | **str**| for OpenStack (v3) only | [optional]
 **compute_resource_project_domain_id** | **str**| for OpenStack (v3) only | [optional]
 **compute_resource_server** | **str**| for VMware | [optional]
 **compute_resource_set_console_password** | **bool**| for Libvirt and VMware only | [optional]
 **compute_resource_display_type** | **str**| for Libvirt and oVirt only | [optional]
 **compute_resource_keyboard_layout** | **str**| for oVirt only | [optional]
 **compute_resource_caching_enabled** | **bool**| enable caching, for VMware only | [optional]
 **compute_resource_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **compute_resource_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_compute_resources_id_associate_vm_id**
> put_compute_resources_id_associate_vm_id(id, vm_id, location_id=location_id, organization_id=organization_id)

Associate VMs to Hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
vm_id = 'vm_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Associate VMs to Hosts
    api_instance.put_compute_resources_id_associate_vm_id(id, vm_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->put_compute_resources_id_associate_vm_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **vm_id** | **str**|  |
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

# **put_compute_resources_id_available_virtual_machines_vm_id_power**
> put_compute_resources_id_available_virtual_machines_vm_id_power(id, vm_id, location_id=location_id, organization_id=organization_id)

Power a Virtual Machine



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
vm_id = 'vm_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Power a Virtual Machine
    api_instance.put_compute_resources_id_available_virtual_machines_vm_id_power(id, vm_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->put_compute_resources_id_available_virtual_machines_vm_id_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **vm_id** | **str**|  |
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

# **put_compute_resources_id_refresh_cache**
> put_compute_resources_id_refresh_cache(id, location_id=location_id, organization_id=organization_id)

Refresh Compute Resource Cache



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ComputeResourcesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Refresh Compute Resource Cache
    api_instance.put_compute_resources_id_refresh_cache(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ComputeResourcesApi->put_compute_resources_id_refresh_cache: %s\n" % e)
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
