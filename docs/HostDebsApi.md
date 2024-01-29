# foreman.HostDebsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hosts_host_id_debs**](HostDebsApi.md#get_hosts_host_id_debs) | **GET** /hosts/{host_id}/debs | List deb packages installed on the host


# **get_hosts_host_id_debs**
> get_hosts_host_id_debs(host_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List deb packages installed on the host

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
    api_instance = foreman.HostDebsApi(api_client)
    host_id = 3.4 # float | ID of the host
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List deb packages installed on the host
        api_instance.get_hosts_host_id_debs(host_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling HostDebsApi->get_hosts_host_id_debs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| ID of the host | 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 

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

