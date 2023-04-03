简体中文 | [English](./face_detection_EN.md)
# 人脸检测

当前支持的人脸检测模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[人脸检测关键点-RetinaFace](#人脸检测关键点-RetinaFace)|face-detection|damo/cv_resnet50_face-detection_retinaface|
|[人脸检测关键点-SCRFD](#人脸检测关键点-SCRFD)|face-detection|damo/cv_resnet_facedetection_scrfd10gkps|
|[人脸检测-MogFace](#人脸检测-MogFace)|face-detection|damo/cv_resnet101_face-detection_cvpr22papermogface|
|[人脸检测-ULFD](#人脸检测-ULFD)|face-detection|damo/cv_manual_face-detection_ulfd|
|[人脸检测关键点-MTCNN](#人脸检测关键点-MTCNN)|face-detection|damo/cv_manual_face-detection_mtcnn|

## 📌人脸检测关键点-RetinaFace ##
### 基本信息
本模型可以检测输入图片中人脸以及对应关键点的位置，RetinaFace为当前学术界和工业界精度较高的人脸检测和人脸关键点定位二合一的方法，被CVPR 2020录取。本模型是基于Wider Face开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_resnet50_face-detection_retinaface'
```

### 客观指标
模型在WiderFace的验证集上客观指标如下：
| Method | Easy | Medium | Hard |
| ------------ | ------------ | ------------ | ------------ |
| RetinaFace | 94.8 | 93.8 | 89.6 |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_resnet50_face-detection_retinaface/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@inproceedings{deng2020retinaface,
title={Retinaface: Single-shot multi-level face localisation in the wild},
author={Deng, Jiankang and Guo, Jia and Ververas, Evangelos and Kotsia, Irene and Zafeiriou, Stefanos},
booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
pages={5203--5212},
year={2020}
}
```


## 📌人脸检测关键点-SCRFD ##
### 基本信息
本模型可以检测输入图片中人脸以及对应关键点的位置，SCRFD的主要贡献是从两处入手提升检测器在效率和精度的平衡：第一，统计训练数据的人脸size分布，在固定分辨率输入下增广更多小样本来训练shallow stage；第二，简化搜索空间，采用RegNet的思路对backbone，neck, head网络结构进行搜索。本模型是基于Wider Face开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_resnet_facedetection_scrfd10gkps'
```

### 客观指标
模型在WIDERFaces数据集(VGA分辨率输入)的评测指标、模型大小、推理耗时(2080ti)如下:

| Name | Easy | Medium | Hard | FLOPS | Params(M) | Infer(ms) |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |------------ |
| SCRFD_10G_BNKPS | 95.40 | 94.01 | 82.80 | 10G | 4.23 | 5.0|
| SCRFD_34G_GNKPS_v2 | 96.17 | 95.19 | 84.88 | 34G | 9.84 | 11.8|

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_resnet_facedetection_scrfd10gkps/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{guo2021sample,
  title={Sample and Computation Redistribution for Efficient Face Detection},
  author={Guo, Jia and Deng, Jiankang and Lattas, Alexandros and Zafeiriou, Stefanos},
  journal={arXiv preprint arXiv:2105.04714},
  year={2021}
}
```


## 📌人脸检测-MogFace ##
### 基本信息
本模型可以检测输入图片中人脸的位置。MogFace为当前SOTA的人脸检测方法，已在Wider Face六项榜单上霸榜一年以上，后续被CVPR2022录取。本模型是基于Wider Face开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_resnet101_face-detection_cvpr22papermogface'
```

### 客观指标
模型在WiderFace的验证集上客观指标如下：
| Method | Easy | Medium | Hard |
| ------------ | ------------ | ------------ | ------------ |
| MogFace | 97.0 | 96.3 | 93.0 |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_resnet101_face-detection_cvpr22papermogface/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@inproceedings{liu2022mogface,
title={MogFace: Towards a Deeper Appreciation on Face Detection},
author={Liu, Yang and Wang, Fei and Deng, Jiankang and Zhou, Zhipeng and Sun, Baigui and Li, Hao},
booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
pages={4093--4102},
year={2022}
}
```

## 📌人脸检测-ULFD ##
### 基本信息
本模型可以检测输入图片中人脸的位置。ULFD([代码地址](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB))为轻量级人脸检测算法, 基于SSD框架手工设计了backbone结构，是业界开源的第一个1M人脸检测模型。本模型是基于Wider Face开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_manual_face-detection_ulfd'
```

### 客观指标
模型在WiderFace的验证集上客观指标如下：
| Method | Easy | Medium | Hard |
| ------------ | ------------ | ------------ | ------------ |
| ULFD | 85.3 | 81.9 | 53.9 |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_manual_face-detection_ulfd/summary)


## 📌人脸检测关键点-MTCNN ##
### 基本信息
本模型可以检测输入图片中人脸的位置。MTCNN是工业界广泛应用的检测关键点二合一模型。本模型是基于Wider Face开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_manual_face-detection_mtcnn'
```

### 客观指标
模型在WiderFace的验证集上客观指标如下：
| Method | Easy | Medium | Hard |
| ------------ | ------------ | ------------ | ------------ |
| MTCNN | 85.1 | 82.0 | 60.7 |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_manual_face-detection_mtcnn/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@inproceedings{xiang2017joint,
title={Joint face detection and facial expression recognition with MTCNN},
author={Xiang, Jia and Zhu, Gengming},
booktitle={2017 4th international conference on information science and control engineering (ICISCE)},
pages={424--427},
year={2017},
organization={IEEE}
}
```
