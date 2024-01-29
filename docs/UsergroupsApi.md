# pyforeman.UsergroupsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_usergroups_id**](UsergroupsApi.md#delete_usergroups_id) | **DELETE** /usergroups/{id} | Delete a user group
[**get_usergroups**](UsergroupsApi.md#get_usergroups) | **GET** /usergroups | List all user groups
[**get_usergroups_id**](UsergroupsApi.md#get_usergroups_id) | **GET** /usergroups/{id} | Show a user group
[**post_usergroups**](UsergroupsApi.md#post_usergroups) | **POST** /usergroups | Create a user group
[**put_usergroups_id**](UsergroupsApi.md#put_usergroups_id) | **PUT** /usergroups/{id} | Update a user group


# **delete_usergroups_id**
> delete_usergroups_id(id, location_id=location_id, organization_id=organization_id)

Delete a user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsergroupsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a user group
    api_instance.delete_usergroups_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling UsergroupsApi->delete_usergroups_id: %s\n" % e)
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

# **get_usergroups**
> get_usergroups(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all user groups



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsergroupsApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all user groups
    api_instance.get_usergroups(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling UsergroupsApi->get_usergroups: %s\n" % e)
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

# **get_usergroups_id**
> get_usergroups_id(id, location_id=location_id, organization_id=organization_id)

Show a user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsergroupsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a user group
    api_instance.get_usergroups_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling UsergroupsApi->get_usergroups_id: %s\n" % e)
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

# **post_usergroups**
> post_usergroups(usergroup_name, location_id=location_id, organization_id=organization_id, usergroup_admin=usergroup_admin, usergroup_user_ids=usergroup_user_ids, usergroup_usergroup_ids=usergroup_usergroup_ids, usergroup_role_ids=usergroup_role_ids)

Create a user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsergroupsApi()
usergroup_name = 'usergroup_name_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
usergroup_admin = true # bool | is an admin user group, can be modified by admins only (optional)
usergroup_user_ids = ['usergroup_user_ids_example'] # list[str] |  (optional)
usergroup_usergroup_ids = ['usergroup_usergroup_ids_example'] # list[str] |  (optional)
usergroup_role_ids = ['usergroup_role_ids_example'] # list[str] |  (optional)

try:
    # Create a user group
    api_instance.post_usergroups(usergroup_name, location_id=location_id, organization_id=organization_id, usergroup_admin=usergroup_admin, usergroup_user_ids=usergroup_user_ids, usergroup_usergroup_ids=usergroup_usergroup_ids, usergroup_role_ids=usergroup_role_ids)
except ApiException as e:
    print("Exception when calling UsergroupsApi->post_usergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_name** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **usergroup_admin** | **bool**| is an admin user group, can be modified by admins only | [optional]
 **usergroup_user_ids** | [**list[str]**](str.md)|  | [optional]
 **usergroup_usergroup_ids** | [**list[str]**](str.md)|  | [optional]
 **usergroup_role_ids** | [**list[str]**](str.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_usergroups_id**
> put_usergroups_id(id, location_id=location_id, organization_id=organization_id, usergroup_name=usergroup_name, usergroup_admin=usergroup_admin, usergroup_user_ids=usergroup_user_ids, usergroup_usergroup_ids=usergroup_usergroup_ids, usergroup_role_ids=usergroup_role_ids)

Update a user group

        User groups linked to external groups (LDAP) are automatically synced         with these groups on update. Remember this synchronization will remove         any LDAP users manually added to the Foreman user group. Only LDAP         users in the external groups will remain. Internal users can be added         or removed freely.

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsergroupsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
usergroup_name = 'usergroup_name_example' # str |  (optional)
usergroup_admin = true # bool | is an admin user group, can be modified by admins only (optional)
usergroup_user_ids = ['usergroup_user_ids_example'] # list[str] |  (optional)
usergroup_usergroup_ids = ['usergroup_usergroup_ids_example'] # list[str] |  (optional)
usergroup_role_ids = ['usergroup_role_ids_example'] # list[str] |  (optional)

try:
    # Update a user group
    api_instance.put_usergroups_id(id, location_id=location_id, organization_id=organization_id, usergroup_name=usergroup_name, usergroup_admin=usergroup_admin, usergroup_user_ids=usergroup_user_ids, usergroup_usergroup_ids=usergroup_usergroup_ids, usergroup_role_ids=usergroup_role_ids)
except ApiException as e:
    print("Exception when calling UsergroupsApi->put_usergroups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **usergroup_name** | **str**|  | [optional]
 **usergroup_admin** | **bool**| is an admin user group, can be modified by admins only | [optional]
 **usergroup_user_ids** | [**list[str]**](str.md)|  | [optional]
 **usergroup_usergroup_ids** | [**list[str]**](str.md)|  | [optional]
 **usergroup_role_ids** | [**list[str]**](str.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
