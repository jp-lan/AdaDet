# Copyright (c) Alibaba, Inc. and its affiliates.
from adadet.utils.config import Config

from modelscope.utils.registry import Registry, build_from_cfg

INFERS = Registry('infers')


class Infer:

    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        pass

    def visualize(self) -> None:
        pass


def build_infer(cfg: Config, **kwargs):
    return build_from_cfg(cfg, INFERS, group_key='adadet_infer', **kwargs)


def infer(cfg: Config = None, **kwargs) -> Infer:
    cfg = cfg.adadet_infer
    return build_infer(cfg, **kwargs)
