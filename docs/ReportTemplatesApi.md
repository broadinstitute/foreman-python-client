# pyforeman.ReportTemplatesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_report_templates_id**](ReportTemplatesApi.md#delete_report_templates_id) | **DELETE** /report_templates/{id} | Delete a report template
[**get_locations_location_id_report_templates**](ReportTemplatesApi.md#get_locations_location_id_report_templates) | **GET** /locations/{location_id}/report_templates | List all report templates per location
[**get_organizations_organization_id_report_templates**](ReportTemplatesApi.md#get_organizations_organization_id_report_templates) | **GET** /organizations/{organization_id}/report_templates | List all report templates per organization
[**get_report_templates**](ReportTemplatesApi.md#get_report_templates) | **GET** /report_templates | List all report templates
[**get_report_templates_id**](ReportTemplatesApi.md#get_report_templates_id) | **GET** /report_templates/{id} | Show a report template
[**get_report_templates_id_export**](ReportTemplatesApi.md#get_report_templates_id_export) | **GET** /report_templates/{id}/export | Export a report template to ERB
[**get_report_templates_id_report_data_job_id**](ReportTemplatesApi.md#get_report_templates_id_report_data_job_id) | **GET** /report_templates/{id}/report_data/{job_id} | Downloads a generated report
[**get_report_templates_revision**](ReportTemplatesApi.md#get_report_templates_revision) | **GET** /report_templates/revision |
[**post_report_templates**](ReportTemplatesApi.md#post_report_templates) | **POST** /report_templates | Create a report template
[**post_report_templates_id_clone**](ReportTemplatesApi.md#post_report_templates_id_clone) | **POST** /report_templates/{id}/clone | Clone a template
[**post_report_templates_id_generate**](ReportTemplatesApi.md#post_report_templates_id_generate) | **POST** /report_templates/{id}/generate | Generate report from a template
[**post_report_templates_id_schedule_report**](ReportTemplatesApi.md#post_report_templates_id_schedule_report) | **POST** /report_templates/{id}/schedule_report | Schedule generating of a report
[**post_report_templates_import**](ReportTemplatesApi.md#post_report_templates_import) | **POST** /report_templates/import | Import a report template
[**put_report_templates_id**](ReportTemplatesApi.md#put_report_templates_id) | **PUT** /report_templates/{id} | Update a report template


# **delete_report_templates_id**
> delete_report_templates_id(id, location_id=location_id, organization_id=organization_id)

Delete a report template



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Delete a report template
    api_instance.delete_report_templates_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->delete_report_templates_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_locations_location_id_report_templates**
> get_locations_location_id_report_templates(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all report templates per location



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all report templates per location
    api_instance.get_locations_location_id_report_templates(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->get_locations_location_id_report_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations |
 **organization_id** | **float**| Scope by organizations |
 **search** | **str**| filter results | [optional]
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_report_templates**
> get_organizations_organization_id_report_templates(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)

List all report templates per organization



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
organization_id = 8.14 # float | Scope by organizations
location_id = 8.14 # float | Scope by locations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all report templates per organization
    api_instance.get_organizations_organization_id_report_templates(organization_id, location_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->get_organizations_organization_id_report_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **float**| Scope by organizations |
 **location_id** | **float**| Scope by locations |
 **search** | **str**| filter results | [optional]
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_templates**
> get_report_templates(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)

List all report templates



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
location_id = 8.14 # float | Scope by locations
organization_id = 8.14 # float | Scope by organizations
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List all report templates
    api_instance.get_report_templates(location_id, organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->get_report_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Scope by locations |
 **organization_id** | **float**| Scope by organizations |
 **search** | **str**| filter results | [optional]
 **order** | **str**| Sort and order by a searchable field, e.g. &#39;&lt;field&gt; DESC&#39; | [optional]
 **page** | **float**| Page number, starting at 1 | [optional]
 **per_page** | **str**| Number of results per page to return, &#39;all&#39; to return all results | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_templates_id**
> get_report_templates_id(id, location_id=location_id, organization_id=organization_id)

Show a report template



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show a report template
    api_instance.get_report_templates_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->get_report_templates_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_report_templates_id_export**
> get_report_templates_id_export(id, location_id=location_id, organization_id=organization_id)

Export a report template to ERB



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Export a report template to ERB
    api_instance.get_report_templates_id_export(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->get_report_templates_id_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **get_report_templates_id_report_data_job_id**
> get_report_templates_id_report_data_job_id(id, job_id, location_id=location_id, organization_id=organization_id)

Downloads a generated report

        Returns the report data as a raw response.         In case the report hasn't been generated yet, it will return an empty response with http status 204 - NoContent.

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
id = 'id_example' # str |
job_id = 'job_id_example' # str | ID assigned to generating job by the schedule command
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Downloads a generated report
    api_instance.get_report_templates_id_report_data_job_id(id, job_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->get_report_templates_id_report_data_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **job_id** | **str**| ID assigned to generating job by the schedule command |
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

# **get_report_templates_revision**
> get_report_templates_revision(location_id=location_id, organization_id=organization_id, version=version)





### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
version = 'version_example' # str | template version (optional)

try:
    api_instance.get_report_templates_revision(location_id=location_id, organization_id=organization_id, version=version)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->get_report_templates_revision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **version** | **str**| template version | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_report_templates**
> post_report_templates(report_template_name, report_template_template, location_id=location_id, organization_id=organization_id, report_template_description=report_template_description, report_template_snippet=report_template_snippet, report_template_audit_comment=report_template_audit_comment, report_template_locked=report_template_locked, report_template_default=report_template_default, report_template_location_ids=report_template_location_ids, report_template_organization_ids=report_template_organization_ids)

Create a report template



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
report_template_name = 'report_template_name_example' # str |
report_template_template = 'report_template_template_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
report_template_description = 'report_template_description_example' # str |  (optional)
report_template_snippet = true # bool |  (optional)
report_template_audit_comment = 'report_template_audit_comment_example' # str |  (optional)
report_template_locked = true # bool | Whether or not the template is locked for editing (optional)
report_template_default = true # bool | Whether or not the template is added automatically to new organizations and locations (optional)
report_template_location_ids = ['report_template_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
report_template_organization_ids = ['report_template_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Create a report template
    api_instance.post_report_templates(report_template_name, report_template_template, location_id=location_id, organization_id=organization_id, report_template_description=report_template_description, report_template_snippet=report_template_snippet, report_template_audit_comment=report_template_audit_comment, report_template_locked=report_template_locked, report_template_default=report_template_default, report_template_location_ids=report_template_location_ids, report_template_organization_ids=report_template_organization_ids)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->post_report_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_template_name** | **str**|  |
 **report_template_template** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **report_template_description** | **str**|  | [optional]
 **report_template_snippet** | **bool**|  | [optional]
 **report_template_audit_comment** | **str**|  | [optional]
 **report_template_locked** | **bool**| Whether or not the template is locked for editing | [optional]
 **report_template_default** | **bool**| Whether or not the template is added automatically to new organizations and locations | [optional]
 **report_template_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **report_template_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_report_templates_id_clone**
> post_report_templates_id_clone(id, report_template_name, location_id=location_id, organization_id=organization_id)

Clone a template



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
id = 'id_example' # str |
report_template_name = 'report_template_name_example' # str | template name
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Clone a template
    api_instance.post_report_templates_id_clone(id, report_template_name, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->post_report_templates_id_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **report_template_name** | **str**| template name |
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

# **post_report_templates_id_generate**
> post_report_templates_id_generate(id, location_id=location_id, organization_id=organization_id, gzip=gzip, report_format=report_format)

Generate report from a template



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
gzip = false # bool | Compress the report uzing gzip (optional) (default to false)
report_format = 'report_format_example' # str | Report format, defaults to 'csv' (optional)

try:
    # Generate report from a template
    api_instance.post_report_templates_id_generate(id, location_id=location_id, organization_id=organization_id, gzip=gzip, report_format=report_format)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->post_report_templates_id_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **gzip** | **bool**| Compress the report uzing gzip | [optional] [default to false]
 **report_format** | **str**| Report format, defaults to &#39;csv&#39; | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_report_templates_id_schedule_report**
> dict(str, ERRORUNKNOWN) post_report_templates_id_schedule_report(id, location_id=location_id, organization_id=organization_id, gzip=gzip, mail_to=mail_to, generate_at=generate_at, report_format=report_format)

Schedule generating of a report

        The reports are generated asynchronously.         If mail_to is not given, action returns an url to get resulting report from (see <b>report_data</b>).

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
gzip = true # bool | Compress the report using gzip (optional)
mail_to = 'mail_to_example' # str | If set, scheduled report will be delivered via e-mail. Use ',' to separate multiple email addresses. (optional)
generate_at = 'generate_at_example' # str | UTC time to generate report at (optional)
report_format = 'report_format_example' # str | Report format, defaults to 'csv' (optional)

try:
    # Schedule generating of a report
    api_response = api_instance.post_report_templates_id_schedule_report(id, location_id=location_id, organization_id=organization_id, gzip=gzip, mail_to=mail_to, generate_at=generate_at, report_format=report_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->post_report_templates_id_schedule_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **gzip** | **bool**| Compress the report using gzip | [optional]
 **mail_to** | **str**| If set, scheduled report will be delivered via e-mail. Use &#39;,&#39; to separate multiple email addresses. | [optional]
 **generate_at** | **str**| UTC time to generate report at | [optional]
 **report_format** | **str**| Report format, defaults to &#39;csv&#39; | [optional]

### Return type

[**dict(str, ERRORUNKNOWN)**](ERRORUNKNOWN.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_report_templates_import**
> post_report_templates_import(location_id=location_id, organization_id=organization_id, report_template_name=report_template_name, report_template_template=report_template_template, report_template_location_ids=report_template_location_ids, report_template_organization_ids=report_template_organization_ids, options_force=options_force, options_associate=options_associate, options_lock=options_lock, options_default=options_default)

Import a report template



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
report_template_name = 'report_template_name_example' # str | template name (optional)
report_template_template = 'report_template_template_example' # str | template contents including metadata (optional)
report_template_location_ids = ['report_template_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
report_template_organization_ids = ['report_template_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)
options_force = true # bool | use if you want update locked templates (optional)
options_associate = 'options_associate_example' # str | determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata (optional)
options_lock = true # bool | lock imported templates (false by default) (optional)
options_default = true # bool | makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default) (optional)

try:
    # Import a report template
    api_instance.post_report_templates_import(location_id=location_id, organization_id=organization_id, report_template_name=report_template_name, report_template_template=report_template_template, report_template_location_ids=report_template_location_ids, report_template_organization_ids=report_template_organization_ids, options_force=options_force, options_associate=options_associate, options_lock=options_lock, options_default=options_default)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->post_report_templates_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **report_template_name** | **str**| template name | [optional]
 **report_template_template** | **str**| template contents including metadata | [optional]
 **report_template_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **report_template_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]
 **options_force** | **bool**| use if you want update locked templates | [optional]
 **options_associate** | **str**| determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata | [optional]
 **options_lock** | **bool**| lock imported templates (false by default) | [optional]
 **options_default** | **bool**| makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default) | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_report_templates_id**
> put_report_templates_id(id, location_id=location_id, organization_id=organization_id, report_template_name=report_template_name, report_template_description=report_template_description, report_template_template=report_template_template, report_template_snippet=report_template_snippet, report_template_audit_comment=report_template_audit_comment, report_template_locked=report_template_locked, report_template_default=report_template_default, report_template_location_ids=report_template_location_ids, report_template_organization_ids=report_template_organization_ids)

Update a report template



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ReportTemplatesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
report_template_name = 'report_template_name_example' # str |  (optional)
report_template_description = 'report_template_description_example' # str |  (optional)
report_template_template = 'report_template_template_example' # str |  (optional)
report_template_snippet = true # bool |  (optional)
report_template_audit_comment = 'report_template_audit_comment_example' # str |  (optional)
report_template_locked = true # bool | Whether or not the template is locked for editing (optional)
report_template_default = true # bool | Whether or not the template is added automatically to new organizations and locations (optional)
report_template_location_ids = ['report_template_location_ids_example'] # list[str] | REPLACE locations with given ids (optional)
report_template_organization_ids = ['report_template_organization_ids_example'] # list[str] | REPLACE organizations with given ids. (optional)

try:
    # Update a report template
    api_instance.put_report_templates_id(id, location_id=location_id, organization_id=organization_id, report_template_name=report_template_name, report_template_description=report_template_description, report_template_template=report_template_template, report_template_snippet=report_template_snippet, report_template_audit_comment=report_template_audit_comment, report_template_locked=report_template_locked, report_template_default=report_template_default, report_template_location_ids=report_template_location_ids, report_template_organization_ids=report_template_organization_ids)
except ApiException as e:
    print("Exception when calling ReportTemplatesApi->put_report_templates_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **report_template_name** | **str**|  | [optional]
 **report_template_description** | **str**|  | [optional]
 **report_template_template** | **str**|  | [optional]
 **report_template_snippet** | **bool**|  | [optional]
 **report_template_audit_comment** | **str**|  | [optional]
 **report_template_locked** | **bool**| Whether or not the template is locked for editing | [optional]
 **report_template_default** | **bool**| Whether or not the template is added automatically to new organizations and locations | [optional]
 **report_template_location_ids** | [**list[str]**](str.md)| REPLACE locations with given ids | [optional]
 **report_template_organization_ids** | [**list[str]**](str.md)| REPLACE organizations with given ids. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
