简体中文 | [English](./object_detection_EN.md)
# 通用目标检测

当前支持的通用目标检测模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[通用目标检测-YOLOX-S](#通用目标检测-YOLOX-S)|image-object-detection|damo/cv_cspnet_image-object-detection_yolox|
|[通用目标检测-YOLOX-Nano](#通用目标检测-YOLOX-nano)|image-object-detection|damo/cv_cspnet_image-object-detection_yolox_nano_coco|
|[通用目标检测-DINO](#通用目标检测-DINO)|image-object-detection|damo/cv_swinl_image-object-detection_dino|
|[通用目标检测-DAMOYOLO-S](#通用目标检测-DAMOYOLO-S)|image-object-detection|damo/cv_tinynas_object-detection_damoyolo|
|[通用目标检测-DAMOYOLO-M](#通用目标检测-DAMOYOLO-M)|image-object-detection|damo/cv_tinynas_object-detection_damoyolo-m|
|[通用目标检测-DAMOYOLO-T](#通用目标检测-DAMOYOLO-T)|image-object-detection|damo/cv_tinynas_object-detection_damoyolo-t|
|[通用目标检测-ViTDet](#通用目标检测-ViTDet)|image-object-detection|damo/cv_vit_object-detection_coco|
|[通用目标检测-AIRDet-S](#通用目标检测-AIRDet-S)|image-object-detection|damo/cv_tinynas_detection|


## 📌通用目标检测-YOLOX-S ##
### 基本信息
本模型基于[YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)模型的small模型训练得到，YOLOX为YOLO检测系列的最近增强版本。在实时通用检测模型中，YOLO系列模型获得显著的进步，大大地推动了社区的发展。
本模型是基于 [COCO2017](https://cocodataset.org/#detection-2017) 训练得到，适用于自然场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_cspnet_image-object-detection_yolox'
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

|Model |size |mAP<sup>val<br>0.5:0.95 |mAP<sup>test<br>0.5:0.95 | Speed V100<br>(ms) | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---: | :---:    | :---:       |:---:     |:---:  | :---: | :----: |
|YOLOX-S    |640  |40.5 |40.5      |9.8      |9.0 | 26.8 | [Official](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth)


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_cspnet_image-object-detection_yolox/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{yolox2021,
  title={{YOLOX}: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```


## 📌通用目标检测-YOLOX-Nano ##
### 基本信息
本模型基于[YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)模型的nano模型训练得到，YOLOX为YOLO检测系列的最近增强版本。在实时通用检测模型中，YOLO系列模型获得显著的进步，大大地推动了社区的发展。
本模型是基于 [COCO2017](https://cocodataset.org/#detection-2017) 训练得到，适用于自然场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_cspnet_image-object-detection_yolox_nano_coco'
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

|Model |size |mAP<sup>val<br>0.5:0.95 | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---:  |  :---:       |:---:     |:---:  | :---: |
| YOLOX-Nano |416  |25.8  | 0.91 |1.08 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_nano.pth) |


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_cspnet_image-object-detection_yolox_nano_coco/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{yolox2021,
  title={{YOLOX}: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```


## 📌通用目标检测-DINO ##
### 基本信息
本模型基于[DINO](https://github.com/alibaba/EasyCV/tree/master/configs/detection/dino)模型训练得到，DINO为DETR系列模型的改进版本。
本模型是基于 [COCO2017](https://cocodataset.org/#detection-2017) 训练得到，适用于自然场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_swinl_image-object-detection_dino'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/dino_trainer.md)和[训练配置样例](../../configs/train/detection/general_object_detection_dino.yaml)，配置文件关键参数作如下修改：

```yaml
adadet_train:
  ...
  model_id: 'damo/cv_swinl_image-object-detection_dino'
  ...
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

| Method | bbox_mAP| AP@0.5 | inference time(V100)| Parameters (backbone/total)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| DINO | 63.39 | 80.25 | 325ms | 195M/218M  |


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_swinl_image-object-detection_dino/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
 @article{zhang2022dino,
      title={DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection},
      author={Hao Zhang and Feng Li and Shilong Liu and Lei Zhang and Hang Su and Jun Zhu and Lionel M. Ni and Heung-Yeung Shum},
      year={2022},
      eprint={2203.03605},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```


## 📌通用目标检测-DAMOYOLO-S ##
### 基本信息
本模型基于[DAMOYOLO](https://github.com/tinyvision/DAMO-YOLO)模型的small模型训练得到，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 [COCO2017](https://cocodataset.org/#detection-2017) 训练得到，适用于自然场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
adadet_train:
  ...
  model_id: 'damo/cv_tinynas_object-detection_damoyolo'
  ...
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

|Model |size |mAP<sup>val<br>0.5:0.95 | Latency(ms)<br>T4-TRT-FP16| FLOPs<br>(G)| Parameters(M)|
| ------        |:---: | :---: |:---:|:---: | :---: |
|YOLOX-S        | 640  | 40.5  | 3.20| 26.8 | 9.0   |
|YOLOv5-S       | 640  | 37.4  | 3.04| 16.5 | 7.2   |
|YOLOv6-S       | 640  | 43.5  | 3.10| 44.2 | 17.0  |
|PP-YOLOE-S     | 640  | 43.0  | 3.21| 17.4 | 7.9   |
|**DAMO-YOLO-S** | 640  | 46.8  | 3.83| 37.8 | 16.3  |

- 表中汇报的mAP是COCO2017 val集上的结果。
- 表中汇报的latency不包括后处理（nms）时间，其测试条件为：T4 GPU，TensorRT=7.2.1.6， CUDA=10.2, CUDNN=8.0.0.1。


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌通用目标检测-DAMOYOLO-M ##
### 基本信息
本模型基于[DAMOYOLO](https://github.com/tinyvision/DAMO-YOLO)模型的medium模型训练得到，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 [COCO2017](https://cocodataset.org/#detection-2017) 训练得到，适用于自然场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo-m'
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

|Model |size |mAP<sup>val<br>0.5:0.95 | Latency(ms)<br>T4-TRT-FP16| FLOPs<br>(G)| Parameters(M)|
| ------        |:---: | :---: |:---:|:---: | :---: |
|YOLOX-M        | 640  | 46.9  | 6.46| 73.8 | 25.3  |
|YOLOv5-M       | 640  | 45.4  | 5.71| 49.0 | 21.2   |
|YOLOv6-M       | 640  | 49.5  | 5.72| 82.2 | 34.3  |
|YOLOv7       | 640  | 51.2  | 9.08| 104.7 | 36.9   |
|PP-YOLOE-M     | 640  | 49.0  | 6.67|49.9 |23.4   |
|**DAMO-YOLO-M** | 640  | 50.0  | 5.62| 61.8 | 28.2  |

- 表中汇报的mAP是COCO2017 val集上的结果。
- 表中汇报的latency不包括后处理（nms）时间，其测试条件为：T4 GPU，TensorRT=7.2.1.6， CUDA=10.2, CUDNN=8.0.0.1。


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo-m/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌通用目标检测-DAMOYOLO-T ##
### 基本信息
本模型基于[DAMOYOLO](https://github.com/tinyvision/DAMO-YOLO)模型的tiny模型训练得到，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 [COCO2017](https://cocodataset.org/#detection-2017) 训练得到，适用于自然场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo-t'
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

|Model |size |mAP<sup>val<br>0.5:0.95 | Latency(ms)<br>T4-TRT-FP16| FLOPs<br>(G)| Parameters(M)|
| ------        |:---: | :---: |:---:|:---: | :---: |
|YOLOX-T | 416  | 32.8  | 1.78| 6.5 | 5.1  |
|YOLOv5-N | 640  | 28.0  | 2.23| 4.5 |1.9  |
|YOLOv5-S | 640  | 37.4  | 3.04| 16.5 | 7.2  |
|YOLOv6-T | 640  | 40.3  | 2.53| 36.7 | 15.0  |
|YOLOv7-T | 640  | 38.7  | 3.13|13.7 | 6.2  |
|**DAMO-YOLO-T** | 640  | 43.0  | 2.78| 18.1 | 8.5  |

- 表中汇报的mAP是COCO2017 val集上的结果。
- 表中汇报的latency不包括后处理（nms）时间，其测试条件为：T4 GPU，TensorRT=7.2.1.6， CUDA=10.2, CUDNN=8.0.0.1。


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo-t/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌通用目标检测-ViTDet ##
### 基本信息
本模型基于[ViTDet](https://arxiv.org/abs/2203.16527)模型训练得到，ViTDet是一个简洁的，没有特征分级的基于ViT的检测框架。
本模型是基于 [COCO2017](https://cocodataset.org/#detection-2017) 训练得到，适用于自然场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_vit_object-detection_coco'
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

| Backbone |  Pretrain   | box mAP | mask mAP |   Remark   |
|:--------:|:-----------:|:-------:|:--------:| ---------- |
| ViT-Base | ImageNet-1k |  51.6   |   45.9   | [official](https://github.com/facebookresearch/detectron2/tree/main/projects/ViTDet) |
| ViT-Base | ImageNet-1k |  51.1   |   45.5   | [unofficial](https://github.com/ViTAE-Transformer/ViTDet) |
| ViT-Base | ImageNet-1k |  51.4   |   45.7   | modelscope |


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_vit_object-detection_coco/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{Li2022ExploringPV,
  title={Exploring Plain Vision Transformer Backbones for Object Detection},
  author={Yanghao Li and Hanzi Mao and Ross B. Girshick and Kaiming He},
  journal={ArXiv},
  year={2022},
  volume={abs/2203.16527}
}
```


## 📌通用目标检测-AIRDet-S ##
### 基本信息
本模型基于AIRDet模型的small模型训练得到，AIRDet-S中使用了引入了Giraffe neck、GFLv2 head、AutoAugmentation等技术，使其在精度上超越了目前的一众YOLO(YOLOX-s, YOLOv6-s, YOLOe-s)，并且仍然保持极高的推理速度。
本模型是基于 [COCO2017](https://cocodataset.org/#detection-2017) 训练得到，适用于自然场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_tinynas_detection'
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

|Model |size |mAP<sup>val<br>0.5:0.95 | Latency V100<br>TRT-FP32-BS32| Latency V100<br>TRT-FP16-BS32| FLOPs<br>(G)| weights |
| ------        |:---: | :---:     |:---:|:---: | :---: | :----: |
|Yolox-S   | 640 | 40.5 | 3.4 | 2.3 | 26.81 | [link]() |
|AIRDet-S | 640 | 44.2 | 4.4 | 2.8 | 27.56 | [link](https://drive.google.com/file/d/119W87oZ4zcJvvjzYCmBudX38cRpZbQc4/view?usp=sharing) |


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_detection/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{jiang2022giraffedet,
  title={GiraffeDet: A Heavy-Neck Paradigm for Object Detection},
  author={Jiang, Yiqi and Tan, Zhiyu and Wang, Junyan and Sun, Xiuyu and Lin, Ming and Li, Hao},
  journal={arXiv preprint arXiv:2202.04256},
  year={2022}
}
@inproceedings{li2021generalized,
  title={Generalized focal loss v2: Learning reliable localization quality estimation for dense object detection},
  author={Li, Xiang and Wang, Wenhai and Hu, Xiaolin and Li, Jun and Tang, Jinhui and Yang, Jian},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={11632--11641},
  year={2021}
}
```
