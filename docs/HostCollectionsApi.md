# pyforeman.HostCollectionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_host_collections_id**](HostCollectionsApi.md#delete_host_collections_id) | **DELETE** /host_collections/{id} | Destroy a host collection
[**get_activation_keys_activation_key_id_host_collections**](HostCollectionsApi.md#get_activation_keys_activation_key_id_host_collections) | **GET** /activation_keys/{activation_key_id}/host_collections | List host collections in an activation key
[**get_host_collections**](HostCollectionsApi.md#get_host_collections) | **GET** /host_collections | List host collections
[**get_host_collections_id**](HostCollectionsApi.md#get_host_collections_id) | **GET** /host_collections/{id} | Show a host collection
[**get_organizations_organization_id_host_collections**](HostCollectionsApi.md#get_organizations_organization_id_host_collections) | **GET** /organizations/{organization_id}/host_collections | List host collections within an organization
[**post_host_collections**](HostCollectionsApi.md#post_host_collections) | **POST** /host_collections | Create a host collection
[**post_host_collections_id_copy**](HostCollectionsApi.md#post_host_collections_id_copy) | **POST** /host_collections/{id}/copy | Make copy of a host collection
[**post_organizations_organization_id_host_collections**](HostCollectionsApi.md#post_organizations_organization_id_host_collections) | **POST** /organizations/{organization_id}/host_collections | Create a host collection
[**put_host_collections_id**](HostCollectionsApi.md#put_host_collections_id) | **PUT** /host_collections/{id} | Update a host collection
[**put_host_collections_id_add_hosts**](HostCollectionsApi.md#put_host_collections_id_add_hosts) | **PUT** /host_collections/{id}/add_hosts | Add host to the host collection
[**put_host_collections_id_remove_hosts**](HostCollectionsApi.md#put_host_collections_id_remove_hosts) | **PUT** /host_collections/{id}/remove_hosts | Remove hosts from the host collection


# **delete_host_collections_id**
> delete_host_collections_id(id)

Destroy a host collection



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
id = 8.14 # float | Id of the host collection

try:
    # Destroy a host collection
    api_instance.delete_host_collections_id(id)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->delete_host_collections_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the host collection |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activation_keys_activation_key_id_host_collections**
> get_activation_keys_activation_key_id_host_collections(activation_key_id, organization_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, host_id=host_id, available_for=available_for)

List host collections in an activation key



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
activation_key_id = 'activation_key_id_example' # str | activation key identifier
organization_id = 8.14 # float | organization identifier
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
name = 'name_example' # str | host collection name to filter by (optional)
host_id = 8.14 # float | Filter products by host id (optional)
available_for = 'available_for_example' # str | Interpret specified object to return only Host Collections that can be associated with specified object. The value 'host' is supported. (optional)

try:
    # List host collections in an activation key
    api_instance.get_activation_keys_activation_key_id_host_collections(activation_key_id, organization_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, host_id=host_id, available_for=available_for)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->get_activation_keys_activation_key_id_host_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activation_key_id** | **str**| activation key identifier |
 **organization_id** | **float**| organization identifier |
 **search** | **str**| Search string | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return | [optional]
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional]
 **full_result** | **bool**| Whether or not to show all results | [optional]
 **sort_by** | **str**| Field to sort the results on | [optional]
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional]
 **name** | **str**| host collection name to filter by | [optional]
 **host_id** | **float**| Filter products by host id | [optional]
 **available_for** | **str**| Interpret specified object to return only Host Collections that can be associated with specified object. The value &#39;host&#39; is supported. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_collections**
> get_host_collections(organization_id, activation_key_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, host_id=host_id, available_for=available_for)

List host collections



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
organization_id = 8.14 # float | organization identifier
activation_key_id = 'activation_key_id_example' # str | activation key identifier
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
name = 'name_example' # str | host collection name to filter by (optional)
host_id = 8.14 # float | Filter products by host id (optional)
available_for = 'available_for_example' # str | Interpret specified object to return only Host Collections that can be associated with specified object. The value 'host' is supported. (optional)

try:
    # List host collections
    api_instance.get_host_collections(organization_id, activation_key_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, host_id=host_id, available_for=available_for)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->get_host_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **activation_key_id** | **str**| activation key identifier |
 **search** | **str**| Search string | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return | [optional]
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional]
 **full_result** | **bool**| Whether or not to show all results | [optional]
 **sort_by** | **str**| Field to sort the results on | [optional]
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional]
 **name** | **str**| host collection name to filter by | [optional]
 **host_id** | **float**| Filter products by host id | [optional]
 **available_for** | **str**| Interpret specified object to return only Host Collections that can be associated with specified object. The value &#39;host&#39; is supported. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_collections_id**
> get_host_collections_id(id, organization_id=organization_id)

Show a host collection



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
id = 8.14 # float | Id of the host collection
organization_id = 8.14 # float | organization identifier (optional)

try:
    # Show a host collection
    api_instance.get_host_collections_id(id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->get_host_collections_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the host collection |
 **organization_id** | **float**| organization identifier | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_host_collections**
> get_organizations_organization_id_host_collections(organization_id, activation_key_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, host_id=host_id, available_for=available_for)

List host collections within an organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
organization_id = 8.14 # float | organization identifier
activation_key_id = 'activation_key_id_example' # str | activation key identifier
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)
name = 'name_example' # str | host collection name to filter by (optional)
host_id = 8.14 # float | Filter products by host id (optional)
available_for = 'available_for_example' # str | Interpret specified object to return only Host Collections that can be associated with specified object. The value 'host' is supported. (optional)

try:
    # List host collections within an organization
    api_instance.get_organizations_organization_id_host_collections(organization_id, activation_key_id, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order, name=name, host_id=host_id, available_for=available_for)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->get_organizations_organization_id_host_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **activation_key_id** | **str**| activation key identifier |
 **search** | **str**| Search string | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **float**| Number of results per page to return | [optional]
 **order** | **str**| Sort field and order, eg. &#39;id DESC&#39; | [optional]
 **full_result** | **bool**| Whether or not to show all results | [optional]
 **sort_by** | **str**| Field to sort the results on | [optional]
 **sort_order** | **str**| How to order the sorted results (e.g. ASC for ascending) | [optional]
 **name** | **str**| host collection name to filter by | [optional]
 **host_id** | **float**| Filter products by host id | [optional]
 **available_for** | **str**| Interpret specified object to return only Host Collections that can be associated with specified object. The value &#39;host&#39; is supported. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_host_collections**
> post_host_collections(organization_id, name, description=description, host_ids=host_ids, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts)

Create a host collection



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
organization_id = 8.14 # float | organization identifier
name = 'name_example' # str | Host Collection name
description = 'description_example' # str |  (optional)
host_ids = ['host_ids_example'] # list[str] | List of host ids to replace the hosts in host collection (optional)
max_hosts = 8.14 # float | Maximum number of hosts in the host collection (optional)
unlimited_hosts = true # bool | Whether or not the host collection may have unlimited hosts (optional)

try:
    # Create a host collection
    api_instance.post_host_collections(organization_id, name, description=description, host_ids=host_ids, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->post_host_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **name** | **str**| Host Collection name |
 **description** | **str**|  | [optional]
 **host_ids** | [**list[str]**](str.md)| List of host ids to replace the hosts in host collection | [optional]
 **max_hosts** | **float**| Maximum number of hosts in the host collection | [optional]
 **unlimited_hosts** | **bool**| Whether or not the host collection may have unlimited hosts | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_host_collections_id_copy**
> post_host_collections_id_copy(id, name)

Make copy of a host collection



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
id = 8.14 # float | ID of the host collection
name = 'name_example' # str | New host collection name

try:
    # Make copy of a host collection
    api_instance.post_host_collections_id_copy(id, name)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->post_host_collections_id_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the host collection |
 **name** | **str**| New host collection name |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_organization_id_host_collections**
> post_organizations_organization_id_host_collections(organization_id, name, description=description, host_ids=host_ids, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts)

Create a host collection



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
organization_id = 8.14 # float | organization identifier
name = 'name_example' # str | Host Collection name
description = 'description_example' # str |  (optional)
host_ids = ['host_ids_example'] # list[str] | List of host ids to replace the hosts in host collection (optional)
max_hosts = 8.14 # float | Maximum number of hosts in the host collection (optional)
unlimited_hosts = true # bool | Whether or not the host collection may have unlimited hosts (optional)

try:
    # Create a host collection
    api_instance.post_organizations_organization_id_host_collections(organization_id, name, description=description, host_ids=host_ids, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->post_organizations_organization_id_host_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **name** | **str**| Host Collection name |
 **description** | **str**|  | [optional]
 **host_ids** | [**list[str]**](str.md)| List of host ids to replace the hosts in host collection | [optional]
 **max_hosts** | **float**| Maximum number of hosts in the host collection | [optional]
 **unlimited_hosts** | **bool**| Whether or not the host collection may have unlimited hosts | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_host_collections_id**
> put_host_collections_id(id, name=name, description=description, host_ids=host_ids, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts)

Update a host collection



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
id = 8.14 # float | Id of the host collection
name = 'name_example' # str | Host Collection name (optional)
description = 'description_example' # str |  (optional)
host_ids = ['host_ids_example'] # list[str] | List of host ids to replace the hosts in host collection (optional)
max_hosts = 8.14 # float | Maximum number of hosts in the host collection (optional)
unlimited_hosts = true # bool | Whether or not the host collection may have unlimited hosts (optional)

try:
    # Update a host collection
    api_instance.put_host_collections_id(id, name=name, description=description, host_ids=host_ids, max_hosts=max_hosts, unlimited_hosts=unlimited_hosts)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->put_host_collections_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the host collection |
 **name** | **str**| Host Collection name | [optional]
 **description** | **str**|  | [optional]
 **host_ids** | [**list[str]**](str.md)| List of host ids to replace the hosts in host collection | [optional]
 **max_hosts** | **float**| Maximum number of hosts in the host collection | [optional]
 **unlimited_hosts** | **bool**| Whether or not the host collection may have unlimited hosts | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_host_collections_id_add_hosts**
> put_host_collections_id_add_hosts(id, host_ids=host_ids)

Add host to the host collection



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
id = 8.14 # float | Id of the host collection
host_ids = ['host_ids_example'] # list[str] | Array of host ids (optional)

try:
    # Add host to the host collection
    api_instance.put_host_collections_id_add_hosts(id, host_ids=host_ids)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->put_host_collections_id_add_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the host collection |
 **host_ids** | [**list[str]**](str.md)| Array of host ids | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_host_collections_id_remove_hosts**
> put_host_collections_id_remove_hosts(id, host_ids=host_ids)

Remove hosts from the host collection



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.HostCollectionsApi()
id = 8.14 # float | Id of the host collection
host_ids = ['host_ids_example'] # list[str] | Array of host ids (optional)

try:
    # Remove hosts from the host collection
    api_instance.put_host_collections_id_remove_hosts(id, host_ids=host_ids)
except ApiException as e:
    print("Exception when calling HostCollectionsApi->put_host_collections_id_remove_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Id of the host collection |
 **host_ids** | [**list[str]**](str.md)| Array of host ids | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
