# pyforeman.ProductsBulkActionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_products_bulk_destroy**](ProductsBulkActionsApi.md#put_products_bulk_destroy) | **PUT** /products/bulk/destroy | Destroy one or more products
[**put_products_bulk_http_proxy**](ProductsBulkActionsApi.md#put_products_bulk_http_proxy) | **PUT** /products/bulk/http_proxy | Update the HTTP proxy configuration on the repositories of one or more products.
[**put_products_bulk_sync**](ProductsBulkActionsApi.md#put_products_bulk_sync) | **PUT** /products/bulk/sync | Sync one or more products
[**put_products_bulk_sync_plan**](ProductsBulkActionsApi.md#put_products_bulk_sync_plan) | **PUT** /products/bulk/sync_plan | Sync one or more products
[**put_products_bulk_verify_checksum**](ProductsBulkActionsApi.md#put_products_bulk_verify_checksum) | **PUT** /products/bulk/verify_checksum | Verify checksum for one or more products


# **put_products_bulk_destroy**
> put_products_bulk_destroy(ids)

Destroy one or more products



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ProductsBulkActionsApi()
ids = ['ids_example'] # list[str] | List of product ids

try:
    # Destroy one or more products
    api_instance.put_products_bulk_destroy(ids)
except ApiException as e:
    print("Exception when calling ProductsBulkActionsApi->put_products_bulk_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of product ids |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_bulk_http_proxy**
> put_products_bulk_http_proxy(ids, http_proxy_policy=http_proxy_policy, http_proxy_id=http_proxy_id)

Update the HTTP proxy configuration on the repositories of one or more products.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ProductsBulkActionsApi()
ids = ['ids_example'] # list[str] | List of product ids
http_proxy_policy = 'http_proxy_policy_example' # str | policy for HTTP proxy for content sync (optional)
http_proxy_id = 8.14 # float | HTTP Proxy identifier to associated (optional)

try:
    # Update the HTTP proxy configuration on the repositories of one or more products.
    api_instance.put_products_bulk_http_proxy(ids, http_proxy_policy=http_proxy_policy, http_proxy_id=http_proxy_id)
except ApiException as e:
    print("Exception when calling ProductsBulkActionsApi->put_products_bulk_http_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of product ids |
 **http_proxy_policy** | **str**| policy for HTTP proxy for content sync | [optional]
 **http_proxy_id** | **float**| HTTP Proxy identifier to associated | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_bulk_sync**
> put_products_bulk_sync(ids, skip_metadata_check=skip_metadata_check, validate_contents=validate_contents)

Sync one or more products



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ProductsBulkActionsApi()
ids = ['ids_example'] # list[str] | List of product ids
skip_metadata_check = true # bool | Force sync even if no upstream changes are detected. Non-yum repositories are skipped. (optional)
validate_contents = true # bool | Force a sync and validate the checksums of all content. Non-yum repositories (or those with                                                      On Demand download policy) are skipped. (optional)

try:
    # Sync one or more products
    api_instance.put_products_bulk_sync(ids, skip_metadata_check=skip_metadata_check, validate_contents=validate_contents)
except ApiException as e:
    print("Exception when calling ProductsBulkActionsApi->put_products_bulk_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of product ids |
 **skip_metadata_check** | **bool**| Force sync even if no upstream changes are detected. Non-yum repositories are skipped. | [optional]
 **validate_contents** | **bool**| Force a sync and validate the checksums of all content. Non-yum repositories (or those with                                                      On Demand download policy) are skipped. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_bulk_sync_plan**
> put_products_bulk_sync_plan(ids, plan_id)

Sync one or more products



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ProductsBulkActionsApi()
ids = ['ids_example'] # list[str] | List of product ids
plan_id = 8.14 # float | Sync plan identifier to attach

try:
    # Sync one or more products
    api_instance.put_products_bulk_sync_plan(ids, plan_id)
except ApiException as e:
    print("Exception when calling ProductsBulkActionsApi->put_products_bulk_sync_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of product ids |
 **plan_id** | **float**| Sync plan identifier to attach |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_bulk_verify_checksum**
> put_products_bulk_verify_checksum(ids)

Verify checksum for one or more products



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ProductsBulkActionsApi()
ids = ['ids_example'] # list[str] | List of product ids

try:
    # Verify checksum for one or more products
    api_instance.put_products_bulk_verify_checksum(ids)
except ApiException as e:
    print("Exception when calling ProductsBulkActionsApi->put_products_bulk_verify_checksum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of product ids |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
