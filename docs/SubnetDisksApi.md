# foreman.SubnetDisksApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bootdisk_subnets_subnet_id**](SubnetDisksApi.md#get_bootdisk_subnets_subnet_id) | **GET** /bootdisk/subnets/{subnet_id} | Download subnet generic image


# **get_bootdisk_subnets_subnet_id**
> get_bootdisk_subnets_subnet_id(subnet_id, location_id=location_id, organization_id=organization_id)

Download subnet generic image

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
    api_instance = foreman.SubnetDisksApi(api_client)
    subnet_id = 'subnet_id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Download subnet generic image
        api_instance.get_bootdisk_subnets_subnet_id(subnet_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

