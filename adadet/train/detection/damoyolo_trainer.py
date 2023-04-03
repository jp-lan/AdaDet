# Copyright (c) Alibaba, Inc. and its affiliates.
import os.path as osp
from typing import Any, Dict

from adadet.train.train import TRAIN_MANAGERS, TrainManager
from adadet.utils.constants import DatasetMode

from modelscope.metainfo import Trainers
from modelscope.msdatasets import MsDataset


@TRAIN_MANAGERS.register_module('adadet_train', 'DamoYoloTrainManager')
class DamoYoloTrainManager(TrainManager):

    def get_ms_trainer_name(self) -> str:
        return Trainers.tinynas_damoyolo

    def get_default_model_path(self) -> str:
        return self._trainer.cfg.train.finetune_path

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

            train_root_dir = train_dataset.config_kwargs['split_config'][
                'train']
            val_root_dir = val_dataset.config_kwargs['split_config'][
                'validation']
            train_img_dir = osp.join(train_root_dir, 'images')
            val_img_dir = osp.join(val_root_dir, 'images')
            train_anno_path = osp.join(train_root_dir, 'train.json')
            val_anno_path = osp.join(val_root_dir, 'val.json')

        elif dataset_mode == DatasetMode.dataset_offline:
            train_img_dir = data.train_cfg.img_dir
            val_img_dir = data.eval_cfg.img_dir
            train_anno_path = data.train_cfg.anno_path
            val_anno_path = data.eval_cfg.anno_path
        else:
            raise NotImplementedError

        train_kwargs = dict(
            model=model_id,
            gpu_ids=modelscope_params.train.gpu_ids,
            batch_size=modelscope_params.train.batch_size,
            max_epochs=modelscope_params.train.max_epochs,
            num_classes=modelscope_params.model.head.num_classes,
            load_pretrain=modelscope_params.train.load_pretrain,
            base_lr_per_img=modelscope_params.train.base_lr_per_img,
            train_image_dir=train_img_dir,
            val_image_dir=val_img_dir,
            train_ann=train_anno_path,
            val_ann=val_anno_path,
            work_dir=modelscope_params.train.work_dir,
            exp_name=modelscope_params.miscs.exp_name,
        )

        return train_kwargs
