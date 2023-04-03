简体中文 | [English](./small_object_detection_EN.md)
# 小目标检测

当前支持的小目标检测模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[高性能通用小目标检测-MaskScoring模型](#高性能通用小目标检测-MaskScoring模型)|image-object-detection|damo/cv_resnet50_object-detection_maskscoring|

## 📌高性能通用小目标检测-MaskScoring模型
### 基本信息
主要是针对长尾和小目标问题解决的高性能通用目标检测模型，采用COCO数据集训练。本模型基于Resnet50-Backbone增加可形变卷积等模块增强多角度单目标识别的精度；在Neck、RPN-head和ROI-head针对长尾和小目标问题进行了模型优化，以适用特定场景下痛点问题的解决。本模型是基于[COCO](https://cocodataset.org/#detection-2017)开源数据训练得到。


### 模型推理
可使用单模型推理功能进行效果体验，目前支持GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'video-object-detection'
  model_id: 'damo/cv_resnet50_object-detection_maskscoring'
```

## 客观指标
| Backbone |  Pretrain   | Box mAP_s |
|:--------:|:-----------:|:-------:|
| R-50-FPN-BFP | ImageNet-1k |  27.8  |
## 引用

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_resnet50_object-detection_maskscoring/summary)

### 相关论文
本模型主要参考论文如下：
```BibTeX
@inproceedings{huang2019msrcnn,
    title={Mask Scoring R-CNN},
    author={Zhaojin Huang and Lichao Huang and Yongchao Gong and Chang Huang and Xinggang Wang},
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
    year={2019},
}
```
