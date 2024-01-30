# pyforeman.SubscriptionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_activation_keys_activation_key_id_subscriptions**](SubscriptionsApi.md#get_activation_keys_activation_key_id_subscriptions) | **GET** /activation_keys/{activation_key_id}/subscriptions | List an activation key&#39;s subscriptions
[**get_organizations_organization_id_subscriptions**](SubscriptionsApi.md#get_organizations_organization_id_subscriptions) | **GET** /organizations/{organization_id}/subscriptions | List organization subscriptions
[**get_organizations_organization_id_subscriptions_id**](SubscriptionsApi.md#get_organizations_organization_id_subscriptions_id) | **GET** /organizations/{organization_id}/subscriptions/{id} | Show a subscription
[**get_organizations_organization_id_subscriptions_manifest_history**](SubscriptionsApi.md#get_organizations_organization_id_subscriptions_manifest_history) | **GET** /organizations/{organization_id}/subscriptions/manifest_history | obtain manifest history for subscriptions
[**get_subscriptions**](SubscriptionsApi.md#get_subscriptions) | **GET** /subscriptions | List subscriptions
[**get_subscriptions_id**](SubscriptionsApi.md#get_subscriptions_id) | **GET** /subscriptions/{id} | Show a subscription
[**post_organizations_organization_id_subscriptions_delete_manifest**](SubscriptionsApi.md#post_organizations_organization_id_subscriptions_delete_manifest) | **POST** /organizations/{organization_id}/subscriptions/delete_manifest | Delete manifest from Red Hat provider
[**post_organizations_organization_id_subscriptions_upload**](SubscriptionsApi.md#post_organizations_organization_id_subscriptions_upload) | **POST** /organizations/{organization_id}/subscriptions/upload | Upload a subscription manifest
[**put_organizations_organization_id_subscriptions_refresh_manifest**](SubscriptionsApi.md#put_organizations_organization_id_subscriptions_refresh_manifest) | **PUT** /organizations/{organization_id}/subscriptions/refresh_manifest | Refresh previously imported manifest for Red Hat provider


# **get_activation_keys_activation_key_id_subscriptions**
> get_activation_keys_activation_key_id_subscriptions(activation_key_id, organization_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_id=host_id, name=name, available_for=available_for, match_host=match_host, match_installed=match_installed, no_overlap=no_overlap)

List an activation key's subscriptions



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
activation_key_id = 'activation_key_id_example' # str | Activation key ID
organization_id = 8.14 # float | Organization ID
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
host_id = 'host_id_example' # str | id of a host (optional)
name = 'name_example' # str | name of the subscription (optional)
available_for = 'available_for_example' # str | Object to show subscriptions available for, either 'host' or 'activation_key' (optional)
match_host = true # bool | Ignore subscriptions that are unavailable to the specified host (optional)
match_installed = true # bool | Return subscriptions that match installed products of the specified host (optional)
no_overlap = true # bool | Return subscriptions which do not overlap with a currently-attached subscription (optional)

try:
    # List an activation key's subscriptions
    api_instance.get_activation_keys_activation_key_id_subscriptions(activation_key_id, organization_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_id=host_id, name=name, available_for=available_for, match_host=match_host, match_installed=match_installed, no_overlap=no_overlap)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_activation_keys_activation_key_id_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_key_id** | **str**| Activation key ID |
 **organization_id** | **float**| Organization ID |
 **search** | **str**| Search string | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return | [optional]
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional]
 **full_result** | **bool**| Whether or not to show all results | [optional]
 **sort_by** | **str**| Field to sort the results on | [optional]
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional]
 **host_id** | **str**| id of a host | [optional]
 **name** | **str**| name of the subscription | [optional]
 **available_for** | **str**| Object to show subscriptions available for, either &#39;host&#39; or &#39;activation_key&#39; | [optional]
 **match_host** | **bool**| Ignore subscriptions that are unavailable to the specified host | [optional]
 **match_installed** | **bool**| Return subscriptions that match installed products of the specified host | [optional]
 **no_overlap** | **bool**| Return subscriptions which do not overlap with a currently-attached subscription | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_subscriptions**
> get_organizations_organization_id_subscriptions(organization_id, activation_key_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_id=host_id, name=name, available_for=available_for, match_host=match_host, match_installed=match_installed, no_overlap=no_overlap)

List organization subscriptions



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
organization_id = 8.14 # float | Organization ID
activation_key_id = 'activation_key_id_example' # str | Activation key ID
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
host_id = 'host_id_example' # str | id of a host (optional)
name = 'name_example' # str | name of the subscription (optional)
available_for = 'available_for_example' # str | Object to show subscriptions available for, either 'host' or 'activation_key' (optional)
match_host = true # bool | Ignore subscriptions that are unavailable to the specified host (optional)
match_installed = true # bool | Return subscriptions that match installed products of the specified host (optional)
no_overlap = true # bool | Return subscriptions which do not overlap with a currently-attached subscription (optional)

try:
    # List organization subscriptions
    api_instance.get_organizations_organization_id_subscriptions(organization_id, activation_key_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_id=host_id, name=name, available_for=available_for, match_host=match_host, match_installed=match_installed, no_overlap=no_overlap)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_organizations_organization_id_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |
 **activation_key_id** | **str**| Activation key ID |
 **search** | **str**| Search string | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return | [optional]
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional]
 **full_result** | **bool**| Whether or not to show all results | [optional]
 **sort_by** | **str**| Field to sort the results on | [optional]
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional]
 **host_id** | **str**| id of a host | [optional]
 **name** | **str**| name of the subscription | [optional]
 **available_for** | **str**| Object to show subscriptions available for, either &#39;host&#39; or &#39;activation_key&#39; | [optional]
 **match_host** | **bool**| Ignore subscriptions that are unavailable to the specified host | [optional]
 **match_installed** | **bool**| Return subscriptions that match installed products of the specified host | [optional]
 **no_overlap** | **bool**| Return subscriptions which do not overlap with a currently-attached subscription | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_subscriptions_id**
> get_organizations_organization_id_subscriptions_id(organization_id, id)

Show a subscription



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
organization_id = 8.14 # float | Organization identifier
id = 8.14 # float | Subscription identifier

try:
    # Show a subscription
    api_instance.get_organizations_organization_id_subscriptions_id(organization_id, id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_organizations_organization_id_subscriptions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier |
 **id** | **float**| Subscription identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_subscriptions_manifest_history**
> get_organizations_organization_id_subscriptions_manifest_history(organization_id)

obtain manifest history for subscriptions



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
organization_id = 8.14 # float | Organization ID

try:
    # obtain manifest history for subscriptions
    api_instance.get_organizations_organization_id_subscriptions_manifest_history(organization_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_organizations_organization_id_subscriptions_manifest_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> get_subscriptions(organization_id, activation_key_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_id=host_id, name=name, available_for=available_for, match_host=match_host, match_installed=match_installed, no_overlap=no_overlap)

List subscriptions



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
organization_id = 8.14 # float | Organization ID
activation_key_id = 'activation_key_id_example' # str | Activation key ID
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
host_id = 'host_id_example' # str | id of a host (optional)
name = 'name_example' # str | name of the subscription (optional)
available_for = 'available_for_example' # str | Object to show subscriptions available for, either 'host' or 'activation_key' (optional)
match_host = true # bool | Ignore subscriptions that are unavailable to the specified host (optional)
match_installed = true # bool | Return subscriptions that match installed products of the specified host (optional)
no_overlap = true # bool | Return subscriptions which do not overlap with a currently-attached subscription (optional)

try:
    # List subscriptions
    api_instance.get_subscriptions(organization_id, activation_key_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, host_id=host_id, name=name, available_for=available_for, match_host=match_host, match_installed=match_installed, no_overlap=no_overlap)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |
 **activation_key_id** | **str**| Activation key ID |
 **search** | **str**| Search string | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return | [optional]
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional]
 **full_result** | **bool**| Whether or not to show all results | [optional]
 **sort_by** | **str**| Field to sort the results on | [optional]
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional]
 **host_id** | **str**| id of a host | [optional]
 **name** | **str**| name of the subscription | [optional]
 **available_for** | **str**| Object to show subscriptions available for, either &#39;host&#39; or &#39;activation_key&#39; | [optional]
 **match_host** | **bool**| Ignore subscriptions that are unavailable to the specified host | [optional]
 **match_installed** | **bool**| Return subscriptions that match installed products of the specified host | [optional]
 **no_overlap** | **bool**| Return subscriptions which do not overlap with a currently-attached subscription | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_id**
> get_subscriptions_id(id, organization_id)

Show a subscription



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
id = 8.14 # float | Subscription identifier
organization_id = 8.14 # float | Organization identifier

try:
    # Show a subscription
    api_instance.get_subscriptions_id(id, organization_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Subscription identifier |
 **organization_id** | **float**| Organization identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_organization_id_subscriptions_delete_manifest**
> post_organizations_organization_id_subscriptions_delete_manifest(organization_id)

Delete manifest from Red Hat provider



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
organization_id = 8.14 # float | Organization id

try:
    # Delete manifest from Red Hat provider
    api_instance.post_organizations_organization_id_subscriptions_delete_manifest(organization_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->post_organizations_organization_id_subscriptions_delete_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_organization_id_subscriptions_upload**
> post_organizations_organization_id_subscriptions_upload(organization_id, content)

Upload a subscription manifest



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
organization_id = 8.14 # float | Organization id
content = '/path/to/file.txt' # file | Subscription manifest file

try:
    # Upload a subscription manifest
    api_instance.post_organizations_organization_id_subscriptions_upload(organization_id, content)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->post_organizations_organization_id_subscriptions_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization id |
 **content** | **file**| Subscription manifest file |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_organization_id_subscriptions_refresh_manifest**
> put_organizations_organization_id_subscriptions_refresh_manifest(organization_id)

Refresh previously imported manifest for Red Hat provider



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.SubscriptionsApi()
organization_id = 8.14 # float | Organization id

try:
    # Refresh previously imported manifest for Red Hat provider
    api_instance.put_organizations_organization_id_subscriptions_refresh_manifest(organization_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->put_organizations_organization_id_subscriptions_refresh_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
