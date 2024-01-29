# pyforeman.RecurringLogicsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recurring_logics**](RecurringLogicsApi.md#get_recurring_logics) | **GET** /recurring_logics | List recurring logics
[**get_recurring_logics_id**](RecurringLogicsApi.md#get_recurring_logics_id) | **GET** /recurring_logics/{id} | Show recurring logic details
[**post_recurring_logics_bulk_destroy**](RecurringLogicsApi.md#post_recurring_logics_bulk_destroy) | **POST** /recurring_logics/bulk_destroy | Delete recurring logics by search query
[**post_recurring_logics_id_cancel**](RecurringLogicsApi.md#post_recurring_logics_id_cancel) | **POST** /recurring_logics/{id}/cancel | Cancel recurring logic
[**put_recurring_logics_id**](RecurringLogicsApi.md#put_recurring_logics_id) | **PUT** /recurring_logics/{id} | Update recurring logic


# **get_recurring_logics**
> get_recurring_logics(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List recurring logics



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RecurringLogicsApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List recurring logics
    api_instance.get_recurring_logics(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling RecurringLogicsApi->get_recurring_logics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **search** | **str**| filter results | [optional]
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recurring_logics_id**
> get_recurring_logics_id(id, location_id=location_id, organization_id=organization_id)

Show recurring logic details



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RecurringLogicsApi()
id = 'id_example' # str | ID of the recurring logic
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show recurring logic details
    api_instance.get_recurring_logics_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RecurringLogicsApi->get_recurring_logics_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the recurring logic |
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

# **post_recurring_logics_bulk_destroy**
> post_recurring_logics_bulk_destroy(search, location_id=location_id, organization_id=organization_id)

Delete recurring logics by search query



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RecurringLogicsApi()
search = 'search_example' # str | Search query
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete recurring logics by search query
    api_instance.post_recurring_logics_bulk_destroy(search, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RecurringLogicsApi->post_recurring_logics_bulk_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query |
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

# **post_recurring_logics_id_cancel**
> post_recurring_logics_id_cancel(id, location_id=location_id, organization_id=organization_id)

Cancel recurring logic



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RecurringLogicsApi()
id = 'id_example' # str | ID of the recurring logic
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Cancel recurring logic
    api_instance.post_recurring_logics_id_cancel(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RecurringLogicsApi->post_recurring_logics_id_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the recurring logic |
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

# **put_recurring_logics_id**
> put_recurring_logics_id(id, location_id=location_id, organization_id=organization_id, enabled=enabled)

Update recurring logic



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RecurringLogicsApi()
id = 'id_example' # str | ID of the recurring logic
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
enabled = true # bool | Whether the recurring logic is enabled or disabled. (optional)

try:
    # Update recurring logic
    api_instance.put_recurring_logics_id(id, location_id=location_id, organization_id=organization_id, enabled=enabled)
except ApiException as e:
    print("Exception when calling RecurringLogicsApi->put_recurring_logics_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the recurring logic |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **enabled** | **bool**| Whether the recurring logic is enabled or disabled. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
