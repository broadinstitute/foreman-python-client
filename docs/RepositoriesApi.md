# pyforeman.RepositoriesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_repositories_id**](RepositoriesApi.md#delete_repositories_id) | **DELETE** /repositories/{id} | Destroy a custom repository
[**get_content_types**](RepositoriesApi.md#get_content_types) | **GET** /content_types | Return the enabled content types
[**get_content_views_id_repositories**](RepositoriesApi.md#get_content_views_id_repositories) | **GET** /content_views/{id}/repositories | List of repositories for a content view
[**get_environments_environment_id_products_product_id_repositories**](RepositoriesApi.md#get_environments_environment_id_products_product_id_repositories) | **GET** /environments/{environment_id}/products/{product_id}/repositories | List of repositories belonging to a product in an environment
[**get_organizations_organization_id_environments_environment_id_repositories**](RepositoriesApi.md#get_organizations_organization_id_environments_environment_id_repositories) | **GET** /organizations/{organization_id}/environments/{environment_id}/repositories | List repositories in the environment
[**get_organizations_organization_id_repositories**](RepositoriesApi.md#get_organizations_organization_id_repositories) | **GET** /organizations/{organization_id}/repositories | List of repositories in an organization
[**get_products_product_id_repositories**](RepositoriesApi.md#get_products_product_id_repositories) | **GET** /products/{product_id}/repositories | List of repositories for a product
[**get_repositories**](RepositoriesApi.md#get_repositories) | **GET** /repositories | List of enabled repositories
[**get_repositories_compare**](RepositoriesApi.md#get_repositories_compare) | **GET** /repositories/compare | List :resource
[**get_repositories_id**](RepositoriesApi.md#get_repositories_id) | **GET** /repositories/{id} | Show a repository
[**get_repositories_id_gpg_key_content**](RepositoriesApi.md#get_repositories_id_gpg_key_content) | **GET** /repositories/{id}/gpg_key_content | Return the content of a repo gpg key, used directly by yum
[**get_repositories_repository_types**](RepositoriesApi.md#get_repositories_repository_types) | **GET** /repositories/repository_types | Show the available repository types
[**post_repositories**](RepositoriesApi.md#post_repositories) | **POST** /repositories | Create a custom repository
[**post_repositories_id_reclaim_space**](RepositoriesApi.md#post_repositories_id_reclaim_space) | **POST** /repositories/{id}/reclaim_space | Reclaim space from an On Demand repository
[**post_repositories_id_sync**](RepositoriesApi.md#post_repositories_id_sync) | **POST** /repositories/{id}/sync | Sync a repository
[**post_repositories_id_upload_content**](RepositoriesApi.md#post_repositories_id_upload_content) | **POST** /repositories/{id}/upload_content | Upload content into the repository
[**post_repositories_id_verify_checksum**](RepositoriesApi.md#post_repositories_id_verify_checksum) | **POST** /repositories/{id}/verify_checksum | Verify checksum of repository contents
[**put_repositories_id**](RepositoriesApi.md#put_repositories_id) | **PUT** /repositories/{id} | Update a repository
[**put_repositories_id_import_uploads**](RepositoriesApi.md#put_repositories_id_import_uploads) | **PUT** /repositories/{id}/import_uploads | Import uploads into a repository
[**put_repositories_id_remove_content**](RepositoriesApi.md#put_repositories_id_remove_content) | **PUT** /repositories/{id}/remove_content |
[**put_repositories_id_remove_docker_manifests**](RepositoriesApi.md#put_repositories_id_remove_docker_manifests) | **PUT** /repositories/{id}/remove_docker_manifests |
[**put_repositories_id_remove_packages**](RepositoriesApi.md#put_repositories_id_remove_packages) | **PUT** /repositories/{id}/remove_packages |
[**put_repositories_id_republish**](RepositoriesApi.md#put_repositories_id_republish) | **PUT** /repositories/{id}/republish | Forces a republish of the specified repository, regenerating metadata and symlinks on the filesystem. Not allowed for repositories with the &#39;Complete Mirroring&#39; mirroring policy.


# **delete_repositories_id**
> delete_repositories_id(id, remove_from_content_view_versions=remove_from_content_view_versions, delete_empty_repo_filters=delete_empty_repo_filters)

Destroy a custom repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float |
remove_from_content_view_versions = true # bool | Force delete the repository by removing it from all content view versions (optional)
delete_empty_repo_filters = true # bool | Delete content view filters that have this repository as the last associated repository. Defaults to true. If false, such filters will now apply to all repositories in the content view. (optional)

try:
    # Destroy a custom repository
    api_instance.delete_repositories_id(id, remove_from_content_view_versions=remove_from_content_view_versions, delete_empty_repo_filters=delete_empty_repo_filters)
except ApiException as e:
    print("Exception when calling RepositoriesApi->delete_repositories_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **remove_from_content_view_versions** | **bool**| Force delete the repository by removing it from all content view versions | [optional]
 **delete_empty_repo_filters** | **bool**| Delete content view filters that have this repository as the last associated repository. Defaults to true. If false, such filters will now apply to all repositories in the content view. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_types**
> get_content_types()

Return the enabled content types



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()

try:
    # Return the enabled content types
    api_instance.get_content_types()
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_content_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_views_id_repositories**
> get_content_views_id_repositories(id, organization_id, product_id, environment_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of repositories for a content view



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float |
organization_id = 8.14 # float | ID of an organization to show repositories in
product_id = 8.14 # float | ID of a product to show repositories of
environment_id = 8.14 # float | ID of an environment to show repositories in
content_view_id = 8.14 # float | ID of a content view to show repositories in (optional)
content_view_version_id = 8.14 # float | ID of a content view version to show repositories in (optional)
deb_id = 'deb_id_example' # str | Id of a deb package to find repositories that contain the deb (optional)
erratum_id = 'erratum_id_example' # str | Id of an erratum to find repositories that contain the erratum (optional)
rpm_id = 'rpm_id_example' # str | Id of a rpm package to find repositories that contain the rpm (optional)
file_id = 'file_id_example' # str | Id of a file to find repositories that contain the file (optional)
ansible_collection_id = 'ansible_collection_id_example' # str | Id of an ansible collection to find repositories that contain the ansible collection (optional)
library = true # bool | show repositories in Library and the default content view (optional)
archived = true # bool | show archived repositories (optional)
content_type = 'content_type_example' # str | Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types (optional)
name = 'name_example' # str | name of the repository (optional)
label = 'label_example' # str | label of the repository (optional)
description = 'description_example' # str | description of the repository (optional)
available_for = 'available_for_example' # str | interpret specified object to return only Repositories that can be associated with specified object.  Only 'content_view' & 'content_view_version' are supported. (optional)
with_content = 'with_content_example' # str | Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \"Indexed?\" types here: /katello/api/repositories/repository_types (optional)
download_policy = 'download_policy_example' # str | limit to only repositories with this download policy (optional)
username = 'username_example' # str | only show the repositories readable by this user with this username (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List of repositories for a content view
    api_instance.get_content_views_id_repositories(id, organization_id, product_id, environment_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_content_views_id_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |
 **organization_id** | **float**| ID of an organization to show repositories in |
 **product_id** | **float**| ID of a product to show repositories of |
 **environment_id** | **float**| ID of an environment to show repositories in |
 **content_view_id** | **float**| ID of a content view to show repositories in | [optional]
 **content_view_version_id** | **float**| ID of a content view version to show repositories in | [optional]
 **deb_id** | **str**| Id of a deb package to find repositories that contain the deb | [optional]
 **erratum_id** | **str**| Id of an erratum to find repositories that contain the erratum | [optional]
 **rpm_id** | **str**| Id of a rpm package to find repositories that contain the rpm | [optional]
 **file_id** | **str**| Id of a file to find repositories that contain the file | [optional]
 **ansible_collection_id** | **str**| Id of an ansible collection to find repositories that contain the ansible collection | [optional]
 **library** | **bool**| show repositories in Library and the default content view | [optional]
 **archived** | **bool**| show archived repositories | [optional]
 **content_type** | **str**| Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types | [optional]
 **name** | **str**| name of the repository | [optional]
 **label** | **str**| label of the repository | [optional]
 **description** | **str**| description of the repository | [optional]
 **available_for** | **str**| interpret specified object to return only Repositories that can be associated with specified object.  Only &#39;content_view&#39; &amp; &#39;content_view_version&#39; are supported. | [optional]
 **with_content** | **str**| Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \&quot;Indexed?\&quot; types here: /katello/api/repositories/repository_types | [optional]
 **download_policy** | **str**| limit to only repositories with this download policy | [optional]
 **username** | **str**| only show the repositories readable by this user with this username | [optional]
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

# **get_environments_environment_id_products_product_id_repositories**
> get_environments_environment_id_products_product_id_repositories(product_id, environment_id, organization_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of repositories belonging to a product in an environment



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
product_id = 8.14 # float | ID of a product to show repositories of
environment_id = 8.14 # float | ID of an environment to show repositories in
organization_id = 8.14 # float | ID of an organization to show repositories in
content_view_id = 8.14 # float | ID of a content view to show repositories in (optional)
content_view_version_id = 8.14 # float | ID of a content view version to show repositories in (optional)
deb_id = 'deb_id_example' # str | Id of a deb package to find repositories that contain the deb (optional)
erratum_id = 'erratum_id_example' # str | Id of an erratum to find repositories that contain the erratum (optional)
rpm_id = 'rpm_id_example' # str | Id of a rpm package to find repositories that contain the rpm (optional)
file_id = 'file_id_example' # str | Id of a file to find repositories that contain the file (optional)
ansible_collection_id = 'ansible_collection_id_example' # str | Id of an ansible collection to find repositories that contain the ansible collection (optional)
library = true # bool | show repositories in Library and the default content view (optional)
archived = true # bool | show archived repositories (optional)
content_type = 'content_type_example' # str | Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types (optional)
name = 'name_example' # str | name of the repository (optional)
label = 'label_example' # str | label of the repository (optional)
description = 'description_example' # str | description of the repository (optional)
available_for = 'available_for_example' # str | interpret specified object to return only Repositories that can be associated with specified object.  Only 'content_view' & 'content_view_version' are supported. (optional)
with_content = 'with_content_example' # str | Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \"Indexed?\" types here: /katello/api/repositories/repository_types (optional)
download_policy = 'download_policy_example' # str | limit to only repositories with this download policy (optional)
username = 'username_example' # str | only show the repositories readable by this user with this username (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List of repositories belonging to a product in an environment
    api_instance.get_environments_environment_id_products_product_id_repositories(product_id, environment_id, organization_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_environments_environment_id_products_product_id_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **float**| ID of a product to show repositories of |
 **environment_id** | **float**| ID of an environment to show repositories in |
 **organization_id** | **float**| ID of an organization to show repositories in |
 **content_view_id** | **float**| ID of a content view to show repositories in | [optional]
 **content_view_version_id** | **float**| ID of a content view version to show repositories in | [optional]
 **deb_id** | **str**| Id of a deb package to find repositories that contain the deb | [optional]
 **erratum_id** | **str**| Id of an erratum to find repositories that contain the erratum | [optional]
 **rpm_id** | **str**| Id of a rpm package to find repositories that contain the rpm | [optional]
 **file_id** | **str**| Id of a file to find repositories that contain the file | [optional]
 **ansible_collection_id** | **str**| Id of an ansible collection to find repositories that contain the ansible collection | [optional]
 **library** | **bool**| show repositories in Library and the default content view | [optional]
 **archived** | **bool**| show archived repositories | [optional]
 **content_type** | **str**| Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types | [optional]
 **name** | **str**| name of the repository | [optional]
 **label** | **str**| label of the repository | [optional]
 **description** | **str**| description of the repository | [optional]
 **available_for** | **str**| interpret specified object to return only Repositories that can be associated with specified object.  Only &#39;content_view&#39; &amp; &#39;content_view_version&#39; are supported. | [optional]
 **with_content** | **str**| Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \&quot;Indexed?\&quot; types here: /katello/api/repositories/repository_types | [optional]
 **download_policy** | **str**| limit to only repositories with this download policy | [optional]
 **username** | **str**| only show the repositories readable by this user with this username | [optional]
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

# **get_organizations_organization_id_environments_environment_id_repositories**
> get_organizations_organization_id_environments_environment_id_repositories(organization_id, environment_id, product_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List repositories in the environment



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
organization_id = 8.14 # float | ID of an organization to show repositories in
environment_id = 8.14 # float | ID of an environment to show repositories in
product_id = 8.14 # float | ID of a product to show repositories of
content_view_id = 8.14 # float | ID of a content view to show repositories in (optional)
content_view_version_id = 8.14 # float | ID of a content view version to show repositories in (optional)
deb_id = 'deb_id_example' # str | Id of a deb package to find repositories that contain the deb (optional)
erratum_id = 'erratum_id_example' # str | Id of an erratum to find repositories that contain the erratum (optional)
rpm_id = 'rpm_id_example' # str | Id of a rpm package to find repositories that contain the rpm (optional)
file_id = 'file_id_example' # str | Id of a file to find repositories that contain the file (optional)
ansible_collection_id = 'ansible_collection_id_example' # str | Id of an ansible collection to find repositories that contain the ansible collection (optional)
library = true # bool | show repositories in Library and the default content view (optional)
archived = true # bool | show archived repositories (optional)
content_type = 'content_type_example' # str | Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types (optional)
name = 'name_example' # str | name of the repository (optional)
label = 'label_example' # str | label of the repository (optional)
description = 'description_example' # str | description of the repository (optional)
available_for = 'available_for_example' # str | interpret specified object to return only Repositories that can be associated with specified object.  Only 'content_view' & 'content_view_version' are supported. (optional)
with_content = 'with_content_example' # str | Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \"Indexed?\" types here: /katello/api/repositories/repository_types (optional)
download_policy = 'download_policy_example' # str | limit to only repositories with this download policy (optional)
username = 'username_example' # str | only show the repositories readable by this user with this username (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List repositories in the environment
    api_instance.get_organizations_organization_id_environments_environment_id_repositories(organization_id, environment_id, product_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_organizations_organization_id_environments_environment_id_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of an organization to show repositories in |
 **environment_id** | **float**| ID of an environment to show repositories in |
 **product_id** | **float**| ID of a product to show repositories of |
 **content_view_id** | **float**| ID of a content view to show repositories in | [optional]
 **content_view_version_id** | **float**| ID of a content view version to show repositories in | [optional]
 **deb_id** | **str**| Id of a deb package to find repositories that contain the deb | [optional]
 **erratum_id** | **str**| Id of an erratum to find repositories that contain the erratum | [optional]
 **rpm_id** | **str**| Id of a rpm package to find repositories that contain the rpm | [optional]
 **file_id** | **str**| Id of a file to find repositories that contain the file | [optional]
 **ansible_collection_id** | **str**| Id of an ansible collection to find repositories that contain the ansible collection | [optional]
 **library** | **bool**| show repositories in Library and the default content view | [optional]
 **archived** | **bool**| show archived repositories | [optional]
 **content_type** | **str**| Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types | [optional]
 **name** | **str**| name of the repository | [optional]
 **label** | **str**| label of the repository | [optional]
 **description** | **str**| description of the repository | [optional]
 **available_for** | **str**| interpret specified object to return only Repositories that can be associated with specified object.  Only &#39;content_view&#39; &amp; &#39;content_view_version&#39; are supported. | [optional]
 **with_content** | **str**| Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \&quot;Indexed?\&quot; types here: /katello/api/repositories/repository_types | [optional]
 **download_policy** | **str**| limit to only repositories with this download policy | [optional]
 **username** | **str**| only show the repositories readable by this user with this username | [optional]
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

# **get_organizations_organization_id_repositories**
> get_organizations_organization_id_repositories(organization_id, product_id, environment_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of repositories in an organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
organization_id = 8.14 # float | ID of an organization to show repositories in
product_id = 8.14 # float | ID of a product to show repositories of
environment_id = 8.14 # float | ID of an environment to show repositories in
content_view_id = 8.14 # float | ID of a content view to show repositories in (optional)
content_view_version_id = 8.14 # float | ID of a content view version to show repositories in (optional)
deb_id = 'deb_id_example' # str | Id of a deb package to find repositories that contain the deb (optional)
erratum_id = 'erratum_id_example' # str | Id of an erratum to find repositories that contain the erratum (optional)
rpm_id = 'rpm_id_example' # str | Id of a rpm package to find repositories that contain the rpm (optional)
file_id = 'file_id_example' # str | Id of a file to find repositories that contain the file (optional)
ansible_collection_id = 'ansible_collection_id_example' # str | Id of an ansible collection to find repositories that contain the ansible collection (optional)
library = true # bool | show repositories in Library and the default content view (optional)
archived = true # bool | show archived repositories (optional)
content_type = 'content_type_example' # str | Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types (optional)
name = 'name_example' # str | name of the repository (optional)
label = 'label_example' # str | label of the repository (optional)
description = 'description_example' # str | description of the repository (optional)
available_for = 'available_for_example' # str | interpret specified object to return only Repositories that can be associated with specified object.  Only 'content_view' & 'content_view_version' are supported. (optional)
with_content = 'with_content_example' # str | Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \"Indexed?\" types here: /katello/api/repositories/repository_types (optional)
download_policy = 'download_policy_example' # str | limit to only repositories with this download policy (optional)
username = 'username_example' # str | only show the repositories readable by this user with this username (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List of repositories in an organization
    api_instance.get_organizations_organization_id_repositories(organization_id, product_id, environment_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_organizations_organization_id_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of an organization to show repositories in |
 **product_id** | **float**| ID of a product to show repositories of |
 **environment_id** | **float**| ID of an environment to show repositories in |
 **content_view_id** | **float**| ID of a content view to show repositories in | [optional]
 **content_view_version_id** | **float**| ID of a content view version to show repositories in | [optional]
 **deb_id** | **str**| Id of a deb package to find repositories that contain the deb | [optional]
 **erratum_id** | **str**| Id of an erratum to find repositories that contain the erratum | [optional]
 **rpm_id** | **str**| Id of a rpm package to find repositories that contain the rpm | [optional]
 **file_id** | **str**| Id of a file to find repositories that contain the file | [optional]
 **ansible_collection_id** | **str**| Id of an ansible collection to find repositories that contain the ansible collection | [optional]
 **library** | **bool**| show repositories in Library and the default content view | [optional]
 **archived** | **bool**| show archived repositories | [optional]
 **content_type** | **str**| Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types | [optional]
 **name** | **str**| name of the repository | [optional]
 **label** | **str**| label of the repository | [optional]
 **description** | **str**| description of the repository | [optional]
 **available_for** | **str**| interpret specified object to return only Repositories that can be associated with specified object.  Only &#39;content_view&#39; &amp; &#39;content_view_version&#39; are supported. | [optional]
 **with_content** | **str**| Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \&quot;Indexed?\&quot; types here: /katello/api/repositories/repository_types | [optional]
 **download_policy** | **str**| limit to only repositories with this download policy | [optional]
 **username** | **str**| only show the repositories readable by this user with this username | [optional]
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

# **get_products_product_id_repositories**
> get_products_product_id_repositories(product_id, organization_id, environment_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of repositories for a product



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
product_id = 8.14 # float | ID of a product to show repositories of
organization_id = 8.14 # float | ID of an organization to show repositories in
environment_id = 8.14 # float | ID of an environment to show repositories in
content_view_id = 8.14 # float | ID of a content view to show repositories in (optional)
content_view_version_id = 8.14 # float | ID of a content view version to show repositories in (optional)
deb_id = 'deb_id_example' # str | Id of a deb package to find repositories that contain the deb (optional)
erratum_id = 'erratum_id_example' # str | Id of an erratum to find repositories that contain the erratum (optional)
rpm_id = 'rpm_id_example' # str | Id of a rpm package to find repositories that contain the rpm (optional)
file_id = 'file_id_example' # str | Id of a file to find repositories that contain the file (optional)
ansible_collection_id = 'ansible_collection_id_example' # str | Id of an ansible collection to find repositories that contain the ansible collection (optional)
library = true # bool | show repositories in Library and the default content view (optional)
archived = true # bool | show archived repositories (optional)
content_type = 'content_type_example' # str | Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types (optional)
name = 'name_example' # str | name of the repository (optional)
label = 'label_example' # str | label of the repository (optional)
description = 'description_example' # str | description of the repository (optional)
available_for = 'available_for_example' # str | interpret specified object to return only Repositories that can be associated with specified object.  Only 'content_view' & 'content_view_version' are supported. (optional)
with_content = 'with_content_example' # str | Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \"Indexed?\" types here: /katello/api/repositories/repository_types (optional)
download_policy = 'download_policy_example' # str | limit to only repositories with this download policy (optional)
username = 'username_example' # str | only show the repositories readable by this user with this username (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List of repositories for a product
    api_instance.get_products_product_id_repositories(product_id, organization_id, environment_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_products_product_id_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **float**| ID of a product to show repositories of |
 **organization_id** | **float**| ID of an organization to show repositories in |
 **environment_id** | **float**| ID of an environment to show repositories in |
 **content_view_id** | **float**| ID of a content view to show repositories in | [optional]
 **content_view_version_id** | **float**| ID of a content view version to show repositories in | [optional]
 **deb_id** | **str**| Id of a deb package to find repositories that contain the deb | [optional]
 **erratum_id** | **str**| Id of an erratum to find repositories that contain the erratum | [optional]
 **rpm_id** | **str**| Id of a rpm package to find repositories that contain the rpm | [optional]
 **file_id** | **str**| Id of a file to find repositories that contain the file | [optional]
 **ansible_collection_id** | **str**| Id of an ansible collection to find repositories that contain the ansible collection | [optional]
 **library** | **bool**| show repositories in Library and the default content view | [optional]
 **archived** | **bool**| show archived repositories | [optional]
 **content_type** | **str**| Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types | [optional]
 **name** | **str**| name of the repository | [optional]
 **label** | **str**| label of the repository | [optional]
 **description** | **str**| description of the repository | [optional]
 **available_for** | **str**| interpret specified object to return only Repositories that can be associated with specified object.  Only &#39;content_view&#39; &amp; &#39;content_view_version&#39; are supported. | [optional]
 **with_content** | **str**| Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \&quot;Indexed?\&quot; types here: /katello/api/repositories/repository_types | [optional]
 **download_policy** | **str**| limit to only repositories with this download policy | [optional]
 **username** | **str**| only show the repositories readable by this user with this username | [optional]
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

# **get_repositories**
> get_repositories(organization_id, product_id, environment_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)

List of enabled repositories



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
organization_id = 8.14 # float | ID of an organization to show repositories in
product_id = 8.14 # float | ID of a product to show repositories of
environment_id = 8.14 # float | ID of an environment to show repositories in
content_view_id = 8.14 # float | ID of a content view to show repositories in (optional)
content_view_version_id = 8.14 # float | ID of a content view version to show repositories in (optional)
deb_id = 'deb_id_example' # str | Id of a deb package to find repositories that contain the deb (optional)
erratum_id = 'erratum_id_example' # str | Id of an erratum to find repositories that contain the erratum (optional)
rpm_id = 'rpm_id_example' # str | Id of a rpm package to find repositories that contain the rpm (optional)
file_id = 'file_id_example' # str | Id of a file to find repositories that contain the file (optional)
ansible_collection_id = 'ansible_collection_id_example' # str | Id of an ansible collection to find repositories that contain the ansible collection (optional)
library = true # bool | show repositories in Library and the default content view (optional)
archived = true # bool | show archived repositories (optional)
content_type = 'content_type_example' # str | Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types (optional)
name = 'name_example' # str | name of the repository (optional)
label = 'label_example' # str | label of the repository (optional)
description = 'description_example' # str | description of the repository (optional)
available_for = 'available_for_example' # str | interpret specified object to return only Repositories that can be associated with specified object.  Only 'content_view' & 'content_view_version' are supported. (optional)
with_content = 'with_content_example' # str | Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \"Indexed?\" types here: /katello/api/repositories/repository_types (optional)
download_policy = 'download_policy_example' # str | limit to only repositories with this download policy (optional)
username = 'username_example' # str | only show the repositories readable by this user with this username (optional)
search = 'search_example' # str | Search string (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 8.14 # float | Number of results per page to return (optional)
order = 'order_example' # str | Sort field and order, eg. 'id DESC' (optional)
full_result = true # bool | Whether or not to show all results (optional)
sort_by = 'sort_by_example' # str | Field to sort the results on (optional)
sort_order = 'sort_order_example' # str | How to order the sorted results (e.g. ASC for ascending) (optional)

try:
    # List of enabled repositories
    api_instance.get_repositories(organization_id, product_id, environment_id, content_view_id=content_view_id, content_view_version_id=content_view_version_id, deb_id=deb_id, erratum_id=erratum_id, rpm_id=rpm_id, file_id=file_id, ansible_collection_id=ansible_collection_id, library=library, archived=archived, content_type=content_type, name=name, label=label, description=description, available_for=available_for, with_content=with_content, download_policy=download_policy, username=username, search=search, page=page, per_page=per_page, order=order, full_result=full_result, sort_by=sort_by, sort_order=sort_order)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| ID of an organization to show repositories in |
 **product_id** | **float**| ID of a product to show repositories of |
 **environment_id** | **float**| ID of an environment to show repositories in |
 **content_view_id** | **float**| ID of a content view to show repositories in | [optional]
 **content_view_version_id** | **float**| ID of a content view version to show repositories in | [optional]
 **deb_id** | **str**| Id of a deb package to find repositories that contain the deb | [optional]
 **erratum_id** | **str**| Id of an erratum to find repositories that contain the erratum | [optional]
 **rpm_id** | **str**| Id of a rpm package to find repositories that contain the rpm | [optional]
 **file_id** | **str**| Id of a file to find repositories that contain the file | [optional]
 **ansible_collection_id** | **str**| Id of an ansible collection to find repositories that contain the ansible collection | [optional]
 **library** | **bool**| show repositories in Library and the default content view | [optional]
 **archived** | **bool**| show archived repositories | [optional]
 **content_type** | **str**| Limit the repository type. Available types endpoint: /katello/api/repositories/repository_types | [optional]
 **name** | **str**| name of the repository | [optional]
 **label** | **str**| label of the repository | [optional]
 **description** | **str**| description of the repository | [optional]
 **available_for** | **str**| interpret specified object to return only Repositories that can be associated with specified object.  Only &#39;content_view&#39; &amp; &#39;content_view_version&#39; are supported. | [optional]
 **with_content** | **str**| Filter repositories by content unit type (erratum, docker_tag, etc.). Check the \&quot;Indexed?\&quot; types here: /katello/api/repositories/repository_types | [optional]
 **download_policy** | **str**| limit to only repositories with this download policy | [optional]
 **username** | **str**| only show the repositories readable by this user with this username | [optional]
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

# **get_repositories_compare**
> get_repositories_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)

List :resource



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
content_view_version_ids = ['content_view_version_ids_example'] # list[str] | content view versions to compare (optional)
repository_id = 8.14 # float | Library repository id to restrict comparisons to (optional)
restrict_comparison = 'restrict_comparison_example' # str | Return same, different or all results (optional)

try:
    # List :resource
    api_instance.get_repositories_compare(content_view_version_ids=content_view_version_ids, repository_id=repository_id, restrict_comparison=restrict_comparison)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_repositories_compare: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_view_version_ids** | [**list[str]**](str.md)| content view versions to compare | [optional]
 **repository_id** | **float**| Library repository id to restrict comparisons to | [optional]
 **restrict_comparison** | **str**| Return same, different or all results | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_id**
> get_repositories_id(id, organization_id=organization_id)

Show a repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID
organization_id = 8.14 # float | Organization ID (optional)

try:
    # Show a repository
    api_instance.get_repositories_id(id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_repositories_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |
 **organization_id** | **float**| Organization ID | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_id_gpg_key_content**
> get_repositories_id_gpg_key_content(id)

Return the content of a repo gpg key, used directly by yum



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float |

try:
    # Return the content of a repo gpg key, used directly by yum
    api_instance.get_repositories_id_gpg_key_content(id)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_repositories_id_gpg_key_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_repository_types**
> get_repositories_repository_types(creatable=creatable)

Show the available repository types



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
creatable = true # bool | When set to 'True' repository types that are creatable will be returned (optional)

try:
    # Show the available repository types
    api_instance.get_repositories_repository_types(creatable=creatable)
except ApiException as e:
    print("Exception when calling RepositoriesApi->get_repositories_repository_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creatable** | **bool**| When set to &#39;True&#39; repository types that are creatable will be returned | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_repositories**
> post_repositories(name, product_id, content_type, description=description, label=label, url=url, os_versions=os_versions, gpg_key_id=gpg_key_id, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, unprotected=unprotected, checksum_type=checksum_type, docker_upstream_name=docker_upstream_name, include_tags=include_tags, exclude_tags=exclude_tags, download_policy=download_policy, download_concurrency=download_concurrency, mirroring_policy=mirroring_policy, verify_ssl_on_sync=verify_ssl_on_sync, upstream_username=upstream_username, upstream_password=upstream_password, upstream_authentication_token=upstream_authentication_token, deb_releases=deb_releases, deb_components=deb_components, deb_architectures=deb_architectures, ignorable_content=ignorable_content, ansible_collection_requirements=ansible_collection_requirements, ansible_collection_auth_url=ansible_collection_auth_url, ansible_collection_auth_token=ansible_collection_auth_token, http_proxy_policy=http_proxy_policy, http_proxy_id=http_proxy_id, arch=arch, retain_package_versions_count=retain_package_versions_count, metadata_expire=metadata_expire, excludes=excludes, includes=includes, package_types=package_types)

Create a custom repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
name = 'name_example' # str | Name of the repository
product_id = 8.14 # float | Product the repository belongs to
content_type = 'content_type_example' # str | Type of repository. Available types endpoint: /katello/api/repositories/repository_types
description = 'description_example' # str | Description of the repository (optional)
label = 'label_example' # str |  (optional)
url = 'url_example' # str | repository source url (optional)
os_versions = ['os_versions_example'] # list[str] | Identifies whether the repository should be unavailable on a client with a non-matching OS version. Pass [] to make repo available for clients regardless of OS version. Maximum length 1; allowed tags are: rhel-6, rhel-7, rhel-8, rhel-9 (optional)
gpg_key_id = 8.14 # float | id of the gpg key that will be assigned to the new repository (optional)
ssl_ca_cert_id = 8.14 # float | Identifier of the content credential containing the SSL CA Cert (optional)
ssl_client_cert_id = 8.14 # float | Identifier of the content credential containing the SSL Client Cert (optional)
ssl_client_key_id = 8.14 # float | Identifier of the content credential containing the SSL Client Key (optional)
unprotected = true # bool | true if this repository can be published via HTTP (optional)
checksum_type = 'checksum_type_example' # str | Checksum of the repository, currently 'sha1' & 'sha256' are supported (optional)
docker_upstream_name = 'docker_upstream_name_example' # str | Name of the upstream docker repository (optional)
include_tags = ['include_tags_example'] # list[str] | Comma-separated list of tags to sync for a container image repository (optional)
exclude_tags = ['exclude_tags_example'] # list[str] | Comma-separated list of tags to exclude when syncing a container image repository. Default: any tag ending in \"-source\" (optional)
download_policy = 'download_policy_example' # str | download policy for yum, deb, and docker repos (either 'immediate' or 'on_demand') (optional)
download_concurrency = 8.14 # float | Used to determine download concurrency of the repository in pulp3. Use value less than 20. Defaults to 10 (optional)
mirroring_policy = 'mirroring_policy_example' # str | Policy to set for mirroring content.  Must be one of additive. (optional)
verify_ssl_on_sync = true # bool | if true, Katello will verify the upstream url's SSL certifcates are signed by a trusted CA (optional)
upstream_username = 'upstream_username_example' # str | Username of the upstream repository user used for authentication (optional)
upstream_password = 'upstream_password_example' # str | Password of the upstream repository user used for authentication (optional)
upstream_authentication_token = 'upstream_authentication_token_example' # str | Password of the upstream authentication token. (optional)
deb_releases = 'deb_releases_example' # str | whitespace-separated list of releases to be synced from deb-archive (optional)
deb_components = 'deb_components_example' # str | whitespace-separated list of repo components to be synced from deb-archive (optional)
deb_architectures = 'deb_architectures_example' # str | whitespace-separated list of architectures to be synced from deb-archive (optional)
ignorable_content = ['ignorable_content_example'] # list[str] | List of content units to ignore while syncing a yum repository. Must be subset of srpm,treeinfo (optional)
ansible_collection_requirements = 'ansible_collection_requirements_example' # str | Contents of requirement yaml file to sync from URL (optional)
ansible_collection_auth_url = 'ansible_collection_auth_url_example' # str | The URL to receive a session token from, e.g. used with Automation Hub. (optional)
ansible_collection_auth_token = 'ansible_collection_auth_token_example' # str | The token key to use for authentication. (optional)
http_proxy_policy = 'http_proxy_policy_example' # str | policies for HTTP proxy for content sync (optional)
http_proxy_id = 8.14 # float | ID of a HTTP Proxy (optional)
arch = 'arch_example' # str | Architecture of content in the repository (optional)
retain_package_versions_count = 8.14 # float | The maximum number of versions of each package to keep. (optional)
metadata_expire = 8.14 # float | Time to expire yum metadata in seconds. Only relevant for custom yum repositories. (optional)
excludes = ['excludes_example'] # list[str] | Python packages to exclude from the upstream URL, names separated by newline. You may also specify versions, for example: django~=2.0. (optional)
includes = ['includes_example'] # list[str] | Python packages to include from the upstream URL, names separated by newline. You may also specify versions, for example: django~=2.0. Leave empty to include every package. (optional)
package_types = ['package_types_example'] # list[str] | Package types to sync for Python content, separated by comma. Leave empty to get every package type. Package types are: bdist_dmg, bdist_dumb, bdist_egg, bdist_msi, bdist_rpm, bdist_wheel, bdist_wininst, sdist. (optional)

try:
    # Create a custom repository
    api_instance.post_repositories(name, product_id, content_type, description=description, label=label, url=url, os_versions=os_versions, gpg_key_id=gpg_key_id, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, unprotected=unprotected, checksum_type=checksum_type, docker_upstream_name=docker_upstream_name, include_tags=include_tags, exclude_tags=exclude_tags, download_policy=download_policy, download_concurrency=download_concurrency, mirroring_policy=mirroring_policy, verify_ssl_on_sync=verify_ssl_on_sync, upstream_username=upstream_username, upstream_password=upstream_password, upstream_authentication_token=upstream_authentication_token, deb_releases=deb_releases, deb_components=deb_components, deb_architectures=deb_architectures, ignorable_content=ignorable_content, ansible_collection_requirements=ansible_collection_requirements, ansible_collection_auth_url=ansible_collection_auth_url, ansible_collection_auth_token=ansible_collection_auth_token, http_proxy_policy=http_proxy_policy, http_proxy_id=http_proxy_id, arch=arch, retain_package_versions_count=retain_package_versions_count, metadata_expire=metadata_expire, excludes=excludes, includes=includes, package_types=package_types)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the repository |
 **product_id** | **float**| Product the repository belongs to |
 **content_type** | **str**| Type of repository. Available types endpoint: /katello/api/repositories/repository_types |
 **description** | **str**| Description of the repository | [optional]
 **label** | **str**|  | [optional]
 **url** | **str**| repository source url | [optional]
 **os_versions** | [**list[str]**](str.md)| Identifies whether the repository should be unavailable on a client with a non-matching OS version. Pass [] to make repo available for clients regardless of OS version. Maximum length 1; allowed tags are: rhel-6, rhel-7, rhel-8, rhel-9 | [optional]
 **gpg_key_id** | **float**| id of the gpg key that will be assigned to the new repository | [optional]
 **ssl_ca_cert_id** | **float**| Identifier of the content credential containing the SSL CA Cert | [optional]
 **ssl_client_cert_id** | **float**| Identifier of the content credential containing the SSL Client Cert | [optional]
 **ssl_client_key_id** | **float**| Identifier of the content credential containing the SSL Client Key | [optional]
 **unprotected** | **bool**| true if this repository can be published via HTTP | [optional]
 **checksum_type** | **str**| Checksum of the repository, currently &#39;sha1&#39; &amp; &#39;sha256&#39; are supported | [optional]
 **docker_upstream_name** | **str**| Name of the upstream docker repository | [optional]
 **include_tags** | [**list[str]**](str.md)| Comma-separated list of tags to sync for a container image repository | [optional]
 **exclude_tags** | [**list[str]**](str.md)| Comma-separated list of tags to exclude when syncing a container image repository. Default: any tag ending in \&quot;-source\&quot; | [optional]
 **download_policy** | **str**| download policy for yum, deb, and docker repos (either &#39;immediate&#39; or &#39;on_demand&#39;) | [optional]
 **download_concurrency** | **float**| Used to determine download concurrency of the repository in pulp3. Use value less than 20. Defaults to 10 | [optional]
 **mirroring_policy** | **str**| Policy to set for mirroring content.  Must be one of additive. | [optional]
 **verify_ssl_on_sync** | **bool**| if true, Katello will verify the upstream url&#39;s SSL certifcates are signed by a trusted CA | [optional]
 **upstream_username** | **str**| Username of the upstream repository user used for authentication | [optional]
 **upstream_password** | **str**| Password of the upstream repository user used for authentication | [optional]
 **upstream_authentication_token** | **str**| Password of the upstream authentication token. | [optional]
 **deb_releases** | **str**| whitespace-separated list of releases to be synced from deb-archive | [optional]
 **deb_components** | **str**| whitespace-separated list of repo components to be synced from deb-archive | [optional]
 **deb_architectures** | **str**| whitespace-separated list of architectures to be synced from deb-archive | [optional]
 **ignorable_content** | [**list[str]**](str.md)| List of content units to ignore while syncing a yum repository. Must be subset of srpm,treeinfo | [optional]
 **ansible_collection_requirements** | **str**| Contents of requirement yaml file to sync from URL | [optional]
 **ansible_collection_auth_url** | **str**| The URL to receive a session token from, e.g. used with Automation Hub. | [optional]
 **ansible_collection_auth_token** | **str**| The token key to use for authentication. | [optional]
 **http_proxy_policy** | **str**| policies for HTTP proxy for content sync | [optional]
 **http_proxy_id** | **float**| ID of a HTTP Proxy | [optional]
 **arch** | **str**| Architecture of content in the repository | [optional]
 **retain_package_versions_count** | **float**| The maximum number of versions of each package to keep. | [optional]
 **metadata_expire** | **float**| Time to expire yum metadata in seconds. Only relevant for custom yum repositories. | [optional]
 **excludes** | [**list[str]**](str.md)| Python packages to exclude from the upstream URL, names separated by newline. You may also specify versions, for example: django~&#x3D;2.0. | [optional]
 **includes** | [**list[str]**](str.md)| Python packages to include from the upstream URL, names separated by newline. You may also specify versions, for example: django~&#x3D;2.0. Leave empty to include every package. | [optional]
 **package_types** | [**list[str]**](str.md)| Package types to sync for Python content, separated by comma. Leave empty to get every package type. Package types are: bdist_dmg, bdist_dumb, bdist_egg, bdist_msi, bdist_rpm, bdist_wheel, bdist_wininst, sdist. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_repositories_id_reclaim_space**
> post_repositories_id_reclaim_space(id)

Reclaim space from an On Demand repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID

try:
    # Reclaim space from an On Demand repository
    api_instance.post_repositories_id_reclaim_space(id)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_repositories_id_reclaim_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_repositories_id_sync**
> post_repositories_id_sync(id, source_url=source_url, incremental=incremental, skip_metadata_check=skip_metadata_check, validate_contents=validate_contents)

Sync a repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID
source_url = 'source_url_example' # str | temporarily override feed URL for sync (optional)
incremental = true # bool | perform an incremental import (optional)
skip_metadata_check = true # bool | Force sync even if no upstream changes are detected. Only used with yum or deb repositories. (optional)
validate_contents = true # bool | Force a sync and validate the checksums of all content. Only used with yum repositories. (optional)

try:
    # Sync a repository
    api_instance.post_repositories_id_sync(id, source_url=source_url, incremental=incremental, skip_metadata_check=skip_metadata_check, validate_contents=validate_contents)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_repositories_id_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |
 **source_url** | **str**| temporarily override feed URL for sync | [optional]
 **incremental** | **bool**| perform an incremental import | [optional]
 **skip_metadata_check** | **bool**| Force sync even if no upstream changes are detected. Only used with yum or deb repositories. | [optional]
 **validate_contents** | **bool**| Force a sync and validate the checksums of all content. Only used with yum repositories. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_repositories_id_upload_content**
> post_repositories_id_upload_content(id, content, content_type=content_type)

Upload content into the repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID
content = '/path/to/file.txt' # file | Content files to upload. Can be a single file or array of files.
content_type = 'content_type_example' # str | The type of content to upload (srpm, file, etc.). Check uploadable types here: /katello/api/repositories/repository_types (optional)

try:
    # Upload content into the repository
    api_instance.post_repositories_id_upload_content(id, content, content_type=content_type)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_repositories_id_upload_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |
 **content** | **file**| Content files to upload. Can be a single file or array of files. |
 **content_type** | **str**| The type of content to upload (srpm, file, etc.). Check uploadable types here: /katello/api/repositories/repository_types | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_repositories_id_verify_checksum**
> post_repositories_id_verify_checksum(id)

Verify checksum of repository contents



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID

try:
    # Verify checksum of repository contents
    api_instance.post_repositories_id_verify_checksum(id)
except ApiException as e:
    print("Exception when calling RepositoriesApi->post_repositories_id_verify_checksum: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repositories_id**
> put_repositories_id(id, name=name, description=description, url=url, os_versions=os_versions, gpg_key_id=gpg_key_id, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, unprotected=unprotected, checksum_type=checksum_type, docker_upstream_name=docker_upstream_name, include_tags=include_tags, exclude_tags=exclude_tags, download_policy=download_policy, download_concurrency=download_concurrency, mirroring_policy=mirroring_policy, verify_ssl_on_sync=verify_ssl_on_sync, upstream_username=upstream_username, upstream_password=upstream_password, upstream_authentication_token=upstream_authentication_token, deb_releases=deb_releases, deb_components=deb_components, deb_architectures=deb_architectures, ignorable_content=ignorable_content, ansible_collection_requirements=ansible_collection_requirements, ansible_collection_auth_url=ansible_collection_auth_url, ansible_collection_auth_token=ansible_collection_auth_token, http_proxy_policy=http_proxy_policy, http_proxy_id=http_proxy_id, arch=arch, retain_package_versions_count=retain_package_versions_count, metadata_expire=metadata_expire, excludes=excludes, includes=includes, package_types=package_types)

Update a repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID
name = 'name_example' # str |  (optional)
description = 'description_example' # str | description of the repository (optional)
url = 'url_example' # str | repository source url (optional)
os_versions = ['os_versions_example'] # list[str] | Identifies whether the repository should be unavailable on a client with a non-matching OS version. Pass [] to make repo available for clients regardless of OS version. Maximum length 1; allowed tags are: rhel-6, rhel-7, rhel-8, rhel-9 (optional)
gpg_key_id = 8.14 # float | id of the gpg key that will be assigned to the new repository (optional)
ssl_ca_cert_id = 8.14 # float | Identifier of the content credential containing the SSL CA Cert (optional)
ssl_client_cert_id = 8.14 # float | Identifier of the content credential containing the SSL Client Cert (optional)
ssl_client_key_id = 8.14 # float | Identifier of the content credential containing the SSL Client Key (optional)
unprotected = true # bool | true if this repository can be published via HTTP (optional)
checksum_type = 'checksum_type_example' # str | Checksum of the repository, currently 'sha1' & 'sha256' are supported (optional)
docker_upstream_name = 'docker_upstream_name_example' # str | Name of the upstream docker repository (optional)
include_tags = ['include_tags_example'] # list[str] | Comma-separated list of tags to sync for a container image repository (optional)
exclude_tags = ['exclude_tags_example'] # list[str] | Comma-separated list of tags to exclude when syncing a container image repository. Default: any tag ending in \"-source\" (optional)
download_policy = 'download_policy_example' # str | download policy for yum, deb, and docker repos (either 'immediate' or 'on_demand') (optional)
download_concurrency = 8.14 # float | Used to determine download concurrency of the repository in pulp3. Use value less than 20. Defaults to 10 (optional)
mirroring_policy = 'mirroring_policy_example' # str | Policy to set for mirroring content.  Must be one of additive. (optional)
verify_ssl_on_sync = true # bool | if true, Katello will verify the upstream url's SSL certifcates are signed by a trusted CA (optional)
upstream_username = 'upstream_username_example' # str | Username of the upstream repository user used for authentication (optional)
upstream_password = 'upstream_password_example' # str | Password of the upstream repository user used for authentication (optional)
upstream_authentication_token = 'upstream_authentication_token_example' # str | Password of the upstream authentication token. (optional)
deb_releases = 'deb_releases_example' # str | whitespace-separated list of releases to be synced from deb-archive (optional)
deb_components = 'deb_components_example' # str | whitespace-separated list of repo components to be synced from deb-archive (optional)
deb_architectures = 'deb_architectures_example' # str | whitespace-separated list of architectures to be synced from deb-archive (optional)
ignorable_content = ['ignorable_content_example'] # list[str] | List of content units to ignore while syncing a yum repository. Must be subset of srpm,treeinfo (optional)
ansible_collection_requirements = 'ansible_collection_requirements_example' # str | Contents of requirement yaml file to sync from URL (optional)
ansible_collection_auth_url = 'ansible_collection_auth_url_example' # str | The URL to receive a session token from, e.g. used with Automation Hub. (optional)
ansible_collection_auth_token = 'ansible_collection_auth_token_example' # str | The token key to use for authentication. (optional)
http_proxy_policy = 'http_proxy_policy_example' # str | policies for HTTP proxy for content sync (optional)
http_proxy_id = 8.14 # float | ID of a HTTP Proxy (optional)
arch = 'arch_example' # str | Architecture of content in the repository (optional)
retain_package_versions_count = 8.14 # float | The maximum number of versions of each package to keep. (optional)
metadata_expire = 8.14 # float | Time to expire yum metadata in seconds. Only relevant for custom yum repositories. (optional)
excludes = ['excludes_example'] # list[str] | Python packages to exclude from the upstream URL, names separated by newline. You may also specify versions, for example: django~=2.0. (optional)
includes = ['includes_example'] # list[str] | Python packages to include from the upstream URL, names separated by newline. You may also specify versions, for example: django~=2.0. Leave empty to include every package. (optional)
package_types = ['package_types_example'] # list[str] | Package types to sync for Python content, separated by comma. Leave empty to get every package type. Package types are: bdist_dmg, bdist_dumb, bdist_egg, bdist_msi, bdist_rpm, bdist_wheel, bdist_wininst, sdist. (optional)

try:
    # Update a repository
    api_instance.put_repositories_id(id, name=name, description=description, url=url, os_versions=os_versions, gpg_key_id=gpg_key_id, ssl_ca_cert_id=ssl_ca_cert_id, ssl_client_cert_id=ssl_client_cert_id, ssl_client_key_id=ssl_client_key_id, unprotected=unprotected, checksum_type=checksum_type, docker_upstream_name=docker_upstream_name, include_tags=include_tags, exclude_tags=exclude_tags, download_policy=download_policy, download_concurrency=download_concurrency, mirroring_policy=mirroring_policy, verify_ssl_on_sync=verify_ssl_on_sync, upstream_username=upstream_username, upstream_password=upstream_password, upstream_authentication_token=upstream_authentication_token, deb_releases=deb_releases, deb_components=deb_components, deb_architectures=deb_architectures, ignorable_content=ignorable_content, ansible_collection_requirements=ansible_collection_requirements, ansible_collection_auth_url=ansible_collection_auth_url, ansible_collection_auth_token=ansible_collection_auth_token, http_proxy_policy=http_proxy_policy, http_proxy_id=http_proxy_id, arch=arch, retain_package_versions_count=retain_package_versions_count, metadata_expire=metadata_expire, excludes=excludes, includes=includes, package_types=package_types)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_repositories_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |
 **name** | **str**|  | [optional]
 **description** | **str**| description of the repository | [optional]
 **url** | **str**| repository source url | [optional]
 **os_versions** | [**list[str]**](str.md)| Identifies whether the repository should be unavailable on a client with a non-matching OS version. Pass [] to make repo available for clients regardless of OS version. Maximum length 1; allowed tags are: rhel-6, rhel-7, rhel-8, rhel-9 | [optional]
 **gpg_key_id** | **float**| id of the gpg key that will be assigned to the new repository | [optional]
 **ssl_ca_cert_id** | **float**| Identifier of the content credential containing the SSL CA Cert | [optional]
 **ssl_client_cert_id** | **float**| Identifier of the content credential containing the SSL Client Cert | [optional]
 **ssl_client_key_id** | **float**| Identifier of the content credential containing the SSL Client Key | [optional]
 **unprotected** | **bool**| true if this repository can be published via HTTP | [optional]
 **checksum_type** | **str**| Checksum of the repository, currently &#39;sha1&#39; &amp; &#39;sha256&#39; are supported | [optional]
 **docker_upstream_name** | **str**| Name of the upstream docker repository | [optional]
 **include_tags** | [**list[str]**](str.md)| Comma-separated list of tags to sync for a container image repository | [optional]
 **exclude_tags** | [**list[str]**](str.md)| Comma-separated list of tags to exclude when syncing a container image repository. Default: any tag ending in \&quot;-source\&quot; | [optional]
 **download_policy** | **str**| download policy for yum, deb, and docker repos (either &#39;immediate&#39; or &#39;on_demand&#39;) | [optional]
 **download_concurrency** | **float**| Used to determine download concurrency of the repository in pulp3. Use value less than 20. Defaults to 10 | [optional]
 **mirroring_policy** | **str**| Policy to set for mirroring content.  Must be one of additive. | [optional]
 **verify_ssl_on_sync** | **bool**| if true, Katello will verify the upstream url&#39;s SSL certifcates are signed by a trusted CA | [optional]
 **upstream_username** | **str**| Username of the upstream repository user used for authentication | [optional]
 **upstream_password** | **str**| Password of the upstream repository user used for authentication | [optional]
 **upstream_authentication_token** | **str**| Password of the upstream authentication token. | [optional]
 **deb_releases** | **str**| whitespace-separated list of releases to be synced from deb-archive | [optional]
 **deb_components** | **str**| whitespace-separated list of repo components to be synced from deb-archive | [optional]
 **deb_architectures** | **str**| whitespace-separated list of architectures to be synced from deb-archive | [optional]
 **ignorable_content** | [**list[str]**](str.md)| List of content units to ignore while syncing a yum repository. Must be subset of srpm,treeinfo | [optional]
 **ansible_collection_requirements** | **str**| Contents of requirement yaml file to sync from URL | [optional]
 **ansible_collection_auth_url** | **str**| The URL to receive a session token from, e.g. used with Automation Hub. | [optional]
 **ansible_collection_auth_token** | **str**| The token key to use for authentication. | [optional]
 **http_proxy_policy** | **str**| policies for HTTP proxy for content sync | [optional]
 **http_proxy_id** | **float**| ID of a HTTP Proxy | [optional]
 **arch** | **str**| Architecture of content in the repository | [optional]
 **retain_package_versions_count** | **float**| The maximum number of versions of each package to keep. | [optional]
 **metadata_expire** | **float**| Time to expire yum metadata in seconds. Only relevant for custom yum repositories. | [optional]
 **excludes** | [**list[str]**](str.md)| Python packages to exclude from the upstream URL, names separated by newline. You may also specify versions, for example: django~&#x3D;2.0. | [optional]
 **includes** | [**list[str]**](str.md)| Python packages to include from the upstream URL, names separated by newline. You may also specify versions, for example: django~&#x3D;2.0. Leave empty to include every package. | [optional]
 **package_types** | [**list[str]**](str.md)| Package types to sync for Python content, separated by comma. Leave empty to get every package type. Package types are: bdist_dmg, bdist_dumb, bdist_egg, bdist_msi, bdist_rpm, bdist_wheel, bdist_wininst, sdist. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repositories_id_import_uploads**
> put_repositories_id_import_uploads(id, _async=_async, publish_repository=publish_repository, sync_capsule=sync_capsule, content_type=content_type, uploads=uploads)

Import uploads into a repository



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | Repository id
_async = true # bool | Do not wait for the ImportUpload action to finish. Default: false (optional)
publish_repository = true # bool | Whether or not to regenerate the repository on disk. Default: true (optional)
sync_capsule = true # bool | Whether or not to sync an external capsule after upload. Default: true (optional)
content_type = 'content_type_example' # str | content type ('deb', 'docker_manifest', 'file', 'ostree_ref', 'rpm', 'srpm') (optional)
uploads = ['uploads_example'] # list[str] | Array of uploads to import (optional)

try:
    # Import uploads into a repository
    api_instance.put_repositories_id_import_uploads(id, _async=_async, publish_repository=publish_repository, sync_capsule=sync_capsule, content_type=content_type, uploads=uploads)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_repositories_id_import_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Repository id |
 **_async** | **bool**| Do not wait for the ImportUpload action to finish. Default: false | [optional]
 **publish_repository** | **bool**| Whether or not to regenerate the repository on disk. Default: true | [optional]
 **sync_capsule** | **bool**| Whether or not to sync an external capsule after upload. Default: true | [optional]
 **content_type** | **str**| content type (&#39;deb&#39;, &#39;docker_manifest&#39;, &#39;file&#39;, &#39;ostree_ref&#39;, &#39;rpm&#39;, &#39;srpm&#39;) | [optional]
 **uploads** | [**list[str]**](str.md)| Array of uploads to import | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repositories_id_remove_content**
> put_repositories_id_remove_content(id, ids, content_type=content_type, sync_capsule=sync_capsule)



Remove content from a repository

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID
ids = ['ids_example'] # list[str] | Array of content ids to remove
content_type = 'content_type_example' # str | The type of content to remove (srpm, docker_manifest, etc.). Check removable types here: /katello/api/repositories/repository_types (optional)
sync_capsule = true # bool | Whether or not to sync an external capsule after upload. Default: true (optional)

try:
    api_instance.put_repositories_id_remove_content(id, ids, content_type=content_type, sync_capsule=sync_capsule)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_repositories_id_remove_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |
 **ids** | [**list[str]**](str.md)| Array of content ids to remove |
 **content_type** | **str**| The type of content to remove (srpm, docker_manifest, etc.). Check removable types here: /katello/api/repositories/repository_types | [optional]
 **sync_capsule** | **bool**| Whether or not to sync an external capsule after upload. Default: true | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repositories_id_remove_docker_manifests**
> put_repositories_id_remove_docker_manifests(id, ids, content_type=content_type, sync_capsule=sync_capsule)



Remove content from a repository

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID
ids = ['ids_example'] # list[str] | Array of content ids to remove
content_type = 'content_type_example' # str | The type of content to remove (srpm, docker_manifest, etc.). Check removable types here: /katello/api/repositories/repository_types (optional)
sync_capsule = true # bool | Whether or not to sync an external capsule after upload. Default: true (optional)

try:
    api_instance.put_repositories_id_remove_docker_manifests(id, ids, content_type=content_type, sync_capsule=sync_capsule)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_repositories_id_remove_docker_manifests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |
 **ids** | [**list[str]**](str.md)| Array of content ids to remove |
 **content_type** | **str**| The type of content to remove (srpm, docker_manifest, etc.). Check removable types here: /katello/api/repositories/repository_types | [optional]
 **sync_capsule** | **bool**| Whether or not to sync an external capsule after upload. Default: true | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repositories_id_remove_packages**
> put_repositories_id_remove_packages(id, ids, content_type=content_type, sync_capsule=sync_capsule)



Remove content from a repository

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | repository ID
ids = ['ids_example'] # list[str] | Array of content ids to remove
content_type = 'content_type_example' # str | The type of content to remove (srpm, docker_manifest, etc.). Check removable types here: /katello/api/repositories/repository_types (optional)
sync_capsule = true # bool | Whether or not to sync an external capsule after upload. Default: true (optional)

try:
    api_instance.put_repositories_id_remove_packages(id, ids, content_type=content_type, sync_capsule=sync_capsule)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_repositories_id_remove_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| repository ID |
 **ids** | [**list[str]**](str.md)| Array of content ids to remove |
 **content_type** | **str**| The type of content to remove (srpm, docker_manifest, etc.). Check removable types here: /katello/api/repositories/repository_types | [optional]
 **sync_capsule** | **bool**| Whether or not to sync an external capsule after upload. Default: true | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repositories_id_republish**
> put_repositories_id_republish(id, force=force)

Forces a republish of the specified repository, regenerating metadata and symlinks on the filesystem. Not allowed for repositories with the 'Complete Mirroring' mirroring policy.



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RepositoriesApi()
id = 8.14 # float | Repository identifier
force = true # bool | Force metadata regeneration to proceed. Dangerous when repositories use the 'Complete Mirroring' mirroring policy (optional)

try:
    # Forces a republish of the specified repository, regenerating metadata and symlinks on the filesystem. Not allowed for repositories with the 'Complete Mirroring' mirroring policy.
    api_instance.put_repositories_id_republish(id, force=force)
except ApiException as e:
    print("Exception when calling RepositoriesApi->put_repositories_id_republish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Repository identifier |
 **force** | **bool**| Force metadata regeneration to proceed. Dangerous when repositories use the &#39;Complete Mirroring&#39; mirroring policy | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
