# foreman.OperatingsystemsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_operatingsystems_id**](OperatingsystemsApi.md#delete_operatingsystems_id) | **DELETE** /operatingsystems/{id} | Delete an operating system
[**get_architectures_architecture_id_operatingsystems**](OperatingsystemsApi.md#get_architectures_architecture_id_operatingsystems) | **GET** /architectures/{architecture_id}/operatingsystems | List all operating systems for nested architecture
[**get_media_medium_id_operatingsystems**](OperatingsystemsApi.md#get_media_medium_id_operatingsystems) | **GET** /media/{medium_id}/operatingsystems | List all operating systems for nested medium
[**get_operatingsystems**](OperatingsystemsApi.md#get_operatingsystems) | **GET** /operatingsystems | List all operating systems
[**get_operatingsystems_id**](OperatingsystemsApi.md#get_operatingsystems_id) | **GET** /operatingsystems/{id} | Show an operating system
[**get_operatingsystems_id_bootfiles**](OperatingsystemsApi.md#get_operatingsystems_id_bootfiles) | **GET** /operatingsystems/{id}/bootfiles | List boot files for an operating system
[**get_provisioning_templates_provisioning_template_id_operatingsystems**](OperatingsystemsApi.md#get_provisioning_templates_provisioning_template_id_operatingsystems) | **GET** /provisioning_templates/{provisioning_template_id}/operatingsystems | List all operating systems for nested provisioning template
[**get_ptables_ptable_id_operatingsystems**](OperatingsystemsApi.md#get_ptables_ptable_id_operatingsystems) | **GET** /ptables/{ptable_id}/operatingsystems | List all operating systems for nested partition table
[**post_operatingsystems**](OperatingsystemsApi.md#post_operatingsystems) | **POST** /operatingsystems | Create an operating system
[**put_operatingsystems_id**](OperatingsystemsApi.md#put_operatingsystems_id) | **PUT** /operatingsystems/{id} | Update an operating system


# **delete_operatingsystems_id**
> delete_operatingsystems_id(id, location_id=location_id, organization_id=organization_id)

Delete an operating system

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete an operating system
        api_instance.delete_operatingsystems_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->delete_operatingsystems_id: %s\n" % e)
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

# **get_architectures_architecture_id_operatingsystems**
> get_architectures_architecture_id_operatingsystems(architecture_id, medium_id, ptable_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)

List all operating systems for nested architecture

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    architecture_id = 'architecture_id_example' # str | ID of architecture
    medium_id = 'medium_id_example' # str | ID of medium
    ptable_id = 'ptable_id_example' # str | ID of partition table
    provisioning_template_id = 'provisioning_template_id_example' # str | ID of template
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    os_parameters_attributes = ['os_parameters_attributes_example'] # List[str] | Array of parameters (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all operating systems for nested architecture
        api_instance.get_architectures_architecture_id_operatingsystems(architecture_id, medium_id, ptable_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->get_architectures_architecture_id_operatingsystems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architecture_id** | **str**| ID of architecture | 
 **medium_id** | **str**| ID of medium | 
 **ptable_id** | **str**| ID of partition table | 
 **provisioning_template_id** | **str**| ID of template | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **os_parameters_attributes** | [**List[str]**](str.md)| Array of parameters | [optional] 
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

# **get_media_medium_id_operatingsystems**
> get_media_medium_id_operatingsystems(medium_id, architecture_id, ptable_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)

List all operating systems for nested medium

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    medium_id = 'medium_id_example' # str | ID of medium
    architecture_id = 'architecture_id_example' # str | ID of architecture
    ptable_id = 'ptable_id_example' # str | ID of partition table
    provisioning_template_id = 'provisioning_template_id_example' # str | ID of template
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    os_parameters_attributes = ['os_parameters_attributes_example'] # List[str] | Array of parameters (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all operating systems for nested medium
        api_instance.get_media_medium_id_operatingsystems(medium_id, architecture_id, ptable_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->get_media_medium_id_operatingsystems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medium_id** | **str**| ID of medium | 
 **architecture_id** | **str**| ID of architecture | 
 **ptable_id** | **str**| ID of partition table | 
 **provisioning_template_id** | **str**| ID of template | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **os_parameters_attributes** | [**List[str]**](str.md)| Array of parameters | [optional] 
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

# **get_operatingsystems**
> get_operatingsystems(architecture_id, medium_id, ptable_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)

List all operating systems

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    architecture_id = 'architecture_id_example' # str | ID of architecture
    medium_id = 'medium_id_example' # str | ID of medium
    ptable_id = 'ptable_id_example' # str | ID of partition table
    provisioning_template_id = 'provisioning_template_id_example' # str | ID of template
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    os_parameters_attributes = ['os_parameters_attributes_example'] # List[str] | Array of parameters (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all operating systems
        api_instance.get_operatingsystems(architecture_id, medium_id, ptable_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->get_operatingsystems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **architecture_id** | **str**| ID of architecture | 
 **medium_id** | **str**| ID of medium | 
 **ptable_id** | **str**| ID of partition table | 
 **provisioning_template_id** | **str**| ID of template | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **os_parameters_attributes** | [**List[str]**](str.md)| Array of parameters | [optional] 
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

# **get_operatingsystems_id**
> get_operatingsystems_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)

Show an operating system

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    show_hidden_parameters = True # bool | Display hidden parameter values (optional)

    try:
        # Show an operating system
        api_instance.get_operatingsystems_id(id, location_id=location_id, organization_id=organization_id, show_hidden_parameters=show_hidden_parameters)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->get_operatingsystems_id: %s\n" % e)
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

# **get_operatingsystems_id_bootfiles**
> get_operatingsystems_id_bootfiles(id, location_id=location_id, organization_id=organization_id, medium=medium, architecture=architecture)

List boot files for an operating system

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    medium = 'medium_example' # str |  (optional)
    architecture = 'architecture_example' # str |  (optional)

    try:
        # List boot files for an operating system
        api_instance.get_operatingsystems_id_bootfiles(id, location_id=location_id, organization_id=organization_id, medium=medium, architecture=architecture)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->get_operatingsystems_id_bootfiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **medium** | **str**|  | [optional] 
 **architecture** | **str**|  | [optional] 

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

# **get_provisioning_templates_provisioning_template_id_operatingsystems**
> get_provisioning_templates_provisioning_template_id_operatingsystems(provisioning_template_id, architecture_id, medium_id, ptable_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)

List all operating systems for nested provisioning template

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    provisioning_template_id = 'provisioning_template_id_example' # str | ID of template
    architecture_id = 'architecture_id_example' # str | ID of architecture
    medium_id = 'medium_id_example' # str | ID of medium
    ptable_id = 'ptable_id_example' # str | ID of partition table
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    os_parameters_attributes = ['os_parameters_attributes_example'] # List[str] | Array of parameters (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all operating systems for nested provisioning template
        api_instance.get_provisioning_templates_provisioning_template_id_operatingsystems(provisioning_template_id, architecture_id, medium_id, ptable_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->get_provisioning_templates_provisioning_template_id_operatingsystems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provisioning_template_id** | **str**| ID of template | 
 **architecture_id** | **str**| ID of architecture | 
 **medium_id** | **str**| ID of medium | 
 **ptable_id** | **str**| ID of partition table | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **os_parameters_attributes** | [**List[str]**](str.md)| Array of parameters | [optional] 
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

# **get_ptables_ptable_id_operatingsystems**
> get_ptables_ptable_id_operatingsystems(ptable_id, architecture_id, medium_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)

List all operating systems for nested partition table

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    ptable_id = 'ptable_id_example' # str | ID of partition table
    architecture_id = 'architecture_id_example' # str | ID of architecture
    medium_id = 'medium_id_example' # str | ID of medium
    provisioning_template_id = 'provisioning_template_id_example' # str | ID of template
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    os_parameters_attributes = ['os_parameters_attributes_example'] # List[str] | Array of parameters (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all operating systems for nested partition table
        api_instance.get_ptables_ptable_id_operatingsystems(ptable_id, architecture_id, medium_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, os_parameters_attributes=os_parameters_attributes, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->get_ptables_ptable_id_operatingsystems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptable_id** | **str**| ID of partition table | 
 **architecture_id** | **str**| ID of architecture | 
 **medium_id** | **str**| ID of medium | 
 **provisioning_template_id** | **str**| ID of template | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **os_parameters_attributes** | [**List[str]**](str.md)| Array of parameters | [optional] 
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

# **post_operatingsystems**
> post_operatingsystems(operatingsystem_name, operatingsystem_major, location_id=location_id, organization_id=organization_id, operatingsystem_minor=operatingsystem_minor, operatingsystem_description=operatingsystem_description, operatingsystem_family=operatingsystem_family, operatingsystem_release_name=operatingsystem_release_name, operatingsystem_os_parameters_attributes=operatingsystem_os_parameters_attributes, operatingsystem_password_hash=operatingsystem_password_hash, operatingsystem_architecture_ids=operatingsystem_architecture_ids, operatingsystem_provisioning_template_ids=operatingsystem_provisioning_template_ids, operatingsystem_medium_ids=operatingsystem_medium_ids, operatingsystem_ptable_ids=operatingsystem_ptable_ids)

Create an operating system

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    operatingsystem_name = 'operatingsystem_name_example' # str | 
    operatingsystem_major = 'operatingsystem_major_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    operatingsystem_minor = 'operatingsystem_minor_example' # str |  (optional)
    operatingsystem_description = 'operatingsystem_description_example' # str |  (optional)
    operatingsystem_family = 'operatingsystem_family_example' # str |  (optional)
    operatingsystem_release_name = 'operatingsystem_release_name_example' # str |  (optional)
    operatingsystem_os_parameters_attributes = ['operatingsystem_os_parameters_attributes_example'] # List[str] | Array of parameters (optional)
    operatingsystem_password_hash = 'operatingsystem_password_hash_example' # str | Root password hash function to use (optional)
    operatingsystem_architecture_ids = ['operatingsystem_architecture_ids_example'] # List[str] | IDs of associated architectures (optional)
    operatingsystem_provisioning_template_ids = ['operatingsystem_provisioning_template_ids_example'] # List[str] | IDs of associated provisioning templates (optional)
    operatingsystem_medium_ids = ['operatingsystem_medium_ids_example'] # List[str] | IDs of associated media (optional)
    operatingsystem_ptable_ids = ['operatingsystem_ptable_ids_example'] # List[str] | IDs of associated partition tables (optional)

    try:
        # Create an operating system
        api_instance.post_operatingsystems(operatingsystem_name, operatingsystem_major, location_id=location_id, organization_id=organization_id, operatingsystem_minor=operatingsystem_minor, operatingsystem_description=operatingsystem_description, operatingsystem_family=operatingsystem_family, operatingsystem_release_name=operatingsystem_release_name, operatingsystem_os_parameters_attributes=operatingsystem_os_parameters_attributes, operatingsystem_password_hash=operatingsystem_password_hash, operatingsystem_architecture_ids=operatingsystem_architecture_ids, operatingsystem_provisioning_template_ids=operatingsystem_provisioning_template_ids, operatingsystem_medium_ids=operatingsystem_medium_ids, operatingsystem_ptable_ids=operatingsystem_ptable_ids)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->post_operatingsystems: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_name** | **str**|  | 
 **operatingsystem_major** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **operatingsystem_minor** | **str**|  | [optional] 
 **operatingsystem_description** | **str**|  | [optional] 
 **operatingsystem_family** | **str**|  | [optional] 
 **operatingsystem_release_name** | **str**|  | [optional] 
 **operatingsystem_os_parameters_attributes** | [**List[str]**](str.md)| Array of parameters | [optional] 
 **operatingsystem_password_hash** | **str**| Root password hash function to use | [optional] 
 **operatingsystem_architecture_ids** | [**List[str]**](str.md)| IDs of associated architectures | [optional] 
 **operatingsystem_provisioning_template_ids** | [**List[str]**](str.md)| IDs of associated provisioning templates | [optional] 
 **operatingsystem_medium_ids** | [**List[str]**](str.md)| IDs of associated media | [optional] 
 **operatingsystem_ptable_ids** | [**List[str]**](str.md)| IDs of associated partition tables | [optional] 

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

# **put_operatingsystems_id**
> put_operatingsystems_id(id, location_id=location_id, organization_id=organization_id, operatingsystem_name=operatingsystem_name, operatingsystem_major=operatingsystem_major, operatingsystem_minor=operatingsystem_minor, operatingsystem_description=operatingsystem_description, operatingsystem_family=operatingsystem_family, operatingsystem_release_name=operatingsystem_release_name, operatingsystem_os_parameters_attributes=operatingsystem_os_parameters_attributes, operatingsystem_password_hash=operatingsystem_password_hash, operatingsystem_architecture_ids=operatingsystem_architecture_ids, operatingsystem_provisioning_template_ids=operatingsystem_provisioning_template_ids, operatingsystem_medium_ids=operatingsystem_medium_ids, operatingsystem_ptable_ids=operatingsystem_ptable_ids)

Update an operating system

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
    api_instance = foreman.OperatingsystemsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    operatingsystem_name = 'operatingsystem_name_example' # str |  (optional)
    operatingsystem_major = 'operatingsystem_major_example' # str |  (optional)
    operatingsystem_minor = 'operatingsystem_minor_example' # str |  (optional)
    operatingsystem_description = 'operatingsystem_description_example' # str |  (optional)
    operatingsystem_family = 'operatingsystem_family_example' # str |  (optional)
    operatingsystem_release_name = 'operatingsystem_release_name_example' # str |  (optional)
    operatingsystem_os_parameters_attributes = ['operatingsystem_os_parameters_attributes_example'] # List[str] | Array of parameters (optional)
    operatingsystem_password_hash = 'operatingsystem_password_hash_example' # str | Root password hash function to use (optional)
    operatingsystem_architecture_ids = ['operatingsystem_architecture_ids_example'] # List[str] | IDs of associated architectures (optional)
    operatingsystem_provisioning_template_ids = ['operatingsystem_provisioning_template_ids_example'] # List[str] | IDs of associated provisioning templates (optional)
    operatingsystem_medium_ids = ['operatingsystem_medium_ids_example'] # List[str] | IDs of associated media (optional)
    operatingsystem_ptable_ids = ['operatingsystem_ptable_ids_example'] # List[str] | IDs of associated partition tables (optional)

    try:
        # Update an operating system
        api_instance.put_operatingsystems_id(id, location_id=location_id, organization_id=organization_id, operatingsystem_name=operatingsystem_name, operatingsystem_major=operatingsystem_major, operatingsystem_minor=operatingsystem_minor, operatingsystem_description=operatingsystem_description, operatingsystem_family=operatingsystem_family, operatingsystem_release_name=operatingsystem_release_name, operatingsystem_os_parameters_attributes=operatingsystem_os_parameters_attributes, operatingsystem_password_hash=operatingsystem_password_hash, operatingsystem_architecture_ids=operatingsystem_architecture_ids, operatingsystem_provisioning_template_ids=operatingsystem_provisioning_template_ids, operatingsystem_medium_ids=operatingsystem_medium_ids, operatingsystem_ptable_ids=operatingsystem_ptable_ids)
    except Exception as e:
        print("Exception when calling OperatingsystemsApi->put_operatingsystems_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **operatingsystem_name** | **str**|  | [optional] 
 **operatingsystem_major** | **str**|  | [optional] 
 **operatingsystem_minor** | **str**|  | [optional] 
 **operatingsystem_description** | **str**|  | [optional] 
 **operatingsystem_family** | **str**|  | [optional] 
 **operatingsystem_release_name** | **str**|  | [optional] 
 **operatingsystem_os_parameters_attributes** | [**List[str]**](str.md)| Array of parameters | [optional] 
 **operatingsystem_password_hash** | **str**| Root password hash function to use | [optional] 
 **operatingsystem_architecture_ids** | [**List[str]**](str.md)| IDs of associated architectures | [optional] 
 **operatingsystem_provisioning_template_ids** | [**List[str]**](str.md)| IDs of associated provisioning templates | [optional] 
 **operatingsystem_medium_ids** | [**List[str]**](str.md)| IDs of associated media | [optional] 
 **operatingsystem_ptable_ids** | [**List[str]**](str.md)| IDs of associated partition tables | [optional] 

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

