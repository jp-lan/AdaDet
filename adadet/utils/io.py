# Copyright (c) Alibaba, Inc. and its affiliates.

import os
from abc import ABCMeta, abstractmethod
from pathlib import Path

import json
import numpy as np
import six
import yaml


def is_str(x):
    """Whether the input is an string instance."""
    return isinstance(x, six.string_types)


class BaseFileHandler(object):

    __metaclass__ = ABCMeta  # python 2 compatibility

    @abstractmethod
    def load_from_content(self, file, key_id=None, **kwargs):
        pass

    @abstractmethod
    def load_from_fileobj(self, file, key_id=None, **kwargs):
        pass

    @abstractmethod
    def dump_to_fileobj(self, obj, file, key_id=None, **kwargs):
        pass

    @abstractmethod
    def dump_to_str(self, obj, key_id=None, **kwargs):
        pass

    def load_from_path(self, filepath, mode='r', key_id=None, **kwargs):
        if key_id:
            mode = 'rb'
        encoding = None if key_id else 'utf-8-sig'
        with open(filepath, mode, encoding=encoding) as f:
            return self.load_from_fileobj(f, **kwargs)

    def dump_to_path(self, obj, filepath, mode='w', key_id=None, **kwargs):
        if key_id:
            mode = 'wb'
        encoding = None if key_id else 'utf-8'
        with open(filepath, mode, encoding=encoding) as f:
            self.dump_to_fileobj(obj, f, **kwargs)


try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class YamlHandler(BaseFileHandler):

    def load_from_fileobj(self, file, **kwargs):
        kwargs.setdefault('Loader', Loader)
        return yaml.load(file, **kwargs)

    def dump_to_fileobj(self, obj, file, **kwargs):
        kwargs.setdefault('Dumper', Dumper)
        yaml.dump(obj, file, **kwargs)

    def dump_to_str(self, obj, **kwargs):
        kwargs.setdefault('Dumper', Dumper)
        return yaml.dump(obj, **kwargs)


class NumpyArrayEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.float32):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


class JsonHandler(BaseFileHandler):

    def load_from_fileobj(self, file, **kwargs):
        return json.load(file)

    def dump_to_fileobj(self, obj, file, **kwargs):
        json.dump(
            obj,
            file,
            ensure_ascii=False,
            indent=4,
            cls=NumpyArrayEncoder,
            **kwargs)
        return

    def dump_to_str(self, obj, **kwargs):
        return json.dumps(obj, **kwargs)


file_handlers = {
    'json': JsonHandler(),
    'yaml': YamlHandler(),
    'yml': YamlHandler(),
}


def load(file, file_format=None, **kwargs):
    """

    Args:
        file:
        file_format:
        key_id:
        **kwargs:

    Returns:

    """
    if isinstance(file, Path):
        file = str(file)
    if file_format is None and is_str(file):
        file_format = file.split('.')[-1]
    if file_format not in file_handlers:
        raise TypeError('Unsupported format: {}'.format(file_format))

    handler = file_handlers[file_format]

    if is_str(file):
        obj = handler.load_from_path(file, **kwargs)
    elif hasattr(file, 'read'):
        obj = handler.load_from_fileobj(file, **kwargs)
    else:
        raise TypeError('"file" must be a filepath str or a file-object')
    return obj


def dump(obj, file=None, file_format=None, auto_mkdir=False, **kwargs):
    if isinstance(file, Path):
        file = str(file)
    if file_format is None:
        if is_str(file):
            file_format = file.split('.')[-1]
        elif file is None:
            raise ValueError(
                'file_format must be specified since file is None')
    if file_format not in file_handlers:
        raise TypeError('Unsupported format: {}'.format(file_format))

    handler = file_handlers[file_format]
    if file is None:
        return handler.dump_to_str(obj, **kwargs)
    elif is_str(file):
        if auto_mkdir:
            os.makedirs(os.path.dirname(file), exist_ok=True)
        handler.dump_to_path(obj, file, **kwargs)
    elif hasattr(file, 'write'):
        handler.dump_to_fileobj(obj, file, **kwargs)
    else:
        raise TypeError('"file" must be a filename str or a file-object')


def load_txt_lines(file_path, rm_cr=False) -> list:
    """从文件读取每一行

    Args:
        file_path:
        rm_cr: 是否删除文件结尾的回车"\n"

    Returns:

    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if rm_cr:
        return [line.strip('\n') for line in lines]
    else:
        return lines


def save_txt_lines(list_data, file_path, add_cr=True):
    """从文件读取每一行

    Args:
        file_path:
        add_cr: 是否添加文件结尾的回车"\n"

    Returns:

    """
    with open(file_path, 'w', encoding='utf-8') as f:
        for li in list_data:
            f.write(li.strip())
            if add_cr:
                f.write('\n')
