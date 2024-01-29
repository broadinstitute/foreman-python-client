# pyforeman.MailNotificationsApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_users_user_id_mail_notifications_mail_notification_id**](MailNotificationsApi.md#delete_users_user_id_mail_notifications_mail_notification_id) | **DELETE** /users/{user_id}/mail_notifications/{mail_notification_id} | Remove an email notification for a user
[**get_mail_notifications**](MailNotificationsApi.md#get_mail_notifications) | **GET** /mail_notifications | List of email notifications
[**get_mail_notifications_id**](MailNotificationsApi.md#get_mail_notifications_id) | **GET** /mail_notifications/{id} | Show an email notification
[**get_users_user_id_mail_notifications**](MailNotificationsApi.md#get_users_user_id_mail_notifications) | **GET** /users/{user_id}/mail_notifications | List all email notifications for a user
[**post_users_user_id_mail_notifications**](MailNotificationsApi.md#post_users_user_id_mail_notifications) | **POST** /users/{user_id}/mail_notifications | Add an email notification for a user
[**put_users_user_id_mail_notifications_mail_notification_id**](MailNotificationsApi.md#put_users_user_id_mail_notifications_mail_notification_id) | **PUT** /users/{user_id}/mail_notifications/{mail_notification_id} | Update an email notification for a user


# **delete_users_user_id_mail_notifications_mail_notification_id**
> delete_users_user_id_mail_notifications_mail_notification_id(user_id, mail_notification_id, location_id=location_id, organization_id=organization_id)

Remove an email notification for a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.MailNotificationsApi()
user_id = 'user_id_example' # str |
mail_notification_id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Remove an email notification for a user
    api_instance.delete_users_user_id_mail_notifications_mail_notification_id(user_id, mail_notification_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling MailNotificationsApi->delete_users_user_id_mail_notifications_mail_notification_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **mail_notification_id** | **float**|  |
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

# **get_mail_notifications**
> get_mail_notifications(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)

List of email notifications



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.MailNotificationsApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
search = 'search_example' # str | filter results (optional)
order = 'order_example' # str | Sort and order by a searchable field, e.g. '<field> DESC' (optional)
page = 8.14 # float | Page number, starting at 1 (optional)
per_page = 'per_page_example' # str | Number of results per page to return, 'all' to return all results (optional)

try:
    # List of email notifications
    api_instance.get_mail_notifications(location_id=location_id, organization_id=organization_id, search=search, order=order, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling MailNotificationsApi->get_mail_notifications: %s\n" % e)
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

# **get_mail_notifications_id**
> get_mail_notifications_id(id, location_id=location_id, organization_id=organization_id)

Show an email notification



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.MailNotificationsApi()
id = 'id_example' # str | Numerical ID or email notification name
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show an email notification
    api_instance.get_mail_notifications_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling MailNotificationsApi->get_mail_notifications_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Numerical ID or email notification name |
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

# **get_users_user_id_mail_notifications**
> get_users_user_id_mail_notifications(user_id, location_id=location_id, organization_id=organization_id)

List all email notifications for a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.MailNotificationsApi()
user_id = 'user_id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List all email notifications for a user
    api_instance.get_users_user_id_mail_notifications(user_id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling MailNotificationsApi->get_users_user_id_mail_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
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

# **post_users_user_id_mail_notifications**
> post_users_user_id_mail_notifications(user_id, mail_notification_id, location_id=location_id, organization_id=organization_id, interval=interval, subscription=subscription, mail_query=mail_query)

Add an email notification for a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.MailNotificationsApi()
user_id = 'user_id_example' # str |
mail_notification_id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
interval = 'interval_example' # str | Mail notification interval option, e.g. Daily, Weekly or Monthly. Required for summary notification (optional)
subscription = 'subscription_example' # str | Mail notification subscription option, e.g. Subscribe, Subscribe to my hosts or Subscribe to all hosts. Required for host built and config error state (optional)
mail_query = 'mail_query_example' # str | Relevant only for audit summary notification (optional)

try:
    # Add an email notification for a user
    api_instance.post_users_user_id_mail_notifications(user_id, mail_notification_id, location_id=location_id, organization_id=organization_id, interval=interval, subscription=subscription, mail_query=mail_query)
except ApiException as e:
    print("Exception when calling MailNotificationsApi->post_users_user_id_mail_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **mail_notification_id** | **float**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **interval** | **str**| Mail notification interval option, e.g. Daily, Weekly or Monthly. Required for summary notification | [optional]
 **subscription** | **str**| Mail notification subscription option, e.g. Subscribe, Subscribe to my hosts or Subscribe to all hosts. Required for host built and config error state | [optional]
 **mail_query** | **str**| Relevant only for audit summary notification | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_users_user_id_mail_notifications_mail_notification_id**
> put_users_user_id_mail_notifications_mail_notification_id(user_id, mail_notification_id, location_id=location_id, organization_id=organization_id, interval=interval, subscription=subscription, mail_query=mail_query)

Update an email notification for a user



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.MailNotificationsApi()
user_id = 'user_id_example' # str |
mail_notification_id = 8.14 # float |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
interval = 'interval_example' # str | Mail notification interval option, e.g. Daily, Weekly or Monthly. Required for summary notification (optional)
subscription = 'subscription_example' # str | Mail notification subscription option, e.g. Subscribe, Subscribe to my hosts or Subscribe to all hosts. Required for host built and config error state (optional)
mail_query = 'mail_query_example' # str | Relevant only for audit summary notification (optional)

try:
    # Update an email notification for a user
    api_instance.put_users_user_id_mail_notifications_mail_notification_id(user_id, mail_notification_id, location_id=location_id, organization_id=organization_id, interval=interval, subscription=subscription, mail_query=mail_query)
except ApiException as e:
    print("Exception when calling MailNotificationsApi->put_users_user_id_mail_notifications_mail_notification_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **mail_notification_id** | **float**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **interval** | **str**| Mail notification interval option, e.g. Daily, Weekly or Monthly. Required for summary notification | [optional]
 **subscription** | **str**| Mail notification subscription option, e.g. Subscribe, Subscribe to my hosts or Subscribe to all hosts. Required for host built and config error state | [optional]
 **mail_query** | **str**| Relevant only for audit summary notification | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
