# foreman.SmartProxyHostsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_smart_proxies_smart_proxy_id_hosts_host_id**](SmartProxyHostsApi.md#delete_smart_proxies_smart_proxy_id_hosts_host_id) | **DELETE** /smart_proxies/{smart_proxy_id}/hosts/{host_id} | Unassign a given host from the smart proxy
[**get_smart_proxies_smart_proxy_id_hosts**](SmartProxyHostsApi.md#get_smart_proxies_smart_proxy_id_hosts) | **GET** /smart_proxies/{smart_proxy_id}/hosts | Get hosts forming the smart proxy
[**put_smart_proxies_smart_proxy_id_hosts_host_id**](SmartProxyHostsApi.md#put_smart_proxies_smart_proxy_id_hosts_host_id) | **PUT** /smart_proxies/{smart_proxy_id}/hosts/{host_id} | Assign a host to the smart proxy


# **delete_smart_proxies_smart_proxy_id_hosts_host_id**
> delete_smart_proxies_smart_proxy_id_hosts_host_id(smart_proxy_id, host_id, location_id=location_id, organization_id=organization_id)

Unassign a given host from the smart proxy

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
    api_instance = foreman.SmartProxyHostsApi(api_client)
    smart_proxy_id = 3.4 # float | 
    host_id = 3.4 # float | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Unassign a given host from the smart proxy
        api_instance.delete_smart_proxies_smart_proxy_id_hosts_host_id(smart_proxy_id, host_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling SmartProxyHostsApi->delete_smart_proxies_smart_proxy_id_hosts_host_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_proxy_id** | **float**|  | 
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

# **get_smart_proxies_smart_proxy_id_hosts**
> get_smart_proxies_smart_proxy_id_hosts(smart_proxy_id, location_id=location_id, organization_id=organization_id)

Get hosts forming the smart proxy

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
    api_instance = foreman.SmartProxyHostsApi(api_client)
    smart_proxy_id = 3.4 # float | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Get hosts forming the smart proxy
        api_instance.get_smart_proxies_smart_proxy_id_hosts(smart_proxy_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling SmartProxyHostsApi->get_smart_proxies_smart_proxy_id_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_proxy_id** | **float**|  | 
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

# **put_smart_proxies_smart_proxy_id_hosts_host_id**
> put_smart_proxies_smart_proxy_id_hosts_host_id(smart_proxy_id, host_id, location_id=location_id, organization_id=organization_id)

Assign a host to the smart proxy

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
    api_instance = foreman.SmartProxyHostsApi(api_client)
    smart_proxy_id = 'smart_proxy_id_example' # str | 
    host_id = 'host_id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Assign a host to the smart proxy
        api_instance.put_smart_proxies_smart_proxy_id_hosts_host_id(smart_proxy_id, host_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling SmartProxyHostsApi->put_smart_proxies_smart_proxy_id_hosts_host_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_proxy_id** | **str**|  | 
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

