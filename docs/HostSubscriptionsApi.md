# foreman.HostSubscriptionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_hosts_host_id_subscriptions**](HostSubscriptionsApi.md#delete_hosts_host_id_subscriptions) | **DELETE** /hosts/{host_id}/subscriptions | Unregister the host as a subscription consumer
[**get_hosts_host_id_subscriptions**](HostSubscriptionsApi.md#get_hosts_host_id_subscriptions) | **GET** /hosts/{host_id}/subscriptions | List a host&#39;s subscriptions
[**get_hosts_host_id_subscriptions_available_release_versions**](HostSubscriptionsApi.md#get_hosts_host_id_subscriptions_available_release_versions) | **GET** /hosts/{host_id}/subscriptions/available_release_versions | Show releases available for the content host
[**get_hosts_host_id_subscriptions_enabled_repositories**](HostSubscriptionsApi.md#get_hosts_host_id_subscriptions_enabled_repositories) | **GET** /hosts/{host_id}/subscriptions/enabled_repositories | Show repositories enabled on the host that are known to Katello
[**get_hosts_host_id_subscriptions_product_content**](HostSubscriptionsApi.md#get_hosts_host_id_subscriptions_product_content) | **GET** /hosts/{host_id}/subscriptions/product_content | Get content and overrides for the host
[**post_hosts_subscriptions**](HostSubscriptionsApi.md#post_hosts_subscriptions) | **POST** /hosts/subscriptions | Register a host with subscription and information
[**put_hosts_host_id_subscriptions_add_subscriptions**](HostSubscriptionsApi.md#put_hosts_host_id_subscriptions_add_subscriptions) | **PUT** /hosts/{host_id}/subscriptions/add_subscriptions | Add a subscription to a host
[**put_hosts_host_id_subscriptions_auto_attach**](HostSubscriptionsApi.md#put_hosts_host_id_subscriptions_auto_attach) | **PUT** /hosts/{host_id}/subscriptions/auto_attach | Trigger an auto-attach of subscriptions
[**put_hosts_host_id_subscriptions_content_override**](HostSubscriptionsApi.md#put_hosts_host_id_subscriptions_content_override) | **PUT** /hosts/{host_id}/subscriptions/content_override | Set content overrides for the host
[**put_hosts_host_id_subscriptions_remove_subscriptions**](HostSubscriptionsApi.md#put_hosts_host_id_subscriptions_remove_subscriptions) | **PUT** /hosts/{host_id}/subscriptions/remove_subscriptions | 


# **delete_hosts_host_id_subscriptions**
> delete_hosts_host_id_subscriptions(host_id)

Unregister the host as a subscription consumer

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 3.4 # float | Id of the host

    try:
        # Unregister the host as a subscription consumer
        api_instance.delete_hosts_host_id_subscriptions(host_id)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->delete_hosts_host_id_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| Id of the host | 

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

# **get_hosts_host_id_subscriptions**
> get_hosts_host_id_subscriptions(host_id)

List a host's subscriptions

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 3.4 # float | Id of the host

    try:
        # List a host's subscriptions
        api_instance.get_hosts_host_id_subscriptions(host_id)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->get_hosts_host_id_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| Id of the host | 

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

# **get_hosts_host_id_subscriptions_available_release_versions**
> get_hosts_host_id_subscriptions_available_release_versions(host_id)

Show releases available for the content host

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 'host_id_example' # str | id of host

    try:
        # Show releases available for the content host
        api_instance.get_hosts_host_id_subscriptions_available_release_versions(host_id)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->get_hosts_host_id_subscriptions_available_release_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| id of host | 

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

# **get_hosts_host_id_subscriptions_enabled_repositories**
> get_hosts_host_id_subscriptions_enabled_repositories(host_id)

Show repositories enabled on the host that are known to Katello

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 'host_id_example' # str | id of host

    try:
        # Show repositories enabled on the host that are known to Katello
        api_instance.get_hosts_host_id_subscriptions_enabled_repositories(host_id)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->get_hosts_host_id_subscriptions_enabled_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| id of host | 

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

# **get_hosts_host_id_subscriptions_product_content**
> get_hosts_host_id_subscriptions_product_content(host_id, content_access_mode_all=content_access_mode_all, content_access_mode_env=content_access_mode_env, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

Get content and overrides for the host

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 'host_id_example' # str | Id of the host
    content_access_mode_all = True # bool | Get all content available, not just that provided by subscriptions (optional)
    content_access_mode_env = True # bool | Limit content to just that available in the host's content view version (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # Get content and overrides for the host
        api_instance.get_hosts_host_id_subscriptions_product_content(host_id, content_access_mode_all=content_access_mode_all, content_access_mode_env=content_access_mode_env, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->get_hosts_host_id_subscriptions_product_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the host | 
 **content_access_mode_all** | **bool**| Get all content available, not just that provided by subscriptions | [optional] 
 **content_access_mode_env** | **bool**| Limit content to just that available in the host&#39;s content view version | [optional] 
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

# **post_hosts_subscriptions**
> post_hosts_subscriptions(name, lifecycle_environment_id, content_view_id, uuid=uuid, hypervisor_guest_uuids=hypervisor_guest_uuids, installed_products=installed_products, release_version=release_version, service_level=service_level)

Register a host with subscription and information

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    name = 'name_example' # str | Name of the host
    lifecycle_environment_id = 3.4 # float | Lifecycle Environment ID
    content_view_id = 3.4 # float | Content View ID
    uuid = 'uuid_example' # str | UUID to use for registered host, random uuid is generated if not provided (optional)
    hypervisor_guest_uuids = ['hypervisor_guest_uuids_example'] # List[str] | UUIDs of the virtual guests from the host's hypervisor (optional)
    installed_products = ['installed_products_example'] # List[str] | List of products installed on the host (optional)
    release_version = 'release_version_example' # str | Release version of the content host (optional)
    service_level = 'service_level_example' # str | A service level for auto-healing process, e.g. SELF-SUPPORT (optional)

    try:
        # Register a host with subscription and information
        api_instance.post_hosts_subscriptions(name, lifecycle_environment_id, content_view_id, uuid=uuid, hypervisor_guest_uuids=hypervisor_guest_uuids, installed_products=installed_products, release_version=release_version, service_level=service_level)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->post_hosts_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the host | 
 **lifecycle_environment_id** | **float**| Lifecycle Environment ID | 
 **content_view_id** | **float**| Content View ID | 
 **uuid** | **str**| UUID to use for registered host, random uuid is generated if not provided | [optional] 
 **hypervisor_guest_uuids** | [**List[str]**](str.md)| UUIDs of the virtual guests from the host&#39;s hypervisor | [optional] 
 **installed_products** | [**List[str]**](str.md)| List of products installed on the host | [optional] 
 **release_version** | **str**| Release version of the content host | [optional] 
 **service_level** | **str**| A service level for auto-healing process, e.g. SELF-SUPPORT | [optional] 

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

# **put_hosts_host_id_subscriptions_add_subscriptions**
> put_hosts_host_id_subscriptions_add_subscriptions(host_id, subscriptions)

Add a subscription to a host

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 3.4 # float | Id of the host
    subscriptions = ['subscriptions_example'] # List[str] | Array of subscriptions to add

    try:
        # Add a subscription to a host
        api_instance.put_hosts_host_id_subscriptions_add_subscriptions(host_id, subscriptions)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->put_hosts_host_id_subscriptions_add_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| Id of the host | 
 **subscriptions** | [**List[str]**](str.md)| Array of subscriptions to add | 

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

# **put_hosts_host_id_subscriptions_auto_attach**
> put_hosts_host_id_subscriptions_auto_attach(host_id)

Trigger an auto-attach of subscriptions

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 3.4 # float | Id of the host

    try:
        # Trigger an auto-attach of subscriptions
        api_instance.put_hosts_host_id_subscriptions_auto_attach(host_id)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->put_hosts_host_id_subscriptions_auto_attach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| Id of the host | 

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

# **put_hosts_host_id_subscriptions_content_override**
> put_hosts_host_id_subscriptions_content_override(host_id, value=value, content_overrides=content_overrides, content_overrides_search_search=content_overrides_search_search, content_overrides_search_page=content_overrides_search_page, content_overrides_search_per_page=content_overrides_search_per_page, content_overrides_search_order=content_overrides_search_order, content_overrides_search_full_result=content_overrides_search_full_result, content_overrides_search_sort_by=content_overrides_search_sort_by, content_overrides_search_sort_order=content_overrides_search_sort_order, content_overrides_search_enabled=content_overrides_search_enabled, content_overrides_search_remove=content_overrides_search_remove)

Set content overrides for the host

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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 'host_id_example' # str | Id of the content host
    value = 'value_example' # str | Override to a boolean value or 'default' (optional)
    content_overrides = ['content_overrides_example'] # List[str] | Array of Content override parameters (optional)
    content_overrides_search_search = 'content_overrides_search_search_example' # str | Search string (optional)
    content_overrides_search_page = 3.4 # float | Page number, starting at 1 (optional)
    content_overrides_search_per_page = 3.4 # float | Number of results per page to return (optional)
    content_overrides_search_order = 'content_overrides_search_order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    content_overrides_search_full_result = True # bool | Whether or not to show all results (optional)
    content_overrides_search_sort_by = 'content_overrides_search_sort_by_example' # str | Field to sort the results on (optional)
    content_overrides_search_sort_order = 'content_overrides_search_sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
    content_overrides_search_enabled = True # bool | Set true to override to enabled; Set false to override to disabled.' (optional)
    content_overrides_search_remove = True # bool | Set true to remove an override and reset it to 'default' (optional)

    try:
        # Set content overrides for the host
        api_instance.put_hosts_host_id_subscriptions_content_override(host_id, value=value, content_overrides=content_overrides, content_overrides_search_search=content_overrides_search_search, content_overrides_search_page=content_overrides_search_page, content_overrides_search_per_page=content_overrides_search_per_page, content_overrides_search_order=content_overrides_search_order, content_overrides_search_full_result=content_overrides_search_full_result, content_overrides_search_sort_by=content_overrides_search_sort_by, content_overrides_search_sort_order=content_overrides_search_sort_order, content_overrides_search_enabled=content_overrides_search_enabled, content_overrides_search_remove=content_overrides_search_remove)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->put_hosts_host_id_subscriptions_content_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the content host | 
 **value** | **str**| Override to a boolean value or &#39;default&#39; | [optional] 
 **content_overrides** | [**List[str]**](str.md)| Array of Content override parameters | [optional] 
 **content_overrides_search_search** | **str**| Search string | [optional] 
 **content_overrides_search_page** | **float**| Page number, starting at 1 | [optional] 
 **content_overrides_search_per_page** | **float**| Number of results per page to return | [optional] 
 **content_overrides_search_order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional] 
 **content_overrides_search_full_result** | **bool**| Whether or not to show all results | [optional] 
 **content_overrides_search_sort_by** | **str**| Field to sort the results on | [optional] 
 **content_overrides_search_sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional] 
 **content_overrides_search_enabled** | **bool**| Set true to override to enabled; Set false to override to disabled.&#39; | [optional] 
 **content_overrides_search_remove** | **bool**| Set true to remove an override and reset it to &#39;default&#39; | [optional] 

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

# **put_hosts_host_id_subscriptions_remove_subscriptions**
> put_hosts_host_id_subscriptions_remove_subscriptions(host_id, subscriptions=subscriptions)



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
    api_instance = foreman.HostSubscriptionsApi(api_client)
    host_id = 3.4 # float | Id of the host
    subscriptions = ['subscriptions_example'] # List[str] | Array of subscriptions to remove (optional)

    try:
        api_instance.put_hosts_host_id_subscriptions_remove_subscriptions(host_id, subscriptions=subscriptions)
    except Exception as e:
        print("Exception when calling HostSubscriptionsApi->put_hosts_host_id_subscriptions_remove_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **float**| Id of the host | 
 **subscriptions** | [**List[str]**](str.md)| Array of subscriptions to remove | [optional] 

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

