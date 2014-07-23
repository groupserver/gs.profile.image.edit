# -*- coding=utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(
    name='gs.profile.image.edit',
    version=version,
    description="Provides a page for a user to set/edit her profile image",
    long_description=open("README.txt").read() + "\n" +
    open(os.path.join("docs", "HISTORY.txt")).read(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers for values
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='Bill Bushey',
    author_email='bill.bushey@e-democracy.org',
    url='http://groupserver.org/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.profile', 'gs.profile.image'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CustomUserFolder',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
