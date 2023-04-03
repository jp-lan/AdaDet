# Copyright (c) Alibaba, Inc. and its affiliates.
import os.path as osp
import platform
import shutil
import sys
import tempfile
from importlib import import_module
from pathlib import Path

from modelscope.utils.config import Config as MSConfig
from modelscope.utils.logger import get_logger

logger = get_logger()
BASE_KEY = '_BASE_'


class Config(MSConfig):

    @staticmethod
    def _file2dict(filename):
        filename = osp.abspath(osp.expanduser(filename))
        if not osp.isfile(filename):
            logger.error(filename + ' not found!')
        fileExtname = osp.splitext(filename)[1]
        if fileExtname not in ['.py', '.json', '.yaml', '.yml']:
            raise IOError('Only py/yml/yaml/json type are supported now!')

        with tempfile.TemporaryDirectory() as temp_config_dir:
            temp_config_file = tempfile.NamedTemporaryFile(
                dir=temp_config_dir, suffix=fileExtname)
            if platform.system() == 'Windows':
                temp_config_file.close()
            temp_config_name = osp.basename(temp_config_file.name)
            shutil.copyfile(filename, temp_config_file.name)

            if filename.endswith('.py'):
                temp_module_name = osp.splitext(temp_config_name)[0]
                sys.path.insert(0, temp_config_dir)
                Config._validate_py_syntax(filename)
                mod = import_module(temp_module_name)
                sys.path.pop(0)
                cfg_dict = {
                    name: value
                    for name, value in mod.__dict__.items()
                    if not name.startswith('__')
                }
                # delete imported module
                del sys.modules[temp_module_name]
            elif filename.endswith(('.yml', '.yaml', '.json')):
                from adadet.utils.io import load

                cfg_dict = load(temp_config_file.name)
            # close temp file
            temp_config_file.close()

        cfg_text = filename + '\n'
        with open(filename, 'r', encoding='utf-8') as f:
            # Setting encoding explicitly to resolve coding issue on windows
            cfg_text += f.read()

        if BASE_KEY in cfg_dict:
            cfg_dir = osp.dirname(filename)
            base_filename = cfg_dict.pop(BASE_KEY)
            base_filename = base_filename if isinstance(
                base_filename, list) else [base_filename]

            cfg_dict_list = list()
            cfg_text_list = list()
            for f in base_filename:
                _cfg_dict, _cfg_text = Config._file2dict(osp.join(cfg_dir, f))
                cfg_dict_list.append(_cfg_dict)
                cfg_text_list.append(_cfg_text)

            base_cfg_dict = dict()
            for c in cfg_dict_list:
                if len(base_cfg_dict.keys() & c.keys()) > 0:
                    raise KeyError('Duplicate key is not allowed among bases')
                base_cfg_dict.update(c)

            base_cfg_dict = Config._merge_a_into_b(cfg_dict, base_cfg_dict)
            cfg_dict = base_cfg_dict

            # merge cfg_text
            cfg_text_list.append(cfg_text)
            cfg_text = '\n'.join(cfg_text_list)

        return cfg_dict, cfg_text

    @staticmethod
    def from_file(filename):
        if isinstance(filename, Path):
            filename = str(filename)
        cfg_dict, cfg_text = Config._file2dict(filename)
        return Config(cfg_dict, cfg_text=cfg_text, filename=filename)
