# pyforeman.AutosignApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_smart_proxies_smart_proxy_id_autosign_id**](AutosignApi.md#delete_smart_proxies_smart_proxy_id_autosign_id) | **DELETE** /smart_proxies/{smart_proxy_id}/autosign/{id} | Delete autosign entry
[**get_smart_proxies_smart_proxy_id_autosign**](AutosignApi.md#get_smart_proxies_smart_proxy_id_autosign) | **GET** /smart_proxies/{smart_proxy_id}/autosign | List all autosign entries
[**post_smart_proxies_smart_proxy_id_autosign**](AutosignApi.md#post_smart_proxies_smart_proxy_id_autosign) | **POST** /smart_proxies/{smart_proxy_id}/autosign | Create autosign entry


# **delete_smart_proxies_smart_proxy_id_autosign_id**
> delete_smart_proxies_smart_proxy_id_autosign_id(id, smart_proxy_id, location_id=location_id, organization_id=organization_id)

Delete autosign entry



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AutosignApi()
id = 'id_example' # str | Autosign entry name
smart_proxy_id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete autosign entry
    api_instance.delete_smart_proxies_smart_proxy_id_autosign_id(id, smart_proxy_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling AutosignApi->delete_smart_proxies_smart_proxy_id_autosign_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autosign entry name |
 **smart_proxy_id** | **float**|  |
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

# **get_smart_proxies_smart_proxy_id_autosign**
> get_smart_proxies_smart_proxy_id_autosign(smart_proxy_id, location_id=location_id, organization_id=organization_id)

List all autosign entries



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AutosignApi()
smart_proxy_id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List all autosign entries
    api_instance.get_smart_proxies_smart_proxy_id_autosign(smart_proxy_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling AutosignApi->get_smart_proxies_smart_proxy_id_autosign: %s\n" % e)
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_smart_proxies_smart_proxy_id_autosign**
> post_smart_proxies_smart_proxy_id_autosign(smart_proxy_id, id, location_id=location_id, organization_id=organization_id)

Create autosign entry



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AutosignApi()
smart_proxy_id = 8.14 # float |
id = 'id_example' # str | Autosign entry name
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Create autosign entry
    api_instance.post_smart_proxies_smart_proxy_id_autosign(smart_proxy_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling AutosignApi->post_smart_proxies_smart_proxy_id_autosign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_proxy_id** | **float**|  |
 **id** | **str**| Autosign entry name |
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
