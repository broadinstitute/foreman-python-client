# pyforeman.SubnetDisksApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bootdisk_subnets_subnet_id**](SubnetDisksApi.md#get_bootdisk_subnets_subnet_id) | **GET** /bootdisk/subnets/{subnet_id} | Download subnet generic image


# **get_bootdisk_subnets_subnet_id**
> get_bootdisk_subnets_subnet_id(subnet_id, location_id=location_id, organization_id=organization_id)

Download subnet generic image



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubnetDisksApi()
subnet_id = 'subnet_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Download subnet generic image
    api_instance.get_bootdisk_subnets_subnet_id(subnet_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling SubnetDisksApi->get_bootdisk_subnets_subnet_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnet_id** | **str**|  |
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
