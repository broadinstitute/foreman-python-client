# foreman.ContentViewVersionsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_content_view_versions_id**](ContentViewVersionsApi.md#delete_content_view_versions_id) | **DELETE** /content_view_versions/{id} | Remove content view version
[**get_content_view_versions**](ContentViewVersionsApi.md#get_content_view_versions) | **GET** /content_view_versions | List content view versions
[**get_content_view_versions_id**](ContentViewVersionsApi.md#get_content_view_versions_id) | **GET** /content_view_versions/{id} | Show content view version
[**get_content_views_content_view_id_content_view_versions**](ContentViewVersionsApi.md#get_content_views_content_view_id_content_view_versions) | **GET** /content_views/{content_view_id}/content_view_versions | List content view versions
[**post_content_view_versions_id_promote**](ContentViewVersionsApi.md#post_content_view_versions_id_promote) | **POST** /content_view_versions/{id}/promote | Promote a content view version
[**post_content_view_versions_incremental_update**](ContentViewVersionsApi.md#post_content_view_versions_incremental_update) | **POST** /content_view_versions/incremental_update | Perform an Incremental Update on one or more Content View Versions
[**put_content_view_versions_id**](ContentViewVersionsApi.md#put_content_view_versions_id) | **PUT** /content_view_versions/{id} | Update a content view version
[**put_content_view_versions_id_republish_repositories**](ContentViewVersionsApi.md#put_content_view_versions_id_republish_repositories) | **PUT** /content_view_versions/{id}/republish_repositories | Forces a republish of the version&#39;s repositories&#39; metadata


# **delete_content_view_versions_id**
> delete_content_view_versions_id(id)

Remove content view version

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
    api_instance = foreman.ContentViewVersionsApi(api_client)
    id = 3.4 # float | Content view version identifier

    try:
        # Remove content view version
        api_instance.delete_content_view_versions_id(id)
    except Exception as e:
        print("Exception when calling ContentViewVersionsApi->delete_content_view_versions_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view version identifier | 

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

# **get_content_view_versions**
> get_content_view_versions(content_view_id, environment_id=environment_id, version=version, composite_version_id=composite_version_id, organization_id=organization_id, include_applied_filters=include_applied_filters, triggered_by_id=triggered_by_id, file_id=file_id, nondefault=nondefault, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List content view versions

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
    api_instance = foreman.ContentViewVersionsApi(api_client)
    content_view_id = 3.4 # float | Content view identifier
    environment_id = 3.4 # float | Filter versions by environment (optional)
    version = 'version_example' # str | Filter versions by version number (optional)
    composite_version_id = 3.4 # float | Filter versions that are components in the specified composite version (optional)
    organization_id = 3.4 # float | Organization identifier (optional)
    include_applied_filters = True # bool | Whether or not to return filters applied to the content view version (optional)
    triggered_by_id = 3.4 # float | Filter composite versions whose publish was triggered by the specified component version (optional)
    file_id = 3.4 # float | Filter content view versions that contain the file (optional)
    nondefault = True # bool | Filter out default content views (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List content view versions
        api_instance.get_content_view_versions(content_view_id, environment_id=environment_id, version=version, composite_version_id=composite_version_id, organization_id=organization_id, include_applied_filters=include_applied_filters, triggered_by_id=triggered_by_id, file_id=file_id, nondefault=nondefault, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ContentViewVersionsApi->get_content_view_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| Content view identifier | 
 **environment_id** | **float**| Filter versions by environment | [optional] 
 **version** | **str**| Filter versions by version number | [optional] 
 **composite_version_id** | **float**| Filter versions that are components in the specified composite version | [optional] 
 **organization_id** | **float**| Organization identifier | [optional] 
 **include_applied_filters** | **bool**| Whether or not to return filters applied to the content view version | [optional] 
 **triggered_by_id** | **float**| Filter composite versions whose publish was triggered by the specified component version | [optional] 
 **file_id** | **float**| Filter content view versions that contain the file | [optional] 
 **nondefault** | **bool**| Filter out default content views | [optional] 
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

# **get_content_view_versions_id**
> get_content_view_versions_id(id, include_applied_filters=include_applied_filters)

Show content view version

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
    api_instance = foreman.ContentViewVersionsApi(api_client)
    id = 3.4 # float | Content view version identifier
    include_applied_filters = True # bool | Whether or not to return filters applied to the content view version (optional)

    try:
        # Show content view version
        api_instance.get_content_view_versions_id(id, include_applied_filters=include_applied_filters)
    except Exception as e:
        print("Exception when calling ContentViewVersionsApi->get_content_view_versions_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view version identifier | 
 **include_applied_filters** | **bool**| Whether or not to return filters applied to the content view version | [optional] 

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

# **get_content_views_content_view_id_content_view_versions**
> get_content_views_content_view_id_content_view_versions(content_view_id, environment_id=environment_id, version=version, composite_version_id=composite_version_id, organization_id=organization_id, include_applied_filters=include_applied_filters, triggered_by_id=triggered_by_id, file_id=file_id, nondefault=nondefault, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List content view versions

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
    api_instance = foreman.ContentViewVersionsApi(api_client)
    content_view_id = 3.4 # float | Content view identifier
    environment_id = 3.4 # float | Filter versions by environment (optional)
    version = 'version_example' # str | Filter versions by version number (optional)
    composite_version_id = 3.4 # float | Filter versions that are components in the specified composite version (optional)
    organization_id = 3.4 # float | Organization identifier (optional)
    include_applied_filters = True # bool | Whether or not to return filters applied to the content view version (optional)
    triggered_by_id = 3.4 # float | Filter composite versions whose publish was triggered by the specified component version (optional)
    file_id = 3.4 # float | Filter content view versions that contain the file (optional)
    nondefault = True # bool | Filter out default content views (optional)
    search = 'search_example' # str | Search string (optional)
    page = 3.4 # float | Page number, starting at 1 (optional)
    per_page = 3.4 # float | Number of results per page to return (optional)
    order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
    full_result = True # bool | Whether or not to show all results (optional)
    sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
    sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

    try:
        # List content view versions
        api_instance.get_content_views_content_view_id_content_view_versions(content_view_id, environment_id=environment_id, version=version, composite_version_id=composite_version_id, organization_id=organization_id, include_applied_filters=include_applied_filters, triggered_by_id=triggered_by_id, file_id=file_id, nondefault=nondefault, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
    except Exception as e:
        print("Exception when calling ContentViewVersionsApi->get_content_views_content_view_id_content_view_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_id** | **float**| Content view identifier | 
 **environment_id** | **float**| Filter versions by environment | [optional] 
 **version** | **str**| Filter versions by version number | [optional] 
 **composite_version_id** | **float**| Filter versions that are components in the specified composite version | [optional] 
 **organization_id** | **float**| Organization identifier | [optional] 
 **include_applied_filters** | **bool**| Whether or not to return filters applied to the content view version | [optional] 
 **triggered_by_id** | **float**| Filter composite versions whose publish was triggered by the specified component version | [optional] 
 **file_id** | **float**| Filter content view versions that contain the file | [optional] 
 **nondefault** | **bool**| Filter out default content views | [optional] 
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

# **post_content_view_versions_id_promote**
> post_content_view_versions_id_promote(id, force=force, environment_ids=environment_ids, description=description)

Promote a content view version

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
    api_instance = foreman.ContentViewVersionsApi(api_client)
    id = 3.4 # float | Content view version identifier
    force = True # bool | force content view promotion and bypass lifecycle environment restriction (optional)
    environment_ids = ['environment_ids_example'] # List[str] | Identifiers for Lifecycle Environment (optional)
    description = 'description_example' # str | The description for the content view version promotion (optional)

    try:
        # Promote a content view version
        api_instance.post_content_view_versions_id_promote(id, force=force, environment_ids=environment_ids, description=description)
    except Exception as e:
        print("Exception when calling ContentViewVersionsApi->post_content_view_versions_id_promote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view version identifier | 
 **force** | **bool**| force content view promotion and bypass lifecycle environment restriction | [optional] 
 **environment_ids** | [**List[str]**](str.md)| Identifiers for Lifecycle Environment | [optional] 
 **description** | **str**| The description for the content view version promotion | [optional] 

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

# **post_content_view_versions_incremental_update**
> post_content_view_versions_incremental_update(content_view_version_environments=content_view_version_environments, description=description, resolve_dependencies=resolve_dependencies, propagate_all_composites=propagate_all_composites, add_content_errata_ids=add_content_errata_ids, add_content_package_ids=add_content_package_ids, add_content_deb_ids=add_content_deb_ids, update_hosts_included_search=update_hosts_included_search, update_hosts_included_ids=update_hosts_included_ids, update_hosts_excluded_ids=update_hosts_excluded_ids)

Perform an Incremental Update on one or more Content View Versions

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
    api_instance = foreman.ContentViewVersionsApi(api_client)
    content_view_version_environments = ['content_view_version_environments_example'] # List[str] |  (optional)
    description = 'description_example' # str | The description for the new generated Content View Versions (optional)
    resolve_dependencies = True # bool | If true, when adding the specified errata or packages, any needed dependencies will be copied as well. Defaults to true (optional)
    propagate_all_composites = True # bool | If true, will publish a new composite version using any specified content_view_version_id that has been promoted to a lifecycle environment (optional)
    add_content_errata_ids = ['add_content_errata_ids_example'] # List[str] | Errata ids to copy into the new versions (optional)
    add_content_package_ids = ['add_content_package_ids_example'] # List[str] | Package ids to copy into the new versions (optional)
    add_content_deb_ids = ['add_content_deb_ids_example'] # List[str] | Deb Package ids to copy into the new versions (optional)
    update_hosts_included_search = 'update_hosts_included_search_example' # str | Search string for host to perform an action on (optional)
    update_hosts_included_ids = ['update_hosts_included_ids_example'] # List[str] | List of host ids to perform an action on (optional)
    update_hosts_excluded_ids = ['update_hosts_excluded_ids_example'] # List[str] | List of host ids to exclude and not run an action on (optional)

    try:
        # Perform an Incremental Update on one or more Content View Versions
        api_instance.post_content_view_versions_incremental_update(content_view_version_environments=content_view_version_environments, description=description, resolve_dependencies=resolve_dependencies, propagate_all_composites=propagate_all_composites, add_content_errata_ids=add_content_errata_ids, add_content_package_ids=add_content_package_ids, add_content_deb_ids=add_content_deb_ids, update_hosts_included_search=update_hosts_included_search, update_hosts_included_ids=update_hosts_included_ids, update_hosts_excluded_ids=update_hosts_excluded_ids)
    except Exception as e:
        print("Exception when calling ContentViewVersionsApi->post_content_view_versions_incremental_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_version_environments** | [**List[str]**](str.md)|  | [optional] 
 **description** | **str**| The description for the new generated Content View Versions | [optional] 
 **resolve_dependencies** | **bool**| If true, when adding the specified errata or packages, any needed dependencies will be copied as well. Defaults to true | [optional] 
 **propagate_all_composites** | **bool**| If true, will publish a new composite version using any specified content_view_version_id that has been promoted to a lifecycle environment | [optional] 
 **add_content_errata_ids** | [**List[str]**](str.md)| Errata ids to copy into the new versions | [optional] 
 **add_content_package_ids** | [**List[str]**](str.md)| Package ids to copy into the new versions | [optional] 
 **add_content_deb_ids** | [**List[str]**](str.md)| Deb Package ids to copy into the new versions | [optional] 
 **update_hosts_included_search** | **str**| Search string for host to perform an action on | [optional] 
 **update_hosts_included_ids** | [**List[str]**](str.md)| List of host ids to perform an action on | [optional] 
 **update_hosts_excluded_ids** | [**List[str]**](str.md)| List of host ids to exclude and not run an action on | [optional] 

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

# **put_content_view_versions_id**
> put_content_view_versions_id(id, description)

Update a content view version

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
    api_instance = foreman.ContentViewVersionsApi(api_client)
    id = 3.4 # float | Content view version identifier
    description = 'description_example' # str | The description for the content view version

    try:
        # Update a content view version
        api_instance.put_content_view_versions_id(id, description)
    except Exception as e:
        print("Exception when calling ContentViewVersionsApi->put_content_view_versions_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view version identifier | 
 **description** | **str**| The description for the content view version | 

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

# **put_content_view_versions_id_republish_repositories**
> put_content_view_versions_id_republish_repositories(id, force=force)

Forces a republish of the version's repositories' metadata

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
    api_instance = foreman.ContentViewVersionsApi(api_client)
    id = 3.4 # float | Content view version identifier
    force = True # bool | Force metadata regeneration to proceed. Dangerous operation when version has repositories with the 'Complete Mirroring' mirroring policy (optional)

    try:
        # Forces a republish of the version's repositories' metadata
        api_instance.put_content_view_versions_id_republish_repositories(id, force=force)
    except Exception as e:
        print("Exception when calling ContentViewVersionsApi->put_content_view_versions_id_republish_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Content view version identifier | 
 **force** | **bool**| Force metadata regeneration to proceed. Dangerous operation when version has repositories with the &#39;Complete Mirroring&#39; mirroring policy | [optional] 

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

