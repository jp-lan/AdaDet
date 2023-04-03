简体中文 | [English](./domain_specific_object_detection_EN.md)
# 垂类目标检测

当前支持的垂类目标检测模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[人体检测-DAMOYOLO](#人体检测-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_human-detection_damoyolo|
|[人头检测-DAMOYOLO](#人头检测-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_head-detection_damoyolo|
|[手部检测-YOLOX-PAI](#手部检测-YOLOX-PAI)|domain-specific-object-detection|damo/cv_yolox-pai_hand-detection|
|[口罩检测-DAMOYOLO](#口罩检测-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_facemask|
|[安全帽检测-DAMOYOLO](#安全帽检测-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_safety-helmet|
|[香烟检测-DAMOYOLO](#香烟检测-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_cigarette|
|[手机检测-DAMOYOLO](#手机检测-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_phone|
|[交通标识检测-DAMOYOLO](#交通标识检测-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_traffic_sign|
|[车辆检测-YOLOX-PAI](#车辆检测-YOLOX-PAI)|image-object-detection|damo/cv_yolox_image-object-detection-auto|
|[烟火检测-DAMOYOLO](#烟火检测-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_smokefire|

## 📌人体检测-DAMOYOLO ##
### 基本信息
本模型为实时人体检测模型，基于[DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO)模型，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 [COCO2017人体数据](https://cocodataset.org/#detection-2017)/[Object365人体数据](http://www.objects365.org/overview.html)/内部积累数据 训练得到，适用于自然场景人体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_human-detection_damoyolo'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_human-detection_damoyolo'
  ...
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

| Method | AP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.837 | 3.83 | 37.8 | 16.3  |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary)

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


## 📌人头检测-DAMOYOLO ##
### 基本信息
本模型为实时人头检测模型，基于[DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO)模型，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 [Safety Helmet Wearing Dataset (SHWD)人头数据](https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset)/内部积累数据 训练得到，适用于自然场景人头检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_head-detection_damoyolo'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_head-detection_damoyolo'
  ...
```

### 客观指标
模型在SHWD的验证集上客观指标如下：

| Method | AP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.934 | 3.83 | 37.8 | 16.3  |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_head-detection_damoyolo/summary)

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


## 📌手部检测-YOLOX-PAI ##
### 基本信息
本模型为实时手部检测模型，基于[YOLOX-PAI](https://github.com/alibaba/EasyCV/blob/master/docs/source/tutorials/yolox.md)模型，YOLOX-PAI是一个面向工业落地的目标检测框架，是对[YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)的改进升级版本。
本模型是基于 COCO-HAND_Big/TV_HAND 训练得到，适用于自然场景手部检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_yolox-pai_hand-detection'
```

### 客观指标
模型在公开测试数据集上的评价指标、模型大小、参数量如下：

| 输入大小 | AR@1 | AR@10 | AR@100 |  AR@100 (small) | AR@100(medium) | AR@100(large) |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| 640x640x3 | **0.2454** | **0.4295** | **0.4334** | **0.3884** | **0.5154** | **0.4978** |

| 输入大小 | mAP | mAP@.50IOU | mAP@.75IOU |  mAP (small) | mAP (medium) | mAP(large) |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| 640x640x3 | **0.3526** | **0.7294** | **0.3035** | **0.3002** | **0.4414** | **0.4218** |


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_yolox-pai_hand-detection/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{DBLP:journals/corr/abs-2208-13040,
  title     = {YOLOX-PAI: An Improved YOLOX Version by PAI[J]},
  author    = {Zou X, Wu Z, Zhou W, et al.},
  journal   = {arXiv preprint arXiv:2208.13040},
  year      = {2022}
}
```


## 📌口罩检测-DAMOYOLO ##
### 基本信息
本模型为实时口罩检测模型，基于[DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO)模型，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 [FaceMaskDetection口罩数据](https://github.com/AIZOOTech/FaceMaskDetection)/内部积累数据 训练得到，适用于自然场景口罩检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_facemask'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_facemask'
  ...
```

### 客观指标
模型在FaceMaskDetection的验证集上客观指标如下：

| Method | mAP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.932 | 3.83 | 37.8 | 16.3  |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_facemask/summary)

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


## 📌安全帽检测-DAMOYOLO ##
### 基本信息
本模型为实时安全帽检测模型，基于[DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO)模型，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 [Safety Helmet Wearing Dataset (SHWD)安全帽数据](https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset)/内部积累数据 训练得到，适用于自然场景安全帽检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_safety-helmet'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_safety-helmet'
  ...
```

### 客观指标
模型在SHWD的验证集上客观指标如下：

| Method | mAP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.935 | 3.83 | 37.8 | 16.3  |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_safety-helmet/summary)

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


## 📌香烟检测-DAMOYOLO ##
### 基本信息
本模型为实时香烟检测模型，基于[DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO)模型，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 内部积累数据 训练得到，适用于自然场景香烟检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_cigarette'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_cigarette'
  ...
```

### 客观指标
模型在cigarette-internal的验证集上客观指标如下：

| Method | AP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.770 | 3.83 | 37.8 | 16.3  |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_cigarette/summary)

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

## 📌手机检测-DAMOYOLO ##
### 基本信息
本模型为实时手机检测模型，基于[DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO)模型，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 内部积累数据 训练得到，适用于自然场景手机检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_phone'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_phone'
  ...
```

### 客观指标
模型在phone-internal的验证集上客观指标如下：

| Method | AP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.888 | 3.83 | 37.8 | 16.3  |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_phone/summary)

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


## 📌交通标识检测-DAMOYOLO ##
### 基本信息
本模型为实时交通标识检测模型，基于[DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO)模型，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是基于 [BDD100K数据](https://www.bdd100k.com/) 训练得到，适用于自动驾驶场景交通标识检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_traffic_sign'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_traffic_sign'
  ...
```

### 客观指标
模型在BDD100K的验证集上客观指标如下：

| Method | mAP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.665 | 3.83 | 37.8 | 16.3  |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_traffic_sign/summary)

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


## 📌车辆检测-YOLOX-PAI ##
### 基本信息
本模型为实时车辆检测模型，基于[YOLOX-PAI](https://github.com/alibaba/EasyCV/blob/master/docs/source/tutorials/yolox.md)模型，YOLOX-PAI是一个面向工业落地的目标检测框架，是对[YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)的改进升级版本。
本模型是基于 Waymo/Nuimage100K/BDD100K 训练得到，适用于自动驾驶场景车辆检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_yolox_image-object-detection-auto'
```

### 客观指标
模型在COCO2017的验证集上客观指标如下：

|Model |size |mAP<sup>val<br>0.5:0.95 | Speed V100<br>(ms) fp16 bs32 | Params<br>(M) |FLOPs<br>(G)|
| ------        |:---:  | :---:       |:---:     |:---:  | :---: |
| YOLOX-PAI   |640  |43.9 |1.15      |23.7 | 49.9 |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_yolox_image-object-detection-auto/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{DBLP:journals/corr/abs-2208-13040,
  title     = {YOLOX-PAI: An Improved YOLOX Version by PAI[J]},
  author    = {Zou X, Wu Z, Zhou W, et al.},
  journal   = {arXiv preprint arXiv:2208.13040},
  year      = {2022}
}
```


## 烟火检测-DAMOYOLO ##
### 基本信息
本模型为实时烟火检测模型模型，基于[DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO)模型，DAMO-YOLO是一个面向工业落地的目标检测框架，兼顾模型速度与精度，其训练的模型效果超越了目前的一众YOLO系列方法，并且仍然保持极高的推理速度。
本模型是适用于烟火场景检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'cv_tinynas_object-detection_damoyolo_smokefire'
```

### 训练评估
可使用单模型训练/评估功能进行模型的微调优化，可以参考[训练文档](../train/detection/damoyolo_trainer.md)和[训练配置样例](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，配置文件关键参数作如下修改：

```yaml
train:
  ...
  model:
    model_id: 'cv_tinynas_object-detection_damoyolo_smokefire'
  ...
```

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_smokefire/summary)

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
