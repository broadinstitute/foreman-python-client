# pyforeman.HostTracerApi

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
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostTracerApi()
host_id = 8.14 # float | ID of the host

try:
    # List services that need restarting on the host
    api_instance.get_hosts_host_id_traces(host_id)
except ApiException as e:
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_host_id_traces_resolve**
> put_hosts_host_id_traces_resolve(host_id, trace_ids)

Resolve traces



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostTracerApi()
host_id = 8.14 # float | ID of the host
trace_ids = ['trace_ids_example'] # list[str] | Array of Trace IDs

try:
    # Resolve traces
    api_instance.put_hosts_host_id_traces_resolve(host_id, trace_ids)
except ApiException as e:
    print("Exception when calling HostTracerApi->put_hosts_host_id_traces_resolve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| ID of the host |
 **trace_ids** | [**list[str]**](str.md)| Array of Trace IDs |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
