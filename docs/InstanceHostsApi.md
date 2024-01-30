# pyforeman.InstanceHostsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_instance_hosts**](InstanceHostsApi.md#get_instance_hosts) | **GET** /instance_hosts | List hosts forming the Foreman instance
[**put_instance_hosts_host_id**](InstanceHostsApi.md#put_instance_hosts_host_id) | **PUT** /instance_hosts/{host_id} | Assign a host to the Foreman instance


# **get_instance_hosts**
> get_instance_hosts(location_id=location_id, organization_id=organization_id)

List hosts forming the Foreman instance



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InstanceHostsApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List hosts forming the Foreman instance
    api_instance.get_instance_hosts(location_id=location_id, organization_id=organization_id)
except ApiException as e:
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_instance_hosts_host_id**
> put_instance_hosts_host_id(host_id, location_id=location_id, organization_id=organization_id)

Assign a host to the Foreman instance



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.InstanceHostsApi()
host_id = 'host_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Assign a host to the Foreman instance
    api_instance.put_instance_hosts_host_id(host_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
