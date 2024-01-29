# foreman.InstanceHostsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destroy_instance_hosts_host_id**](InstanceHostsApi.md#destroy_instance_hosts_host_id) | **DELETE** /instance_hosts/{host_id} | Unassign a given host from the Foreman instance
[**get_instance_hosts**](InstanceHostsApi.md#get_instance_hosts) | **GET** /instance_hosts | List hosts forming the Foreman instance
[**put_instance_hosts_host_id**](InstanceHostsApi.md#put_instance_hosts_host_id) | **PUT** /instance_hosts/{host_id} | Assign a host to the Foreman instance


# **destroy_instance_hosts_host_id**
> destroy_instance_hosts_host_id(host_id, location_id=location_id, organization_id=organization_id)

Unassign a given host from the Foreman instance

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
    api_instance = foreman.InstanceHostsApi(api_client)
    host_id = 3.4 # float | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Unassign a given host from the Foreman instance
        api_instance.destroy_instance_hosts_host_id(host_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling InstanceHostsApi->destroy_instance_hosts_host_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**|  | 
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

# **get_instance_hosts**
> get_instance_hosts(location_id=location_id, organization_id=organization_id)

List hosts forming the Foreman instance

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
    api_instance = foreman.InstanceHostsApi(api_client)
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # List hosts forming the Foreman instance
        api_instance.get_instance_hosts(location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling InstanceHostsApi->get_instance_hosts: %s\n" % e)
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

# **put_instance_hosts_host_id**
> put_instance_hosts_host_id(host_id, location_id=location_id, organization_id=organization_id)

Assign a host to the Foreman instance

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
    api_instance = foreman.InstanceHostsApi(api_client)
    host_id = 'host_id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Assign a host to the Foreman instance
        api_instance.put_instance_hosts_host_id(host_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling InstanceHostsApi->put_instance_hosts_host_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 
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

