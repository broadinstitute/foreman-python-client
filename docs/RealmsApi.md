# pyforeman.RealmsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_realms_id**](RealmsApi.md#delete_realms_id) | **DELETE** /realms/{id} | Delete a realm
[**get_realms**](RealmsApi.md#get_realms) | **GET** /realms | List of realms
[**get_realms_id**](RealmsApi.md#get_realms_id) | **GET** /realms/{id} | Show a realm
[**post_realms**](RealmsApi.md#post_realms) | **POST** /realms | Create a realm
[**put_realms_id**](RealmsApi.md#put_realms_id) | **PUT** /realms/{id} | Update a realm


# **delete_realms_id**
> delete_realms_id(id, location_id=location_id, organization_id=organization_id)

Delete a realm



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RealmsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a realm
    api_instance.delete_realms_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RealmsApi->delete_realms_id: %s\n" % e)
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

# **get_realms**
> get_realms(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of realms



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RealmsApi()
location_id = 8.14 # float | Scope by locations (optional)
organization_id = 8.14 # float | Scope by organizations (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of realms
    api_instance.get_realms(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling RealmsApi->get_realms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations | [optional]
 **organization_id** | **float**| Scope by organizations | [optional]
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

# **get_realms_id**
> get_realms_id(id, location_id=location_id, organization_id=organization_id)

Show a realm



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RealmsApi()
id = 'id_example' # str | Numerical ID or realm name
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a realm
    api_instance.get_realms_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RealmsApi->get_realms_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Numerical ID or realm name |
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

# **post_realms**
> post_realms(realm_name, realm_realm_proxy_id, realm_realm_type, location_id=location_id, organization_id=organization_id, realm_location_ids=realm_location_ids, realm_organization_ids=realm_organization_ids)

Create a realm

        The <b>name</b> field is used for the name of the realm.

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RealmsApi()
realm_name = 'realm_name_example' # str | The realm name, e.g. EXAMPLE.COM
realm_realm_proxy_id = 8.14 # float | Proxy ID to use within this realm
realm_realm_type = 'realm_realm_type_example' # str | Realm type, e.g. FreeIPA or Active Directory
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
realm_location_ids = ['realm_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
realm_organization_ids = ['realm_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Create a realm
    api_instance.post_realms(realm_name, realm_realm_proxy_id, realm_realm_type, location_id=location_id, organization_id=organization_id, realm_location_ids=realm_location_ids, realm_organization_ids=realm_organization_ids)
except ApiException as e:
    print("Exception when calling RealmsApi->post_realms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm_name** | **str**| The realm name, e.g. EXAMPLE.COM |
 **realm_realm_proxy_id** | **float**| Proxy ID to use within this realm |
 **realm_realm_type** | **str**| Realm type, e.g. FreeIPA or Active Directory |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **realm_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **realm_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_realms_id**
> put_realms_id(id, location_id=location_id, organization_id=organization_id, realm_name=realm_name, realm_realm_proxy_id=realm_realm_proxy_id, realm_realm_type=realm_realm_type, realm_location_ids=realm_location_ids, realm_organization_ids=realm_organization_ids)

Update a realm



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RealmsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
realm_name = 'realm_name_example' # str | The realm name, e.g. EXAMPLE.COM (optional)
realm_realm_proxy_id = 8.14 # float | Proxy ID to use within this realm (optional)
realm_realm_type = 'realm_realm_type_example' # str | Realm type, e.g. FreeIPA or Active Directory (optional)
realm_location_ids = ['realm_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
realm_organization_ids = ['realm_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Update a realm
    api_instance.put_realms_id(id, location_id=location_id, organization_id=organization_id, realm_name=realm_name, realm_realm_proxy_id=realm_realm_proxy_id, realm_realm_type=realm_realm_type, realm_location_ids=realm_location_ids, realm_organization_ids=realm_organization_ids)
except ApiException as e:
    print("Exception when calling RealmsApi->put_realms_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **realm_name** | **str**| The realm name, e.g. EXAMPLE.COM | [optional]
 **realm_realm_proxy_id** | **float**| Proxy ID to use within this realm | [optional]
 **realm_realm_type** | **str**| Realm type, e.g. FreeIPA or Active Directory | [optional]
 **realm_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **realm_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
