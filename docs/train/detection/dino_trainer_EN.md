[简体中文](./dino_trainer.md) | English
# DinoTrainer

This document introduces the details (configuration file and result format) of DinoTrainer, and the trained model can be used as a node of the indrustrial solution.

❗️Note: Single model training and evaluation only support GPU model now.

## Train

### Quick Start
Execute [run_train.sh](../../../tools/run_train.sh):

```python
python tools/train.py --config configs/train/detection/general_object_detection_dino.yaml
```
The command takes [training configuration file](../../../configs/train/detection/general_object_detection_dino.yaml) as input parameter to [train API](../../../tools/train.py).

### Configuration

The contents of [training configuration file](../../../configs/train/detection/general_object_detection_dino.yaml) are as follows:
```yaml
adadet_train:
  type: 'DinoTrainManager'
  model_id: 'damo/cv_swinl_image-object-detection_dino'
  data:
    dataset_mode: 'dataset_online'
    train_cfg:
      dataset_name: 'small_coco_for_test'
      namespace: 'EasyCV'
      split: 'train'
    eval_cfg:
      dataset_name: 'small_coco_for_test'
      namespace: 'EasyCV'
      split: 'validation'
  modelscope_params:
    train:
      work_dir: './output'
      max_epochs: 18
      dataloader:
        batch_size_per_gpu: 1
    model:
      head:
        num_classes: 80

```

#### Parameters

- `adadet_train`: The parameters about training.
    + `type` (str): Type of trainer, e.g., `'DinoTrainManager'` for DINO.
    + `model_id` (str): The model_id in ModelScope, e.g., `'damo/cv_swinl_image-object-detection_dino'` for dino detection model. Please refer to [modelcard](https://modelscope.cn/models/damo/cv_swinl_image-object-detection_dino/summary) for the model_id of a specific model.
    + `data`: The parameters about datasets. Note: Only support COCO format dataset now.
        * `dataset_mode` (str): Support online dataset and offline data, i.e., `'dataset_online'` and `'dataset_offline'`.
        * `train_cfg`/`eval_cfg`: The parameters about training set and evaluation set.
            - Online dataset (refer to [create dataset](https://modelscope.cn/docs/%E6%89%98%E7%AE%A1%E5%88%B0ModelScope%E6%95%B0%E6%8D%AE%E9%9B%86%E5%88%9B%E5%BB%BA%E6%B5%81%E7%A8%8B) for creating an online dataset). The related parameters are as follows:
                + `dataset_name` (str): The name of the dataset, e.g., `'small_coco_for_test'`. Refer to [dataset homepage](https://modelscope.cn/datasets/EasyCV/small_coco_for_test/summary) for the name of a dataset.
                + `namespace` (str): The namespace of the dataset. Refer to owner on [dataset settings](https://modelscope.cn/datasets/EasyCV/small_coco_for_test/summary).
                + `split` (str): The split of the dataset. Refer to [dataset configuration file](https://modelscope.cn/datasets/EasyCV/small_coco_for_test/file/view/master/small_coco_for_test.json) for the split details.
            - Offline dataset, The related parameters are as follows:
                + `img_dir` (str): The root directory of images.
                + `anno_path` (str): The path to annotation file.
    + `modelscope_params`: The hyper-parameters for trainer.
        * `train`:
            - `work_dir` (str): The path to work dirtectory.
            - `max_epochs` (int): The total number of traing epoch.
            - `dataloader`:
                + `batch_size_per_gpu` (int): number of training samples per GPU.
        * `model`: Model parameters.
            - `head`:
                + `num_classes` (int): The class number.
        * All parameters in [configuration.json](https://modelscope.cn/models/damo/cv_swinl_image-object-detection_dino/file/view/master/configuration.json) can be assigned in this way.


### Work Directory

The work directory can be set by `"work_dir"`. The work directory is as below:

```bash
  ├── epoch_xxx.pth # Model checkpoint
  ├── xxx.log # The training log
  ├── xxx.log.json # The training log in json format
  ├── output # Directory in modelhub style for inference
  │   ├── ...

```


## Evaluation

N/A
