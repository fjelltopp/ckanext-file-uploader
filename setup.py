# -*- coding: utf-8 -*-
from codecs import open  # To use a consistent encoding
from os import path

from setuptools import find_packages, setup  # Always prefer setuptools over distutils

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

install_requires =
include_package_data = True

setup(
    name="""ckanext-file-uploader""",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version="1.0.0",
    description="""CKAN Extension providing a javascript enhanced file upload widget for creating and editing resources.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fjelltopp/ckanext-file-uploader",
    author="""Chas Nelson""",
    author_email="""info@fjelltopp.org""",
    license="AGPL",
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="""CKAN resource file upload javascript widget""",
        packages=find_packages(exclude=["contrib", "docs", "tests*", "react"]),
    namespace_packages=["ckanext"],
    install_requires=[],
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    include_package_data=True,
    package_data={},
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html
    # installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points="""
        [ckan.plugins]
        file_uploader = ckanext.file_uploader.plugin:FileUploaderPlugin

        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    """,
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    message_extractors={
        "ckanext": [
            ("**/node_modules/**", "ignore", None),
            ("**.py", "python", None),
            ("**.js", "javascript", None),
            ("**.html", "ckan", None),
        ]
    },
)
