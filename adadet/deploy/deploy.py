# Copyright (c) Alibaba, Inc. and its affiliates.
from adadet.utils.config import Config

from modelscope.utils.registry import Registry, build_from_cfg

DEPLOYS = Registry('deploys')


class Deploy:

    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        pass

    def visualize(self) -> None:
        pass


def build_deploy(cfg: Config, **kwargs):
    return build_from_cfg(cfg, DEPLOYS, group_key='adadet_deploy', **kwargs)


def deploy(cfg: Config = None, **kwargs) -> Deploy:
    cfg = cfg.adadet_deploy
    return build_deploy(cfg, **kwargs)
