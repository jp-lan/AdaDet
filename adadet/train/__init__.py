# Copyright (c) Alibaba, Inc. and its affiliates.
from .detection.damoyolo_trainer import DamoYoloTrainManager
from .detection.dino_trainer import DinoTrainManager
from .train import train_manager

__all__ = ['train_manager', 'DamoYoloTrainManager', 'DinoTrainManager']
