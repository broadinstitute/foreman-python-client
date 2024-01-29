# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "foreman-python-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Foreman (params in:formData)",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Foreman (params in:formData)"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description="""\
     &lt;p&gt;Foreman API v2 is currently the default API version.&lt;/p&gt; 
    """,  # noqa: E501
    package_data={"foreman": ["py.typed"]},
)