# foreman.ActivationKeysApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_activation_keys_id**](ActivationKeysApi.md#delete_activation_keys_id) | **DELETE** /activation_keys/{id} | Destroy an activation key
[**get_activation_keys**](ActivationKeysApi.md#get_activation_keys) | **GET** /activation_keys | List activation keys
[**get_activation_keys_id**](ActivationKeysApi.md#get_activation_keys_id) | **GET** /activation_keys/{id} | Show an activation key
[**get_activation_keys_id_host_collections_available**](ActivationKeysApi.md#get_activation_keys_id_host_collections_available) | **GET** /activation_keys/{id}/host_collections/available | List host collections the activation key does not belong to
[**get_activation_keys_id_product_content**](ActivationKeysApi.md#get_activation_keys_id_product_content) | **GET** /activation_keys/{id}/product_content | Show content available for an activation key
[**get_activation_keys_id_releases**](ActivationKeysApi.md#get_activation_keys_id_releases) | **GET** /activation_keys/{id}/releases | Show release versions available for an activation key
[**get_environments_environment_id_activation_keys**](ActivationKeysApi.md#get_environments_environment_id_activation_keys) | **GET** /environments/{environment_id}/activation_keys | 
[**get_organizations_organization_id_activation_keys**](ActivationKeysApi.md#get_organizations_organization_id_activation_keys) | **GET** /organizations/{organization_id}/activation_keys | 
[**post_activation_keys**](ActivationKeysApi.md#post_activation_keys) | **POST** /activation_keys | Create an activation key
[**post_activation_keys_id_copy**](ActivationKeysApi.md#post_activation_keys_id_copy) | **POST** /activation_keys/{id}/copy | Copy an activation key
[**post_activation_keys_id_host_collections**](ActivationKeysApi.md#post_activation_keys_id_host_collections) | **POST** /activation_keys/{id}/host_collections | 
[**put_activation_keys_id**](ActivationKeysApi.md#put_activation_keys_id) | **PUT** /activation_keys/{id} | Update an activation key
[**put_activation_keys_id_add_subscriptions**](ActivationKeysApi.md#put_activation_keys_id_add_subscriptions) | **PUT** /activation_keys/{id}/add_subscriptions | Attach a subscription
[**put_activation_keys_id_content_override**](ActivationKeysApi.md#put_activation_keys_id_content_override) | **PUT** /activation_keys/{id}/content_override | Override content for activation_key
[**put_activation_keys_id_host_collections**](ActivationKeysApi.md#put_activation_keys_id_host_collections) | **PUT** /activation_keys/{id}/host_collections | 
[**put_activation_keys_id_remove_subscriptions**](ActivationKeysApi.md#put_activation_keys_id_remove_subscriptions) | **PUT** /activation_keys/{id}/remove_subscriptions | Unattach a subscription


# **delete_activation_keys_id**
> delete_activation_keys_id(id)

Destroy an activation key

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key

    try:
        # Destroy an activation key
        api_instance.delete_activation_keys_id(id)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->delete_activation_keys_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 

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

# **get_activation_keys**
> get_activation_keys(organization_id, environment_id, content_view_id=content_view_id, name=name, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List activation keys

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
    api_instance = foreman.ActivationKeysApi(api_client)
    organization_id = 3.4 # float | organization identifier
    environment_id = 3.4 # float | environment identifier
    content_view_id = 3.4 # float | content view identifier (optional)
    name = 'name_example' # str | activation key name to filter by (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List activation keys
        api_instance.get_activation_keys(organization_id, environment_id, content_view_id=content_view_id, name=name, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->get_activation_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier | 
 **environment_id** | **float**| environment identifier | 
 **content_view_id** | **float**| content view identifier | [optional] 
 **name** | **str**| activation key name to filter by | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 

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

# **get_activation_keys_id**
> get_activation_keys_id(id, organization_id=organization_id, show_hosts=show_hosts)

Show an activation key

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key
    organization_id = 3.4 # float | organization identifier (optional)
    show_hosts = True # bool | Show hosts associated to an activation key (optional)

    try:
        # Show an activation key
        api_instance.get_activation_keys_id(id, organization_id=organization_id, show_hosts=show_hosts)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->get_activation_keys_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 
 **organization_id** | **float**| organization identifier | [optional] 
 **show_hosts** | **bool**| Show hosts associated to an activation key | [optional] 

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

# **get_activation_keys_id_host_collections_available**
> get_activation_keys_id_host_collections_available(id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name)

List host collections the activation key does not belong to

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | 
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
    name = 'name_example' # str | host collection name to filter by (optional)

    try:
        # List host collections the activation key does not belong to
        api_instance.get_activation_keys_id_host_collections_available(id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->get_activation_keys_id_host_collections_available: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 
 **name** | **str**| host collection name to filter by | [optional] 

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

# **get_activation_keys_id_product_content**
> get_activation_keys_id_product_content(id, content_access_mode_all=content_access_mode_all, content_access_mode_env=content_access_mode_env, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

Show content available for an activation key

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 'id_example' # str | ID of the activation key
    content_access_mode_all = True # bool | Get all content available, not just that provided by subscriptions (optional)
    content_access_mode_env = True # bool | Limit content to just that available in the activation key's content view version (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # Show content available for an activation key
        api_instance.get_activation_keys_id_product_content(id, content_access_mode_all=content_access_mode_all, content_access_mode_env=content_access_mode_env, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->get_activation_keys_id_product_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the activation key | 
 **content_access_mode_all** | **bool**| Get all content available, not just that provided by subscriptions | [optional] 
 **content_access_mode_env** | **bool**| Limit content to just that available in the activation key&#39;s content view version | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 

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

# **get_activation_keys_id_releases**
> get_activation_keys_id_releases(id)

Show release versions available for an activation key

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 'id_example' # str | ID of the activation key

    try:
        # Show release versions available for an activation key
        api_instance.get_activation_keys_id_releases(id)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->get_activation_keys_id_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the activation key | 

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

# **get_environments_environment_id_activation_keys**
> get_environments_environment_id_activation_keys(environment_id, organization_id, content_view_id=content_view_id, name=name, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)



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
    api_instance = foreman.ActivationKeysApi(api_client)
    environment_id = 3.4 # float | environment identifier
    organization_id = 3.4 # float | organization identifier
    content_view_id = 3.4 # float | content view identifier (optional)
    name = 'name_example' # str | activation key name to filter by (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        api_instance.get_environments_environment_id_activation_keys(environment_id, organization_id, content_view_id=content_view_id, name=name, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->get_environments_environment_id_activation_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **float**| environment identifier | 
 **organization_id** | **float**| organization identifier | 
 **content_view_id** | **float**| content view identifier | [optional] 
 **name** | **str**| activation key name to filter by | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 

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

# **get_organizations_organization_id_activation_keys**
> get_organizations_organization_id_activation_keys(organization_id, environment_id, content_view_id=content_view_id, name=name, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)



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
    api_instance = foreman.ActivationKeysApi(api_client)
    organization_id = 3.4 # float | organization identifier
    environment_id = 3.4 # float | environment identifier
    content_view_id = 3.4 # float | content view identifier (optional)
    name = 'name_example' # str | activation key name to filter by (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        api_instance.get_organizations_organization_id_activation_keys(organization_id, environment_id, content_view_id=content_view_id, name=name, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->get_organizations_organization_id_activation_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier | 
 **environment_id** | **float**| environment identifier | 
 **content_view_id** | **float**| content view identifier | [optional] 
 **name** | **str**| activation key name to filter by | [optional] 
 **search** | **str**| Search string | [optional] 
 **page** | **float**| Page number, starting at 1 | [optional] 
 **per_page** | **float**| Number of results per page to return | [optional] 
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **full_result** | **bool**| Whether or not to show all results | [optional] 
 **sort_by** | **str**| Field to sort the results on | [optional] 
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 

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

# **post_activation_keys**
> post_activation_keys(organization_id, name, description=description, environment_id=environment_id, content_view_id=content_view_id, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts, release_version=release_version, service_level=service_level, auto_attach=auto_attach, purpose_usage=purpose_usage, purpose_role=purpose_role, purpose_addons=purpose_addons)

Create an activation key

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
    api_instance = foreman.ActivationKeysApi(api_client)
    organization_id = 3.4 # float | organization identifier
    name = 'name_example' # str | name
    description = 'description_example' # str | description (optional)
    environment_id = 3.4 # float | environment id (optional)
    content_view_id = 3.4 # float | content view id (optional)
    max_hosts = 3.4 # float | maximum number of registered content hosts (optional)
    unlimited_hosts = True # bool | can the activation key have unlimited hosts (optional)
    release_version = 'release_version_example' # str | content release version (optional)
    service_level = 'service_level_example' # str | service level (optional)
    auto_attach = True # bool | auto attach subscriptions upon registration (optional)
    purpose_usage = 'purpose_usage_example' # str | Sets the system purpose usage (optional)
    purpose_role = 'purpose_role_example' # str | Sets the system purpose usage (optional)
    purpose_addons = ['purpose_addons_example'] # List[str] | Sets the system add-ons (optional)

    try:
        # Create an activation key
        api_instance.post_activation_keys(organization_id, name, description=description, environment_id=environment_id, content_view_id=content_view_id, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts, release_version=release_version, service_level=service_level, auto_attach=auto_attach, purpose_usage=purpose_usage, purpose_role=purpose_role, purpose_addons=purpose_addons)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->post_activation_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier | 
 **name** | **str**| name | 
 **description** | **str**| description | [optional] 
 **environment_id** | **float**| environment id | [optional] 
 **content_view_id** | **float**| content view id | [optional] 
 **max_hosts** | **float**| maximum number of registered content hosts | [optional] 
 **unlimited_hosts** | **bool**| can the activation key have unlimited hosts | [optional] 
 **release_version** | **str**| content release version | [optional] 
 **service_level** | **str**| service level | [optional] 
 **auto_attach** | **bool**| auto attach subscriptions upon registration | [optional] 
 **purpose_usage** | **str**| Sets the system purpose usage | [optional] 
 **purpose_role** | **str**| Sets the system purpose usage | [optional] 
 **purpose_addons** | [**List[str]**](str.md)| Sets the system add-ons | [optional] 

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

# **post_activation_keys_id_copy**
> post_activation_keys_id_copy(id, new_name, organization_id=organization_id)

Copy an activation key

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key
    new_name = 'new_name_example' # str | Name of new activation key
    organization_id = 3.4 # float | organization identifier (optional)

    try:
        # Copy an activation key
        api_instance.post_activation_keys_id_copy(id, new_name, organization_id=organization_id)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->post_activation_keys_id_copy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 
 **new_name** | **str**| Name of new activation key | 
 **organization_id** | **float**| organization identifier | [optional] 

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

# **post_activation_keys_id_host_collections**
> post_activation_keys_id_host_collections(id, host_collection_ids)



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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key
    host_collection_ids = ['host_collection_ids_example'] # List[str] | List of host collection IDs to associate with activation key

    try:
        api_instance.post_activation_keys_id_host_collections(id, host_collection_ids)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->post_activation_keys_id_host_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 
 **host_collection_ids** | [**List[str]**](str.md)| List of host collection IDs to associate with activation key | 

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

# **put_activation_keys_id**
> put_activation_keys_id(id, organization_id, name=name, description=description, environment_id=environment_id, content_view_id=content_view_id, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts, release_version=release_version, service_level=service_level, auto_attach=auto_attach, purpose_usage=purpose_usage, purpose_role=purpose_role, purpose_addons=purpose_addons)

Update an activation key

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key
    organization_id = 3.4 # float | organization identifier
    name = 'name_example' # str | name (optional)
    description = 'description_example' # str | description (optional)
    environment_id = 3.4 # float | environment id (optional)
    content_view_id = 3.4 # float | content view id (optional)
    max_hosts = 3.4 # float | maximum number of registered content hosts (optional)
    unlimited_hosts = True # bool | can the activation key have unlimited hosts (optional)
    release_version = 'release_version_example' # str | content release version (optional)
    service_level = 'service_level_example' # str | service level (optional)
    auto_attach = True # bool | auto attach subscriptions upon registration (optional)
    purpose_usage = 'purpose_usage_example' # str | Sets the system purpose usage (optional)
    purpose_role = 'purpose_role_example' # str | Sets the system purpose usage (optional)
    purpose_addons = ['purpose_addons_example'] # List[str] | Sets the system add-ons (optional)

    try:
        # Update an activation key
        api_instance.put_activation_keys_id(id, organization_id, name=name, description=description, environment_id=environment_id, content_view_id=content_view_id, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts, release_version=release_version, service_level=service_level, auto_attach=auto_attach, purpose_usage=purpose_usage, purpose_role=purpose_role, purpose_addons=purpose_addons)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->put_activation_keys_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 
 **organization_id** | **float**| organization identifier | 
 **name** | **str**| name | [optional] 
 **description** | **str**| description | [optional] 
 **environment_id** | **float**| environment id | [optional] 
 **content_view_id** | **float**| content view id | [optional] 
 **max_hosts** | **float**| maximum number of registered content hosts | [optional] 
 **unlimited_hosts** | **bool**| can the activation key have unlimited hosts | [optional] 
 **release_version** | **str**| content release version | [optional] 
 **service_level** | **str**| service level | [optional] 
 **auto_attach** | **bool**| auto attach subscriptions upon registration | [optional] 
 **purpose_usage** | **str**| Sets the system purpose usage | [optional] 
 **purpose_role** | **str**| Sets the system purpose usage | [optional] 
 **purpose_addons** | [**List[str]**](str.md)| Sets the system add-ons | [optional] 

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

# **put_activation_keys_id_add_subscriptions**
> put_activation_keys_id_add_subscriptions(id, subscription_id=subscription_id, quantity=quantity, subscriptions=subscriptions)

Attach a subscription

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key
    subscription_id = 3.4 # float | Subscription identifier (optional)
    quantity = 3.4 # float | Quantity of this subscription to add (optional)
    subscriptions = ['subscriptions_example'] # List[str] | Array of subscriptions to add (optional)

    try:
        # Attach a subscription
        api_instance.put_activation_keys_id_add_subscriptions(id, subscription_id=subscription_id, quantity=quantity, subscriptions=subscriptions)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->put_activation_keys_id_add_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 
 **subscription_id** | **float**| Subscription identifier | [optional] 
 **quantity** | **float**| Quantity of this subscription to add | [optional] 
 **subscriptions** | [**List[str]**](str.md)| Array of subscriptions to add | [optional] 

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

# **put_activation_keys_id_content_override**
> put_activation_keys_id_content_override(id, content_overrides=content_overrides)

Override content for activation_key

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key
    content_overrides = ['content_overrides_example'] # List[str] | Array of Content override parameters to be added in bulk (optional)

    try:
        # Override content for activation_key
        api_instance.put_activation_keys_id_content_override(id, content_overrides=content_overrides)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->put_activation_keys_id_content_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 
 **content_overrides** | [**List[str]**](str.md)| Array of Content override parameters to be added in bulk | [optional] 

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

# **put_activation_keys_id_host_collections**
> put_activation_keys_id_host_collections(id, host_collection_ids)



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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key
    host_collection_ids = ['host_collection_ids_example'] # List[str] | List of host collection IDs to disassociate from the activation key

    try:
        api_instance.put_activation_keys_id_host_collections(id, host_collection_ids)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->put_activation_keys_id_host_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 
 **host_collection_ids** | [**List[str]**](str.md)| List of host collection IDs to disassociate from the activation key | 

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

# **put_activation_keys_id_remove_subscriptions**
> put_activation_keys_id_remove_subscriptions(id, subscription_id=subscription_id, subscriptions=subscriptions)

Unattach a subscription

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
    api_instance = foreman.ActivationKeysApi(api_client)
    id = 3.4 # float | ID of the activation key
    subscription_id = 'subscription_id_example' # str | Subscription ID (optional)
    subscriptions = ['subscriptions_example'] # List[str] | Array of subscriptions to add (optional)

    try:
        # Unattach a subscription
        api_instance.put_activation_keys_id_remove_subscriptions(id, subscription_id=subscription_id, subscriptions=subscriptions)
    except Exception as e:
        print("Exception when calling ActivationKeysApi->put_activation_keys_id_remove_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the activation key | 
 **subscription_id** | **str**| Subscription ID | [optional] 
 **subscriptions** | [**List[str]**](str.md)| Array of subscriptions to add | [optional] 

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

