# foreman.PersonalAccessTokensApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_user_id_personal_access_tokens_id**](PersonalAccessTokensApi.md#delete_users_user_id_personal_access_tokens_id) | **DELETE** /users/{user_id}/personal_access_tokens/{id} | Revoke a Personal Access Token for a user
[**get_users_user_id_personal_access_tokens**](PersonalAccessTokensApi.md#get_users_user_id_personal_access_tokens) | **GET** /users/{user_id}/personal_access_tokens | List all Personal Access Tokens for a user
[**get_users_user_id_personal_access_tokens_id**](PersonalAccessTokensApi.md#get_users_user_id_personal_access_tokens_id) | **GET** /users/{user_id}/personal_access_tokens/{id} | Show a Personal Access Token for a user
[**post_users_user_id_personal_access_tokens**](PersonalAccessTokensApi.md#post_users_user_id_personal_access_tokens) | **POST** /users/{user_id}/personal_access_tokens | Create a Personal Access Token for a user


# **delete_users_user_id_personal_access_tokens_id**
> delete_users_user_id_personal_access_tokens_id(id, user_id, location_id=location_id, organization_id=organization_id)

Revoke a Personal Access Token for a user

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
    api_instance = foreman.PersonalAccessTokensApi(api_client)
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str | ID of the user
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Revoke a Personal Access Token for a user
        api_instance.delete_users_user_id_personal_access_tokens_id(id, user_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling PersonalAccessTokensApi->delete_users_user_id_personal_access_tokens_id: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_user_id_personal_access_tokens**
> get_users_user_id_personal_access_tokens(user_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List all Personal Access Tokens for a user

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
    api_instance = foreman.PersonalAccessTokensApi(api_client)
    user_id = 'user_id_example' # str | ID of the user
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    search = 'search_example' # str | filter results (optional)
    order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

    try:
        # List all Personal Access Tokens for a user
        api_instance.get_users_user_id_personal_access_tokens(user_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PersonalAccessTokensApi->get_users_user_id_personal_access_tokens: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_user_id_personal_access_tokens_id**
> get_users_user_id_personal_access_tokens_id(id, user_id, location_id=location_id, organization_id=organization_id)

Show a Personal Access Token for a user

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
    api_instance = foreman.PersonalAccessTokensApi(api_client)
    id = 'id_example' # str | 
    user_id = 'user_id_example' # str | ID of the user
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)

    try:
        # Show a Personal Access Token for a user
        api_instance.get_users_user_id_personal_access_tokens_id(id, user_id, location_id=location_id, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling PersonalAccessTokensApi->get_users_user_id_personal_access_tokens_id: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_users_user_id_personal_access_tokens**
> post_users_user_id_personal_access_tokens(user_id, personal_access_token_name, location_id=location_id, organization_id=organization_id, personal_access_token_expires_at=personal_access_token_expires_at)

Create a Personal Access Token for a user

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
    api_instance = foreman.PersonalAccessTokensApi(api_client)
    user_id = 'user_id_example' # str | ID of the user
    personal_access_token_name = 'personal_access_token_name_example' # str | 
    location_id = 3.4 # float | Set the current location context for the request (optional)
    organization_id = 3.4 # float | Set the current organization context for the request (optional)
    personal_access_token_expires_at = 'personal_access_token_expires_at_example' # str | Expiry Date (optional)

    try:
        # Create a Personal Access Token for a user
        api_instance.post_users_user_id_personal_access_tokens(user_id, personal_access_token_name, location_id=location_id, organization_id=organization_id, personal_access_token_expires_at=personal_access_token_expires_at)
    except Exception as e:
        print("Exception when calling PersonalAccessTokensApi->post_users_user_id_personal_access_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user | 
 **personal_access_token_name** | **str**|  | 
 **location_id** | **float**| Set the current location context for the request | [optional] 
 **organization_id** | **float**| Set the current organization context for the request | [optional] 
 **personal_access_token_expires_at** | **str**| Expiry Date | [optional] 

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

