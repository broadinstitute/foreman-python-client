# foreman.AuthSourceLdapsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_auth_source_ldaps_id**](AuthSourceLdapsApi.md#delete_auth_source_ldaps_id) | **DELETE** /auth_source_ldaps/{id} | Delete an LDAP authentication source
[**get_auth_source_ldaps**](AuthSourceLdapsApi.md#get_auth_source_ldaps) | **GET** /auth_source_ldaps | List all LDAP authentication sources
[**get_auth_source_ldaps_id**](AuthSourceLdapsApi.md#get_auth_source_ldaps_id) | **GET** /auth_source_ldaps/{id} | Show an LDAP authentication source
[**get_locations_location_id_auth_source_ldaps**](AuthSourceLdapsApi.md#get_locations_location_id_auth_source_ldaps) | **GET** /locations/{location_id}/auth_source_ldaps | List LDAP authentication sources per location
[**get_organizations_organization_id_auth_source_ldaps**](AuthSourceLdapsApi.md#get_organizations_organization_id_auth_source_ldaps) | **GET** /organizations/{organization_id}/auth_source_ldaps | List LDAP authentication sources per organization
[**post_auth_source_ldaps**](AuthSourceLdapsApi.md#post_auth_source_ldaps) | **POST** /auth_source_ldaps | Create an LDAP authentication source
[**put_auth_source_ldaps_id**](AuthSourceLdapsApi.md#put_auth_source_ldaps_id) | **PUT** /auth_source_ldaps/{id} | Update an LDAP authentication source
[**put_auth_source_ldaps_id_test**](AuthSourceLdapsApi.md#put_auth_source_ldaps_id_test) | **PUT** /auth_source_ldaps/{id}/test | Test LDAP connection


# **delete_auth_source_ldaps_id**
> delete_auth_source_ldaps_id(id, location_id=location_id, organization_id=organization_id)

Delete an LDAP authentication source

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
    api_instance = foreman.AuthSourceLdapsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Delete an LDAP authentication source
        api_instance.delete_auth_source_ldaps_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling AuthSourceLdapsApi->delete_auth_source_ldaps_id: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_source_ldaps**
> get_auth_source_ldaps(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all LDAP authentication sources

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
    api_instance = foreman.AuthSourceLdapsApi(api_client)
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all LDAP authentication sources
        api_instance.get_auth_source_ldaps(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AuthSourceLdapsApi->get_auth_source_ldaps: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_source_ldaps_id**
> get_auth_source_ldaps_id(id, location_id=location_id, organization_id=organization_id)

Show an LDAP authentication source

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
    api_instance = foreman.AuthSourceLdapsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show an LDAP authentication source
        api_instance.get_auth_source_ldaps_id(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling AuthSourceLdapsApi->get_auth_source_ldaps_id: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations_location_id_auth_source_ldaps**
> get_locations_location_id_auth_source_ldaps(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List LDAP authentication sources per location

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
    api_instance = foreman.AuthSourceLdapsApi(api_client)
    location_id = 3.4 # float | Scope by locations
    organization_id = 3.4 # float | Scope by organizations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List LDAP authentication sources per location
        api_instance.get_locations_location_id_auth_source_ldaps(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AuthSourceLdapsApi->get_locations_location_id_auth_source_ldaps: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_auth_source_ldaps**
> get_organizations_organization_id_auth_source_ldaps(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)

List LDAP authentication sources per organization

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
    api_instance = foreman.AuthSourceLdapsApi(api_client)
    organization_id = 3.4 # float | Scope by organizations
    location_id = 3.4 # float | Scope by locations
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List LDAP authentication sources per organization
        api_instance.get_organizations_organization_id_auth_source_ldaps(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AuthSourceLdapsApi->get_organizations_organization_id_auth_source_ldaps: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_source_ldaps**
> post_auth_source_ldaps(auth_source_ldap_name, auth_source_ldap_host, location_id=location_id, organization_id=organization_id, auth_source_ldap_port=auth_source_ldap_port, auth_source_ldap_account=auth_source_ldap_account, auth_source_ldap_base_dn=auth_source_ldap_base_dn, auth_source_ldap_account_password=auth_source_ldap_account_password, auth_source_ldap_attr_login=auth_source_ldap_attr_login, auth_source_ldap_attr_firstname=auth_source_ldap_attr_firstname, auth_source_ldap_attr_lastname=auth_source_ldap_attr_lastname, auth_source_ldap_attr_mail=auth_source_ldap_attr_mail, auth_source_ldap_attr_photo=auth_source_ldap_attr_photo, auth_source_ldap_onthefly_register=auth_source_ldap_onthefly_register, auth_source_ldap_usergroup_sync=auth_source_ldap_usergroup_sync, auth_source_ldap_tls=auth_source_ldap_tls, auth_source_ldap_groups_base=auth_source_ldap_groups_base, auth_source_ldap_use_netgroups=auth_source_ldap_use_netgroups, auth_source_ldap_server_type=auth_source_ldap_server_type, auth_source_ldap_ldap_filter=auth_source_ldap_ldap_filter, auth_source_ldap_location_ids=auth_source_ldap_location_ids, auth_source_ldap_organization_ids=auth_source_ldap_organization_ids)

Create an LDAP authentication source

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
    api_instance = foreman.AuthSourceLdapsApi(api_client)
    auth_source_ldap_name = 'auth_source_ldap_name_example' # str | 
    auth_source_ldap_host = 'auth_source_ldap_host_example' # str | The hostname of the LDAP server
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    auth_source_ldap_port = 3.4 # float | defaults to 389 (optional)
    auth_source_ldap_account = 'auth_source_ldap_account_example' # str |  (optional)
    auth_source_ldap_base_dn = 'auth_source_ldap_base_dn_example' # str |  (optional)
    auth_source_ldap_account_password = 'auth_source_ldap_account_password_example' # str | required if onthefly_register is true (optional)
    auth_source_ldap_attr_login = 'uid' # str | required if onthefly_register is true (optional) (default to 'uid')
    auth_source_ldap_attr_firstname = 'givenName' # str | required if onthefly_register is true (optional) (default to 'givenName')
    auth_source_ldap_attr_lastname = 'sn' # str | required if onthefly_register is true (optional) (default to 'sn')
    auth_source_ldap_attr_mail = 'mail' # str | required if onthefly_register is true (optional) (default to 'mail')
    auth_source_ldap_attr_photo = 'jpegPhoto' # str |  (optional) (default to 'jpegPhoto')
    auth_source_ldap_onthefly_register = True # bool |  (optional)
    auth_source_ldap_usergroup_sync = True # bool | sync external user groups on login (optional)
    auth_source_ldap_tls = True # bool |  (optional)
    auth_source_ldap_groups_base = 'auth_source_ldap_groups_base_example' # str | groups base DN (optional)
    auth_source_ldap_use_netgroups = True # bool | use NIS netgroups instead of posix groups, applicable only when server_type is posix or free_ipa (optional)
    auth_source_ldap_server_type = 'auth_source_ldap_server_type_example' # str | type of the LDAP server (optional)
    auth_source_ldap_ldap_filter = 'auth_source_ldap_ldap_filter_example' # str | LDAP filter (optional)
    auth_source_ldap_location_ids = ['auth_source_ldap_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    auth_source_ldap_organization_ids = ['auth_source_ldap_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Create an LDAP authentication source
        api_instance.post_auth_source_ldaps(auth_source_ldap_name, auth_source_ldap_host, location_id=location_id, organization_id=organization_id, auth_source_ldap_port=auth_source_ldap_port, auth_source_ldap_account=auth_source_ldap_account, auth_source_ldap_base_dn=auth_source_ldap_base_dn, auth_source_ldap_account_password=auth_source_ldap_account_password, auth_source_ldap_attr_login=auth_source_ldap_attr_login, auth_source_ldap_attr_firstname=auth_source_ldap_attr_firstname, auth_source_ldap_attr_lastname=auth_source_ldap_attr_lastname, auth_source_ldap_attr_mail=auth_source_ldap_attr_mail, auth_source_ldap_attr_photo=auth_source_ldap_attr_photo, auth_source_ldap_onthefly_register=auth_source_ldap_onthefly_register, auth_source_ldap_usergroup_sync=auth_source_ldap_usergroup_sync, auth_source_ldap_tls=auth_source_ldap_tls, auth_source_ldap_groups_base=auth_source_ldap_groups_base, auth_source_ldap_use_netgroups=auth_source_ldap_use_netgroups, auth_source_ldap_server_type=auth_source_ldap_server_type, auth_source_ldap_ldap_filter=auth_source_ldap_ldap_filter, auth_source_ldap_location_ids=auth_source_ldap_location_ids, auth_source_ldap_organization_ids=auth_source_ldap_organization_ids)
    except Exception as e:
        print("Exception when calling AuthSourceLdapsApi->post_auth_source_ldaps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_source_ldap_name** | **str**|  | 
 **auth_source_ldap_host** | **str**| The hostname of the LDAP server | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **auth_source_ldap_port** | **float**| defaults to 389 | [optional] 
 **auth_source_ldap_account** | **str**|  | [optional] 
 **auth_source_ldap_base_dn** | **str**|  | [optional] 
 **auth_source_ldap_account_password** | **str**| required if onthefly_register is true | [optional] 
 **auth_source_ldap_attr_login** | **str**| required if onthefly_register is true | [optional] [default to &#39;uid&#39;]
 **auth_source_ldap_attr_firstname** | **str**| required if onthefly_register is true | [optional] [default to &#39;givenName&#39;]
 **auth_source_ldap_attr_lastname** | **str**| required if onthefly_register is true | [optional] [default to &#39;sn&#39;]
 **auth_source_ldap_attr_mail** | **str**| required if onthefly_register is true | [optional] [default to &#39;mail&#39;]
 **auth_source_ldap_attr_photo** | **str**|  | [optional] [default to &#39;jpegPhoto&#39;]
 **auth_source_ldap_onthefly_register** | **bool**|  | [optional] 
 **auth_source_ldap_usergroup_sync** | **bool**| sync external user groups on login | [optional] 
 **auth_source_ldap_tls** | **bool**|  | [optional] 
 **auth_source_ldap_groups_base** | **str**| groups base DN | [optional] 
 **auth_source_ldap_use_netgroups** | **bool**| use NIS netgroups instead of posix groups, applicable only when server_type is posix or free_ipa | [optional] 
 **auth_source_ldap_server_type** | **str**| type of the LDAP server | [optional] 
 **auth_source_ldap_ldap_filter** | **str**| LDAP filter | [optional] 
 **auth_source_ldap_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **auth_source_ldap_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_auth_source_ldaps_id**
> put_auth_source_ldaps_id(id, location_id=location_id, organization_id=organization_id, auth_source_ldap_name=auth_source_ldap_name, auth_source_ldap_host=auth_source_ldap_host, auth_source_ldap_port=auth_source_ldap_port, auth_source_ldap_account=auth_source_ldap_account, auth_source_ldap_base_dn=auth_source_ldap_base_dn, auth_source_ldap_account_password=auth_source_ldap_account_password, auth_source_ldap_attr_login=auth_source_ldap_attr_login, auth_source_ldap_attr_firstname=auth_source_ldap_attr_firstname, auth_source_ldap_attr_lastname=auth_source_ldap_attr_lastname, auth_source_ldap_attr_mail=auth_source_ldap_attr_mail, auth_source_ldap_attr_photo=auth_source_ldap_attr_photo, auth_source_ldap_onthefly_register=auth_source_ldap_onthefly_register, auth_source_ldap_usergroup_sync=auth_source_ldap_usergroup_sync, auth_source_ldap_tls=auth_source_ldap_tls, auth_source_ldap_groups_base=auth_source_ldap_groups_base, auth_source_ldap_use_netgroups=auth_source_ldap_use_netgroups, auth_source_ldap_server_type=auth_source_ldap_server_type, auth_source_ldap_ldap_filter=auth_source_ldap_ldap_filter, auth_source_ldap_location_ids=auth_source_ldap_location_ids, auth_source_ldap_organization_ids=auth_source_ldap_organization_ids)

Update an LDAP authentication source

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
    api_instance = foreman.AuthSourceLdapsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    auth_source_ldap_name = 'auth_source_ldap_name_example' # str |  (optional)
    auth_source_ldap_host = 'auth_source_ldap_host_example' # str | The hostname of the LDAP server (optional)
    auth_source_ldap_port = 3.4 # float | defaults to 389 (optional)
    auth_source_ldap_account = 'auth_source_ldap_account_example' # str |  (optional)
    auth_source_ldap_base_dn = 'auth_source_ldap_base_dn_example' # str |  (optional)
    auth_source_ldap_account_password = 'auth_source_ldap_account_password_example' # str | required if onthefly_register is true (optional)
    auth_source_ldap_attr_login = 'uid' # str | required if onthefly_register is true (optional) (default to 'uid')
    auth_source_ldap_attr_firstname = 'givenName' # str | required if onthefly_register is true (optional) (default to 'givenName')
    auth_source_ldap_attr_lastname = 'sn' # str | required if onthefly_register is true (optional) (default to 'sn')
    auth_source_ldap_attr_mail = 'mail' # str | required if onthefly_register is true (optional) (default to 'mail')
    auth_source_ldap_attr_photo = 'jpegPhoto' # str |  (optional) (default to 'jpegPhoto')
    auth_source_ldap_onthefly_register = True # bool |  (optional)
    auth_source_ldap_usergroup_sync = True # bool | sync external user groups on login (optional)
    auth_source_ldap_tls = True # bool |  (optional)
    auth_source_ldap_groups_base = 'auth_source_ldap_groups_base_example' # str | groups base DN (optional)
    auth_source_ldap_use_netgroups = True # bool | use NIS netgroups instead of posix groups, applicable only when server_type is posix or free_ipa (optional)
    auth_source_ldap_server_type = 'auth_source_ldap_server_type_example' # str | type of the LDAP server (optional)
    auth_source_ldap_ldap_filter = 'auth_source_ldap_ldap_filter_example' # str | LDAP filter (optional)
    auth_source_ldap_location_ids = ['auth_source_ldap_location_ids_example'] # List[str] | REPLACE locations with given ids (optional)
    auth_source_ldap_organization_ids = ['auth_source_ldap_organization_ids_example'] # List[str] | REPLACE organizations with given ids. (optional)

    try:
        # Update an LDAP authentication source
        api_instance.put_auth_source_ldaps_id(id, location_id=location_id, organization_id=organization_id, auth_source_ldap_name=auth_source_ldap_name, auth_source_ldap_host=auth_source_ldap_host, auth_source_ldap_port=auth_source_ldap_port, auth_source_ldap_account=auth_source_ldap_account, auth_source_ldap_base_dn=auth_source_ldap_base_dn, auth_source_ldap_account_password=auth_source_ldap_account_password, auth_source_ldap_attr_login=auth_source_ldap_attr_login, auth_source_ldap_attr_firstname=auth_source_ldap_attr_firstname, auth_source_ldap_attr_lastname=auth_source_ldap_attr_lastname, auth_source_ldap_attr_mail=auth_source_ldap_attr_mail, auth_source_ldap_attr_photo=auth_source_ldap_attr_photo, auth_source_ldap_onthefly_register=auth_source_ldap_onthefly_register, auth_source_ldap_usergroup_sync=auth_source_ldap_usergroup_sync, auth_source_ldap_tls=auth_source_ldap_tls, auth_source_ldap_groups_base=auth_source_ldap_groups_base, auth_source_ldap_use_netgroups=auth_source_ldap_use_netgroups, auth_source_ldap_server_type=auth_source_ldap_server_type, auth_source_ldap_ldap_filter=auth_source_ldap_ldap_filter, auth_source_ldap_location_ids=auth_source_ldap_location_ids, auth_source_ldap_organization_ids=auth_source_ldap_organization_ids)
    except Exception as e:
        print("Exception when calling AuthSourceLdapsApi->put_auth_source_ldaps_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **auth_source_ldap_name** | **str**|  | [optional] 
 **auth_source_ldap_host** | **str**| The hostname of the LDAP server | [optional] 
 **auth_source_ldap_port** | **float**| defaults to 389 | [optional] 
 **auth_source_ldap_account** | **str**|  | [optional] 
 **auth_source_ldap_base_dn** | **str**|  | [optional] 
 **auth_source_ldap_account_password** | **str**| required if onthefly_register is true | [optional] 
 **auth_source_ldap_attr_login** | **str**| required if onthefly_register is true | [optional] [default to &#39;uid&#39;]
 **auth_source_ldap_attr_firstname** | **str**| required if onthefly_register is true | [optional] [default to &#39;givenName&#39;]
 **auth_source_ldap_attr_lastname** | **str**| required if onthefly_register is true | [optional] [default to &#39;sn&#39;]
 **auth_source_ldap_attr_mail** | **str**| required if onthefly_register is true | [optional] [default to &#39;mail&#39;]
 **auth_source_ldap_attr_photo** | **str**|  | [optional] [default to &#39;jpegPhoto&#39;]
 **auth_source_ldap_onthefly_register** | **bool**|  | [optional] 
 **auth_source_ldap_usergroup_sync** | **bool**| sync external user groups on login | [optional] 
 **auth_source_ldap_tls** | **bool**|  | [optional] 
 **auth_source_ldap_groups_base** | **str**| groups base DN | [optional] 
 **auth_source_ldap_use_netgroups** | **bool**| use NIS netgroups instead of posix groups, applicable only when server_type is posix or free_ipa | [optional] 
 **auth_source_ldap_server_type** | **str**| type of the LDAP server | [optional] 
 **auth_source_ldap_ldap_filter** | **str**| LDAP filter | [optional] 
 **auth_source_ldap_location_ids** | [**List[str]**](str.md)| REPLACE locations with given ids | [optional] 
 **auth_source_ldap_organization_ids** | [**List[str]**](str.md)| REPLACE organizations with given ids. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_auth_source_ldaps_id_test**
> put_auth_source_ldaps_id_test(id, location_id=location_id, organization_id=organization_id)

Test LDAP connection

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
    api_instance = foreman.AuthSourceLdapsApi(api_client)
    id = 'id_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Test LDAP connection
        api_instance.put_auth_source_ldaps_id_test(id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling AuthSourceLdapsApi->put_auth_source_ldaps_id_test: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

