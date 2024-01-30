# pyforeman.UsersApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_id**](UsersApi.md#delete_users_id) | **DELETE** /users/{id} | Delete a user
[**get_auth_source_externals_auth_source_external_id_users**](UsersApi.md#get_auth_source_externals_auth_source_external_id_users) | **GET** /auth_source_externals/{auth_source_external_id}/users | List all users for external authentication source
[**get_auth_source_ldaps_auth_source_ldap_id_users**](UsersApi.md#get_auth_source_ldaps_auth_source_ldap_id_users) | **GET** /auth_source_ldaps/{auth_source_ldap_id}/users | List all users for LDAP authentication source
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /current_user | Show the currently logged-in user
[**get_locations_location_id_users**](UsersApi.md#get_locations_location_id_users) | **GET** /locations/{location_id}/users | List all users for location
[**get_organizations_organization_id_users**](UsersApi.md#get_organizations_organization_id_users) | **GET** /organizations/{organization_id}/users | List all users for organization
[**get_roles_role_id_users**](UsersApi.md#get_roles_role_id_users) | **GET** /roles/{role_id}/users | List all users for role
[**get_usergroups_usergroup_id_users**](UsersApi.md#get_usergroups_usergroup_id_users) | **GET** /usergroups/{usergroup_id}/users | List all users for user group
[**get_users**](UsersApi.md#get_users) | **GET** /users | List all users
[**get_users_extlogin**](UsersApi.md#get_users_extlogin) | **GET** /users/extlogin | Use to authenticate against external authentication source
[**get_users_id**](UsersApi.md#get_users_id) | **GET** /users/{id} | Show a user
[**post_users**](UsersApi.md#post_users) | **POST** /users | Create a user
[**put_users_id**](UsersApi.md#put_users_id) | **PUT** /users/{id} | Update a user


# **delete_users_id**
> delete_users_id(id, location_id=location_id, organization_id=organization_id)

Delete a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a user
    api_instance.delete_users_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_users_id: %s\n" % e)
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

# **get_auth_source_externals_auth_source_external_id_users**
> get_auth_source_externals_auth_source_external_id_users(auth_source_external_id, auth_source_ldap_id, usergroup_id, role_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all users for external authentication source



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
auth_source_external_id = 8.14 # float |
auth_source_ldap_id = 'auth_source_ldap_id_example' # str | ID of LDAP authentication source
usergroup_id = 'usergroup_id_example' # str | ID of user group
role_id = 'role_id_example' # str | ID of role
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all users for external authentication source
    api_instance.get_auth_source_externals_auth_source_external_id_users(auth_source_external_id, auth_source_ldap_id, usergroup_id, role_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling UsersApi->get_auth_source_externals_auth_source_external_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_source_external_id** | **float**|  |
 **auth_source_ldap_id** | **str**| ID of LDAP authentication source |
 **usergroup_id** | **str**| ID of user group |
 **role_id** | **str**| ID of role |
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

# **get_auth_source_ldaps_auth_source_ldap_id_users**
> get_auth_source_ldaps_auth_source_ldap_id_users(auth_source_ldap_id, usergroup_id, role_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all users for LDAP authentication source



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
auth_source_ldap_id = 'auth_source_ldap_id_example' # str | ID of LDAP authentication source
usergroup_id = 'usergroup_id_example' # str | ID of user group
role_id = 'role_id_example' # str | ID of role
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all users for LDAP authentication source
    api_instance.get_auth_source_ldaps_auth_source_ldap_id_users(auth_source_ldap_id, usergroup_id, role_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling UsersApi->get_auth_source_ldaps_auth_source_ldap_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_source_ldap_id** | **str**| ID of LDAP authentication source |
 **usergroup_id** | **str**| ID of user group |
 **role_id** | **str**| ID of role |
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

# **get_current_user**
> get_current_user(location_id=location_id, organization_id=organization_id)

Show the currently logged-in user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show the currently logged-in user
    api_instance.get_current_user(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_locations_location_id_users**
> get_locations_location_id_users(location_id, auth_source_ldap_id, usergroup_id, role_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all users for location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
location_id = 8.14 # float | Scope by locations
auth_source_ldap_id = 'auth_source_ldap_id_example' # str | ID of LDAP authentication source
usergroup_id = 'usergroup_id_example' # str | ID of user group
role_id = 'role_id_example' # str | ID of role
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all users for location
    api_instance.get_locations_location_id_users(location_id, auth_source_ldap_id, usergroup_id, role_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling UsersApi->get_locations_location_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations |
 **auth_source_ldap_id** | **str**| ID of LDAP authentication source |
 **usergroup_id** | **str**| ID of user group |
 **role_id** | **str**| ID of role |
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

# **get_organizations_organization_id_users**
> get_organizations_organization_id_users(organization_id, auth_source_ldap_id, usergroup_id, role_id, location_id, search=search, order=order, page=page, per_page=per_page)

List all users for organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
organization_id = 8.14 # float | Scope by organizations
auth_source_ldap_id = 'auth_source_ldap_id_example' # str | ID of LDAP authentication source
usergroup_id = 'usergroup_id_example' # str | ID of user group
role_id = 'role_id_example' # str | ID of role
location_id = 8.14 # float | Scope by locations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all users for organization
    api_instance.get_organizations_organization_id_users(organization_id, auth_source_ldap_id, usergroup_id, role_id, location_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling UsersApi->get_organizations_organization_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations |
 **auth_source_ldap_id** | **str**| ID of LDAP authentication source |
 **usergroup_id** | **str**| ID of user group |
 **role_id** | **str**| ID of role |
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

# **get_roles_role_id_users**
> get_roles_role_id_users(role_id, auth_source_ldap_id, usergroup_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all users for role



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
role_id = 'role_id_example' # str | ID of role
auth_source_ldap_id = 'auth_source_ldap_id_example' # str | ID of LDAP authentication source
usergroup_id = 'usergroup_id_example' # str | ID of user group
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all users for role
    api_instance.get_roles_role_id_users(role_id, auth_source_ldap_id, usergroup_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling UsersApi->get_roles_role_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| ID of role |
 **auth_source_ldap_id** | **str**| ID of LDAP authentication source |
 **usergroup_id** | **str**| ID of user group |
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

# **get_usergroups_usergroup_id_users**
> get_usergroups_usergroup_id_users(usergroup_id, auth_source_ldap_id, role_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all users for user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
usergroup_id = 'usergroup_id_example' # str | ID of user group
auth_source_ldap_id = 'auth_source_ldap_id_example' # str | ID of LDAP authentication source
role_id = 'role_id_example' # str | ID of role
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all users for user group
    api_instance.get_usergroups_usergroup_id_users(usergroup_id, auth_source_ldap_id, role_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling UsersApi->get_usergroups_usergroup_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_id** | **str**| ID of user group |
 **auth_source_ldap_id** | **str**| ID of LDAP authentication source |
 **role_id** | **str**| ID of role |
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

# **get_users**
> get_users(auth_source_ldap_id, usergroup_id, role_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all users



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
auth_source_ldap_id = 'auth_source_ldap_id_example' # str | ID of LDAP authentication source
usergroup_id = 'usergroup_id_example' # str | ID of user group
role_id = 'role_id_example' # str | ID of role
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all users
    api_instance.get_users(auth_source_ldap_id, usergroup_id, role_id, location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_source_ldap_id** | **str**| ID of LDAP authentication source |
 **usergroup_id** | **str**| ID of user group |
 **role_id** | **str**| ID of role |
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

# **get_users_extlogin**
> get_users_extlogin(location_id=location_id, organization_id=organization_id)

Use to authenticate against external authentication source



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Use to authenticate against external authentication source
    api_instance.get_users_extlogin(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_extlogin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_users_id**
> get_users_id(id, location_id=location_id, organization_id=organization_id)

Show a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a user
    api_instance.get_users_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_id: %s\n" % e)
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

# **post_users**
> post_users(user_login, user_mail, user_auth_source_id, location_id=location_id, organization_id=organization_id, user_firstname=user_firstname, user_lastname=user_lastname, user_description=user_description, user_disabled=user_disabled, user_admin=user_admin, user_password=user_password, user_default_location_id=user_default_location_id, user_default_organization_id=user_default_organization_id, user_timezone=user_timezone, user_locale=user_locale, user_role_ids=user_role_ids, user_mail_enabled=user_mail_enabled, user_location_ids=user_location_ids, user_organization_ids=user_organization_ids)

Create a user

        Adds role 'Default role' to the user by default

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
user_login = 'user_login_example' # str |
user_mail = 'user_mail_example' # str |
user_auth_source_id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
user_firstname = 'user_firstname_example' # str |  (optional)
user_lastname = 'user_lastname_example' # str |  (optional)
user_description = 'user_description_example' # str |  (optional)
user_disabled = true # bool |  (optional)
user_admin = true # bool | is an admin account (optional)
user_password = 'user_password_example' # str | Required unless user is in an external authentication source (optional)
user_default_location_id = 8.14 # float |  (optional)
user_default_organization_id = 8.14 # float |  (optional)
user_timezone = 'user_timezone_example' # str | User's timezone (optional)
user_locale = 'user_locale_example' # str | User's preferred locale (optional)
user_role_ids = ['user_role_ids_example'] # list[str] |  (optional)
user_mail_enabled = true # bool | Enable user's email (optional)
user_location_ids = ['user_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
user_organization_ids = ['user_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Create a user
    api_instance.post_users(user_login, user_mail, user_auth_source_id, location_id=location_id, organization_id=organization_id, user_firstname=user_firstname, user_lastname=user_lastname, user_description=user_description, user_disabled=user_disabled, user_admin=user_admin, user_password=user_password, user_default_location_id=user_default_location_id, user_default_organization_id=user_default_organization_id, user_timezone=user_timezone, user_locale=user_locale, user_role_ids=user_role_ids, user_mail_enabled=user_mail_enabled, user_location_ids=user_location_ids, user_organization_ids=user_organization_ids)
except ApiException as e:
    print("Exception when calling UsersApi->post_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_login** | **str**|  |
 **user_mail** | **str**|  |
 **user_auth_source_id** | **float**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **user_firstname** | **str**|  | [optional]
 **user_lastname** | **str**|  | [optional]
 **user_description** | **str**|  | [optional]
 **user_disabled** | **bool**|  | [optional]
 **user_admin** | **bool**| is an admin account | [optional]
 **user_password** | **str**| Required unless user is in an external authentication source | [optional]
 **user_default_location_id** | **float**|  | [optional]
 **user_default_organization_id** | **float**|  | [optional]
 **user_timezone** | **str**| User&#39;s timezone | [optional]
 **user_locale** | **str**| User&#39;s preferred locale | [optional]
 **user_role_ids** | [**list[str]**](str.md)|  | [optional]
 **user_mail_enabled** | **bool**| Enable user&#39;s email | [optional]
 **user_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **user_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_users_id**
> put_users_id(id, location_id=location_id, organization_id=organization_id, user_login=user_login, user_firstname=user_firstname, user_lastname=user_lastname, user_mail=user_mail, user_description=user_description, user_disabled=user_disabled, user_admin=user_admin, user_password=user_password, user_default_location_id=user_default_location_id, user_default_organization_id=user_default_organization_id, user_auth_source_id=user_auth_source_id, user_timezone=user_timezone, user_locale=user_locale, user_role_ids=user_role_ids, user_mail_enabled=user_mail_enabled, user_location_ids=user_location_ids, user_organization_ids=user_organization_ids, user_current_password=user_current_password)

Update a user

        Adds role 'Default role' to the user if it is not already present.         Only another admin can change the admin account attribute.

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UsersApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
user_login = 'user_login_example' # str |  (optional)
user_firstname = 'user_firstname_example' # str |  (optional)
user_lastname = 'user_lastname_example' # str |  (optional)
user_mail = 'user_mail_example' # str |  (optional)
user_description = 'user_description_example' # str |  (optional)
user_disabled = true # bool |  (optional)
user_admin = true # bool | is an admin account (optional)
user_password = 'user_password_example' # str | Required unless user is in an external authentication source (optional)
user_default_location_id = 8.14 # float |  (optional)
user_default_organization_id = 8.14 # float |  (optional)
user_auth_source_id = 8.14 # float |  (optional)
user_timezone = 'user_timezone_example' # str | User's timezone (optional)
user_locale = 'user_locale_example' # str | User's preferred locale (optional)
user_role_ids = ['user_role_ids_example'] # list[str] |  (optional)
user_mail_enabled = true # bool | Enable user's email (optional)
user_location_ids = ['user_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
user_organization_ids = ['user_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)
user_current_password = 'user_current_password_example' # str | Required when user want to change own password (optional)

try:
    # Update a user
    api_instance.put_users_id(id, location_id=location_id, organization_id=organization_id, user_login=user_login, user_firstname=user_firstname, user_lastname=user_lastname, user_mail=user_mail, user_description=user_description, user_disabled=user_disabled, user_admin=user_admin, user_password=user_password, user_default_location_id=user_default_location_id, user_default_organization_id=user_default_organization_id, user_auth_source_id=user_auth_source_id, user_timezone=user_timezone, user_locale=user_locale, user_role_ids=user_role_ids, user_mail_enabled=user_mail_enabled, user_location_ids=user_location_ids, user_organization_ids=user_organization_ids, user_current_password=user_current_password)
except ApiException as e:
    print("Exception when calling UsersApi->put_users_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **user_login** | **str**|  | [optional]
 **user_firstname** | **str**|  | [optional]
 **user_lastname** | **str**|  | [optional]
 **user_mail** | **str**|  | [optional]
 **user_description** | **str**|  | [optional]
 **user_disabled** | **bool**|  | [optional]
 **user_admin** | **bool**| is an admin account | [optional]
 **user_password** | **str**| Required unless user is in an external authentication source | [optional]
 **user_default_location_id** | **float**|  | [optional]
 **user_default_organization_id** | **float**|  | [optional]
 **user_auth_source_id** | **float**|  | [optional]
 **user_timezone** | **str**| User&#39;s timezone | [optional]
 **user_locale** | **str**| User&#39;s preferred locale | [optional]
 **user_role_ids** | [**list[str]**](str.md)|  | [optional]
 **user_mail_enabled** | **bool**| Enable user&#39;s email | [optional]
 **user_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **user_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]
 **user_current_password** | **str**| Required when user want to change own password | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
