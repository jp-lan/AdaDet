# Copyright (c) Alibaba, Inc. and its affiliates.
from setuptools import find_packages, setup

version_file = 'adadet/version.py'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


def readme():
    """Fetch readme content from README.md"""
    with open('README_EN.md', encoding='utf-8') as f:
        content = f.read()
    return content


setup(
    name='AdaDet',
    version=get_version(),
    description='Development toolkit for object detection based on ModelScope',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/modelscope/adadet',
    author='AdaDet Team',
    packages=find_packages(exclude=('test', 'tools', 'docs')),
)
