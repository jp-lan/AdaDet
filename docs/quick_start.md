简体中文 | [English](./quick_start_EN.md)
# 快速开始
本快速开始教程以人体检测模型单模型和闯入检测场景化方案为例，让客户快速熟悉AdaDet的使用方式和使用流程。

## 一、模型推理
```python
# 使用训练好的人体垂类检测模型进行模型快速推理。
python tools/infer.py --config configs/infer/model_infer.yaml
```
推理结果保存在./infer_out路径下将保存生成下列文件：

```bash
  ├── test_walker1.json
  ├── vis
  │   ├── test_walker1.jpeg
```

其中test_walker1.jpg.json为图片输出结果，其输出内容字段为：
```python

{
    "scores": [
        0.8139657378196716,
        0.7489762306213379,
        ...
    ],
    "labels": [
        "person",
        "person",
        ...
    ],
    "boxes": [
        [
            561.63720703125,
            377.2309265136719,
            622.9022827148438,
            488.0690002441406
        ],
        [
            371.8719177246094,
            203.49237060546875,
            387.8343200683594,
            253.65220642089844
        ],
        ...
    ]
}

```

可视化结果如下：

<img src='./assets/test_walker1_vis.jpeg' width=400>

## 二、模型训练评估（二次开发）
若对于模型的效果不满意，则可以准备数据进行模型的二次开发（finetune）。

注意：此部分必须要配置GPU环境。

### 1、数据准备
数据准备在[训练文档](./train/detection/damoyolo_trainer.md)的参数设置中有详细介绍，此处我们以准备好的[线上数据集](https://modelscope.cn/datasets/modelscope/person_detection_for_train/summary)为例进行模型训练（线下数据集的准备参见[训练文档](./train/detection/damoyolo_trainer.md)）。

### 2、训练
根据选定的模型类型和准备好的数据，把相应参数填入[训练配置文件](../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，可直接通过下列命令跑通finetune流程：

```python
python tools/train.py --config configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml
```

训练结果默认的保存目录为`./workdirs`。完成训练后，工作目录的目录结构如下：

```bash
  ├── epoch_xxx_ckpt.pth # 模型文件
  ├── latest_ckpt.pth # 最新的模型文件
  ├── train_log.txt # 训练日志文件
  ├── inference
  │   ├── bbox.json # 预测框文件
  │   ├── coco_results.pth # COCO eval结果文件
  │   ├── predictions.pth # 预测结果文件

```

### 3、评估
在上述训练的过程中，会在验证集上进行模型评估，若需要对指定的模型单独进行模型评估，可以通过下列命令进行模型评估：
```python
python tools/eval.py --config configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml \
                     --checkpoint the/path/to/your/checkpoint.pth
```
注意，如果没有指定`checkpoint`参数，则默认使用训练器自带的预训练模型进行评估。

## 三、场景化解决方案效果体验
场景化解决方案是面向产业界的落地应用，[闯入检测](./deploy/human/break_in_deploy.md)场景化解决方案串联了人体检测模型节点和区域闯入判断节点。
该解决方案可以通过下列命令快速跑通：
```python
python deploy.py --config configs/deploy/human/break_in_det_deploy.yaml
```
结果默认保存在`./deploy_res`，可到该文件夹查看相关输出结果和可视化结果。
若需对闯入检测中的人体检测模型进行效果调优，参见[模型训练评估](#二模型训练评估二次开发)。
