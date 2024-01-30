# pyforeman.LifecycleEnvironmentsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_environments_id**](LifecycleEnvironmentsApi.md#delete_environments_id) | **DELETE** /environments/{id} | Destroy an environment
[**delete_organizations_organization_id_environments_id**](LifecycleEnvironmentsApi.md#delete_organizations_organization_id_environments_id) | **DELETE** /organizations/{organization_id}/environments/{id} | Destroy an environment in an organization
[**get_environments**](LifecycleEnvironmentsApi.md#get_environments) | **GET** /environments | List environments in an organization
[**get_environments_id**](LifecycleEnvironmentsApi.md#get_environments_id) | **GET** /environments/{id} | Show an environment
[**get_organizations_organization_id_environments**](LifecycleEnvironmentsApi.md#get_organizations_organization_id_environments) | **GET** /organizations/{organization_id}/environments | List environments in an organization
[**get_organizations_organization_id_environments_environment_id**](LifecycleEnvironmentsApi.md#get_organizations_organization_id_environments_environment_id) | **GET** /organizations/{organization_id}/environments/{environment_id} | Show an environment
[**get_organizations_organization_id_environments_paths**](LifecycleEnvironmentsApi.md#get_organizations_organization_id_environments_paths) | **GET** /organizations/{organization_id}/environments/paths | List environment paths
[**post_environments**](LifecycleEnvironmentsApi.md#post_environments) | **POST** /environments | Create an environment
[**post_organizations_organization_id_environments**](LifecycleEnvironmentsApi.md#post_organizations_organization_id_environments) | **POST** /organizations/{organization_id}/environments | Create an environment in an organization
[**put_environments_id**](LifecycleEnvironmentsApi.md#put_environments_id) | **PUT** /environments/{id} | Update an environment
[**put_organizations_organization_id_environments_id**](LifecycleEnvironmentsApi.md#put_organizations_organization_id_environments_id) | **PUT** /organizations/{organization_id}/environments/{id} | Update an environment in an organization


# **delete_environments_id**
> delete_environments_id(id, organization_id)

Destroy an environment



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
id = 8.14 # float | ID of the environment
organization_id = 8.14 # float | organization identifier

try:
    # Destroy an environment
    api_instance.delete_environments_id(id, organization_id)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->delete_environments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the environment |
 **organization_id** | **float**| organization identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organizations_organization_id_environments_id**
> delete_organizations_organization_id_environments_id(id, organization_id)

Destroy an environment in an organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
id = 8.14 # float | ID of the environment
organization_id = 8.14 # float | organization identifier

try:
    # Destroy an environment in an organization
    api_instance.delete_organizations_organization_id_environments_id(id, organization_id)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->delete_organizations_organization_id_environments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the environment |
 **organization_id** | **float**| organization identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environments**
> get_environments(organization_id, library=library, name=name, label=label, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List environments in an organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
organization_id = 8.14 # float | organization identifier
library = true # bool | set true if you want to see only library environments (optional)
name = 'name_example' # str | filter only environments containing this name (optional)
label = 'label_example' # str | filter only environments containing this label (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List environments in an organization
    api_instance.get_environments(organization_id, library=library, name=name, label=label, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->get_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **library** | **bool**| set true if you want to see only library environments | [optional]
 **name** | **str**| filter only environments containing this name | [optional]
 **label** | **str**| filter only environments containing this label | [optional]
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environments_id**
> get_environments_id(id, organization_id)

Show an environment



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
id = 8.14 # float | ID of the environment
organization_id = 8.14 # float | ID of the organization

try:
    # Show an environment
    api_instance.get_environments_id(id, organization_id)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->get_environments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the environment |
 **organization_id** | **float**| ID of the organization |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_environments**
> get_organizations_organization_id_environments(organization_id, library=library, name=name, label=label, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List environments in an organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
organization_id = 8.14 # float | organization identifier
library = true # bool | set true if you want to see only library environments (optional)
name = 'name_example' # str | filter only environments containing this name (optional)
label = 'label_example' # str | filter only environments containing this label (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List environments in an organization
    api_instance.get_organizations_organization_id_environments(organization_id, library=library, name=name, label=label, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->get_organizations_organization_id_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **library** | **bool**| set true if you want to see only library environments | [optional]
 **name** | **str**| filter only environments containing this name | [optional]
 **label** | **str**| filter only environments containing this label | [optional]
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

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_environments_environment_id**
> get_organizations_organization_id_environments_environment_id(organization_id, environment_id, id)

Show an environment



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
organization_id = 8.14 # float | ID of the organization
environment_id = 8.14 # float |
id = 8.14 # float | ID of the environment

try:
    # Show an environment
    api_instance.get_organizations_organization_id_environments_environment_id(organization_id, environment_id, id)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->get_organizations_organization_id_environments_environment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of the organization |
 **environment_id** | **float**|  |
 **id** | **float**| ID of the environment |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_environments_paths**
> get_organizations_organization_id_environments_paths(organization_id, content_source_id=content_source_id, permission_type=permission_type)

List environment paths



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
organization_id = 8.14 # float | organization identifier
content_source_id = 8.14 # float | Show whether each lifecycle environment is associated with the given Smart Proxy id. (optional)
permission_type = 'permission_type_example' # str |       The associated permission type. One of (readable | promotable)       Default: readable  (optional)

try:
    # List environment paths
    api_instance.get_organizations_organization_id_environments_paths(organization_id, content_source_id=content_source_id, permission_type=permission_type)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->get_organizations_organization_id_environments_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **content_source_id** | **float**| Show whether each lifecycle environment is associated with the given Smart Proxy id. | [optional]
 **permission_type** | **str**|       The associated permission type. One of (readable | promotable)       Default: readable  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_environments**
> post_environments(organization_id, name, prior_id, label=label, description=description, registry_name_pattern=registry_name_pattern, registry_unauthenticated_pull=registry_unauthenticated_pull)

Create an environment



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
organization_id = 8.14 # float | name of organization
name = 'name_example' # str | name of the environment
prior_id = 8.14 # float |       ID of an environment that is prior to the new environment in the chain. It has to be       either the ID of Library or the ID of an environment at the end of a chain.
label = 'label_example' # str | label of the environment (optional)
description = 'description_example' # str | description of the environment (optional)
registry_name_pattern = 'registry_name_pattern_example' # str | pattern for container image names (optional)
registry_unauthenticated_pull = true # bool | allow unauthenticed pull of container images (optional)

try:
    # Create an environment
    api_instance.post_environments(organization_id, name, prior_id, label=label, description=description, registry_name_pattern=registry_name_pattern, registry_unauthenticated_pull=registry_unauthenticated_pull)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->post_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| name of organization |
 **name** | **str**| name of the environment |
 **prior_id** | **float**|       ID of an environment that is prior to the new environment in the chain. It has to be       either the ID of Library or the ID of an environment at the end of a chain.  |
 **label** | **str**| label of the environment | [optional]
 **description** | **str**| description of the environment | [optional]
 **registry_name_pattern** | **str**| pattern for container image names | [optional]
 **registry_unauthenticated_pull** | **bool**| allow unauthenticed pull of container images | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_organization_id_environments**
> post_organizations_organization_id_environments(organization_id, name, prior_id, label=label, description=description, registry_name_pattern=registry_name_pattern, registry_unauthenticated_pull=registry_unauthenticated_pull)

Create an environment in an organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
organization_id = 8.14 # float | name of organization
name = 'name_example' # str | name of the environment
prior_id = 8.14 # float |       ID of an environment that is prior to the new environment in the chain. It has to be       either the ID of Library or the ID of an environment at the end of a chain.
label = 'label_example' # str | label of the environment (optional)
description = 'description_example' # str | description of the environment (optional)
registry_name_pattern = 'registry_name_pattern_example' # str | pattern for container image names (optional)
registry_unauthenticated_pull = true # bool | allow unauthenticed pull of container images (optional)

try:
    # Create an environment in an organization
    api_instance.post_organizations_organization_id_environments(organization_id, name, prior_id, label=label, description=description, registry_name_pattern=registry_name_pattern, registry_unauthenticated_pull=registry_unauthenticated_pull)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->post_organizations_organization_id_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| name of organization |
 **name** | **str**| name of the environment |
 **prior_id** | **float**|       ID of an environment that is prior to the new environment in the chain. It has to be       either the ID of Library or the ID of an environment at the end of a chain.  |
 **label** | **str**| label of the environment | [optional]
 **description** | **str**| description of the environment | [optional]
 **registry_name_pattern** | **str**| pattern for container image names | [optional]
 **registry_unauthenticated_pull** | **bool**| allow unauthenticed pull of container images | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_environments_id**
> put_environments_id(id, organization_id, new_name=new_name, description=description, registry_name_pattern=registry_name_pattern, registry_unauthenticated_pull=registry_unauthenticated_pull, _async=_async)

Update an environment



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
id = 8.14 # float | ID of the environment
organization_id = 8.14 # float | name of the organization
new_name = 'new_name_example' # str | new name to be given to the environment (optional)
description = 'description_example' # str | description of the environment (optional)
registry_name_pattern = 'registry_name_pattern_example' # str | pattern for container image names (optional)
registry_unauthenticated_pull = true # bool | allow unauthenticed pull of container images (optional)
_async = true # bool | Do not wait for the update action to finish. Default: true (optional)

try:
    # Update an environment
    api_instance.put_environments_id(id, organization_id, new_name=new_name, description=description, registry_name_pattern=registry_name_pattern, registry_unauthenticated_pull=registry_unauthenticated_pull, _async=_async)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->put_environments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the environment |
 **organization_id** | **float**| name of the organization |
 **new_name** | **str**| new name to be given to the environment | [optional]
 **description** | **str**| description of the environment | [optional]
 **registry_name_pattern** | **str**| pattern for container image names | [optional]
 **registry_unauthenticated_pull** | **bool**| allow unauthenticed pull of container images | [optional]
 **_async** | **bool**| Do not wait for the update action to finish. Default: true | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_organization_id_environments_id**
> put_organizations_organization_id_environments_id(id, organization_id, new_name=new_name, description=description, registry_name_pattern=registry_name_pattern, registry_unauthenticated_pull=registry_unauthenticated_pull, _async=_async)

Update an environment in an organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.LifecycleEnvironmentsApi()
id = 8.14 # float | ID of the environment
organization_id = 8.14 # float | name of the organization
new_name = 'new_name_example' # str | new name to be given to the environment (optional)
description = 'description_example' # str | description of the environment (optional)
registry_name_pattern = 'registry_name_pattern_example' # str | pattern for container image names (optional)
registry_unauthenticated_pull = true # bool | allow unauthenticed pull of container images (optional)
_async = true # bool | Do not wait for the update action to finish. Default: true (optional)

try:
    # Update an environment in an organization
    api_instance.put_organizations_organization_id_environments_id(id, organization_id, new_name=new_name, description=description, registry_name_pattern=registry_name_pattern, registry_unauthenticated_pull=registry_unauthenticated_pull, _async=_async)
except ApiException as e:
    print("Exception when calling LifecycleEnvironmentsApi->put_organizations_organization_id_environments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| ID of the environment |
 **organization_id** | **float**| name of the organization |
 **new_name** | **str**| new name to be given to the environment | [optional]
 **description** | **str**| description of the environment | [optional]
 **registry_name_pattern** | **str**| pattern for container image names | [optional]
 **registry_unauthenticated_pull** | **bool**| allow unauthenticed pull of container images | [optional]
 **_async** | **bool**| Do not wait for the update action to finish. Default: true | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
