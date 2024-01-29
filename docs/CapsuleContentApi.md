# foreman.CapsuleContentApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_capsules_id_content_lifecycle_environments_environment_id**](CapsuleContentApi.md#delete_capsules_id_content_lifecycle_environments_environment_id) | **DELETE** /capsules/{id}/content/lifecycle_environments/{environment_id} | Remove lifecycle environments from the smart proxy
[**delete_capsules_id_content_sync**](CapsuleContentApi.md#delete_capsules_id_content_sync) | **DELETE** /capsules/{id}/content/sync | Cancel running smart proxy synchronization
[**get_capsules_id_content_available_lifecycle_environments**](CapsuleContentApi.md#get_capsules_id_content_available_lifecycle_environments) | **GET** /capsules/{id}/content/available_lifecycle_environments | List the lifecycle environments not attached to the smart proxy
[**get_capsules_id_content_counts**](CapsuleContentApi.md#get_capsules_id_content_counts) | **GET** /capsules/{id}/content/counts | List content counts for the smart proxy
[**get_capsules_id_content_lifecycle_environments**](CapsuleContentApi.md#get_capsules_id_content_lifecycle_environments) | **GET** /capsules/{id}/content/lifecycle_environments | List the lifecycle environments attached to the smart proxy
[**get_capsules_id_content_sync**](CapsuleContentApi.md#get_capsules_id_content_sync) | **GET** /capsules/{id}/content/sync | Get current smart proxy synchronization status
[**post_capsules_id_content_lifecycle_environments**](CapsuleContentApi.md#post_capsules_id_content_lifecycle_environments) | **POST** /capsules/{id}/content/lifecycle_environments | Add lifecycle environments to the smart proxy
[**post_capsules_id_content_reclaim_space**](CapsuleContentApi.md#post_capsules_id_content_reclaim_space) | **POST** /capsules/{id}/content/reclaim_space | Reclaim space from all On Demand repositories on a smart proxy
[**post_capsules_id_content_sync**](CapsuleContentApi.md#post_capsules_id_content_sync) | **POST** /capsules/{id}/content/sync | Synchronize the content to the smart proxy
[**post_capsules_id_content_update_counts**](CapsuleContentApi.md#post_capsules_id_content_update_counts) | **POST** /capsules/{id}/content/update_counts | Update content counts for the smart proxy


# **delete_capsules_id_content_lifecycle_environments_environment_id**
> delete_capsules_id_content_lifecycle_environments_environment_id(id, environment_id)

Remove lifecycle environments from the smart proxy

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy
    environment_id = 3.4 # float | Id of the lifecycle environment

    try:
        # Remove lifecycle environments from the smart proxy
        api_instance.delete_capsules_id_content_lifecycle_environments_environment_id(id, environment_id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->delete_capsules_id_content_lifecycle_environments_environment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 
 **environment_id** | **float**| Id of the lifecycle environment | 

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

# **delete_capsules_id_content_sync**
> delete_capsules_id_content_sync(id)

Cancel running smart proxy synchronization

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy

    try:
        # Cancel running smart proxy synchronization
        api_instance.delete_capsules_id_content_sync(id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->delete_capsules_id_content_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 

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

# **get_capsules_id_content_available_lifecycle_environments**
> get_capsules_id_content_available_lifecycle_environments(id, organization_id=organization_id)

List the lifecycle environments not attached to the smart proxy

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy
    organization_id = 3.4 # float | Id of the organization to limit environments on (optional)

    try:
        # List the lifecycle environments not attached to the smart proxy
        api_instance.get_capsules_id_content_available_lifecycle_environments(id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->get_capsules_id_content_available_lifecycle_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 
 **organization_id** | **float**| Id of the organization to limit environments on | [optional] 

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

# **get_capsules_id_content_counts**
> get_capsules_id_content_counts(id)

List content counts for the smart proxy

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy

    try:
        # List content counts for the smart proxy
        api_instance.get_capsules_id_content_counts(id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->get_capsules_id_content_counts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 

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

# **get_capsules_id_content_lifecycle_environments**
> get_capsules_id_content_lifecycle_environments(id, organization_id=organization_id)

List the lifecycle environments attached to the smart proxy

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy
    organization_id = 3.4 # float | Id of the organization to limit environments on (optional)

    try:
        # List the lifecycle environments attached to the smart proxy
        api_instance.get_capsules_id_content_lifecycle_environments(id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->get_capsules_id_content_lifecycle_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 
 **organization_id** | **float**| Id of the organization to limit environments on | [optional] 

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

# **get_capsules_id_content_sync**
> get_capsules_id_content_sync(id, organization_id=organization_id)

Get current smart proxy synchronization status

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy
    organization_id = 3.4 # float | Id of the organization to get the status for (optional)

    try:
        # Get current smart proxy synchronization status
        api_instance.get_capsules_id_content_sync(id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->get_capsules_id_content_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 
 **organization_id** | **float**| Id of the organization to get the status for | [optional] 

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

# **post_capsules_id_content_lifecycle_environments**
> post_capsules_id_content_lifecycle_environments(id, environment_id)

Add lifecycle environments to the smart proxy

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy
    environment_id = 3.4 # float | Id of the lifecycle environment

    try:
        # Add lifecycle environments to the smart proxy
        api_instance.post_capsules_id_content_lifecycle_environments(id, environment_id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->post_capsules_id_content_lifecycle_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 
 **environment_id** | **float**| Id of the lifecycle environment | 

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

# **post_capsules_id_content_reclaim_space**
> post_capsules_id_content_reclaim_space(id)

Reclaim space from all On Demand repositories on a smart proxy

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy

    try:
        # Reclaim space from all On Demand repositories on a smart proxy
        api_instance.post_capsules_id_content_reclaim_space(id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->post_capsules_id_content_reclaim_space: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 

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

# **post_capsules_id_content_sync**
> post_capsules_id_content_sync(id, environment_id=environment_id, content_view_id=content_view_id, repository_id=repository_id, skip_metadata_check=skip_metadata_check)

Synchronize the content to the smart proxy

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy
    environment_id = 3.4 # float | Id of the environment to limit the synchronization on (optional)
    content_view_id = 3.4 # float | Id of the content view to limit the synchronization on (optional)
    repository_id = 3.4 # float | Id of the repository to limit the synchronization on (optional)
    skip_metadata_check = True # bool | Skip metadata check on each repository on the smart proxy (optional)

    try:
        # Synchronize the content to the smart proxy
        api_instance.post_capsules_id_content_sync(id, environment_id=environment_id, content_view_id=content_view_id, repository_id=repository_id, skip_metadata_check=skip_metadata_check)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->post_capsules_id_content_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 
 **environment_id** | **float**| Id of the environment to limit the synchronization on | [optional] 
 **content_view_id** | **float**| Id of the content view to limit the synchronization on | [optional] 
 **repository_id** | **float**| Id of the repository to limit the synchronization on | [optional] 
 **skip_metadata_check** | **bool**| Skip metadata check on each repository on the smart proxy | [optional] 

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

# **post_capsules_id_content_update_counts**
> post_capsules_id_content_update_counts(id)

Update content counts for the smart proxy

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
    api_instance = foreman.CapsuleContentApi(api_client)
    id = 3.4 # float | Id of the smart proxy

    try:
        # Update content counts for the smart proxy
        api_instance.post_capsules_id_content_update_counts(id)
    except Exception as e:
        print("Exception when calling CapsuleContentApi->post_capsules_id_content_update_counts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the smart proxy | 

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

