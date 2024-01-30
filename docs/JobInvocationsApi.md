# pyforeman.JobInvocationsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_invocations**](JobInvocationsApi.md#get_job_invocations) | **GET** /job_invocations | List job invocations
[**get_job_invocations_id**](JobInvocationsApi.md#get_job_invocations_id) | **GET** /job_invocations/{id} | Show job invocation
[**get_job_invocations_id_hosts_host_id**](JobInvocationsApi.md#get_job_invocations_id_hosts_host_id) | **GET** /job_invocations/{id}/hosts/{host_id} | Get output for a host
[**get_job_invocations_id_hosts_host_id_raw**](JobInvocationsApi.md#get_job_invocations_id_hosts_host_id_raw) | **GET** /job_invocations/{id}/hosts/{host_id}/raw | Get raw output for a host
[**get_job_invocations_id_outputs**](JobInvocationsApi.md#get_job_invocations_id_outputs) | **GET** /job_invocations/{id}/outputs | Get outputs of hosts in a job
[**post_job_invocations**](JobInvocationsApi.md#post_job_invocations) | **POST** /job_invocations | Create a job invocation
[**post_job_invocations_id_cancel**](JobInvocationsApi.md#post_job_invocations_id_cancel) | **POST** /job_invocations/{id}/cancel | Cancel job invocation
[**post_job_invocations_id_rerun**](JobInvocationsApi.md#post_job_invocations_id_rerun) | **POST** /job_invocations/{id}/rerun | Rerun job on failed hosts


# **get_job_invocations**
> get_job_invocations(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List job invocations



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.JobInvocationsApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List job invocations
    api_instance.get_job_invocations(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling JobInvocationsApi->get_job_invocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
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

# **get_job_invocations_id**
> get_job_invocations_id(id, location_id=location_id, organization_id=organization_id, host_status=host_status)

Show job invocation



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.JobInvocationsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
host_status = true # bool | Show Job status for the hosts (optional)

try:
    # Show job invocation
    api_instance.get_job_invocations_id(id, location_id=location_id, organization_id=organization_id, host_status=host_status)
except ApiException as e:
    print("Exception when calling JobInvocationsApi->get_job_invocations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **host_status** | **bool**| Show Job status for the hosts | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_invocations_id_hosts_host_id**
> get_job_invocations_id_hosts_host_id(id, host_id, location_id=location_id, organization_id=organization_id, since=since)

Get output for a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.JobInvocationsApi()
id = 'id_example' # str |
host_id = 'host_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
since = 'since_example' # str |  (optional)

try:
    # Get output for a host
    api_instance.get_job_invocations_id_hosts_host_id(id, host_id, location_id=location_id, organization_id=organization_id, since=since)
except ApiException as e:
    print("Exception when calling JobInvocationsApi->get_job_invocations_id_hosts_host_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **host_id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **since** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_invocations_id_hosts_host_id_raw**
> get_job_invocations_id_hosts_host_id_raw(id, host_id, location_id=location_id, organization_id=organization_id)

Get raw output for a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.JobInvocationsApi()
id = 'id_example' # str |
host_id = 'host_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Get raw output for a host
    api_instance.get_job_invocations_id_hosts_host_id_raw(id, host_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling JobInvocationsApi->get_job_invocations_id_hosts_host_id_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **host_id** | **str**|  |
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

# **get_job_invocations_id_outputs**
> get_job_invocations_id_outputs(id, location_id=location_id, organization_id=organization_id, search_query=search_query, since=since, raw=raw)

Get outputs of hosts in a job



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.JobInvocationsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search_query = 'search_query_example' # str |  (optional)
since = 'since_example' # str |  (optional)
raw = 'raw_example' # str |  (optional)

try:
    # Get outputs of hosts in a job
    api_instance.get_job_invocations_id_outputs(id, location_id=location_id, organization_id=organization_id, search_query=search_query, since=since, raw=raw)
except ApiException as e:
    print("Exception when calling JobInvocationsApi->get_job_invocations_id_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **search_query** | **str**|  | [optional]
 **since** | **str**|  | [optional]
 **raw** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job_invocations**
> post_job_invocations(job_invocation_targeting_type, location_id=location_id, organization_id=organization_id, job_invocation_job_template_id=job_invocation_job_template_id, job_invocation_randomized_ordering=job_invocation_randomized_ordering, job_invocation_ssh_effective_user=job_invocation_ssh_effective_user, job_invocation_ssh_effective_user_password=job_invocation_ssh_effective_user_password, job_invocation_ssh_user=job_invocation_ssh_user, job_invocation_password=job_invocation_password, job_invocation_key_passphrase=job_invocation_key_passphrase, job_invocation_recurrence_cron_line=job_invocation_recurrence_cron_line, job_invocation_recurrence_max_iteration=job_invocation_recurrence_max_iteration, job_invocation_recurrence_end_time=job_invocation_recurrence_end_time, job_invocation_recurrence_purpose=job_invocation_recurrence_purpose, job_invocation_scheduling_start_at=job_invocation_scheduling_start_at, job_invocation_scheduling_start_before=job_invocation_scheduling_start_before, job_invocation_concurrency_control_concurrency_level=job_invocation_concurrency_control_concurrency_level, job_invocation_bookmark_id=job_invocation_bookmark_id, job_invocation_search_query=job_invocation_search_query, job_invocation_description_format=job_invocation_description_format, job_invocation_execution_timeout_interval=job_invocation_execution_timeout_interval, job_invocation_feature=job_invocation_feature, job_invocation_time_to_pickup=job_invocation_time_to_pickup)

Create a job invocation



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.JobInvocationsApi()
job_invocation_targeting_type = 'job_invocation_targeting_type_example' # str | Invocation type, one of {\"static_query\"=>\"Static Query\", \"dynamic_query\"=>\"Dynamic Query\"}
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
job_invocation_job_template_id = 'job_invocation_job_template_id_example' # str | The job template to use, parameter is required unless feature was specified (optional)
job_invocation_randomized_ordering = true # bool | Execute the jobs on hosts in randomized order (optional)
job_invocation_ssh_effective_user = 'job_invocation_ssh_effective_user_example' # str | What user should be used to run the script (using sudo-like mechanisms). Defaults to a template parameter or global setting. (optional)
job_invocation_ssh_effective_user_password = 'job_invocation_ssh_effective_user_password_example' # str | Set password for effective user (using sudo-like mechanisms) (optional)
job_invocation_ssh_user = 'job_invocation_ssh_user_example' # str | Set SSH user (optional)
job_invocation_password = 'job_invocation_password_example' # str | Set SSH password (optional)
job_invocation_key_passphrase = 'job_invocation_key_passphrase_example' # str | Set SSH key passphrase (optional)
job_invocation_recurrence_cron_line = 'job_invocation_recurrence_cron_line_example' # str | How often the job should occur, in the cron format (optional)
job_invocation_recurrence_max_iteration = 8.14 # float | Repeat a maximum of N times (optional)
job_invocation_recurrence_end_time = 'job_invocation_recurrence_end_time_example' # str | Perform no more executions after this time (optional)
job_invocation_recurrence_purpose = 'job_invocation_recurrence_purpose_example' # str | Designation of a special purpose (optional)
job_invocation_scheduling_start_at = 'job_invocation_scheduling_start_at_example' # str | Schedule the job for a future time (optional)
job_invocation_scheduling_start_before = 'job_invocation_scheduling_start_before_example' # str | Indicates that the action should be cancelled if it cannot be started before this time. (optional)
job_invocation_concurrency_control_concurrency_level = 8.14 # float | Run at most N tasks at a time (optional)
job_invocation_bookmark_id = 8.14 # float |  (optional)
job_invocation_search_query = 'job_invocation_search_query_example' # str |  (optional)
job_invocation_description_format = 'job_invocation_description_format_example' # str | Override the description format from the template for this invocation only (optional)
job_invocation_execution_timeout_interval = 8.14 # float | Override the timeout interval from the template for this invocation only (optional)
job_invocation_feature = 'job_invocation_feature_example' # str | Remote execution feature label that should be triggered, job template assigned to this feature will be used (optional)
job_invocation_time_to_pickup = 8.14 # float | Override the global time to pickup interval for this invocation only (optional)

try:
    # Create a job invocation
    api_instance.post_job_invocations(job_invocation_targeting_type, location_id=location_id, organization_id=organization_id, job_invocation_job_template_id=job_invocation_job_template_id, job_invocation_randomized_ordering=job_invocation_randomized_ordering, job_invocation_ssh_effective_user=job_invocation_ssh_effective_user, job_invocation_ssh_effective_user_password=job_invocation_ssh_effective_user_password, job_invocation_ssh_user=job_invocation_ssh_user, job_invocation_password=job_invocation_password, job_invocation_key_passphrase=job_invocation_key_passphrase, job_invocation_recurrence_cron_line=job_invocation_recurrence_cron_line, job_invocation_recurrence_max_iteration=job_invocation_recurrence_max_iteration, job_invocation_recurrence_end_time=job_invocation_recurrence_end_time, job_invocation_recurrence_purpose=job_invocation_recurrence_purpose, job_invocation_scheduling_start_at=job_invocation_scheduling_start_at, job_invocation_scheduling_start_before=job_invocation_scheduling_start_before, job_invocation_concurrency_control_concurrency_level=job_invocation_concurrency_control_concurrency_level, job_invocation_bookmark_id=job_invocation_bookmark_id, job_invocation_search_query=job_invocation_search_query, job_invocation_description_format=job_invocation_description_format, job_invocation_execution_timeout_interval=job_invocation_execution_timeout_interval, job_invocation_feature=job_invocation_feature, job_invocation_time_to_pickup=job_invocation_time_to_pickup)
except ApiException as e:
    print("Exception when calling JobInvocationsApi->post_job_invocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_invocation_targeting_type** | **str**| Invocation type, one of {\&quot;static_query\&quot;&#x3D;&gt;\&quot;Static Query\&quot;, \&quot;dynamic_query\&quot;&#x3D;&gt;\&quot;Dynamic Query\&quot;} |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **job_invocation_job_template_id** | **str**| The job template to use, parameter is required unless feature was specified | [optional]
 **job_invocation_randomized_ordering** | **bool**| Execute the jobs on hosts in randomized order | [optional]
 **job_invocation_ssh_effective_user** | **str**| What user should be used to run the script (using sudo-like mechanisms). Defaults to a template parameter or global setting. | [optional]
 **job_invocation_ssh_effective_user_password** | **str**| Set password for effective user (using sudo-like mechanisms) | [optional]
 **job_invocation_ssh_user** | **str**| Set SSH user | [optional]
 **job_invocation_password** | **str**| Set SSH password | [optional]
 **job_invocation_key_passphrase** | **str**| Set SSH key passphrase | [optional]
 **job_invocation_recurrence_cron_line** | **str**| How often the job should occur, in the cron format | [optional]
 **job_invocation_recurrence_max_iteration** | **float**| Repeat a maximum of N times | [optional]
 **job_invocation_recurrence_end_time** | **str**| Perform no more executions after this time | [optional]
 **job_invocation_recurrence_purpose** | **str**| Designation of a special purpose | [optional]
 **job_invocation_scheduling_start_at** | **str**| Schedule the job for a future time | [optional]
 **job_invocation_scheduling_start_before** | **str**| Indicates that the action should be cancelled if it cannot be started before this time. | [optional]
 **job_invocation_concurrency_control_concurrency_level** | **float**| Run at most N tasks at a time | [optional]
 **job_invocation_bookmark_id** | **float**|  | [optional]
 **job_invocation_search_query** | **str**|  | [optional]
 **job_invocation_description_format** | **str**| Override the description format from the template for this invocation only | [optional]
 **job_invocation_execution_timeout_interval** | **float**| Override the timeout interval from the template for this invocation only | [optional]
 **job_invocation_feature** | **str**| Remote execution feature label that should be triggered, job template assigned to this feature will be used | [optional]
 **job_invocation_time_to_pickup** | **float**| Override the global time to pickup interval for this invocation only | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job_invocations_id_cancel**
> post_job_invocations_id_cancel(id, location_id=location_id, organization_id=organization_id, force=force)

Cancel job invocation



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.JobInvocationsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
force = true # bool |  (optional)

try:
    # Cancel job invocation
    api_instance.post_job_invocations_id_cancel(id, location_id=location_id, organization_id=organization_id, force=force)
except ApiException as e:
    print("Exception when calling JobInvocationsApi->post_job_invocations_id_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **force** | **bool**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job_invocations_id_rerun**
> post_job_invocations_id_rerun(id, location_id=location_id, organization_id=organization_id, failed_only=failed_only)

Rerun job on failed hosts



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.JobInvocationsApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
failed_only = true # bool |  (optional)

try:
    # Rerun job on failed hosts
    api_instance.post_job_invocations_id_rerun(id, location_id=location_id, organization_id=organization_id, failed_only=failed_only)
except ApiException as e:
    print("Exception when calling JobInvocationsApi->post_job_invocations_id_rerun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **failed_only** | **bool**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
