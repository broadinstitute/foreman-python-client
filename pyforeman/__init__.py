# coding: utf-8

# flake8: noqa

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p>   # noqa: E501

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from pyforeman.api.activation_keys_api import ActivationKeysApi
from pyforeman.api.alternate_content_sources_api import AlternateContentSourcesApi
from pyforeman.api.alternate_content_sources_bulk_actions_api import (
    AlternateContentSourcesBulkActionsApi,
)
from pyforeman.api.ansible_collections_api import AnsibleCollectionsApi
from pyforeman.api.architectures_api import ArchitecturesApi
from pyforeman.api.audits_api import AuditsApi
from pyforeman.api.auth_source_externals_api import AuthSourceExternalsApi
from pyforeman.api.auth_source_internals_api import AuthSourceInternalsApi
from pyforeman.api.auth_source_ldaps_api import AuthSourceLdapsApi
from pyforeman.api.auth_sources_api import AuthSourcesApi
from pyforeman.api.autosign_api import AutosignApi
from pyforeman.api.bookmarks_api import BookmarksApi
from pyforeman.api.capsule_content_api import CapsuleContentApi
from pyforeman.api.capsules_api import CapsulesApi
from pyforeman.api.common_parameters_api import CommonParametersApi
from pyforeman.api.compute_attributes_api import ComputeAttributesApi
from pyforeman.api.compute_profiles_api import ComputeProfilesApi
from pyforeman.api.compute_resources_api import ComputeResourcesApi
from pyforeman.api.config_reports_api import ConfigReportsApi
from pyforeman.api.content_credentials_api import ContentCredentialsApi
from pyforeman.api.content_export_incrementals_api import ContentExportIncrementalsApi
from pyforeman.api.content_exports_api import ContentExportsApi
from pyforeman.api.content_imports_api import ContentImportsApi
from pyforeman.api.content_uploads_api import ContentUploadsApi
from pyforeman.api.content_view_components_api import ContentViewComponentsApi
from pyforeman.api.content_view_filter_rules_api import ContentViewFilterRulesApi
from pyforeman.api.content_view_filters_api import ContentViewFiltersApi
from pyforeman.api.content_view_histories_api import ContentViewHistoriesApi
from pyforeman.api.content_view_versions_api import ContentViewVersionsApi
from pyforeman.api.content_views_api import ContentViewsApi
from pyforeman.api.dashboard_api import DashboardApi
from pyforeman.api.debs_api import DebsApi
from pyforeman.api.disks_api import DisksApi
from pyforeman.api.docker_manifest_lists_api import DockerManifestListsApi
from pyforeman.api.docker_manifests_api import DockerManifestsApi
from pyforeman.api.docker_tags_api import DockerTagsApi
from pyforeman.api.domains_api import DomainsApi
from pyforeman.api.errata_api import ErrataApi
from pyforeman.api.external_usergroups_api import ExternalUsergroupsApi
from pyforeman.api.fact_values_api import FactValuesApi
from pyforeman.api.file_units_api import FileUnitsApi
from pyforeman.api.filters_api import FiltersApi
from pyforeman.api.foreign_input_sets_api import ForeignInputSetsApi
from pyforeman.api.foreman_tasks_api import ForemanTasksApi
from pyforeman.api.generic_content_units_api import GenericContentUnitsApi
from pyforeman.api.home_api import HomeApi
from pyforeman.api.host_collections_api import HostCollectionsApi
from pyforeman.api.host_debs_api import HostDebsApi
from pyforeman.api.host_errata_api import HostErrataApi
from pyforeman.api.host_module_streams_api import HostModuleStreamsApi
from pyforeman.api.host_packages_api import HostPackagesApi
from pyforeman.api.host_statuses_api import HostStatusesApi
from pyforeman.api.host_subscriptions_api import HostSubscriptionsApi
from pyforeman.api.host_tracer_api import HostTracerApi
from pyforeman.api.hostgroups_api import HostgroupsApi
from pyforeman.api.hosts_api import HostsApi
from pyforeman.api.hosts_bulk_actions_api import HostsBulkActionsApi
from pyforeman.api.http_proxies_api import HttpProxiesApi
from pyforeman.api.images_api import ImagesApi
from pyforeman.api.instance_hosts_api import InstanceHostsApi
from pyforeman.api.interfaces_api import InterfacesApi
from pyforeman.api.job_invocations_api import JobInvocationsApi
from pyforeman.api.job_templates_api import JobTemplatesApi
from pyforeman.api.lifecycle_environments_api import LifecycleEnvironmentsApi
from pyforeman.api.locations_api import LocationsApi
from pyforeman.api.mail_notifications_api import MailNotificationsApi
from pyforeman.api.media_api import MediaApi
from pyforeman.api.models_api import ModelsApi
from pyforeman.api.module_streams_api import ModuleStreamsApi
from pyforeman.api.operatingsystems_api import OperatingsystemsApi
from pyforeman.api.organizations_api import OrganizationsApi
from pyforeman.api.os_default_templates_api import OsDefaultTemplatesApi
from pyforeman.api.package_groups_api import PackageGroupsApi
from pyforeman.api.packages_api import PackagesApi
from pyforeman.api.parameters_api import ParametersApi
from pyforeman.api.permissions_api import PermissionsApi
from pyforeman.api.personal_access_tokens_api import PersonalAccessTokensApi
from pyforeman.api.ping_api import PingApi
from pyforeman.api.plugins_api import PluginsApi
from pyforeman.api.products_api import ProductsApi
from pyforeman.api.products_bulk_actions_api import ProductsBulkActionsApi
from pyforeman.api.provisioning_templates_api import ProvisioningTemplatesApi
from pyforeman.api.ptables_api import PtablesApi
from pyforeman.api.realms_api import RealmsApi
from pyforeman.api.recurring_logics_api import RecurringLogicsApi
from pyforeman.api.registration_api import RegistrationApi
from pyforeman.api.registration_commands_api import RegistrationCommandsApi
from pyforeman.api.remote_execution_features_api import RemoteExecutionFeaturesApi
from pyforeman.api.report_templates_api import ReportTemplatesApi
from pyforeman.api.repositories_api import RepositoriesApi
from pyforeman.api.repositories_bulk_actions_api import RepositoriesBulkActionsApi
from pyforeman.api.repository_sets_api import RepositorySetsApi
from pyforeman.api.roles_api import RolesApi
from pyforeman.api.settings_api import SettingsApi
from pyforeman.api.simple_content_access_api import SimpleContentAccessApi
from pyforeman.api.smart_proxies_api import SmartProxiesApi
from pyforeman.api.smart_proxy_hosts_api import SmartProxyHostsApi
from pyforeman.api.srpms_api import SrpmsApi
from pyforeman.api.ssh_keys_api import SshKeysApi
from pyforeman.api.subnet_disks_api import SubnetDisksApi
from pyforeman.api.subnets_api import SubnetsApi
from pyforeman.api.subscriptions_api import SubscriptionsApi
from pyforeman.api.sync_api import SyncApi
from pyforeman.api.sync_plans_api import SyncPlansApi
from pyforeman.api.table_preferences_api import TablePreferencesApi
from pyforeman.api.tasks_api import TasksApi
from pyforeman.api.template_combinations_api import TemplateCombinationsApi
from pyforeman.api.template_inputs_api import TemplateInputsApi
from pyforeman.api.template_invocations_api import TemplateInvocationsApi
from pyforeman.api.template_kinds_api import TemplateKindsApi
from pyforeman.api.upstream_subscriptions_api import UpstreamSubscriptionsApi
from pyforeman.api.usergroups_api import UsergroupsApi
from pyforeman.api.users_api import UsersApi

# import ApiClient
from pyforeman.api_client import ApiClient
from pyforeman.configuration import Configuration

# import models into sdk package
from pyforeman.models.setting_params import SettingParams
