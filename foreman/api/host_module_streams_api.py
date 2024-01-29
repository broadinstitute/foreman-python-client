# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBool, StrictFloat, StrictInt, StrictStr, field_validator

from typing import Optional, Union


from foreman.api_client import ApiClient
from foreman.api_response import ApiResponse
from foreman.rest import RESTResponseType


class HostModuleStreamsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_hosts_host_id_module_streams(
        self,
        host_id: Annotated[
            Union[StrictFloat, StrictInt], Field(description="ID of the host")
        ],
        status: Annotated[
            Optional[StrictStr],
            Field(description="Streams based on the host based on their status"),
        ] = None,
        install_status: Annotated[
            Optional[StrictStr],
            Field(
                description="Streams based on the host based on the installation status"
            ),
        ] = None,
        search: Annotated[
            Optional[StrictStr], Field(description="Search string")
        ] = None,
        page: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(description="Page number, starting at 1"),
        ] = None,
        per_page: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(description="Number of results per page to return"),
        ] = None,
        order: Annotated[
            Optional[StrictStr],
            Field(description="Sort field and order, eg. 'id DESC'"),
        ] = None,
        full_result: Annotated[
            Optional[StrictBool],
            Field(description="Whether or not to show all results"),
        ] = None,
        sort_by: Annotated[
            Optional[StrictStr], Field(description="Field to sort the results on")
        ] = None,
        sort_order: Annotated[
            Optional[StrictStr],
            Field(
                description="How to order the sorted results (e.g. ASC for ascending)"
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """List module streams available to the host


        :param host_id: ID of the host (required)
        :type host_id: float
        :param status: Streams based on the host based on their status
        :type status: str
        :param install_status: Streams based on the host based on the installation status
        :type install_status: str
        :param search: Search string
        :type search: str
        :param page: Page number, starting at 1
        :type page: float
        :param per_page: Number of results per page to return
        :type per_page: float
        :param order: Sort field and order, eg. 'id DESC'
        :type order: str
        :param full_result: Whether or not to show all results
        :type full_result: bool
        :param sort_by: Field to sort the results on
        :type sort_by: str
        :param sort_order: How to order the sorted results (e.g. ASC for ascending)
        :type sort_order: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_hosts_host_id_module_streams_serialize(
            host_id=host_id,
            status=status,
            install_status=install_status,
            search=search,
            page=page,
            per_page=per_page,
            order=order,
            full_result=full_result,
            sort_by=sort_by,
            sort_order=sort_order,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": None,
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_hosts_host_id_module_streams_with_http_info(
        self,
        host_id: Annotated[
            Union[StrictFloat, StrictInt], Field(description="ID of the host")
        ],
        status: Annotated[
            Optional[StrictStr],
            Field(description="Streams based on the host based on their status"),
        ] = None,
        install_status: Annotated[
            Optional[StrictStr],
            Field(
                description="Streams based on the host based on the installation status"
            ),
        ] = None,
        search: Annotated[
            Optional[StrictStr], Field(description="Search string")
        ] = None,
        page: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(description="Page number, starting at 1"),
        ] = None,
        per_page: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(description="Number of results per page to return"),
        ] = None,
        order: Annotated[
            Optional[StrictStr],
            Field(description="Sort field and order, eg. 'id DESC'"),
        ] = None,
        full_result: Annotated[
            Optional[StrictBool],
            Field(description="Whether or not to show all results"),
        ] = None,
        sort_by: Annotated[
            Optional[StrictStr], Field(description="Field to sort the results on")
        ] = None,
        sort_order: Annotated[
            Optional[StrictStr],
            Field(
                description="How to order the sorted results (e.g. ASC for ascending)"
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """List module streams available to the host


        :param host_id: ID of the host (required)
        :type host_id: float
        :param status: Streams based on the host based on their status
        :type status: str
        :param install_status: Streams based on the host based on the installation status
        :type install_status: str
        :param search: Search string
        :type search: str
        :param page: Page number, starting at 1
        :type page: float
        :param per_page: Number of results per page to return
        :type per_page: float
        :param order: Sort field and order, eg. 'id DESC'
        :type order: str
        :param full_result: Whether or not to show all results
        :type full_result: bool
        :param sort_by: Field to sort the results on
        :type sort_by: str
        :param sort_order: How to order the sorted results (e.g. ASC for ascending)
        :type sort_order: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_hosts_host_id_module_streams_serialize(
            host_id=host_id,
            status=status,
            install_status=install_status,
            search=search,
            page=page,
            per_page=per_page,
            order=order,
            full_result=full_result,
            sort_by=sort_by,
            sort_order=sort_order,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": None,
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_hosts_host_id_module_streams_without_preload_content(
        self,
        host_id: Annotated[
            Union[StrictFloat, StrictInt], Field(description="ID of the host")
        ],
        status: Annotated[
            Optional[StrictStr],
            Field(description="Streams based on the host based on their status"),
        ] = None,
        install_status: Annotated[
            Optional[StrictStr],
            Field(
                description="Streams based on the host based on the installation status"
            ),
        ] = None,
        search: Annotated[
            Optional[StrictStr], Field(description="Search string")
        ] = None,
        page: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(description="Page number, starting at 1"),
        ] = None,
        per_page: Annotated[
            Optional[Union[StrictFloat, StrictInt]],
            Field(description="Number of results per page to return"),
        ] = None,
        order: Annotated[
            Optional[StrictStr],
            Field(description="Sort field and order, eg. 'id DESC'"),
        ] = None,
        full_result: Annotated[
            Optional[StrictBool],
            Field(description="Whether or not to show all results"),
        ] = None,
        sort_by: Annotated[
            Optional[StrictStr], Field(description="Field to sort the results on")
        ] = None,
        sort_order: Annotated[
            Optional[StrictStr],
            Field(
                description="How to order the sorted results (e.g. ASC for ascending)"
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List module streams available to the host


        :param host_id: ID of the host (required)
        :type host_id: float
        :param status: Streams based on the host based on their status
        :type status: str
        :param install_status: Streams based on the host based on the installation status
        :type install_status: str
        :param search: Search string
        :type search: str
        :param page: Page number, starting at 1
        :type page: float
        :param per_page: Number of results per page to return
        :type per_page: float
        :param order: Sort field and order, eg. 'id DESC'
        :type order: str
        :param full_result: Whether or not to show all results
        :type full_result: bool
        :param sort_by: Field to sort the results on
        :type sort_by: str
        :param sort_order: How to order the sorted results (e.g. ASC for ascending)
        :type sort_order: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_hosts_host_id_module_streams_serialize(
            host_id=host_id,
            status=status,
            install_status=install_status,
            search=search,
            page=page,
            per_page=per_page,
            order=order,
            full_result=full_result,
            sort_by=sort_by,
            sort_order=sort_order,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": None,
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        return response_data.response

    def _get_hosts_host_id_module_streams_serialize(
        self,
        host_id,
        status,
        install_status,
        search,
        page,
        per_page,
        order,
        full_result,
        sort_by,
        sort_order,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if host_id is not None:
            _path_params["host_id"] = host_id
        # process the query parameters
        if status is not None:
            _query_params.append(("status", status))

        if install_status is not None:
            _query_params.append(("install_status", install_status))

        if search is not None:
            _query_params.append(("search", search))

        if page is not None:
            _query_params.append(("page", page))

        if per_page is not None:
            _query_params.append(("per_page", per_page))

        if order is not None:
            _query_params.append(("order", order))

        if full_result is not None:
            _query_params.append(("full_result", full_result))

        if sort_by is not None:
            _query_params.append(("sort_by", sort_by))

        if sort_order is not None:
            _query_params.append(("sort_order", sort_order))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/hosts/{host_id}/module_streams",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
