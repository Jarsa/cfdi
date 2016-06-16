# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cfdi',
    version='1.0.0.dev1',
    description='A Python library to generate CFDI for Mexico',
    long_description=long_description,
    url='https://github.com/jarsa/cfdi',
    author='Jarsa Sistemas, S.A. de C.V.',
    author_email='info@jarsa.com.mx',
    license='APGLv3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Affero General Public License v3 or '
        'later (AGPLv3+)',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='cfdi mexico invoice einvoice',
    packages=find_packages(),
    install_requires=[
        'lxml',
        'Jinja2',
        'M2Crypto',
        ],
    test_suite="cfdi.test",
    package_data={
        'cfdi': [
            'data/*.jinja',
            'data/*.xslt',
            'test/*cer',
            'test/*.key',
            ],
    },
)
