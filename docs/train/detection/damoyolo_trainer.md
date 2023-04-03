简体中文 | [English](./damoyolo_trainer_EN.md)
# DamoYoloTrainer使用文档

单模型训练功能用于训练单个模型，训练好的模型可以作为后续场景化解决方案的一个节点。此文档用于介绍DAMOYOLO模型训练功能（train）的配置文件和保存结果。

❗️注意：单模型训练评估功能只支持在GPU模式，没有GPU环境的机器无法体验！
## 模型训练

### 快速开始
该功能可通过[run_train.sh](../../../tools/run_train.sh)运行体验，具体运行命令如下：
```python
python tools/train.py --config configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml
```
该命令需要把[配置文件](../../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)作为参数输入到[训练功能接口](../../../tools/train.py)中。

### 配置文件说明
DAMOYOLO训练功能可以通过[配置文件](../../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)进行参数配置，主要配置参数说明如下：
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

#### 参数说明

对配置文件中的参数说明如下：

- `adadet_train`: 训练功能主要配置参数部分。
    + `type` (str): trainer的类型，DAMOYOLO的类别为`'DamoYoloTrainManager'`。
    + `model_id` (str): ModelScope中模型库的模型id名称，当前示例使用人体检测模型的model_id为`'damo/cv_tinynas_human-detection_damoyolo'`，可从对应[模型库](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary)介绍中获得。
    + `data`: 数据集相关参数。注意：目前DamoYoloTrainer仅支持COCO格式的数据集。
        * `dataset_mode` (str): 目前支持使用在线（online）数据集或本地离线（offline）数据集，分别对应`'dataset_online'`和`'dataset_offline'`。
        * `train_cfg`/`eval_cfg`: 训练集/验证集相关参数。
            - 如果是使用在线数据集（如何创建模型可以参考[新建数据集文档](https://modelscope.cn/docs/%E6%89%98%E7%AE%A1%E5%88%B0ModelScope%E6%95%B0%E6%8D%AE%E9%9B%86%E5%88%9B%E5%BB%BA%E6%B5%81%E7%A8%8B)），上述的示例即为在线数据集，需要设置如下三个参数：
                + `dataset_name` (str): 数据集的名称，当前示例使用人体检测数据集的名称为`'person_detection_for_train'`，可从对应的[数据集](https://modelscope.cn/datasets/modelscope/person_detection_for_train/summary)介绍中获取。
                + `namespace` (str): 数据集账号名称，可以在[数据集设置](https://modelscope.cn/datasets/modelscope/person_detection_for_train/settings)中查看，其中所有者即为对应的namespace。
                + `split` (str): 数据集分片，可以在[数据集配置文件](https://modelscope.cn/datasets/modelscope/person_detection_for_train/file/view/master/person_detection_for_train.json)中查看分片信息。
            - 如果是使用离线数据集（可以参考[配置文件](../../../configs/train/detection/domain_specific_object_detection_damoyolo_offline.yaml)），需要设置如下两个参数：
                + `img_dir` (str): 图片根目录。
                + `anno_path` (str): 标注文件的路径。
    + `modelscope_params`: 此部分与modelscope参数列表一致
        * `train`: 训练相关参数
          - `gpu_ids` (list[int]): 用于训练的GPU的id。
          - `batch_size` (int): 训练的批大小。
          - `max_epochs` (int): 训练的总轮次。
          - `base_lr_per_img` (float): 单图学习率，最终学习率是`batch_size`乘以`base_lr_per_img`。
          - `load_pretrain` (bool): 是否使用预训练模型，默认使用[模型库](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary)中提供的模型作为预训练模型。
          - `work_dir` (str): 工作目录。
        * `model`: 模型结构相关参数。
          - `head`:
            + `num_classes` (int): 训练数据集的类别数。

### 保存结果说明

DamoYoloTrainer默认的工作目录为`./workdirs`。完成训练后，工作目录的目录结构如下：

```bash
  ├── epoch_xxx_ckpt.pth # 模型文件
  ├── latest_ckpt.pth # 最新的模型文件
  ├── train_log.txt # 训练日志文件
  ├── inference
  │   ├── bbox.json # 预测框文件
  │   ├── coco_results.pth # COCO eval结果文件
  │   ├── predictions.pth # 预测结果文件

```


## 模型评估

在上述训练的过程中，会在验证集上进行模型评估，若需要对指定的模型单独进行模型评估，可以通过[run_eval.sh](../../../tools/run_eval.sh)运行体验，具体运行命令如下：
```python
python tools/eval.py --config configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml \
                     --checkpoint the/path/to/your/checkpoint.pth
```
该命令需要把[配置文件](../../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)作为参数输入到[评估功能接口](../../../tools/eval.py)中。注意，如果没有指定`checkpoint`参数，则默认使用DAMOYOLO自带的预训练模型进行评估。
