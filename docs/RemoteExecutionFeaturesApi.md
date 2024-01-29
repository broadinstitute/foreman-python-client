# foreman.RemoteExecutionFeaturesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_hosts_id_available_remote_execution_features**](RemoteExecutionFeaturesApi.md#get_api_hosts_id_available_remote_execution_features) | **GET** /api/hosts/{id}/available_remote_execution_features | List available remote execution features for a host
[**get_remote_execution_features**](RemoteExecutionFeaturesApi.md#get_remote_execution_features) | **GET** /remote_execution_features | List remote execution features
[**get_remote_execution_features_id**](RemoteExecutionFeaturesApi.md#get_remote_execution_features_id) | **GET** /remote_execution_features/{id} | Show remote execution feature
[**put_remote_execution_features_id**](RemoteExecutionFeaturesApi.md#put_remote_execution_features_id) | **PUT** /remote_execution_features/{id} | Update a job template


# **get_api_hosts_id_available_remote_execution_features**
> get_api_hosts_id_available_remote_execution_features(id, location_id=location_id, organization_id=organization_id)

List available remote execution features for a host

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
    api_instance = foreman.RemoteExecutionFeaturesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # List available remote execution features for a host
        api_instance.get_api_hosts_id_available_remote_execution_features(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RemoteExecutionFeaturesApi->get_api_hosts_id_available_remote_execution_features: %s\n" % e)
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

# **get_remote_execution_features**
> get_remote_execution_features(location_id=location_id, organization_id=organization_id)

List remote execution features

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
    api_instance = foreman.RemoteExecutionFeaturesApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # List remote execution features
        api_instance.get_remote_execution_features(location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RemoteExecutionFeaturesApi->get_remote_execution_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_remote_execution_features_id**
> get_remote_execution_features_id(id, location_id=location_id, organization_id=organization_id)

Show remote execution feature

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
    api_instance = foreman.RemoteExecutionFeaturesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show remote execution feature
        api_instance.get_remote_execution_features_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling RemoteExecutionFeaturesApi->get_remote_execution_features_id: %s\n" % e)
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

# **put_remote_execution_features_id**
> put_remote_execution_features_id(id, location_id=location_id, organization_id=organization_id, remote_execution_feature_job_template_id=remote_execution_feature_job_template_id)

Update a job template

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
    api_instance = foreman.RemoteExecutionFeaturesApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    remote_execution_feature_job_template_id = 'remote_execution_feature_job_template_id_example' # str | Job template ID to be used for the feature (optional)

    try:
        # Update a job template
        api_instance.put_remote_execution_features_id(id, location_id=location_id, organization_id=organization_id, remote_execution_feature_job_template_id=remote_execution_feature_job_template_id)
    except Exception as e:
        print("Exception when calling RemoteExecutionFeaturesApi->put_remote_execution_features_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **remote_execution_feature_job_template_id** | **str**| Job template ID to be used for the feature | [optional] 

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

