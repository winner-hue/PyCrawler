#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

'''
打包pycrawler
'''

setup(
    name="pycrawler",
    version="1.0",
    author="winner-hub",
    author_email="1344246287@qq.com",
    description=("A distributed crawler framework based on Python"),
    license="Apache 2.0",
    keywords="pycrawler crawler spider pyspider",
    url="https://github.com/winner-hue/pycrawler",
    packages=['dispatch', 'download', 'extractor', 'storage_dup', 'util', ''],
    package_dir={'': 'lib'},
    # 需要安装的依赖
    install_requires=[
        'beautifulsoup4>=4.9.1',
        'bs4>=0.0.1',
        'certifi>=2020.6.20',
        'chardet>=3.0.4',
        'DBUtils>=1.3',
        'Faker>=4.1.1',
        'gne>=0.2.1',
        'idna>=2.10',
        'lxml>=4.5.2',
        'numpy>=1.19.0',
        'pika>=1.1.0',
        'psutil>=5.7.0',
        'pymongo>=3.10.1',
        'PyMySQL>=0.9.3',
        'python-dateutil>=2.8.1',
        'PyYAML>=5.3.1',
        'redis>=3.5.3',
        'requests>=2.24.0',
        'requests-file>=1.5.1',
        'six>=1.15.0',
        'soupsieve>=2.0.1',
        'text-unidecode>=1.3',
        'tldextract>=2.2.2',
        'urllib3>=1.25.9',

    ],
    entry_points={'console_scripts': [
        'redis_run = pycrawler.test:main',
    ]},
    # long_description=read('README.md'),
    # classifiers=[  # 程序的所属分类列表
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: GNU General Public License (GPL)",
    # ],
    # 此项需要，否则卸载时报windows error
    zip_safe=False
)
