# pyforeman.AuthSourceExternalsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_source_externals**](AuthSourceExternalsApi.md#get_auth_source_externals) | **GET** /auth_source_externals | List external authentication sources
[**get_auth_source_externals_id**](AuthSourceExternalsApi.md#get_auth_source_externals_id) | **GET** /auth_source_externals/{id} | Show an external authentication source
[**get_locations_location_id_auth_source_externals**](AuthSourceExternalsApi.md#get_locations_location_id_auth_source_externals) | **GET** /locations/{location_id}/auth_source_externals | List external authentication sources per location
[**get_organizations_organization_id_auth_source_externals**](AuthSourceExternalsApi.md#get_organizations_organization_id_auth_source_externals) | **GET** /organizations/{organization_id}/auth_source_externals | List external authentication sources per organization
[**put_auth_source_externals_id**](AuthSourceExternalsApi.md#put_auth_source_externals_id) | **PUT** /auth_source_externals/{id} | Update an external authentication source


# **get_auth_source_externals**
> get_auth_source_externals(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List external authentication sources



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AuthSourceExternalsApi()
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List external authentication sources
    api_instance.get_auth_source_externals(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling AuthSourceExternalsApi->get_auth_source_externals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations |
 **organization_id** | **float**| Scope by organizations |
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

# **get_auth_source_externals_id**
> get_auth_source_externals_id(id, location_id=location_id, organization_id=organization_id)

Show an external authentication source



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AuthSourceExternalsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show an external authentication source
    api_instance.get_auth_source_externals_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling AuthSourceExternalsApi->get_auth_source_externals_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_locations_location_id_auth_source_externals**
> get_locations_location_id_auth_source_externals(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List external authentication sources per location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AuthSourceExternalsApi()
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List external authentication sources per location
    api_instance.get_locations_location_id_auth_source_externals(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling AuthSourceExternalsApi->get_locations_location_id_auth_source_externals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations |
 **organization_id** | **float**| Scope by organizations |
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

# **get_organizations_organization_id_auth_source_externals**
> get_organizations_organization_id_auth_source_externals(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)

List external authentication sources per organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AuthSourceExternalsApi()
organization_id = 8.14 # float | Scope by organizations
location_id = 8.14 # float | Scope by locations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List external authentication sources per organization
    api_instance.get_organizations_organization_id_auth_source_externals(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling AuthSourceExternalsApi->get_organizations_organization_id_auth_source_externals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations |
 **location_id** | **float**| Scope by locations |
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

# **put_auth_source_externals_id**
> put_auth_source_externals_id(id, location_id=location_id, organization_id=organization_id, auth_source_external_name=auth_source_external_name, auth_source_external_location_ids=auth_source_external_location_ids, auth_source_external_organization_ids=auth_source_external_organization_ids)

Update an external authentication source



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AuthSourceExternalsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
auth_source_external_name = 'auth_source_external_name_example' # str |  (optional)
auth_source_external_location_ids = ['auth_source_external_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
auth_source_external_organization_ids = ['auth_source_external_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Update an external authentication source
    api_instance.put_auth_source_externals_id(id, location_id=location_id, organization_id=organization_id, auth_source_external_name=auth_source_external_name, auth_source_external_location_ids=auth_source_external_location_ids, auth_source_external_organization_ids=auth_source_external_organization_ids)
except ApiException as e:
    print("Exception when calling AuthSourceExternalsApi->put_auth_source_externals_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **auth_source_external_name** | **str**|  | [optional]
 **auth_source_external_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **auth_source_external_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
