# pyforeman.SshKeysApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_user_id_ssh_keys_id**](SshKeysApi.md#delete_users_user_id_ssh_keys_id) | **DELETE** /users/{user_id}/ssh_keys/{id} | Delete an SSH key for a user
[**get_users_user_id_ssh_keys**](SshKeysApi.md#get_users_user_id_ssh_keys) | **GET** /users/{user_id}/ssh_keys | List all SSH keys for a user
[**get_users_user_id_ssh_keys_id**](SshKeysApi.md#get_users_user_id_ssh_keys_id) | **GET** /users/{user_id}/ssh_keys/{id} | Show an SSH key from a user
[**post_users_user_id_ssh_keys**](SshKeysApi.md#post_users_user_id_ssh_keys) | **POST** /users/{user_id}/ssh_keys | Add an SSH key for a user


# **delete_users_user_id_ssh_keys_id**
> delete_users_user_id_ssh_keys_id(id, user_id, location_id=location_id, organization_id=organization_id)

Delete an SSH key for a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SshKeysApi()
id = 'id_example' # str |
user_id = 'user_id_example' # str | ID of the user
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete an SSH key for a user
    api_instance.delete_users_user_id_ssh_keys_id(id, user_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling SshKeysApi->delete_users_user_id_ssh_keys_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user_id** | **str**| ID of the user |
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

# **get_users_user_id_ssh_keys**
> get_users_user_id_ssh_keys(user_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all SSH keys for a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SshKeysApi()
user_id = 'user_id_example' # str | ID of the user
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all SSH keys for a user
    api_instance.get_users_user_id_ssh_keys(user_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling SshKeysApi->get_users_user_id_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user |
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

# **get_users_user_id_ssh_keys_id**
> get_users_user_id_ssh_keys_id(id, user_id, location_id=location_id, organization_id=organization_id)

Show an SSH key from a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SshKeysApi()
id = 'id_example' # str |
user_id = 'user_id_example' # str | ID of the user
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show an SSH key from a user
    api_instance.get_users_user_id_ssh_keys_id(id, user_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling SshKeysApi->get_users_user_id_ssh_keys_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user_id** | **str**| ID of the user |
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

# **post_users_user_id_ssh_keys**
> post_users_user_id_ssh_keys(user_id, ssh_key_name, ssh_key_key, location_id=location_id, organization_id=organization_id)

Add an SSH key for a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SshKeysApi()
user_id = 'user_id_example' # str | ID of the user
ssh_key_name = 'ssh_key_name_example' # str |
ssh_key_key = 'ssh_key_key_example' # str | Public SSH key
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Add an SSH key for a user
    api_instance.post_users_user_id_ssh_keys(user_id, ssh_key_name, ssh_key_key, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling SshKeysApi->post_users_user_id_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user |
 **ssh_key_name** | **str**|  |
 **ssh_key_key** | **str**| Public SSH key |
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
