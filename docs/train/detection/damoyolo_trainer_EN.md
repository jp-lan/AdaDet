[简体中文](./damoyolo_trainer.md) | English
# DamoYoloTrainer

This document introduces the details (configuration file and work directory structure) of DamoYoloTrainer, and the trained model can be used as a node of the indrustrial solution.

❗️Note: Single model training and evaluation only support GPU model now.

## Train

### Quick Start
Execute [run_train.sh](../../../tools/run_train.sh):

```python
python tools/train.py --config configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml
```

The command takes [training configuration file](../../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) as input parameter to [train API](../../../tools/train.py).

### Configuration

The contents of [training configuration file](../../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) are as follows:
```yaml
adadet_train:
  type: 'DamoYoloTrainManager'
  model_id: 'damo/cv_tinynas_human-detection_damoyolo'
  data:
    dataset_mode: 'dataset_online'
    train_cfg:
      dataset_name: 'person_detection_for_train'
      namespace: 'modelscope'
      split: 'train'
    eval_cfg:
      dataset_name: 'person_detection_for_train'
      namespace: 'modelscope'
      split: 'validation'
  modelscope_params:
    train:
      gpu_ids: [0, ]
      batch_size: 2
      max_epochs: 3
      base_lr_per_img: 0.001
      load_pretrain: True
      work_dir: './workdirs'
    model:
      head:
        num_classes: 1
```

#### Parameters


- `adadet_train`: The parameters about training.
    + `type` (str): Type of trainer, e.g., `'DamoYoloTrainManager'` for DAMOYOLO.
    + `model_id` (str): The model_id in ModelScope, e.g., `'damo/cv_tinynas_human-detection_damoyolo'` for human detection model. Please refer to [modelcard](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary) for the model_id of a specific model.
    + `data`: The parameters about datasets. Note: Only support COCO format dataset now.
        * `dataset_mode` (str): Support online dataset and offline data, i.e., `'dataset_online'` and `'dataset_offline'`.
        * `train_cfg`/`eval_cfg`: The parameters about training set and evaluation set.
            - Online dataset (refer to [create dataset](https://modelscope.cn/docs/%E6%89%98%E7%AE%A1%E5%88%B0ModelScope%E6%95%B0%E6%8D%AE%E9%9B%86%E5%88%9B%E5%BB%BA%E6%B5%81%E7%A8%8B) for creating an online dataset). The related parameters are as follows:
                + `dataset_name` (str): The name of the dataset, e.g., `'person_detection_for_train'`. Refer to [dataset homepage](https://modelscope.cn/datasets/modelscope/person_detection_for_train/summary) for the name of a dataset.
                + `namespace` (str): The namespace of the dataset. Refer to owner on [dataset settings](https://modelscope.cn/datasets/modelscope/person_detection_for_train/settings).
                + `split` (str): The split of the dataset. Refer to [dataset configuration file](https://modelscope.cn/datasets/modelscope/person_detection_for_train/file/view/master/person_detection_for_train.json) for the split details.
            - Offline dataset(refer to [offline config](../../../configs/train/detection/domain_specific_object_detection_damoyolo_offline.yaml)), The related parameters are as follows:
                + `img_dir` (str): The root directory of images.
                + `anno_path` (str): The path to annotation file.
    + `modelscope_params`: The hyper-parameters for trainer.
      - `train`: train parameters.
        * `gpu_ids` (list[int]): The ids of GPU for training.
        * `batch_size` (int): The batch size for training.
        * `max_epochs` (int): The total number of training epoch.
        * `base_lr_per_img` (float): The learning rate per image. The final learning rate can be calculated by `batch_size * base_lr_per_img`.
        * `load_pretrain` (bool): Whether to use pretrained model. Default using the model file on [modelhub](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary) as a pretrained model.
        * `work_dir` (str): working directory path.
        * `model`: model parameters
          + `head`:
            - `num_classes` (int): The class number.

### Work Directory

The default work directory of DamoYoloTrainer is `./workdirs`. The work directory is as below:

```bash
  ├── epoch_xxx_ckpt.pth # Model checkpoint
  ├── latest_ckpt.pth # The latest checkpoint
  ├── train_log.txt # The training log
  ├── inference
  │   ├── bbox.json # The file saves the predicted bounding bbox
  │   ├── coco_results.pth # The file saves the results of COCO evaluation
  │   ├── predictions.pth # The file saves the results of predictions

```


## Evaluation

The model is evaluated on eval set during training process. Execute [run_eval.sh](../../../tools/run_eval.sh) for model evaluation:

```python
python tools/eval.py --config configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml \
                     --checkpoint the/path/to/your/checkpoint.pth
```

The command takes [training configuration file](../../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) as input parameter to [eval API](../../../tools/train.py). Note: If `checkpoint` is not set, the default model will be used.
