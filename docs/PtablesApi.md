# foreman.PtablesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ptables_id**](PtablesApi.md#delete_ptables_id) | **DELETE** /ptables/{id} | Delete a partition table
[**get_locations_location_id_ptables**](PtablesApi.md#get_locations_location_id_ptables) | **GET** /locations/{location_id}/ptables | List all partition tables per location
[**get_operatingsystems_operatingsystem_id_ptables**](PtablesApi.md#get_operatingsystems_operatingsystem_id_ptables) | **GET** /operatingsystems/{operatingsystem_id}/ptables | List all partition tables for an operating system
[**get_organizations_organization_id_ptables**](PtablesApi.md#get_organizations_organization_id_ptables) | **GET** /organizations/{organization_id}/ptables | List all partition tables per organization
[**get_ptables**](PtablesApi.md#get_ptables) | **GET** /ptables | List all partition tables
[**get_ptables_id**](PtablesApi.md#get_ptables_id) | **GET** /ptables/{id} | Show a partition table
[**get_ptables_id_export**](PtablesApi.md#get_ptables_id_export) | **GET** /ptables/{id}/export | Export a partition template to ERB
[**get_ptables_revision**](PtablesApi.md#get_ptables_revision) | **GET** /ptables/revision | 
[**post_ptables**](PtablesApi.md#post_ptables) | **POST** /ptables | Create a partition table
[**post_ptables_id_clone**](PtablesApi.md#post_ptables_id_clone) | **POST** /ptables/{id}/clone | Clone a template
[**post_ptables_import**](PtablesApi.md#post_ptables_import) | **POST** /ptables/import | Import a partition table
[**put_ptables_id**](PtablesApi.md#put_ptables_id) | **PUT** /ptables/{id} | Update a partition table


# **delete_ptables_id**
> delete_ptables_id(id, location_id=location_id, organization_id=organization_id)

Delete a partition table

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
    api_instance = foreman.PtablesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a partition table
        api_instance.delete_ptables_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling PtablesApi->delete_ptables_id: %s\n" % e)
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

# **get_locations_location_id_ptables**
> get_locations_location_id_ptables(location_id, operatingsystem_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all partition tables per location

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
    api_instance = foreman.PtablesApi(api_client)
    location_id = 3.4 # float | Scope by locations
    operatingsystem_id = 3.4 # float | ID of operating system
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all partition tables per location
        api_instance.get_locations_location_id_ptables(location_id, operatingsystem_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PtablesApi->get_locations_location_id_ptables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **organization_id** | **float**| Scope by organizations | 
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

# **get_operatingsystems_operatingsystem_id_ptables**
> get_operatingsystems_operatingsystem_id_ptables(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all partition tables for an operating system

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
    api_instance = foreman.PtablesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all partition tables for an operating system
        api_instance.get_operatingsystems_operatingsystem_id_ptables(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PtablesApi->get_operatingsystems_operatingsystem_id_ptables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
 **organization_id** | **float**| Scope by organizations | 
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

# **get_organizations_organization_id_ptables**
> get_organizations_organization_id_ptables(organization_id, operatingsystem_id, location_id, search=search, order=order, page=page, per_page=per_page)

List all partition tables per organization

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
    api_instance = foreman.PtablesApi(api_client)
    organization_id = 3.4 # float | Scope by organizations
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all partition tables per organization
        api_instance.get_organizations_organization_id_ptables(organization_id, operatingsystem_id, location_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PtablesApi->get_organizations_organization_id_ptables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
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

# **get_ptables**
> get_ptables(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all partition tables

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
    api_instance = foreman.PtablesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all partition tables
        api_instance.get_ptables(operatingsystem_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PtablesApi->get_ptables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Scope by locations | 
 **organization_id** | **float**| Scope by organizations | 
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

# **get_ptables_id**
> get_ptables_id(id, location_id=location_id, organization_id=organization_id)

Show a partition table

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
    api_instance = foreman.PtablesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show a partition table
        api_instance.get_ptables_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling PtablesApi->get_ptables_id: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ptables_id_export**
> get_ptables_id_export(id, location_id=location_id, organization_id=organization_id)

Export a partition template to ERB

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
    api_instance = foreman.PtablesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Export a partition template to ERB
        api_instance.get_ptables_id_export(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling PtablesApi->get_ptables_id_export: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ptables_revision**
> get_ptables_revision(location_id=location_id, organization_id=organization_id, version=version)



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
    api_instance = foreman.PtablesApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    version = 'version_example' # str | template version (optional)

    try:
        api_instance.get_ptables_revision(location_id=location_id, organization_id=organization_id, version=version)
    except Exception as e:
        print("Exception when calling PtablesApi->get_ptables_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **version** | **str**| template version | [optional] 

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

# **post_ptables**
> post_ptables(ptable_name, ptable_layout, location_id=location_id, organization_id=organization_id, ptable_description=ptable_description, ptable_snippet=ptable_snippet, ptable_audit_comment=ptable_audit_comment, ptable_locked=ptable_locked, ptable_os_family=ptable_os_family, ptable_operatingsystem_ids=ptable_operatingsystem_ids, ptable_host_ids=ptable_host_ids, ptable_hostgroup_ids=ptable_hostgroup_ids, ptable_location_ids=ptable_location_ids, ptable_organization_ids=ptable_organization_ids)

Create a partition table

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
    api_instance = foreman.PtablesApi(api_client)
    ptable_name = 'ptable_name_example' # str | 
    ptable_layout = 'ptable_layout_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    ptable_description = 'ptable_description_example' # str |  (optional)
    ptable_snippet = True # bool |  (optional)
    ptable_audit_comment = 'ptable_audit_comment_example' # str |  (optional)
    ptable_locked = True # bool | Whether or not the template is locked for editing (optional)
    ptable_os_family = 'ptable_os_family_example' # str |  (optional)
    ptable_operatingsystem_ids = ['ptable_operatingsystem_ids_example'] # List[str] | Array of operating system IDs to associate with the partition table (optional)
    ptable_host_ids = ['ptable_host_ids_example'] # List[str] | Array of host IDs to associate with the partition table (optional)
    ptable_hostgroup_ids = ['ptable_hostgroup_ids_example'] # List[str] | Array of host group IDs to associate with the partition table (optional)
    ptable_location_ids = ['ptable_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    ptable_organization_ids = ['ptable_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Create a partition table
        api_instance.post_ptables(ptable_name, ptable_layout, location_id=location_id, organization_id=organization_id, ptable_description=ptable_description, ptable_snippet=ptable_snippet, ptable_audit_comment=ptable_audit_comment, ptable_locked=ptable_locked, ptable_os_family=ptable_os_family, ptable_operatingsystem_ids=ptable_operatingsystem_ids, ptable_host_ids=ptable_host_ids, ptable_hostgroup_ids=ptable_hostgroup_ids, ptable_location_ids=ptable_location_ids, ptable_organization_ids=ptable_organization_ids)
    except Exception as e:
        print("Exception when calling PtablesApi->post_ptables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptable_name** | **str**|  | 
 **ptable_layout** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **ptable_description** | **str**|  | [optional] 
 **ptable_snippet** | **bool**|  | [optional] 
 **ptable_audit_comment** | **str**|  | [optional] 
 **ptable_locked** | **bool**| Whether or not the template is locked for editing | [optional] 
 **ptable_os_family** | **str**|  | [optional] 
 **ptable_operatingsystem_ids** | [**List[str]**](str.md)| Array of operating system IDs to associate with the partition table | [optional] 
 **ptable_host_ids** | [**List[str]**](str.md)| Array of host IDs to associate with the partition table | [optional] 
 **ptable_hostgroup_ids** | [**List[str]**](str.md)| Array of host group IDs to associate with the partition table | [optional] 
 **ptable_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **ptable_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

# **post_ptables_id_clone**
> post_ptables_id_clone(id, ptable_name, location_id=location_id, organization_id=organization_id)

Clone a template

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
    api_instance = foreman.PtablesApi(api_client)
    id = 'id_example' # str | 
    ptable_name = 'ptable_name_example' # str | template name
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Clone a template
        api_instance.post_ptables_id_clone(id, ptable_name, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling PtablesApi->post_ptables_id_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ptable_name** | **str**| template name | 
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

# **post_ptables_import**
> post_ptables_import(location_id=location_id, organization_id=organization_id, ptable_name=ptable_name, ptable_template=ptable_template, ptable_location_ids=ptable_location_ids, ptable_organization_ids=ptable_organization_ids, options_force=options_force, options_associate=options_associate, options_lock=options_lock, options_default=options_default)

Import a partition table

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
    api_instance = foreman.PtablesApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    ptable_name = 'ptable_name_example' # str | template name (optional)
    ptable_template = 'ptable_template_example' # str | template contents including metadata (optional)
    ptable_location_ids = ['ptable_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    ptable_organization_ids = ['ptable_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)
    options_force = True # bool | use if you want update locked templates (optional)
    options_associate = 'options_associate_example' # str | determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata (optional)
    options_lock = True # bool | lock imported templates (false by default) (optional)
    options_default = True # bool | makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default) (optional)

    try:
        # Import a partition table
        api_instance.post_ptables_import(location_id=location_id, organization_id=organization_id, ptable_name=ptable_name, ptable_template=ptable_template, ptable_location_ids=ptable_location_ids, ptable_organization_ids=ptable_organization_ids, options_force=options_force, options_associate=options_associate, options_lock=options_lock, options_default=options_default)
    except Exception as e:
        print("Exception when calling PtablesApi->post_ptables_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **ptable_name** | **str**| template name | [optional] 
 **ptable_template** | **str**| template contents including metadata | [optional] 
 **ptable_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **ptable_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 
 **options_force** | **bool**| use if you want update locked templates | [optional] 
 **options_associate** | **str**| determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata | [optional] 
 **options_lock** | **bool**| lock imported templates (false by default) | [optional] 
 **options_default** | **bool**| makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default) | [optional] 

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

# **put_ptables_id**
> put_ptables_id(id, location_id=location_id, organization_id=organization_id, ptable_name=ptable_name, ptable_description=ptable_description, ptable_layout=ptable_layout, ptable_snippet=ptable_snippet, ptable_audit_comment=ptable_audit_comment, ptable_locked=ptable_locked, ptable_os_family=ptable_os_family, ptable_operatingsystem_ids=ptable_operatingsystem_ids, ptable_host_ids=ptable_host_ids, ptable_hostgroup_ids=ptable_hostgroup_ids, ptable_location_ids=ptable_location_ids, ptable_organization_ids=ptable_organization_ids)

Update a partition table

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
    api_instance = foreman.PtablesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    ptable_name = 'ptable_name_example' # str |  (optional)
    ptable_description = 'ptable_description_example' # str |  (optional)
    ptable_layout = 'ptable_layout_example' # str |  (optional)
    ptable_snippet = True # bool |  (optional)
    ptable_audit_comment = 'ptable_audit_comment_example' # str |  (optional)
    ptable_locked = True # bool | Whether or not the template is locked for editing (optional)
    ptable_os_family = 'ptable_os_family_example' # str |  (optional)
    ptable_operatingsystem_ids = ['ptable_operatingsystem_ids_example'] # List[str] | Array of operating system IDs to associate with the partition table (optional)
    ptable_host_ids = ['ptable_host_ids_example'] # List[str] | Array of host IDs to associate with the partition table (optional)
    ptable_hostgroup_ids = ['ptable_hostgroup_ids_example'] # List[str] | Array of host group IDs to associate with the partition table (optional)
    ptable_location_ids = ['ptable_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    ptable_organization_ids = ['ptable_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Update a partition table
        api_instance.put_ptables_id(id, location_id=location_id, organization_id=organization_id, ptable_name=ptable_name, ptable_description=ptable_description, ptable_layout=ptable_layout, ptable_snippet=ptable_snippet, ptable_audit_comment=ptable_audit_comment, ptable_locked=ptable_locked, ptable_os_family=ptable_os_family, ptable_operatingsystem_ids=ptable_operatingsystem_ids, ptable_host_ids=ptable_host_ids, ptable_hostgroup_ids=ptable_hostgroup_ids, ptable_location_ids=ptable_location_ids, ptable_organization_ids=ptable_organization_ids)
    except Exception as e:
        print("Exception when calling PtablesApi->put_ptables_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **ptable_name** | **str**|  | [optional] 
 **ptable_description** | **str**|  | [optional] 
 **ptable_layout** | **str**|  | [optional] 
 **ptable_snippet** | **bool**|  | [optional] 
 **ptable_audit_comment** | **str**|  | [optional] 
 **ptable_locked** | **bool**| Whether or not the template is locked for editing | [optional] 
 **ptable_os_family** | **str**|  | [optional] 
 **ptable_operatingsystem_ids** | [**List[str]**](str.md)| Array of operating system IDs to associate with the partition table | [optional] 
 **ptable_host_ids** | [**List[str]**](str.md)| Array of host IDs to associate with the partition table | [optional] 
 **ptable_hostgroup_ids** | [**List[str]**](str.md)| Array of host group IDs to associate with the partition table | [optional] 
 **ptable_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **ptable_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

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

