# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

import torch
from adadet.train import train_manager
from adadet.utils.config import Config

from modelscope.utils.test_utils import test_level


class DinoTrainManagerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.config_path = 'configs/train/detection/general_object_detection_dino.yaml'
        self.dataset_cfg = dict(
            train=dict(
                dataset_name='small_coco_for_test',
                namespace='EasyCV',
                split='train'),
            val=dict(
                dataset_name='small_coco_for_test',
                namespace='EasyCV',
                split='validation'))
        self.train_cfg = dict(max_epochs=1, num_classes=80)

    @unittest.skipUnless(test_level() >= 0 and torch.cuda.is_available(),
                         'skip test in current test level')
    def test_dino_train_manager(self):
        cfg = Config.from_file(self.config_path)
        cfg.adadet_train.data.train_cfg.dataset_name = self.dataset_cfg[
            'train']['dataset_name']
        cfg.adadet_train.data.train_cfg.namespace = self.dataset_cfg['train'][
            'namespace']
        cfg.adadet_train.data.train_cfg.split = self.dataset_cfg['train'][
            'split']
        cfg.adadet_train.data.eval_cfg.dataset_name = self.dataset_cfg['val'][
            'dataset_name']
        cfg.adadet_train.data.eval_cfg.namespace = self.dataset_cfg['val'][
            'namespace']
        cfg.adadet_train.data.eval_cfg.split = self.dataset_cfg['val']['split']
        cfg.adadet_train.modelscope_params[
            'train.max_epochs'] = self.train_cfg['max_epochs']
        cfg.adadet_train.modelscope_params[
            'model.head.num_classes'] = self.train_cfg['num_classes']
        trainer = train_manager(cfg)
        trainer.train()


if __name__ == '__main__':
    unittest.main()
