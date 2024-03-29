# pyforeman.UpstreamSubscriptionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organizations_organization_id_upstream_subscriptions**](UpstreamSubscriptionsApi.md#delete_organizations_organization_id_upstream_subscriptions) | **DELETE** /organizations/{organization_id}/upstream_subscriptions | Remove one or more subscriptions from an upstream manifest
[**get_organizations_organization_id_upstream_subscriptions**](UpstreamSubscriptionsApi.md#get_organizations_organization_id_upstream_subscriptions) | **GET** /organizations/{organization_id}/upstream_subscriptions | List available subscriptions from Red Hat Subscription Management
[**get_organizations_organization_id_upstream_subscriptions_ping**](UpstreamSubscriptionsApi.md#get_organizations_organization_id_upstream_subscriptions_ping) | **GET** /organizations/{organization_id}/upstream_subscriptions/ping | Check if a connection can be made to Red Hat Subscription Management.
[**post_organizations_organization_id_upstream_subscriptions**](UpstreamSubscriptionsApi.md#post_organizations_organization_id_upstream_subscriptions) | **POST** /organizations/{organization_id}/upstream_subscriptions | Add subscriptions consumed by a manifest from Red Hat Subscription Management
[**put_organizations_organization_id_upstream_subscriptions**](UpstreamSubscriptionsApi.md#put_organizations_organization_id_upstream_subscriptions) | **PUT** /organizations/{organization_id}/upstream_subscriptions | Update the quantity of one or more subscriptions on an upstream allocation


# **delete_organizations_organization_id_upstream_subscriptions**
> delete_organizations_organization_id_upstream_subscriptions(organization_id, pool_ids)

Remove one or more subscriptions from an upstream manifest



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UpstreamSubscriptionsApi()
organization_id = 8.14 # float | Organization ID
pool_ids = ['pool_ids_example'] # list[str] | Array of local pool IDs. Only pools originating upstream are accepted.

try:
    # Remove one or more subscriptions from an upstream manifest
    api_instance.delete_organizations_organization_id_upstream_subscriptions(organization_id, pool_ids)
except ApiException as e:
    print("Exception when calling UpstreamSubscriptionsApi->delete_organizations_organization_id_upstream_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |
 **pool_ids** | [**list[str]**](str.md)| Array of local pool IDs. Only pools originating upstream are accepted. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_upstream_subscriptions**
> get_organizations_organization_id_upstream_subscriptions(organization_id, page=page, per_page=per_page, order=order, sort_by=sort_by, pool_ids=pool_ids, quantities_only=quantities_only, attachable=attachable)

List available subscriptions from Red Hat Subscription Management



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UpstreamSubscriptionsApi()
organization_id = 8.14 # float | Organization ID
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return. (optional)
order = 'order_example' # str | The order to sort the results in. ['asc', 'desc'] Defaults to 'desc'. (optional)
sort_by = 'sort_by_example' # str | The field to sort the data by. Defaults to the created date. (optional)
pool_ids = ['pool_ids_example'] # list[str] | Return only the upstream pools which map to the given Katello pool IDs (optional)
quantities_only = true # bool | Only returns id and quantity fields (optional)
attachable = true # bool | Return only subscriptions which can be attached to the upstream allocation (optional)

try:
    # List available subscriptions from Red Hat Subscription Management
    api_instance.get_organizations_organization_id_upstream_subscriptions(organization_id, page=page, per_page=per_page, order=order, sort_by=sort_by, pool_ids=pool_ids, quantities_only=quantities_only, attachable=attachable)
except ApiException as e:
    print("Exception when calling UpstreamSubscriptionsApi->get_organizations_organization_id_upstream_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return. | [optional]
 **order** | **str**| The order to sort the results in. [&#39;asc&#39;, &#39;desc&#39;] Defaults to &#39;desc&#39;. | [optional]
 **sort_by** | **str**| The field to sort the data by. Defaults to the created date. | [optional]
 **pool_ids** | [**list[str]**](str.md)| Return only the upstream pools which map to the given Katello pool IDs | [optional]
 **quantities_only** | **bool**| Only returns id and quantity fields | [optional]
 **attachable** | **bool**| Return only subscriptions which can be attached to the upstream allocation | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_upstream_subscriptions_ping**
> get_organizations_organization_id_upstream_subscriptions_ping(organization_id)

Check if a connection can be made to Red Hat Subscription Management.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UpstreamSubscriptionsApi()
organization_id = 8.14 # float |

try:
    # Check if a connection can be made to Red Hat Subscription Management.
    api_instance.get_organizations_organization_id_upstream_subscriptions_ping(organization_id)
except ApiException as e:
    print("Exception when calling UpstreamSubscriptionsApi->get_organizations_organization_id_upstream_subscriptions_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_organization_id_upstream_subscriptions**
> post_organizations_organization_id_upstream_subscriptions(organization_id, pools)

Add subscriptions consumed by a manifest from Red Hat Subscription Management



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UpstreamSubscriptionsApi()
organization_id = 8.14 # float | Organization ID
pools = ['pools_example'] # list[str] | Array of pools to add

try:
    # Add subscriptions consumed by a manifest from Red Hat Subscription Management
    api_instance.post_organizations_organization_id_upstream_subscriptions(organization_id, pools)
except ApiException as e:
    print("Exception when calling UpstreamSubscriptionsApi->post_organizations_organization_id_upstream_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |
 **pools** | [**list[str]**](str.md)| Array of pools to add |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_organization_id_upstream_subscriptions**
> put_organizations_organization_id_upstream_subscriptions(organization_id, pools)

Update the quantity of one or more subscriptions on an upstream allocation



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.UpstreamSubscriptionsApi()
organization_id = 8.14 # float | Organization ID
pools = ['pools_example'] # list[str] | Array of Pools to be updated. Only pools originating upstream are accepted.

try:
    # Update the quantity of one or more subscriptions on an upstream allocation
    api_instance.put_organizations_organization_id_upstream_subscriptions(organization_id, pools)
except ApiException as e:
    print("Exception when calling UpstreamSubscriptionsApi->put_organizations_organization_id_upstream_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization ID |
 **pools** | [**list[str]**](str.md)| Array of Pools to be updated. Only pools originating upstream are accepted. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
