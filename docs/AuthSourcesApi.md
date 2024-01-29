# pyforeman.AuthSourcesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_sources**](AuthSourcesApi.md#get_auth_sources) | **GET** /auth_sources | List all authentication sources
[**get_locations_location_id_auth_sources**](AuthSourcesApi.md#get_locations_location_id_auth_sources) | **GET** /locations/{location_id}/auth_sources | List all authentication sources per location
[**get_organizations_organization_id_auth_sources**](AuthSourcesApi.md#get_organizations_organization_id_auth_sources) | **GET** /organizations/{organization_id}/auth_sources | List all authentication sources per organization


# **get_auth_sources**
> get_auth_sources(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all authentication sources



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AuthSourcesApi()
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all authentication sources
    api_instance.get_auth_sources(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling AuthSourcesApi->get_auth_sources: %s\n" % e)
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

# **get_locations_location_id_auth_sources**
> get_locations_location_id_auth_sources(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all authentication sources per location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AuthSourcesApi()
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all authentication sources per location
    api_instance.get_locations_location_id_auth_sources(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling AuthSourcesApi->get_locations_location_id_auth_sources: %s\n" % e)
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

# **get_organizations_organization_id_auth_sources**
> get_organizations_organization_id_auth_sources(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)

List all authentication sources per organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.AuthSourcesApi()
organization_id = 8.14 # float | Scope by organizations
location_id = 8.14 # float | Scope by locations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all authentication sources per organization
    api_instance.get_organizations_organization_id_auth_sources(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling AuthSourcesApi->get_organizations_organization_id_auth_sources: %s\n" % e)
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
