[简体中文](./small_object_detection.md) | English
# Small Object Detection

Supported models：

|model name|task_name|model_id|
|:--:|:--:|:--:|
|[small-object-detection-MaskScoring](#small-object-detection-MaskScoring)|image-object-detection|damo/cv_resnet50_object-detection_maskscoring|

## 📌small-object-detection-MaskScoring
### Introduction
Small object detection aims to detect objects of small size. The model is based on the Resnet-50 backbone. More modules, such as deformable convolutions, are added to the backbone network to improve accuracy. Also, some modifications are performed on the neck, RPN-head, and ROI-head to solve the long-tail and small object problems.

This model is trained on [COCO](https://cocodataset.org/#detection-2017).


### Inference
Please use the model infer function to make predictions. Currently, the model only supports GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'video-object-detection'
  model_id: 'damo/cv_resnet50_object-detection_maskscoring'
```

## Performance
| Backbone |  Pretrain   | Box mAP_s |
|:--------:|:-----------:|:-------:|
| R-50-FPN-BFP | ImageNet-1k |  27.8  |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_resnet50_object-detection_maskscoring/summary)

### Citations
```BibTeX
@inproceedings{huang2019msrcnn,
    title={Mask Scoring R-CNN},
    author={Zhaojin Huang and Lichao Huang and Yongchao Gong and Chang Huang and Xinggang Wang},
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
    year={2019},
}
```
