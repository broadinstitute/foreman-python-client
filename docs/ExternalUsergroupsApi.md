# pyforeman.ExternalUsergroupsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_usergroups_usergroup_id_external_usergroups_id**](ExternalUsergroupsApi.md#delete_usergroups_usergroup_id_external_usergroups_id) | **DELETE** /usergroups/{usergroup_id}/external_usergroups/{id} | Delete an external user group
[**get_auth_source_ldaps_auth_source_ldap_id_external_usergroups**](ExternalUsergroupsApi.md#get_auth_source_ldaps_auth_source_ldap_id_external_usergroups) | **GET** /auth_source_ldaps/{auth_source_ldap_id}/external_usergroups | List all external user groups for LDAP authentication source
[**get_auth_source_ldaps_auth_source_ldap_id_external_usergroups_id**](ExternalUsergroupsApi.md#get_auth_source_ldaps_auth_source_ldap_id_external_usergroups_id) | **GET** /auth_source_ldaps/{auth_source_ldap_id}/external_usergroups/{id} | Show an external user group for LDAP authentication source
[**get_usergroups_usergroup_id_external_usergroups**](ExternalUsergroupsApi.md#get_usergroups_usergroup_id_external_usergroups) | **GET** /usergroups/{usergroup_id}/external_usergroups | List all external user groups for user group
[**get_usergroups_usergroup_id_external_usergroups_id**](ExternalUsergroupsApi.md#get_usergroups_usergroup_id_external_usergroups_id) | **GET** /usergroups/{usergroup_id}/external_usergroups/{id} | Show an external user group for user group
[**post_usergroups_usergroup_id_external_usergroups**](ExternalUsergroupsApi.md#post_usergroups_usergroup_id_external_usergroups) | **POST** /usergroups/{usergroup_id}/external_usergroups | Create an external user group linked to a user group
[**put_usergroups_usergroup_id_external_usergroups_id**](ExternalUsergroupsApi.md#put_usergroups_usergroup_id_external_usergroups_id) | **PUT** /usergroups/{usergroup_id}/external_usergroups/{id} | Update external user group
[**put_usergroups_usergroup_id_external_usergroups_id_refresh**](ExternalUsergroupsApi.md#put_usergroups_usergroup_id_external_usergroups_id_refresh) | **PUT** /usergroups/{usergroup_id}/external_usergroups/{id}/refresh | Refresh external user group


# **delete_usergroups_usergroup_id_external_usergroups_id**
> delete_usergroups_usergroup_id_external_usergroups_id(usergroup_id, id, location_id=location_id, organization_id=organization_id)

Delete an external user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ExternalUsergroupsApi()
usergroup_id = 'usergroup_id_example' # str | ID or name of user group
id = 'id_example' # str | ID or name external user group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete an external user group
    api_instance.delete_usergroups_usergroup_id_external_usergroups_id(usergroup_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ExternalUsergroupsApi->delete_usergroups_usergroup_id_external_usergroups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_id** | **str**| ID or name of user group |
 **id** | **str**| ID or name external user group |
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

# **get_auth_source_ldaps_auth_source_ldap_id_external_usergroups**
> get_auth_source_ldaps_auth_source_ldap_id_external_usergroups(auth_source_ldap_id, usergroup_id, location_id=location_id, organization_id=organization_id)

List all external user groups for LDAP authentication source



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ExternalUsergroupsApi()
auth_source_ldap_id = 8.14 # float |
usergroup_id = 'usergroup_id_example' # str | ID or name of user group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List all external user groups for LDAP authentication source
    api_instance.get_auth_source_ldaps_auth_source_ldap_id_external_usergroups(auth_source_ldap_id, usergroup_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ExternalUsergroupsApi->get_auth_source_ldaps_auth_source_ldap_id_external_usergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_source_ldap_id** | **float**|  |
 **usergroup_id** | **str**| ID or name of user group |
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

# **get_auth_source_ldaps_auth_source_ldap_id_external_usergroups_id**
> get_auth_source_ldaps_auth_source_ldap_id_external_usergroups_id(id, auth_source_ldap_id, usergroup_id, location_id=location_id, organization_id=organization_id)

Show an external user group for LDAP authentication source



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ExternalUsergroupsApi()
id = 'id_example' # str | ID or name of external user group
auth_source_ldap_id = 8.14 # float |
usergroup_id = 'usergroup_id_example' # str | ID or name of user group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show an external user group for LDAP authentication source
    api_instance.get_auth_source_ldaps_auth_source_ldap_id_external_usergroups_id(id, auth_source_ldap_id, usergroup_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ExternalUsergroupsApi->get_auth_source_ldaps_auth_source_ldap_id_external_usergroups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID or name of external user group |
 **auth_source_ldap_id** | **float**|  |
 **usergroup_id** | **str**| ID or name of user group |
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

# **get_usergroups_usergroup_id_external_usergroups**
> get_usergroups_usergroup_id_external_usergroups(usergroup_id, location_id=location_id, organization_id=organization_id)

List all external user groups for user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ExternalUsergroupsApi()
usergroup_id = 'usergroup_id_example' # str | ID or name of user group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List all external user groups for user group
    api_instance.get_usergroups_usergroup_id_external_usergroups(usergroup_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ExternalUsergroupsApi->get_usergroups_usergroup_id_external_usergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_id** | **str**| ID or name of user group |
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

# **get_usergroups_usergroup_id_external_usergroups_id**
> get_usergroups_usergroup_id_external_usergroups_id(usergroup_id, id, location_id=location_id, organization_id=organization_id)

Show an external user group for user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ExternalUsergroupsApi()
usergroup_id = 'usergroup_id_example' # str | ID or name of user group
id = 'id_example' # str | ID or name of external user group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show an external user group for user group
    api_instance.get_usergroups_usergroup_id_external_usergroups_id(usergroup_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ExternalUsergroupsApi->get_usergroups_usergroup_id_external_usergroups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_id** | **str**| ID or name of user group |
 **id** | **str**| ID or name of external user group |
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

# **post_usergroups_usergroup_id_external_usergroups**
> post_usergroups_usergroup_id_external_usergroups(usergroup_id, external_usergroup_name, external_usergroup_auth_source_id, location_id=location_id, organization_id=organization_id)

Create an external user group linked to a user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ExternalUsergroupsApi()
usergroup_id = 'usergroup_id_example' # str | ID or name of user group
external_usergroup_name = 'external_usergroup_name_example' # str | External user group name
external_usergroup_auth_source_id = 8.14 # float | ID of linked authentication source
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Create an external user group linked to a user group
    api_instance.post_usergroups_usergroup_id_external_usergroups(usergroup_id, external_usergroup_name, external_usergroup_auth_source_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ExternalUsergroupsApi->post_usergroups_usergroup_id_external_usergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_id** | **str**| ID or name of user group |
 **external_usergroup_name** | **str**| External user group name |
 **external_usergroup_auth_source_id** | **float**| ID of linked authentication source |
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

# **put_usergroups_usergroup_id_external_usergroups_id**
> put_usergroups_usergroup_id_external_usergroups_id(usergroup_id, id, location_id=location_id, organization_id=organization_id, external_usergroup_name=external_usergroup_name, external_usergroup_auth_source_id=external_usergroup_auth_source_id)

Update external user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ExternalUsergroupsApi()
usergroup_id = 'usergroup_id_example' # str | ID or name of user group
id = 'id_example' # str | ID or name of external user group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
external_usergroup_name = 'external_usergroup_name_example' # str | External user group name (optional)
external_usergroup_auth_source_id = 8.14 # float | ID of linked authentication source (optional)

try:
    # Update external user group
    api_instance.put_usergroups_usergroup_id_external_usergroups_id(usergroup_id, id, location_id=location_id, organization_id=organization_id, external_usergroup_name=external_usergroup_name, external_usergroup_auth_source_id=external_usergroup_auth_source_id)
except ApiException as e:
    print("Exception when calling ExternalUsergroupsApi->put_usergroups_usergroup_id_external_usergroups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_id** | **str**| ID or name of user group |
 **id** | **str**| ID or name of external user group |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **external_usergroup_name** | **str**| External user group name | [optional]
 **external_usergroup_auth_source_id** | **float**| ID of linked authentication source | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_usergroups_usergroup_id_external_usergroups_id_refresh**
> put_usergroups_usergroup_id_external_usergroups_id_refresh(usergroup_id, id, location_id=location_id, organization_id=organization_id)

Refresh external user group



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ExternalUsergroupsApi()
usergroup_id = 'usergroup_id_example' # str | ID or name of user group
id = 'id_example' # str | ID or name of external user group
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Refresh external user group
    api_instance.put_usergroups_usergroup_id_external_usergroups_id_refresh(usergroup_id, id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ExternalUsergroupsApi->put_usergroups_usergroup_id_external_usergroups_id_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usergroup_id** | **str**| ID or name of user group |
 **id** | **str**| ID or name of external user group |
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
