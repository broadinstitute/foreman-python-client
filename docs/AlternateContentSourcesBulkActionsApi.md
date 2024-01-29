# pyforeman.AlternateContentSourcesBulkActionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_alternate_content_sources_bulk_refresh**](AlternateContentSourcesBulkActionsApi.md#post_alternate_content_sources_bulk_refresh) | **POST** /alternate_content_sources/bulk/refresh | Refresh alternate content sources
[**post_alternate_content_sources_bulk_refresh_all**](AlternateContentSourcesBulkActionsApi.md#post_alternate_content_sources_bulk_refresh_all) | **POST** /alternate_content_sources/bulk/refresh_all | Refresh all alternate content sources
[**put_alternate_content_sources_bulk_destroy**](AlternateContentSourcesBulkActionsApi.md#put_alternate_content_sources_bulk_destroy) | **PUT** /alternate_content_sources/bulk/destroy | Destroy one or more alternate content sources


# **post_alternate_content_sources_bulk_refresh**
> post_alternate_content_sources_bulk_refresh(ids)

Refresh alternate content sources



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesBulkActionsApi()
ids = ['ids_example'] # list[str] | List of alternate content source IDs

try:
    # Refresh alternate content sources
    api_instance.post_alternate_content_sources_bulk_refresh(ids)
except ApiException as e:
    print("Exception when calling AlternateContentSourcesBulkActionsApi->post_alternate_content_sources_bulk_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of alternate content source IDs |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_alternate_content_sources_bulk_refresh_all**
> post_alternate_content_sources_bulk_refresh_all()

Refresh all alternate content sources



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesBulkActionsApi()

try:
    # Refresh all alternate content sources
    api_instance.post_alternate_content_sources_bulk_refresh_all()
except ApiException as e:
    print("Exception when calling AlternateContentSourcesBulkActionsApi->post_alternate_content_sources_bulk_refresh_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alternate_content_sources_bulk_destroy**
> put_alternate_content_sources_bulk_destroy(ids)

Destroy one or more alternate content sources



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AlternateContentSourcesBulkActionsApi()
ids = ['ids_example'] # list[str] | List of alternate content source IDs

try:
    # Destroy one or more alternate content sources
    api_instance.put_alternate_content_sources_bulk_destroy(ids)
except ApiException as e:
    print("Exception when calling AlternateContentSourcesBulkActionsApi->put_alternate_content_sources_bulk_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of alternate content source IDs |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
