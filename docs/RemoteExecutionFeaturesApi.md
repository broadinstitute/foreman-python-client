# pyforeman.RemoteExecutionFeaturesApi

All URIs are relative to *https://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_hosts_id_available_remote_execution_features**](RemoteExecutionFeaturesApi.md#get_api_hosts_id_available_remote_execution_features) | **GET** /api/hosts/{id}/available_remote_execution_features | List available remote execution features for a host
[**get_remote_execution_features**](RemoteExecutionFeaturesApi.md#get_remote_execution_features) | **GET** /remote_execution_features | List remote execution features
[**get_remote_execution_features_id**](RemoteExecutionFeaturesApi.md#get_remote_execution_features_id) | **GET** /remote_execution_features/{id} | Show remote execution feature
[**put_remote_execution_features_id**](RemoteExecutionFeaturesApi.md#put_remote_execution_features_id) | **PUT** /remote_execution_features/{id} | Update a job template


# **get_api_hosts_id_available_remote_execution_features**
> get_api_hosts_id_available_remote_execution_features(id, location_id=location_id, organization_id=organization_id)

List available remote execution features for a host



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RemoteExecutionFeaturesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List available remote execution features for a host
    api_instance.get_api_hosts_id_available_remote_execution_features(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RemoteExecutionFeaturesApi->get_api_hosts_id_available_remote_execution_features: %s\n" % e)
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

# **get_remote_execution_features**
> get_remote_execution_features(location_id=location_id, organization_id=organization_id)

List remote execution features



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RemoteExecutionFeaturesApi()
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # List remote execution features
    api_instance.get_remote_execution_features(location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RemoteExecutionFeaturesApi->get_remote_execution_features: %s\n" % e)
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

# **get_remote_execution_features_id**
> get_remote_execution_features_id(id, location_id=location_id, organization_id=organization_id)

Show remote execution feature



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RemoteExecutionFeaturesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)

try:
    # Show remote execution feature
    api_instance.get_remote_execution_features_id(id, location_id=location_id, organization_id=organization_id)
except ApiException as e:
    print("Exception when calling RemoteExecutionFeaturesApi->get_remote_execution_features_id: %s\n" % e)
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

# **put_remote_execution_features_id**
> put_remote_execution_features_id(id, location_id=location_id, organization_id=organization_id, remote_execution_feature_job_template_id=remote_execution_feature_job_template_id)

Update a job template



### Example
```python
from __future__ import print_function
import time
import pyforeman
from pyforeman.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyforeman.RemoteExecutionFeaturesApi()
id = 'id_example' # str |
location_id = 8.14 # float | Set the current location context for the request (optional)
organization_id = 8.14 # float | Set the current organization context for the request (optional)
remote_execution_feature_job_template_id = 'remote_execution_feature_job_template_id_example' # str | Job template ID to be used for the feature (optional)

try:
    # Update a job template
    api_instance.put_remote_execution_features_id(id, location_id=location_id, organization_id=organization_id, remote_execution_feature_job_template_id=remote_execution_feature_job_template_id)
except ApiException as e:
    print("Exception when calling RemoteExecutionFeaturesApi->put_remote_execution_features_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **location_id** | **float**| Set the current location context for the request | [optional]
 **organization_id** | **float**| Set the current organization context for the request | [optional]
 **remote_execution_feature_job_template_id** | **str**| Job template ID to be used for the feature | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
