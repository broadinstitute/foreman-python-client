# pyforeman.ForemanTasksApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tasks**](ForemanTasksApi.md#get_tasks) | **GET** /tasks | List tasks
[**get_tasks_id**](ForemanTasksApi.md#get_tasks_id) | **GET** /tasks/{id} | Show task details
[**get_tasks_id_details**](ForemanTasksApi.md#get_tasks_id_details) | **GET** /tasks/{id}/details | Show task extended details
[**get_tasks_parent_task_id_sub_tasks**](ForemanTasksApi.md#get_tasks_parent_task_id_sub_tasks) | **GET** /tasks/{parent_task_id}/sub_tasks | Show sub_tasks details
[**get_tasks_summary**](ForemanTasksApi.md#get_tasks_summary) | **GET** /tasks/summary | Show task summary
[**post_tasks_bulk_cancel**](ForemanTasksApi.md#post_tasks_bulk_cancel) | **POST** /tasks/bulk_cancel | Cancel selected cancellable tasks
[**post_tasks_bulk_resume**](ForemanTasksApi.md#post_tasks_bulk_resume) | **POST** /tasks/bulk_resume | Resume all paused error tasks
[**post_tasks_bulk_search**](ForemanTasksApi.md#post_tasks_bulk_search) | **POST** /tasks/bulk_search | List dynflow tasks for uuids
[**post_tasks_bulk_stop**](ForemanTasksApi.md#post_tasks_bulk_stop) | **POST** /tasks/bulk_stop | Stop selected stoppable tasks
[**post_tasks_callback**](ForemanTasksApi.md#post_tasks_callback) | **POST** /tasks/callback | Send data to the task from external executor (such as smart_proxy_dynflow)


# **get_tasks**
> get_tasks(parent_task_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List tasks



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
parent_task_id = 'parent_task_id_example' # str | UUID of the task
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List tasks
    api_instance.get_tasks(parent_task_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_task_id** | **str**| UUID of the task |
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

# **get_tasks_id**
> get_tasks_id(id, location_id=location_id, organization_id=organization_id)

Show task details



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
id = 'id_example' # str | UUID of the task
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show task details
    api_instance.get_tasks_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->get_tasks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID of the task |
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

# **get_tasks_id_details**
> get_tasks_id_details(id, location_id=location_id, organization_id=organization_id)

Show task extended details



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
id = 'id_example' # str | UUID of the task
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show task extended details
    api_instance.get_tasks_id_details(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->get_tasks_id_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID of the task |
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

# **get_tasks_parent_task_id_sub_tasks**
> get_tasks_parent_task_id_sub_tasks(parent_task_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

Show sub_tasks details



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
parent_task_id = 'parent_task_id_example' # str | UUID of the task
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # Show sub_tasks details
    api_instance.get_tasks_parent_task_id_sub_tasks(parent_task_id, location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->get_tasks_parent_task_id_sub_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_task_id** | **str**| UUID of the task |
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

# **get_tasks_summary**
> get_tasks_summary(location_id=location_id, organization_id=organization_id)

Show task summary



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show task summary
    api_instance.get_tasks_summary(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->get_tasks_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **post_tasks_bulk_cancel**
> post_tasks_bulk_cancel(location_id=location_id, organization_id=organization_id, search=search, task_ids=task_ids)

Cancel selected cancellable tasks

Cancels all selected cancellable tasks. Requires a search query or an explicit list of task IDs to be provided.

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | Cancel tasks matching search string (optional)
task_ids = ['task_ids_example'] # list[str] | Cancel specific tasks by ID (optional)

try:
    # Cancel selected cancellable tasks
    api_instance.post_tasks_bulk_cancel(location_id=location_id, organization_id=organization_id, search=search, task_ids=task_ids)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->post_tasks_bulk_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **search** | **str**| Cancel tasks matching search string | [optional]
 **task_ids** | [**list[str]**](str.md)| Cancel specific tasks by ID | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tasks_bulk_resume**
> post_tasks_bulk_resume(location_id=location_id, organization_id=organization_id, search=search, task_ids=task_ids)

Resume all paused error tasks

Resumes all selected resumable tasks. If neither a search query nor an explicit list of task IDs is provided, it tries to resume all tasks in paused state with result error.

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | Resume tasks matching search string (optional)
task_ids = ['task_ids_example'] # list[str] | Resume specific tasks by ID (optional)

try:
    # Resume all paused error tasks
    api_instance.post_tasks_bulk_resume(location_id=location_id, organization_id=organization_id, search=search, task_ids=task_ids)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->post_tasks_bulk_resume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **search** | **str**| Resume tasks matching search string | [optional]
 **task_ids** | [**list[str]**](str.md)| Resume specific tasks by ID | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tasks_bulk_search**
> post_tasks_bulk_search(location_id=location_id, organization_id=organization_id, searches=searches)

List dynflow tasks for uuids

        For every search it returns the list of tasks that satisfty the condition.         The reason for supporting multiple searches is the UI that might be ending         needing periodic updates on task status for various searches at the same time.         This way, it is possible to get all the task statuses with one request.

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
searches = ['searches_example'] # list[str] | List of uuids to fetch info about (optional)

try:
    # List dynflow tasks for uuids
    api_instance.post_tasks_bulk_search(location_id=location_id, organization_id=organization_id, searches=searches)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->post_tasks_bulk_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **searches** | [**list[str]**](str.md)| List of uuids to fetch info about | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tasks_bulk_stop**
> post_tasks_bulk_stop(location_id=location_id, organization_id=organization_id, search=search, task_ids=task_ids)

Stop selected stoppable tasks

Stops all selected tasks which are not already stopped. Requires a search query or an explicit list of task IDs to be provided.

### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | Stop tasks matching search string (optional)
task_ids = ['task_ids_example'] # list[str] | Stop specific tasks by ID (optional)

try:
    # Stop selected stoppable tasks
    api_instance.post_tasks_bulk_stop(location_id=location_id, organization_id=organization_id, search=search, task_ids=task_ids)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->post_tasks_bulk_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **search** | **str**| Stop tasks matching search string | [optional]
 **task_ids** | [**list[str]**](str.md)| Stop specific tasks by ID | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tasks_callback**
> post_tasks_callback(location_id=location_id, organization_id=organization_id, callback_task_id=callback_task_id, callback_step_id=callback_step_id, callbacks=callbacks)

Send data to the task from external executor (such as smart_proxy_dynflow)



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.ForemanTasksApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
callback_task_id = 'callback_task_id_example' # str | UUID of the task (optional)
callback_step_id = 'callback_step_id_example' # str | The ID of the step inside the execution plan to send the event to (optional)
callbacks = ['callbacks_example'] # list[str] |  (optional)

try:
    # Send data to the task from external executor (such as smart_proxy_dynflow)
    api_instance.post_tasks_callback(location_id=location_id, organization_id=organization_id, callback_task_id=callback_task_id, callback_step_id=callback_step_id, callbacks=callbacks)
except ApiException as e:
    print("Exception when calling ForemanTasksApi->post_tasks_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **callback_task_id** | **str**| UUID of the task | [optional]
 **callback_step_id** | **str**| The ID of the step inside the execution plan to send the event to | [optional]
 **callbacks** | [**list[str]**](str.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
