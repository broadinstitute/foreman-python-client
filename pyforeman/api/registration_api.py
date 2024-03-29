# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p>   # noqa: E501

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pyforeman.api_client import ApiClient


class RegistrationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_register(self, **kwargs):  # noqa: E501
        """Render Global registration template  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_register(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float organization_id: ID of the Organization to register the host in
        :param float location_id: ID of the Location to register the host in
        :param float hostgroup_id: ID of the Host group to register the host in
        :param float operatingsystem_id: ID of the Operating System to register the host in
        :param bool setup_insights: Set 'host_registration_insights' parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems
        :param bool setup_remote_execution: Set 'host_registration_remote_execution' parameter for the host. If it is set to true, SSH keys will be installed on the host
        :param str packages: Packages to install on the host when registered. Can be set by `host_packages` parameter, example: `pkg1 pkg2`
        :param bool update_packages: Update all packages on the host
        :param str repo: Repository URL / details, for example for Debian OS family: 'deb http://deb.example.com/ buster 1.0', for Red Hat OS family: 'http://yum.theforeman.org/client/latest/el8/x86_64/'
        :param str repo_gpg_key_url: URL of the GPG key for the repository
        :param str remote_execution_interface: Identifier of the Host interface for Remote execution
        :param bool setup_remote_execution_pull: Set 'host_registration_remote_execution_pull' parameter for the host. If it is set to true, pull provider client will be deployed on the host
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_register_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_register_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_register_with_http_info(self, **kwargs):  # noqa: E501
        """Render Global registration template  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_register_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float organization_id: ID of the Organization to register the host in
        :param float location_id: ID of the Location to register the host in
        :param float hostgroup_id: ID of the Host group to register the host in
        :param float operatingsystem_id: ID of the Operating System to register the host in
        :param bool setup_insights: Set 'host_registration_insights' parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems
        :param bool setup_remote_execution: Set 'host_registration_remote_execution' parameter for the host. If it is set to true, SSH keys will be installed on the host
        :param str packages: Packages to install on the host when registered. Can be set by `host_packages` parameter, example: `pkg1 pkg2`
        :param bool update_packages: Update all packages on the host
        :param str repo: Repository URL / details, for example for Debian OS family: 'deb http://deb.example.com/ buster 1.0', for Red Hat OS family: 'http://yum.theforeman.org/client/latest/el8/x86_64/'
        :param str repo_gpg_key_url: URL of the GPG key for the repository
        :param str remote_execution_interface: Identifier of the Host interface for Remote execution
        :param bool setup_remote_execution_pull: Set 'host_registration_remote_execution_pull' parameter for the host. If it is set to true, pull provider client will be deployed on the host
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "organization_id",
            "location_id",
            "hostgroup_id",
            "operatingsystem_id",
            "setup_insights",
            "setup_remote_execution",
            "packages",
            "update_packages",
            "repo",
            "repo_gpg_key_url",
            "remote_execution_interface",
            "setup_remote_execution_pull",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_register" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "organization_id" in params:
            query_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "location_id" in params:
            query_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "hostgroup_id" in params:
            query_params.append(("hostgroup_id", params["hostgroup_id"]))  # noqa: E501
        if "operatingsystem_id" in params:
            query_params.append(
                ("operatingsystem_id", params["operatingsystem_id"])
            )  # noqa: E501
        if "setup_insights" in params:
            query_params.append(
                ("setup_insights", params["setup_insights"])
            )  # noqa: E501
        if "setup_remote_execution" in params:
            query_params.append(
                ("setup_remote_execution", params["setup_remote_execution"])
            )  # noqa: E501
        if "packages" in params:
            query_params.append(("packages", params["packages"]))  # noqa: E501
        if "update_packages" in params:
            query_params.append(
                ("update_packages", params["update_packages"])
            )  # noqa: E501
        if "repo" in params:
            query_params.append(("repo", params["repo"]))  # noqa: E501
        if "repo_gpg_key_url" in params:
            query_params.append(
                ("repo_gpg_key_url", params["repo_gpg_key_url"])
            )  # noqa: E501
        if "remote_execution_interface" in params:
            query_params.append(
                ("remote_execution_interface", params["remote_execution_interface"])
            )  # noqa: E501
        if "setup_remote_execution_pull" in params:
            query_params.append(
                ("setup_remote_execution_pull", params["setup_remote_execution_pull"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/x-www-form-urlencoded", "multipart/form-data"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/register",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_register(self, **kwargs):  # noqa: E501
        """Find or create a host and render the 'Host initial configuration' template  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_register(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str host_name:
        :param float host_location_id:
        :param float host_organization_id:
        :param str host_ip: IPv4 address, not required if using a subnet with DHCP proxy
        :param str host_ip6: IPv6 address, not required if using a subnet with DHCP proxy
        :param str host_mac: required for managed host that is bare metal, not required if it's a virtual machine
        :param float host_domain_id: required if host is managed and value is not inherited from host group
        :param float host_operatingsystem_id: required if host is managed and value is not inherited from host group
        :param float host_subnet_id: required if host is managed and value is not inherited from host group
        :param float host_model_id:
        :param float host_hostgroup_id:
        :param list[str] host_host_parameters_attributes: Host's parameters (array or indexed hash)
        :param bool host_build:
        :param bool host_enabled: Include this host within Foreman reporting
        :param bool host_managed: True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not
        :param str host_comment: Additional information about this host
        :param list[str] host_interfaces_attributes: Host's network interfaces
        :param float host_content_facet_attributes_content_view_id:
        :param float host_content_facet_attributes_lifecycle_environment_id:
        :param float host_content_facet_attributes_content_source_id:
        :param float host_content_facet_attributes_kickstart_repository_id: Repository Id associated with the kickstart repo used for provisioning
        :param str host_subscription_facet_attributes_release_version: Release version for this Host to use (7Server, 7.1, etc)
        :param bool host_subscription_facet_attributes_autoheal: Sets whether the Host will autoheal subscriptions upon checkin
        :param str host_subscription_facet_attributes_purpose_usage: Sets the system purpose usage
        :param str host_subscription_facet_attributes_purpose_role: Sets the system purpose usage
        :param list[str] host_subscription_facet_attributes_purpose_addons: Sets the system add-ons
        :param str host_subscription_facet_attributes_service_level: Service level to be used for autoheal
        :param list[str] host_subscription_facet_attributes_hypervisor_guest_uuids: List of hypervisor guest uuids
        :param list[str] host_subscription_facet_attributes_installed_products_attributes: List of products installed on the host
        :param bool setup_insights: Set 'host_registration_insights' parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems
        :param bool setup_remote_execution: Set 'host_registration_remote_execution' parameter for the host. If it is set to true, SSH keys will be installed on the host
        :param str remote_execution_interface: Identifier of the Host interface for Remote execution
        :param bool setup_remote_execution_pull: Set 'host_registration_remote_execution_pull' parameter for the host. If it is set to true, pull provider client will be deployed on the host
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_register_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.post_register_with_http_info(**kwargs)  # noqa: E501
            return data

    def post_register_with_http_info(self, **kwargs):  # noqa: E501
        """Find or create a host and render the 'Host initial configuration' template  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_register_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str host_name:
        :param float host_location_id:
        :param float host_organization_id:
        :param str host_ip: IPv4 address, not required if using a subnet with DHCP proxy
        :param str host_ip6: IPv6 address, not required if using a subnet with DHCP proxy
        :param str host_mac: required for managed host that is bare metal, not required if it's a virtual machine
        :param float host_domain_id: required if host is managed and value is not inherited from host group
        :param float host_operatingsystem_id: required if host is managed and value is not inherited from host group
        :param float host_subnet_id: required if host is managed and value is not inherited from host group
        :param float host_model_id:
        :param float host_hostgroup_id:
        :param list[str] host_host_parameters_attributes: Host's parameters (array or indexed hash)
        :param bool host_build:
        :param bool host_enabled: Include this host within Foreman reporting
        :param bool host_managed: True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not
        :param str host_comment: Additional information about this host
        :param list[str] host_interfaces_attributes: Host's network interfaces
        :param float host_content_facet_attributes_content_view_id:
        :param float host_content_facet_attributes_lifecycle_environment_id:
        :param float host_content_facet_attributes_content_source_id:
        :param float host_content_facet_attributes_kickstart_repository_id: Repository Id associated with the kickstart repo used for provisioning
        :param str host_subscription_facet_attributes_release_version: Release version for this Host to use (7Server, 7.1, etc)
        :param bool host_subscription_facet_attributes_autoheal: Sets whether the Host will autoheal subscriptions upon checkin
        :param str host_subscription_facet_attributes_purpose_usage: Sets the system purpose usage
        :param str host_subscription_facet_attributes_purpose_role: Sets the system purpose usage
        :param list[str] host_subscription_facet_attributes_purpose_addons: Sets the system add-ons
        :param str host_subscription_facet_attributes_service_level: Service level to be used for autoheal
        :param list[str] host_subscription_facet_attributes_hypervisor_guest_uuids: List of hypervisor guest uuids
        :param list[str] host_subscription_facet_attributes_installed_products_attributes: List of products installed on the host
        :param bool setup_insights: Set 'host_registration_insights' parameter for the host. If it is set to true, insights client will be installed and registered on Red Hat family operating systems
        :param bool setup_remote_execution: Set 'host_registration_remote_execution' parameter for the host. If it is set to true, SSH keys will be installed on the host
        :param str remote_execution_interface: Identifier of the Host interface for Remote execution
        :param bool setup_remote_execution_pull: Set 'host_registration_remote_execution_pull' parameter for the host. If it is set to true, pull provider client will be deployed on the host
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "location_id",
            "organization_id",
            "host_name",
            "host_location_id",
            "host_organization_id",
            "host_ip",
            "host_ip6",
            "host_mac",
            "host_domain_id",
            "host_operatingsystem_id",
            "host_subnet_id",
            "host_model_id",
            "host_hostgroup_id",
            "host_host_parameters_attributes",
            "host_build",
            "host_enabled",
            "host_managed",
            "host_comment",
            "host_interfaces_attributes",
            "host_content_facet_attributes_content_view_id",
            "host_content_facet_attributes_lifecycle_environment_id",
            "host_content_facet_attributes_content_source_id",
            "host_content_facet_attributes_kickstart_repository_id",
            "host_subscription_facet_attributes_release_version",
            "host_subscription_facet_attributes_autoheal",
            "host_subscription_facet_attributes_purpose_usage",
            "host_subscription_facet_attributes_purpose_role",
            "host_subscription_facet_attributes_purpose_addons",
            "host_subscription_facet_attributes_service_level",
            "host_subscription_facet_attributes_hypervisor_guest_uuids",
            "host_subscription_facet_attributes_installed_products_attributes",
            "setup_insights",
            "setup_remote_execution",
            "remote_execution_interface",
            "setup_remote_execution_pull",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_register" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "location_id" in params:
            form_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            form_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "host_name" in params:
            form_params.append(("host[name]", params["host_name"]))  # noqa: E501
        if "host_location_id" in params:
            form_params.append(
                ("host[location_id]", params["host_location_id"])
            )  # noqa: E501
        if "host_organization_id" in params:
            form_params.append(
                ("host[organization_id]", params["host_organization_id"])
            )  # noqa: E501
        if "host_ip" in params:
            form_params.append(("host[ip]", params["host_ip"]))  # noqa: E501
        if "host_ip6" in params:
            form_params.append(("host[ip6]", params["host_ip6"]))  # noqa: E501
        if "host_mac" in params:
            form_params.append(("host[mac]", params["host_mac"]))  # noqa: E501
        if "host_domain_id" in params:
            form_params.append(
                ("host[domain_id]", params["host_domain_id"])
            )  # noqa: E501
        if "host_operatingsystem_id" in params:
            form_params.append(
                ("host[operatingsystem_id]", params["host_operatingsystem_id"])
            )  # noqa: E501
        if "host_subnet_id" in params:
            form_params.append(
                ("host[subnet_id]", params["host_subnet_id"])
            )  # noqa: E501
        if "host_model_id" in params:
            form_params.append(
                ("host[model_id]", params["host_model_id"])
            )  # noqa: E501
        if "host_hostgroup_id" in params:
            form_params.append(
                ("host[hostgroup_id]", params["host_hostgroup_id"])
            )  # noqa: E501
        if "host_host_parameters_attributes" in params:
            form_params.append(
                (
                    "host[host_parameters_attributes]",
                    params["host_host_parameters_attributes"],
                )
            )  # noqa: E501
            collection_formats["host[host_parameters_attributes]"] = "csv"  # noqa: E501
        if "host_build" in params:
            form_params.append(("host[build]", params["host_build"]))  # noqa: E501
        if "host_enabled" in params:
            form_params.append(("host[enabled]", params["host_enabled"]))  # noqa: E501
        if "host_managed" in params:
            form_params.append(("host[managed]", params["host_managed"]))  # noqa: E501
        if "host_comment" in params:
            form_params.append(("host[comment]", params["host_comment"]))  # noqa: E501
        if "host_interfaces_attributes" in params:
            form_params.append(
                ("host[interfaces_attributes]", params["host_interfaces_attributes"])
            )  # noqa: E501
            collection_formats["host[interfaces_attributes]"] = "csv"  # noqa: E501
        if "host_content_facet_attributes_content_view_id" in params:
            form_params.append(
                (
                    "host[content_facet_attributes][content_view_id]",
                    params["host_content_facet_attributes_content_view_id"],
                )
            )  # noqa: E501
        if "host_content_facet_attributes_lifecycle_environment_id" in params:
            form_params.append(
                (
                    "host[content_facet_attributes][lifecycle_environment_id]",
                    params["host_content_facet_attributes_lifecycle_environment_id"],
                )
            )  # noqa: E501
        if "host_content_facet_attributes_content_source_id" in params:
            form_params.append(
                (
                    "host[content_facet_attributes][content_source_id]",
                    params["host_content_facet_attributes_content_source_id"],
                )
            )  # noqa: E501
        if "host_content_facet_attributes_kickstart_repository_id" in params:
            form_params.append(
                (
                    "host[content_facet_attributes][kickstart_repository_id]",
                    params["host_content_facet_attributes_kickstart_repository_id"],
                )
            )  # noqa: E501
        if "host_subscription_facet_attributes_release_version" in params:
            form_params.append(
                (
                    "host[subscription_facet_attributes][release_version]",
                    params["host_subscription_facet_attributes_release_version"],
                )
            )  # noqa: E501
        if "host_subscription_facet_attributes_autoheal" in params:
            form_params.append(
                (
                    "host[subscription_facet_attributes][autoheal]",
                    params["host_subscription_facet_attributes_autoheal"],
                )
            )  # noqa: E501
        if "host_subscription_facet_attributes_purpose_usage" in params:
            form_params.append(
                (
                    "host[subscription_facet_attributes][purpose_usage]",
                    params["host_subscription_facet_attributes_purpose_usage"],
                )
            )  # noqa: E501
        if "host_subscription_facet_attributes_purpose_role" in params:
            form_params.append(
                (
                    "host[subscription_facet_attributes][purpose_role]",
                    params["host_subscription_facet_attributes_purpose_role"],
                )
            )  # noqa: E501
        if "host_subscription_facet_attributes_purpose_addons" in params:
            form_params.append(
                (
                    "host[subscription_facet_attributes][purpose_addons]",
                    params["host_subscription_facet_attributes_purpose_addons"],
                )
            )  # noqa: E501
            collection_formats[
                "host[subscription_facet_attributes][purpose_addons]"
            ] = "csv"  # noqa: E501
        if "host_subscription_facet_attributes_service_level" in params:
            form_params.append(
                (
                    "host[subscription_facet_attributes][service_level]",
                    params["host_subscription_facet_attributes_service_level"],
                )
            )  # noqa: E501
        if "host_subscription_facet_attributes_hypervisor_guest_uuids" in params:
            form_params.append(
                (
                    "host[subscription_facet_attributes][hypervisor_guest_uuids]",
                    params["host_subscription_facet_attributes_hypervisor_guest_uuids"],
                )
            )  # noqa: E501
            collection_formats[
                "host[subscription_facet_attributes][hypervisor_guest_uuids]"
            ] = "csv"  # noqa: E501
        if "host_subscription_facet_attributes_installed_products_attributes" in params:
            form_params.append(
                (
                    "host[subscription_facet_attributes][installed_products_attributes]",
                    params[
                        "host_subscription_facet_attributes_installed_products_attributes"
                    ],
                )
            )  # noqa: E501
            collection_formats[
                "host[subscription_facet_attributes][installed_products_attributes]"
            ] = "csv"  # noqa: E501
        if "setup_insights" in params:
            form_params.append(
                ("setup_insights", params["setup_insights"])
            )  # noqa: E501
        if "setup_remote_execution" in params:
            form_params.append(
                ("setup_remote_execution", params["setup_remote_execution"])
            )  # noqa: E501
        if "remote_execution_interface" in params:
            form_params.append(
                ("remote_execution_interface", params["remote_execution_interface"])
            )  # noqa: E501
        if "setup_remote_execution_pull" in params:
            form_params.append(
                ("setup_remote_execution_pull", params["setup_remote_execution_pull"])
            )  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/x-www-form-urlencoded", "multipart/form-data"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/register",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
