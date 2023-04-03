# Copyright (c) Alibaba, Inc. and its affiliates.
from abc import ABC, abstractmethod
from typing import Any, Dict

from adadet.utils.config import Config

from modelscope.trainers import build_trainer as build_ms_trainer
from modelscope.trainers.base import BaseTrainer as MsBaseTrainer
from modelscope.utils.constant import ThirdParty
from modelscope.utils.registry import Registry, build_from_cfg

TRAIN_MANAGERS = Registry('train_managers')


class TrainManager(ABC):

    def __init__(self, model_id, data, modelscope_params, **kwargs) -> None:

        ms_trainer_name = self.get_ms_trainer_name()
        train_kwargs = self.build_kwargs(model_id, data, modelscope_params,
                                         **kwargs)
        train_kwargs = self._set_third_party(train_kwargs)
        self._trainer = build_ms_trainer(ms_trainer_name, train_kwargs)

    def train(self) -> None:
        return self._trainer.train()

    def evaluate(self, *args, **kwargs) -> None:
        return self._trainer.evaluate(*args, **kwargs)

    def _set_third_party(self, train_kwargs) -> Dict[str, Any]:
        train_kwargs[ThirdParty.KEY] = getattr(ThirdParty, 'ADADET', 'adadet')
        return train_kwargs

    @property
    def trainer(self) -> MsBaseTrainer:
        return self._trainer

    @abstractmethod
    def get_ms_trainer_name(self) -> str:
        """ Get modelscope trainer name for specific trainer.
        """
        pass

    @abstractmethod
    def get_default_model_path(self) -> str:
        """ Get default model path for specific trainer.
        """
        pass

    @abstractmethod
    def build_kwargs(self, model, data, params, **kwargs) -> Dict[str, Any]:
        """ Build kwargs for specific trainer.
        """
        pass


def build_train_manager(cfg: Config, **kwargs):
    return build_from_cfg(
        cfg, TRAIN_MANAGERS, group_key='adadet_train', **kwargs)


def train_manager(cfg: Config = None, **kwargs) -> TrainManager:
    cfg = cfg.adadet_train
    return build_train_manager(cfg, **kwargs)
