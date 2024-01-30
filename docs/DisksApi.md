# pyforeman.DisksApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bootdisk**](DisksApi.md#get_bootdisk) | **GET** /bootdisk | Boot disks
[**get_bootdisk_generic**](DisksApi.md#get_bootdisk_generic) | **GET** /bootdisk/generic | Download generic image
[**get_bootdisk_hosts_host_id**](DisksApi.md#get_bootdisk_hosts_host_id) | **GET** /bootdisk/hosts/{host_id} | Download host image


# **get_bootdisk**
> get_bootdisk(location_id=location_id, organization_id=organization_id)

Boot disks



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DisksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Boot disks
    api_instance.get_bootdisk(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling DisksApi->get_bootdisk: %s\n" % e)
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

# **get_bootdisk_generic**
> get_bootdisk_generic(location_id=location_id, organization_id=organization_id)

Download generic image



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DisksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Download generic image
    api_instance.get_bootdisk_generic(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling DisksApi->get_bootdisk_generic: %s\n" % e)
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

# **get_bootdisk_hosts_host_id**
> get_bootdisk_hosts_host_id(host_id, location_id=location_id, organization_id=organization_id, full=full)

Download host image



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.DisksApi()
host_id = 'host_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
full = true # bool | True for full, false for basic reusable image (optional)

try:
    # Download host image
    api_instance.get_bootdisk_hosts_host_id(host_id, location_id=location_id, organization_id=organization_id, full=full)
except ApiException as e:
    print("Exception when calling DisksApi->get_bootdisk_hosts_host_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **full** | **bool**| True for full, false for basic reusable image | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
