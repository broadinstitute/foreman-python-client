# foreman.HostTracerApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hosts_host_id_traces**](HostTracerApi.md#get_hosts_host_id_traces) | **GET** /hosts/{host_id}/traces | List services that need restarting on the host
[**put_hosts_host_id_traces_resolve**](HostTracerApi.md#put_hosts_host_id_traces_resolve) | **PUT** /hosts/{host_id}/traces/resolve | Resolve traces


# **get_hosts_host_id_traces**
> get_hosts_host_id_traces(host_id)

List services that need restarting on the host

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
    api_instance = foreman.HostTracerApi(api_client)
    host_id = 3.4 # float | ID of the host

    try:
        # List services that need restarting on the host
        api_instance.get_hosts_host_id_traces(host_id)
    except Exception as e:
        print("Exception when calling HostTracerApi->get_hosts_host_id_traces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| ID of the host | 

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

# **put_hosts_host_id_traces_resolve**
> put_hosts_host_id_traces_resolve(host_id, trace_ids)

Resolve traces

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
    api_instance = foreman.HostTracerApi(api_client)
    host_id = 3.4 # float | ID of the host
    trace_ids = ['trace_ids_example'] # List[str] | Array of Trace IDs

    try:
        # Resolve traces
        api_instance.put_hosts_host_id_traces_resolve(host_id, trace_ids)
    except Exception as e:
        print("Exception when calling HostTracerApi->put_hosts_host_id_traces_resolve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| ID of the host | 
 **trace_ids** | [**List[str]**](str.md)| Array of Trace IDs | 

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

