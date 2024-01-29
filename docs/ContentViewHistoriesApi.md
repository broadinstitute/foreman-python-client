# pyforeman.ContentViewHistoriesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_views_id_history**](ContentViewHistoriesApi.md#get_content_views_id_history) | **GET** /content_views/{id}/history | Show a content view&#39;s history


# **get_content_views_id_history**
> get_content_views_id_history(id)

Show a content view's history



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewHistoriesApi()
id = 8.14 # float | content view numeric identifier

try:
    # Show a content view's history
    api_instance.get_content_views_id_history(id)
except ApiException as e:
    print("Exception when calling ContentViewHistoriesApi->get_content_views_id_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| content view numeric identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
