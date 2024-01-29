# foreman.OsDefaultTemplatesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_operatingsystems_operatingsystem_id_os_default_templates_id**](OsDefaultTemplatesApi.md#delete_operatingsystems_operatingsystem_id_os_default_templates_id) | **DELETE** /operatingsystems/{operatingsystem_id}/os_default_templates/{id} | Delete a default template combination for an operating system
[**get_operatingsystems_operatingsystem_id_os_default_templates**](OsDefaultTemplatesApi.md#get_operatingsystems_operatingsystem_id_os_default_templates) | **GET** /operatingsystems/{operatingsystem_id}/os_default_templates | List default templates combinations for an operating system
[**get_operatingsystems_operatingsystem_id_os_default_templates_id**](OsDefaultTemplatesApi.md#get_operatingsystems_operatingsystem_id_os_default_templates_id) | **GET** /operatingsystems/{operatingsystem_id}/os_default_templates/{id} | Show a default template combination for an operating system
[**get_provisioning_templates_provisioning_template_id_os_default_templates**](OsDefaultTemplatesApi.md#get_provisioning_templates_provisioning_template_id_os_default_templates) | **GET** /provisioning_templates/{provisioning_template_id}/os_default_templates | List operating systems where this template is set as a default
[**post_operatingsystems_operatingsystem_id_os_default_templates**](OsDefaultTemplatesApi.md#post_operatingsystems_operatingsystem_id_os_default_templates) | **POST** /operatingsystems/{operatingsystem_id}/os_default_templates | Create a default template combination for an operating system
[**put_operatingsystems_operatingsystem_id_os_default_templates_id**](OsDefaultTemplatesApi.md#put_operatingsystems_operatingsystem_id_os_default_templates_id) | **PUT** /operatingsystems/{operatingsystem_id}/os_default_templates/{id} | Update a default template combination for an operating system


# **delete_operatingsystems_operatingsystem_id_os_default_templates_id**
> delete_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, location_id=location_id, organization_id=organization_id)

Delete a default template combination for an operating system

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
    api_instance = foreman.OsDefaultTemplatesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete a default template combination for an operating system
        api_instance.delete_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling OsDefaultTemplatesApi->delete_operatingsystems_operatingsystem_id_os_default_templates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
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

# **get_operatingsystems_operatingsystem_id_os_default_templates**
> get_operatingsystems_operatingsystem_id_os_default_templates(operatingsystem_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)

List default templates combinations for an operating system

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
    api_instance = foreman.OsDefaultTemplatesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    provisioning_template_id = 'provisioning_template_id_example' # str | ID of provisioning template
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List default templates combinations for an operating system
        api_instance.get_operatingsystems_operatingsystem_id_os_default_templates(operatingsystem_id, provisioning_template_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling OsDefaultTemplatesApi->get_operatingsystems_operatingsystem_id_os_default_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **provisioning_template_id** | **str**| ID of provisioning template | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
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

# **get_operatingsystems_operatingsystem_id_os_default_templates_id**
> get_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, location_id=location_id, organization_id=organization_id)

Show a default template combination for an operating system

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
    api_instance = foreman.OsDefaultTemplatesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    id = 3.4 # float | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show a default template combination for an operating system
        api_instance.get_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling OsDefaultTemplatesApi->get_operatingsystems_operatingsystem_id_os_default_templates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **id** | **float**|  | 
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

# **get_provisioning_templates_provisioning_template_id_os_default_templates**
> get_provisioning_templates_provisioning_template_id_os_default_templates(provisioning_template_id, operatingsystem_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)

List operating systems where this template is set as a default

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
    api_instance = foreman.OsDefaultTemplatesApi(api_client)
    provisioning_template_id = 'provisioning_template_id_example' # str | ID of provisioning template
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List operating systems where this template is set as a default
        api_instance.get_provisioning_templates_provisioning_template_id_os_default_templates(provisioning_template_id, operatingsystem_id, location_id=location_id, organization_id=organization_id, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling OsDefaultTemplatesApi->get_provisioning_templates_provisioning_template_id_os_default_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provisioning_template_id** | **str**| ID of provisioning template | 
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
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

# **post_operatingsystems_operatingsystem_id_os_default_templates**
> post_operatingsystems_operatingsystem_id_os_default_templates(operatingsystem_id, location_id=location_id, organization_id=organization_id, os_default_template_template_kind_id=os_default_template_template_kind_id, os_default_template_provisioning_template_id=os_default_template_provisioning_template_id)

Create a default template combination for an operating system

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
    api_instance = foreman.OsDefaultTemplatesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    os_default_template_template_kind_id = 3.4 # float |  (optional)
    os_default_template_provisioning_template_id = 3.4 # float | ID of provisioning template (optional)

    try:
        # Create a default template combination for an operating system
        api_instance.post_operatingsystems_operatingsystem_id_os_default_templates(operatingsystem_id, location_id=location_id, organization_id=organization_id, os_default_template_template_kind_id=os_default_template_template_kind_id, os_default_template_provisioning_template_id=os_default_template_provisioning_template_id)
    except Exception as e:
        print("Exception when calling OsDefaultTemplatesApi->post_operatingsystems_operatingsystem_id_os_default_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **os_default_template_template_kind_id** | **float**|  | [optional] 
 **os_default_template_provisioning_template_id** | **float**| ID of provisioning template | [optional] 

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

# **put_operatingsystems_operatingsystem_id_os_default_templates_id**
> put_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, location_id=location_id, organization_id=organization_id, os_default_template_template_kind_id=os_default_template_template_kind_id, os_default_template_provisioning_template_id=os_default_template_provisioning_template_id)

Update a default template combination for an operating system

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
    api_instance = foreman.OsDefaultTemplatesApi(api_client)
    operatingsystem_id = 3.4 # float | ID of operating system
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    os_default_template_template_kind_id = 3.4 # float |  (optional)
    os_default_template_provisioning_template_id = 3.4 # float | ID of provisioning template (optional)

    try:
        # Update a default template combination for an operating system
        api_instance.put_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, location_id=location_id, organization_id=organization_id, os_default_template_template_kind_id=os_default_template_template_kind_id, os_default_template_provisioning_template_id=os_default_template_provisioning_template_id)
    except Exception as e:
        print("Exception when calling OsDefaultTemplatesApi->put_operatingsystems_operatingsystem_id_os_default_templates_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operatingsystem_id** | **float**| ID of operating system | 
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **os_default_template_template_kind_id** | **float**|  | [optional] 
 **os_default_template_provisioning_template_id** | **float**| ID of provisioning template | [optional] 

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

