简体中文 | [English](./dino_trainer_EN.md)
# DinoTrainer使用文档

单模型训练功能用于训练单个模型，训练好的模型可以作为后续场景化解决方案的一个节点。此文档用于介绍DINO模型训练功能（train）的配置文件和工作目录结构。

❗️注意：单模型训练评估功能只支持在GPU模式，没有GPU环境的机器无法体验！
## 模型训练
### 快速开始
该功能可通过[run_train.sh](../../../tools/run_train.sh)运行体验，具体运行命令如下：
```python
python tools/train.py --config configs/train/detection/general_object_detection_dino.yaml
```
该命令需要把[配置文件](../../../configs/train/detection/general_object_detection_dino.yaml)作为参数输入到[训练功能接口](../../../tools/train.py)中。

### 配置文件说明
DINO训练功能可以通过[配置文件](../../../configs/train/detection/general_object_detection_dino.yaml)进行参数配置，主要配置参数说明如下：
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

#### 参数说明

对配置文件中的参数说明如下：

- `adadet_train`: 训练功能主要配置参数部分。
    + `type` (str): trainer的类型，DINO的类别为`'DinoTrainManager'`。
    + `model_id` (str): ModelScope中模型库的模型id名称，当前示例使用DINO-高精度目标检测模型的model_id为`'damo/cv_swinl_image-object-detection_dino'`，可从对应[模型库](https://modelscope.cn/models/damo/cv_swinl_image-object-detection_dino/summary)介绍中获得。
    + `data`: 数据集相关参数。注意：目前DinoTrainer仅支持COCO格式的数据集。
        * `dataset_mode` (str): 目前支持使用在线（online）数据集或本地离线（offline）数据集，分别对应`'dataset_online'`和`'dataset_offline'`。
        * `train_cfg`/`eval_cfg`: 训练集/验证集相关参数。
            - 如果是使用在线数据集（如何创建模型可以参考[新建数据集文档](https://modelscope.cn/docs/%E6%89%98%E7%AE%A1%E5%88%B0ModelScope%E6%95%B0%E6%8D%AE%E9%9B%86%E5%88%9B%E5%BB%BA%E6%B5%81%E7%A8%8B)），上述的示例即为在线数据集，需要设置如下三个参数：
                + `dataset_name` (str): 数据集的名称，当前示例使用人体检测数据集的名称为`'small_coco_for_test'`，可从对应的[数据集](https://modelscope.cn/datasets/EasyCV/small_coco_for_test/summary)介绍中获取。
                + `namespace` (str): 数据集账号名称，可以在[数据集设置](https://modelscope.cn/datasets/EasyCV/small_coco_for_test/summary)中查看，其中所有者即为对应的namespace。
                + `split` (str): 数据集分片，可以在[数据集配置文件](https://modelscope.cn/datasets/EasyCV/small_coco_for_test/file/view/master/small_coco_for_test.json)中查看分片信息。
            - 如果是使用离线数据集，需要设置如下两个参数：
                + `img_dir` (str): 图片根目录。
                + `anno_path` (str): 标注文件的路径。
    + `modelscope_params`: 此部分与modelscope参数列表一致。
        * `train`:
            - `work_dir` (str): 工作目录。
            - `max_epochs` (int): 训练的总轮次。
            - `dataloader`:
                + `batch_size_per_gpu` (int): 每张GPU的训练样本数。
        * `model`: 模型结构相关参数。
            - `head`:
                + `num_classes` (int): 训练数据集的类别数。
        * 配置文件中所有的参数均支持使用类似的方式进行设置，具体的参数可以参考[configuration.json](https://modelscope.cn/models/damo/cv_swinl_image-object-detection_dino/file/view/master/configuration.json)。

### 保存结果说明

DinoTrainer工作目录为可以通过`work_dir`字段进行设置。完成训练后，工作目录的目录结构如下：

```bash
  ├── epoch_xxx.pth # 模型文件
  ├── xxx.log # 训练日志文件
  ├── xxx.log.json # json格式训练日志文件
  ├── output # DINO ModelScope modelhub文件
  │   ├── ...

```


## 模型评估

暂不支持。
