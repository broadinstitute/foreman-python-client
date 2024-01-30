# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p>   # noqa: E501

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pyforeman
from pyforeman.api.compute_resources_api import ComputeResourcesApi  # noqa: E501
from pyforeman.rest import ApiException


class TestComputeResourcesApi(unittest.TestCase):
    """ComputeResourcesApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.compute_resources_api.ComputeResourcesApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_compute_resources_id(self):
        """Test case for delete_compute_resources_id

        Delete a compute resource  # noqa: E501
        """
        pass

    def test_delete_compute_resources_id_available_virtual_machines_vm_id(self):
        """Test case for delete_compute_resources_id_available_virtual_machines_vm_id

        Delete a Virtual Machine  # noqa: E501
        """
        pass

    def test_get_compute_resources(self):
        """Test case for get_compute_resources

        List all compute resources  # noqa: E501
        """
        pass

    def test_get_compute_resources_id(self):
        """Test case for get_compute_resources_id

        Show a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_clusters(self):
        """Test case for get_compute_resources_id_available_clusters

        List available clusters for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_clusters_cluster_id_available_networks(
        self,
    ):
        """Test case for get_compute_resources_id_available_clusters_cluster_id_available_networks

        List available networks for a compute resource cluster  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_clusters_cluster_id_available_resource_pools(
        self,
    ):
        """Test case for get_compute_resources_id_available_clusters_cluster_id_available_resource_pools

        List resource pools for a compute resource cluster  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_clusters_cluster_id_available_storage_domains(
        self,
    ):
        """Test case for get_compute_resources_id_available_clusters_cluster_id_available_storage_domains

        List storage domains for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_clusters_cluster_id_available_storage_pods(
        self,
    ):
        """Test case for get_compute_resources_id_available_clusters_cluster_id_available_storage_pods

        List storage pods for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_flavors(self):
        """Test case for get_compute_resources_id_available_flavors

        List available flavors for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_folders(self):
        """Test case for get_compute_resources_id_available_folders

        List available folders for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_images(self):
        """Test case for get_compute_resources_id_available_images

        List available images for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_networks(self):
        """Test case for get_compute_resources_id_available_networks

        List available networks for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_security_groups(self):
        """Test case for get_compute_resources_id_available_security_groups

        List available security groups for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_storage_domains(self):
        """Test case for get_compute_resources_id_available_storage_domains

        List storage domains for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_storage_domains_storage_domain(self):
        """Test case for get_compute_resources_id_available_storage_domains_storage_domain

        List attributes for a given storage domain  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_storage_pods(self):
        """Test case for get_compute_resources_id_available_storage_pods

        List storage pods for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_storage_pods_storage_pod(self):
        """Test case for get_compute_resources_id_available_storage_pods_storage_pod

        List attributes for a given storage pod  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_virtual_machines(self):
        """Test case for get_compute_resources_id_available_virtual_machines

        List available virtual machines for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_virtual_machines_vm_id(self):
        """Test case for get_compute_resources_id_available_virtual_machines_vm_id

        Show a virtual machine  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_vnic_profiles(self):
        """Test case for get_compute_resources_id_available_vnic_profiles

        List available vnic profiles for a compute resource, for oVirt only  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_available_zones(self):
        """Test case for get_compute_resources_id_available_zones

        List available zone for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_storage_domains_storage_domain_id(self):
        """Test case for get_compute_resources_id_storage_domains_storage_domain_id

        List attributes for a given storage domain  # noqa: E501
        """
        pass

    def test_get_compute_resources_id_storage_pods_storage_pod_id(self):
        """Test case for get_compute_resources_id_storage_pods_storage_pod_id

        List attributes for a given storage pod  # noqa: E501
        """
        pass

    def test_post_compute_resources(self):
        """Test case for post_compute_resources

        Create a compute resource  # noqa: E501
        """
        pass

    def test_put_compute_resources_id(self):
        """Test case for put_compute_resources_id

        Update a compute resource  # noqa: E501
        """
        pass

    def test_put_compute_resources_id_associate_vm_id(self):
        """Test case for put_compute_resources_id_associate_vm_id

        Associate VMs to Hosts  # noqa: E501
        """
        pass

    def test_put_compute_resources_id_available_virtual_machines_vm_id_power(self):
        """Test case for put_compute_resources_id_available_virtual_machines_vm_id_power

        Power a Virtual Machine  # noqa: E501
        """
        pass

    def test_put_compute_resources_id_refresh_cache(self):
        """Test case for put_compute_resources_id_refresh_cache

        Refresh Compute Resource Cache  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
