# pyforeman.HostsBulkActionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_hosts_bulk**](HostsBulkActionsApi.md#delete_hosts_bulk) | **DELETE** /hosts/bulk | Delete multiple hosts
[**post_hosts_bulk_applicable_errata**](HostsBulkActionsApi.md#post_hosts_bulk_applicable_errata) | **POST** /hosts/bulk/applicable_errata | Fetch applicable errata for one or more hosts.
[**post_hosts_bulk_available_incremental_updates**](HostsBulkActionsApi.md#post_hosts_bulk_available_incremental_updates) | **POST** /hosts/bulk/available_incremental_updates | Given a set of hosts and errata, lists the content view versions and environments that need updating.
[**post_hosts_bulk_installable_errata**](HostsBulkActionsApi.md#post_hosts_bulk_installable_errata) | **POST** /hosts/bulk/installable_errata | Fetch installable errata for one or more hosts.
[**post_hosts_bulk_module_streams**](HostsBulkActionsApi.md#post_hosts_bulk_module_streams) | **POST** /hosts/bulk/module_streams | Fetch available module streams for hosts.
[**post_hosts_bulk_traces**](HostsBulkActionsApi.md#post_hosts_bulk_traces) | **POST** /hosts/bulk/traces | Fetch traces for one or more hosts
[**put_hosts_bulk_add_host_collections**](HostsBulkActionsApi.md#put_hosts_bulk_add_host_collections) | **PUT** /hosts/bulk/add_host_collections | Add one or more host collections to one or more hosts
[**put_hosts_bulk_add_subscriptions**](HostsBulkActionsApi.md#put_hosts_bulk_add_subscriptions) | **PUT** /hosts/bulk/add_subscriptions | Add subscriptions to one or more hosts
[**put_hosts_bulk_auto_attach**](HostsBulkActionsApi.md#put_hosts_bulk_auto_attach) | **PUT** /hosts/bulk/auto_attach | Trigger an auto-attach of subscriptions on one or more hosts
[**put_hosts_bulk_change_content_source**](HostsBulkActionsApi.md#put_hosts_bulk_change_content_source) | **PUT** /hosts/bulk/change_content_source | Update the content source for specified hosts and generate the reconfiguration script
[**put_hosts_bulk_content_overrides**](HostsBulkActionsApi.md#put_hosts_bulk_content_overrides) | **PUT** /hosts/bulk/content_overrides | Set content overrides to one or more hosts
[**put_hosts_bulk_destroy**](HostsBulkActionsApi.md#put_hosts_bulk_destroy) | **PUT** /hosts/bulk/destroy | Destroy one or more hosts
[**put_hosts_bulk_environment_content_view**](HostsBulkActionsApi.md#put_hosts_bulk_environment_content_view) | **PUT** /hosts/bulk/environment_content_view | Assign the environment and content view to one or more hosts
[**put_hosts_bulk_release_version**](HostsBulkActionsApi.md#put_hosts_bulk_release_version) | **PUT** /hosts/bulk/release_version | Assign the release version to one or more hosts
[**put_hosts_bulk_remove_host_collections**](HostsBulkActionsApi.md#put_hosts_bulk_remove_host_collections) | **PUT** /hosts/bulk/remove_host_collections | Remove one or more host collections from one or more hosts
[**put_hosts_bulk_remove_subscriptions**](HostsBulkActionsApi.md#put_hosts_bulk_remove_subscriptions) | **PUT** /hosts/bulk/remove_subscriptions | Remove subscriptions from one or more hosts
[**put_hosts_bulk_resolve_traces**](HostsBulkActionsApi.md#put_hosts_bulk_resolve_traces) | **PUT** /hosts/bulk/resolve_traces | Resolve traces for one or more hosts
[**put_hosts_bulk_system_purpose**](HostsBulkActionsApi.md#put_hosts_bulk_system_purpose) | **PUT** /hosts/bulk/system_purpose | Assign system purpose attributes on one or more hosts


# **delete_hosts_bulk**
> delete_hosts_bulk(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Delete multiple hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string describing which hosts to perform the action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform the action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not perform the action on (optional)

try:
    # Delete multiple hosts
    api_instance.delete_hosts_bulk(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->delete_hosts_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string describing which hosts to perform the action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform the action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not perform the action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hosts_bulk_applicable_errata**
> post_hosts_bulk_applicable_errata(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Fetch applicable errata for one or more hosts.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Fetch applicable errata for one or more hosts.
    api_instance.post_hosts_bulk_applicable_errata(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->post_hosts_bulk_applicable_errata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hosts_bulk_available_incremental_updates**
> post_hosts_bulk_available_incremental_updates(organization_id, errata_ids, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Given a set of hosts and errata, lists the content view versions and environments that need updating.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
errata_ids = ['errata_ids_example'] # list[str] | List of Errata ids
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Given a set of hosts and errata, lists the content view versions and environments that need updating.
    api_instance.post_hosts_bulk_available_incremental_updates(organization_id, errata_ids, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->post_hosts_bulk_available_incremental_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **errata_ids** | [**list[str]**](str.md)| List of Errata ids |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hosts_bulk_installable_errata**
> post_hosts_bulk_installable_errata(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Fetch installable errata for one or more hosts.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Fetch installable errata for one or more hosts.
    api_instance.post_hosts_bulk_installable_errata(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->post_hosts_bulk_installable_errata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hosts_bulk_module_streams**
> post_hosts_bulk_module_streams(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Fetch available module streams for hosts.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Fetch available module streams for hosts.
    api_instance.post_hosts_bulk_module_streams(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->post_hosts_bulk_module_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hosts_bulk_traces**
> post_hosts_bulk_traces(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Fetch traces for one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Fetch traces for one or more hosts
    api_instance.post_hosts_bulk_traces(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->post_hosts_bulk_traces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_add_host_collections**
> put_hosts_bulk_add_host_collections(organization_id, host_collection_ids, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Add one or more host collections to one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
host_collection_ids = ['host_collection_ids_example'] # list[str] | List of host collection ids
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Add one or more host collections to one or more hosts
    api_instance.put_hosts_bulk_add_host_collections(organization_id, host_collection_ids, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_add_host_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **host_collection_ids** | [**list[str]**](str.md)| List of host collection ids |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_add_subscriptions**
> put_hosts_bulk_add_subscriptions(organization_id, subscriptions, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Add subscriptions to one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
subscriptions = ['subscriptions_example'] # list[str] | Array of subscriptions to add
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Add subscriptions to one or more hosts
    api_instance.put_hosts_bulk_add_subscriptions(organization_id, subscriptions, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_add_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **subscriptions** | [**list[str]**](str.md)| Array of subscriptions to add |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_auto_attach**
> put_hosts_bulk_auto_attach(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Trigger an auto-attach of subscriptions on one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Trigger an auto-attach of subscriptions on one or more hosts
    api_instance.put_hosts_bulk_auto_attach(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_auto_attach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_change_content_source**
> put_hosts_bulk_change_content_source(host_ids, environment_id, content_view_id, content_source_id, location_id=location_id, organization_id=organization_id)

Update the content source for specified hosts and generate the reconfiguration script



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
host_ids = ['host_ids_example'] # list[str] | The ids of the hosts to alter. Hosts not managed by Katello are ignored
environment_id = 8.14 # float | The id of the lifecycle environment
content_view_id = 8.14 # float | The id of the content view
content_source_id = 8.14 # float | The id of the content source
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Update the content source for specified hosts and generate the reconfiguration script
    api_instance.put_hosts_bulk_change_content_source(host_ids, environment_id, content_view_id, content_source_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_change_content_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_ids** | [**list[str]**](str.md)| The ids of the hosts to alter. Hosts not managed by Katello are ignored |
 **environment_id** | **float**| The id of the lifecycle environment |
 **content_view_id** | **float**| The id of the content view |
 **content_source_id** | **float**| The id of the content source |
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

# **put_hosts_bulk_content_overrides**
> put_hosts_bulk_content_overrides(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, content_overrides=content_overrides)

Set content overrides to one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)
content_overrides = ['content_overrides_example'] # list[str] | Array of Content override parameters (optional)

try:
    # Set content overrides to one or more hosts
    api_instance.put_hosts_bulk_content_overrides(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, content_overrides=content_overrides)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_content_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]
 **content_overrides** | [**list[str]**](str.md)| Array of Content override parameters | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_destroy**
> put_hosts_bulk_destroy(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Destroy one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Destroy one or more hosts
    api_instance.put_hosts_bulk_destroy(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_environment_content_view**
> put_hosts_bulk_environment_content_view(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, environment_id=environment_id, content_view_id=content_view_id)

Assign the environment and content view to one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)
environment_id = 8.14 # float |  (optional)
content_view_id = 8.14 # float |  (optional)

try:
    # Assign the environment and content view to one or more hosts
    api_instance.put_hosts_bulk_environment_content_view(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, environment_id=environment_id, content_view_id=content_view_id)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_environment_content_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]
 **environment_id** | **float**|  | [optional]
 **content_view_id** | **float**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_release_version**
> put_hosts_bulk_release_version(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, release_version=release_version)

Assign the release version to one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)
release_version = 'release_version_example' # str | content release version (optional)

try:
    # Assign the release version to one or more hosts
    api_instance.put_hosts_bulk_release_version(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, release_version=release_version)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_release_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]
 **release_version** | **str**| content release version | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_remove_host_collections**
> put_hosts_bulk_remove_host_collections(organization_id, host_collection_ids, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Remove one or more host collections from one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
host_collection_ids = ['host_collection_ids_example'] # list[str] | List of host collection ids
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Remove one or more host collections from one or more hosts
    api_instance.put_hosts_bulk_remove_host_collections(organization_id, host_collection_ids, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_remove_host_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **host_collection_ids** | [**list[str]**](str.md)| List of host collection ids |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_remove_subscriptions**
> put_hosts_bulk_remove_subscriptions(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, subscriptions=subscriptions)

Remove subscriptions from one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)
subscriptions = ['subscriptions_example'] # list[str] | Array of subscriptions to remove (optional)

try:
    # Remove subscriptions from one or more hosts
    api_instance.put_hosts_bulk_remove_subscriptions(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, subscriptions=subscriptions)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_remove_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]
 **subscriptions** | [**list[str]**](str.md)| Array of subscriptions to remove | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_resolve_traces**
> put_hosts_bulk_resolve_traces(organization_id, trace_ids, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)

Resolve traces for one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
trace_ids = ['trace_ids_example'] # list[str] | Array of Trace IDs
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)

try:
    # Resolve traces for one or more hosts
    api_instance.put_hosts_bulk_resolve_traces(organization_id, trace_ids, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_resolve_traces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **trace_ids** | [**list[str]**](str.md)| Array of Trace IDs |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_hosts_bulk_system_purpose**
> put_hosts_bulk_system_purpose(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, service_level=service_level, purpose_role=purpose_role, purpose_usage=purpose_usage, purpose_addons=purpose_addons)

Assign system purpose attributes on one or more hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostsBulkActionsApi()
organization_id = 8.14 # float | ID of the organization
location_id = 8.14 # float | Set the current location context for the request (optional)
included_search = 'included_search_example' # str | Search string for hosts to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of host ids to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of host ids to exclude and not run an action on (optional)
service_level = 'service_level_example' # str | Service level of host (optional)
purpose_role = 'purpose_role_example' # str | Role of host (optional)
purpose_usage = 'purpose_usage_example' # str | Usage of host (optional)
purpose_addons = ['purpose_addons_example'] # list[str] | Sets the system add-ons (optional)

try:
    # Assign system purpose attributes on one or more hosts
    api_instance.put_hosts_bulk_system_purpose(organization_id, location_id=location_id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, service_level=service_level, purpose_role=purpose_role, purpose_usage=purpose_usage, purpose_addons=purpose_addons)
except ApiException as e:
    print("Exception when calling HostsBulkActionsApi->put_hosts_bulk_system_purpose: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **included_search** | **str**| Search string for hosts to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of host ids to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of host ids to exclude and not run an action on | [optional]
 **service_level** | **str**| Service level of host | [optional]
 **purpose_role** | **str**| Role of host | [optional]
 **purpose_usage** | **str**| Usage of host | [optional]
 **purpose_addons** | [**list[str]**](str.md)| Sets the system add-ons | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
