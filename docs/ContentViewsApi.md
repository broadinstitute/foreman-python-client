# pyforeman.ContentViewsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_content_views_id**](ContentViewsApi.md#delete_content_views_id) | **DELETE** /content_views/{id} | Delete a content view
[**delete_content_views_id_environments_environment_id**](ContentViewsApi.md#delete_content_views_id_environments_environment_id) | **DELETE** /content_views/{id}/environments/{environment_id} | Remove a content view from an environment
[**get_content_views**](ContentViewsApi.md#get_content_views) | **GET** /content_views | List content views
[**get_content_views_id**](ContentViewsApi.md#get_content_views_id) | **GET** /content_views/{id} | Show a content view
[**get_organizations_organization_id_content_views**](ContentViewsApi.md#get_organizations_organization_id_content_views) | **GET** /organizations/{organization_id}/content_views | List content views
[**post_content_views**](ContentViewsApi.md#post_content_views) | **POST** /content_views | Create a content view
[**post_content_views_id_copy**](ContentViewsApi.md#post_content_views_id_copy) | **POST** /content_views/{id}/copy | Make copy of a content view
[**post_content_views_id_publish**](ContentViewsApi.md#post_content_views_id_publish) | **POST** /content_views/{id}/publish | Publish a content view
[**post_organizations_organization_id_content_views**](ContentViewsApi.md#post_organizations_organization_id_content_views) | **POST** /organizations/{organization_id}/content_views | Create a content view
[**put_content_views_id**](ContentViewsApi.md#put_content_views_id) | **PUT** /content_views/{id} | Update a content view
[**put_content_views_id_bulk_delete_versions**](ContentViewsApi.md#put_content_views_id_bulk_delete_versions) | **PUT** /content_views/{id}/bulk_delete_versions | Bulk remove versions from a content view and reassign systems and keys
[**put_content_views_id_remove**](ContentViewsApi.md#put_content_views_id_remove) | **PUT** /content_views/{id}/remove | Remove versions and/or environments from a content view and reassign systems and keys
[**put_content_views_id_remove_filters**](ContentViewsApi.md#put_content_views_id_remove_filters) | **PUT** /content_views/{id}/remove_filters | Delete multiple filters from a content view


# **delete_content_views_id**
> delete_content_views_id(id)

Delete a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | content view numeric identifier

try:
    # Delete a content view
    api_instance.delete_content_views_id(id)
except ApiException as e:
    print("Exception when calling ContentViewsApi->delete_content_views_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| content view numeric identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_views_id_environments_environment_id**
> delete_content_views_id_environments_environment_id(id, environment_id)

Remove a content view from an environment



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | content view numeric identifier
environment_id = 8.14 # float | environment numeric identifier

try:
    # Remove a content view from an environment
    api_instance.delete_content_views_id_environments_environment_id(id, environment_id)
except ApiException as e:
    print("Exception when calling ContentViewsApi->delete_content_views_id_environments_environment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| content view numeric identifier |
 **environment_id** | **float**| environment numeric identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_views**
> get_content_views(organization_id, environment_id=environment_id, nondefault=nondefault, noncomposite=noncomposite, composite=composite, without=without, name=name, label=label, include_generated=include_generated, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List content views



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
organization_id = 8.14 # float | organization identifier
environment_id = 8.14 # float | environment identifier (optional)
nondefault = true # bool | Filter out default content views (optional)
noncomposite = true # bool | Filter out composite content views (optional)
composite = true # bool | Filter only composite content views (optional)
without = ['without_example'] # list[str] | Do not include this array of content views (optional)
name = 'name_example' # str | Name of the content view (optional)
label = 'label_example' # str | Label of the content view (optional)
include_generated = true # bool | Include content views generated by imports/exports. Defaults to false (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List content views
    api_instance.get_content_views(organization_id, environment_id=environment_id, nondefault=nondefault, noncomposite=noncomposite, composite=composite, without=without, name=name, label=label, include_generated=include_generated, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling ContentViewsApi->get_content_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **environment_id** | **float**| environment identifier | [optional]
 **nondefault** | **bool**| Filter out default content views | [optional]
 **noncomposite** | **bool**| Filter out composite content views | [optional]
 **composite** | **bool**| Filter only composite content views | [optional]
 **without** | [**list[str]**](str.md)| Do not include this array of content views | [optional]
 **name** | **str**| Name of the content view | [optional]
 **label** | **str**| Label of the content view | [optional]
 **include_generated** | **bool**| Include content views generated by imports/exports. Defaults to false | [optional]
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

# **get_content_views_id**
> get_content_views_id(id)

Show a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | content view numeric identifier

try:
    # Show a content view
    api_instance.get_content_views_id(id)
except ApiException as e:
    print("Exception when calling ContentViewsApi->get_content_views_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| content view numeric identifier |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_content_views**
> get_organizations_organization_id_content_views(organization_id, environment_id=environment_id, nondefault=nondefault, noncomposite=noncomposite, composite=composite, without=without, name=name, label=label, include_generated=include_generated, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List content views



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
organization_id = 8.14 # float | organization identifier
environment_id = 8.14 # float | environment identifier (optional)
nondefault = true # bool | Filter out default content views (optional)
noncomposite = true # bool | Filter out composite content views (optional)
composite = true # bool | Filter only composite content views (optional)
without = ['without_example'] # list[str] | Do not include this array of content views (optional)
name = 'name_example' # str | Name of the content view (optional)
label = 'label_example' # str | Label of the content view (optional)
include_generated = true # bool | Include content views generated by imports/exports. Defaults to false (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List content views
    api_instance.get_organizations_organization_id_content_views(organization_id, environment_id=environment_id, nondefault=nondefault, noncomposite=noncomposite, composite=composite, without=without, name=name, label=label, include_generated=include_generated, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling ContentViewsApi->get_organizations_organization_id_content_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| organization identifier |
 **environment_id** | **float**| environment identifier | [optional]
 **nondefault** | **bool**| Filter out default content views | [optional]
 **noncomposite** | **bool**| Filter out composite content views | [optional]
 **composite** | **bool**| Filter only composite content views | [optional]
 **without** | [**list[str]**](str.md)| Do not include this array of content views | [optional]
 **name** | **str**| Name of the content view | [optional]
 **label** | **str**| Label of the content view | [optional]
 **include_generated** | **bool**| Include content views generated by imports/exports. Defaults to false | [optional]
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

# **post_content_views**
> post_content_views(organization_id, name, label=label, composite=composite, description=description, repository_ids=repository_ids, component_ids=component_ids, auto_publish=auto_publish, solve_dependencies=solve_dependencies, import_only=import_only)

Create a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
organization_id = 8.14 # float | Organization identifier
name = 'name_example' # str | Name of the content view
label = 'label_example' # str | Content view label (optional)
composite = true # bool | Composite content view (optional)
description = 'description_example' # str | Description for the content view (optional)
repository_ids = ['repository_ids_example'] # list[str] | List of repository ids (optional)
component_ids = ['component_ids_example'] # list[str] | List of component content view version ids for composite views (optional)
auto_publish = true # bool | Enable/Disable auto publish of composite view (optional)
solve_dependencies = true # bool | Solve RPM dependencies by default on Content View publish, defaults to false (optional)
import_only = true # bool | Designate this Content View for importing from upstream servers only. Defaults to false (optional)

try:
    # Create a content view
    api_instance.post_content_views(organization_id, name, label=label, composite=composite, description=description, repository_ids=repository_ids, component_ids=component_ids, auto_publish=auto_publish, solve_dependencies=solve_dependencies, import_only=import_only)
except ApiException as e:
    print("Exception when calling ContentViewsApi->post_content_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier |
 **name** | **str**| Name of the content view |
 **label** | **str**| Content view label | [optional]
 **composite** | **bool**| Composite content view | [optional]
 **description** | **str**| Description for the content view | [optional]
 **repository_ids** | [**list[str]**](str.md)| List of repository ids | [optional]
 **component_ids** | [**list[str]**](str.md)| List of component content view version ids for composite views | [optional]
 **auto_publish** | **bool**| Enable/Disable auto publish of composite view | [optional]
 **solve_dependencies** | **bool**| Solve RPM dependencies by default on Content View publish, defaults to false | [optional]
 **import_only** | **bool**| Designate this Content View for importing from upstream servers only. Defaults to false | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_views_id_copy**
> post_content_views_id_copy(id, name)

Make copy of a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | Content view numeric identifier
name = 'name_example' # str | New content view name

try:
    # Make copy of a content view
    api_instance.post_content_views_id_copy(id, name)
except ApiException as e:
    print("Exception when calling ContentViewsApi->post_content_views_id_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view numeric identifier |
 **name** | **str**| New content view name |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_content_views_id_publish**
> post_content_views_id_publish(id, description=description, major=major, minor=minor, environment_ids=environment_ids, publish_only_if_needed=publish_only_if_needed, is_force_promote=is_force_promote, repos_units=repos_units)

Publish a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | Content view identifier
description = 'description_example' # str | Description for the new published content view version (optional)
major = 8.14 # float | Override the major version number (optional)
minor = 8.14 # float | Override the minor version number (optional)
environment_ids = ['environment_ids_example'] # list[str] | Identifiers for Lifecycle Environment (optional)
publish_only_if_needed = true # bool | Check audited changes and proceed only if content or filters have changed since last publish (optional)
is_force_promote = true # bool | Force content view promotion and bypass lifecycle environment restriction (optional)
repos_units = ['repos_units_example'] # list[str] | Specify the list of units in each repo (optional)

try:
    # Publish a content view
    api_instance.post_content_views_id_publish(id, description=description, major=major, minor=minor, environment_ids=environment_ids, publish_only_if_needed=publish_only_if_needed, is_force_promote=is_force_promote, repos_units=repos_units)
except ApiException as e:
    print("Exception when calling ContentViewsApi->post_content_views_id_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view identifier |
 **description** | **str**| Description for the new published content view version | [optional]
 **major** | **float**| Override the major version number | [optional]
 **minor** | **float**| Override the minor version number | [optional]
 **environment_ids** | [**list[str]**](str.md)| Identifiers for Lifecycle Environment | [optional]
 **publish_only_if_needed** | **bool**| Check audited changes and proceed only if content or filters have changed since last publish | [optional]
 **is_force_promote** | **bool**| Force content view promotion and bypass lifecycle environment restriction | [optional]
 **repos_units** | [**list[str]**](str.md)| Specify the list of units in each repo | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_organization_id_content_views**
> post_organizations_organization_id_content_views(organization_id, name, label=label, composite=composite, description=description, repository_ids=repository_ids, component_ids=component_ids, auto_publish=auto_publish, solve_dependencies=solve_dependencies, import_only=import_only)

Create a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
organization_id = 8.14 # float | Organization identifier
name = 'name_example' # str | Name of the content view
label = 'label_example' # str | Content view label (optional)
composite = true # bool | Composite content view (optional)
description = 'description_example' # str | Description for the content view (optional)
repository_ids = ['repository_ids_example'] # list[str] | List of repository ids (optional)
component_ids = ['component_ids_example'] # list[str] | List of component content view version ids for composite views (optional)
auto_publish = true # bool | Enable/Disable auto publish of composite view (optional)
solve_dependencies = true # bool | Solve RPM dependencies by default on Content View publish, defaults to false (optional)
import_only = true # bool | Designate this Content View for importing from upstream servers only. Defaults to false (optional)

try:
    # Create a content view
    api_instance.post_organizations_organization_id_content_views(organization_id, name, label=label, composite=composite, description=description, repository_ids=repository_ids, component_ids=component_ids, auto_publish=auto_publish, solve_dependencies=solve_dependencies, import_only=import_only)
except ApiException as e:
    print("Exception when calling ContentViewsApi->post_organizations_organization_id_content_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Organization identifier |
 **name** | **str**| Name of the content view |
 **label** | **str**| Content view label | [optional]
 **composite** | **bool**| Composite content view | [optional]
 **description** | **str**| Description for the content view | [optional]
 **repository_ids** | [**list[str]**](str.md)| List of repository ids | [optional]
 **component_ids** | [**list[str]**](str.md)| List of component content view version ids for composite views | [optional]
 **auto_publish** | **bool**| Enable/Disable auto publish of composite view | [optional]
 **solve_dependencies** | **bool**| Solve RPM dependencies by default on Content View publish, defaults to false | [optional]
 **import_only** | **bool**| Designate this Content View for importing from upstream servers only. Defaults to false | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_id**
> put_content_views_id(id, name=name, description=description, repository_ids=repository_ids, component_ids=component_ids, auto_publish=auto_publish, solve_dependencies=solve_dependencies, import_only=import_only)

Update a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | Content view identifier
name = 'name_example' # str | New name for the content view (optional)
description = 'description_example' # str | Description for the content view (optional)
repository_ids = ['repository_ids_example'] # list[str] | List of repository ids (optional)
component_ids = ['component_ids_example'] # list[str] | List of component content view version ids for composite views (optional)
auto_publish = true # bool | Enable/Disable auto publish of composite view (optional)
solve_dependencies = true # bool | Solve RPM dependencies by default on Content View publish, defaults to false (optional)
import_only = true # bool | Designate this Content View for importing from upstream servers only. Defaults to false (optional)

try:
    # Update a content view
    api_instance.put_content_views_id(id, name=name, description=description, repository_ids=repository_ids, component_ids=component_ids, auto_publish=auto_publish, solve_dependencies=solve_dependencies, import_only=import_only)
except ApiException as e:
    print("Exception when calling ContentViewsApi->put_content_views_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view identifier |
 **name** | **str**| New name for the content view | [optional]
 **description** | **str**| Description for the content view | [optional]
 **repository_ids** | [**list[str]**](str.md)| List of repository ids | [optional]
 **component_ids** | [**list[str]**](str.md)| List of component content view version ids for composite views | [optional]
 **auto_publish** | **bool**| Enable/Disable auto publish of composite view | [optional]
 **solve_dependencies** | **bool**| Solve RPM dependencies by default on Content View publish, defaults to false | [optional]
 **import_only** | **bool**| Designate this Content View for importing from upstream servers only. Defaults to false | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_id_bulk_delete_versions**
> put_content_views_id_bulk_delete_versions(id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, system_content_view_id=system_content_view_id, system_environment_id=system_environment_id, key_content_view_id=key_content_view_id, key_environment_id=key_environment_id)

Bulk remove versions from a content view and reassign systems and keys



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | content view numeric identifier
included_search = 'included_search_example' # str | Search string for versions to perform an action on (optional)
included_ids = ['included_ids_example'] # list[str] | List of versions to perform an action on (optional)
excluded_ids = ['excluded_ids_example'] # list[str] | List of versions to exclude and not run an action on (optional)
system_content_view_id = 8.14 # float | content view to reassign orphaned systems to (optional)
system_environment_id = 8.14 # float | environment to reassign orphaned systems to (optional)
key_content_view_id = 8.14 # float | content view to reassign orphaned activation keys to (optional)
key_environment_id = 8.14 # float | environment to reassign orphaned activation keys to (optional)

try:
    # Bulk remove versions from a content view and reassign systems and keys
    api_instance.put_content_views_id_bulk_delete_versions(id, included_search=included_search, included_ids=included_ids, excluded_ids=excluded_ids, system_content_view_id=system_content_view_id, system_environment_id=system_environment_id, key_content_view_id=key_content_view_id, key_environment_id=key_environment_id)
except ApiException as e:
    print("Exception when calling ContentViewsApi->put_content_views_id_bulk_delete_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| content view numeric identifier |
 **included_search** | **str**| Search string for versions to perform an action on | [optional]
 **included_ids** | [**list[str]**](str.md)| List of versions to perform an action on | [optional]
 **excluded_ids** | [**list[str]**](str.md)| List of versions to exclude and not run an action on | [optional]
 **system_content_view_id** | **float**| content view to reassign orphaned systems to | [optional]
 **system_environment_id** | **float**| environment to reassign orphaned systems to | [optional]
 **key_content_view_id** | **float**| content view to reassign orphaned activation keys to | [optional]
 **key_environment_id** | **float**| environment to reassign orphaned activation keys to | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_id_remove**
> put_content_views_id_remove(id, environment_ids=environment_ids, content_view_version_ids=content_view_version_ids, system_content_view_id=system_content_view_id, system_environment_id=system_environment_id, key_content_view_id=key_content_view_id, key_environment_id=key_environment_id, destroy_content_view=destroy_content_view)

Remove versions and/or environments from a content view and reassign systems and keys



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | content view numeric identifier
environment_ids = ['environment_ids_example'] # list[str] | environment numeric identifiers to be removed (optional)
content_view_version_ids = ['content_view_version_ids_example'] # list[str] | content view version identifiers to be deleted (optional)
system_content_view_id = 8.14 # float | content view to reassign orphaned systems to (optional)
system_environment_id = 8.14 # float | environment to reassign orphaned systems to (optional)
key_content_view_id = 8.14 # float | content view to reassign orphaned activation keys to (optional)
key_environment_id = 8.14 # float | environment to reassign orphaned activation keys to (optional)
destroy_content_view = true # bool | delete the content view with all the versions and environments (optional)

try:
    # Remove versions and/or environments from a content view and reassign systems and keys
    api_instance.put_content_views_id_remove(id, environment_ids=environment_ids, content_view_version_ids=content_view_version_ids, system_content_view_id=system_content_view_id, system_environment_id=system_environment_id, key_content_view_id=key_content_view_id, key_environment_id=key_environment_id, destroy_content_view=destroy_content_view)
except ApiException as e:
    print("Exception when calling ContentViewsApi->put_content_views_id_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| content view numeric identifier |
 **environment_ids** | [**list[str]**](str.md)| environment numeric identifiers to be removed | [optional]
 **content_view_version_ids** | [**list[str]**](str.md)| content view version identifiers to be deleted | [optional]
 **system_content_view_id** | **float**| content view to reassign orphaned systems to | [optional]
 **system_environment_id** | **float**| environment to reassign orphaned systems to | [optional]
 **key_content_view_id** | **float**| content view to reassign orphaned activation keys to | [optional]
 **key_environment_id** | **float**| environment to reassign orphaned activation keys to | [optional]
 **destroy_content_view** | **bool**| delete the content view with all the versions and environments | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_content_views_id_remove_filters**
> put_content_views_id_remove_filters(id, filter_ids)

Delete multiple filters from a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ContentViewsApi()
id = 8.14 # float | content view numeric identifier
filter_ids = ['filter_ids_example'] # list[str] | filter identifiers

try:
    # Delete multiple filters from a content view
    api_instance.put_content_views_id_remove_filters(id, filter_ids)
except ApiException as e:
    print("Exception when calling ContentViewsApi->put_content_views_id_remove_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| content view numeric identifier |
 **filter_ids** | [**list[str]**](str.md)| filter identifiers |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
