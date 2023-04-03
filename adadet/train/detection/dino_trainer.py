# Copyright (c) Alibaba, Inc. and its affiliates.
import os
from typing import Any, Dict

from adadet.train.train import TRAIN_MANAGERS, TrainManager
from adadet.utils.constants import DatasetMode

from modelscope.metainfo import Trainers
from modelscope.msdatasets import MsDataset
from modelscope.msdatasets.dataset_cls.dataset import ExternalDataset
from modelscope.utils.constant import ModelFile


@TRAIN_MANAGERS.register_module('adadet_train', 'DinoTrainManager')
class DinoTrainManager(TrainManager):

    def get_ms_trainer_name(self) -> str:
        return Trainers.easycv

    def get_default_model_path(self) -> str:
        return os.path.join(self._trainer.model_dir,
                            ModelFile.TORCH_MODEL_FILE)

    def build_kwargs(self, model_id, data, modelscope_params,
                     **kwargs) -> Dict[str, Any]:

        dataset_mode = data.get('dataset_mode', DatasetMode.dataset_online)

        if dataset_mode == DatasetMode.dataset_online:
            train_dataset = MsDataset.load(
                data.train_cfg.dataset_name,
                namespace=data.train_cfg.namespace,
                split=data.train_cfg.split)
            val_dataset = MsDataset.load(
                data.eval_cfg.dataset_name,
                namespace=data.eval_cfg.namespace,
                split=data.eval_cfg.split)

        elif dataset_mode == DatasetMode.dataset_offline:
            train_img_dir = data.train_cfg.img_dir
            val_img_dir = data.eval_cfg.img_dir
            train_anno_path = data.train_cfg.anno_path
            val_anno_path = data.eval_cfg.anno_path
            train_split_path_dict = dict(train='')
            train_config_kwargs = dict(
                data_source=dict(
                    ann_file=train_anno_path, img_prefix=train_img_dir), )
            val_split_path_dict = dict(validation='')
            val_config_kwargs = dict(
                data_source=dict(
                    ann_file=val_anno_path, img_prefix=val_img_dir), )
            train_external_dataset = ExternalDataset(train_split_path_dict,
                                                     train_config_kwargs)
            val_external_dataset = ExternalDataset(val_split_path_dict,
                                                   val_config_kwargs)
            train_dataset = MsDataset(train_external_dataset)
            val_dataset = MsDataset(val_external_dataset)
        else:
            raise NotImplementedError

        train_kwargs = dict(
            model=model_id,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            cfg_options=modelscope_params)

        return train_kwargs
