[简体中文](./face_detection.md) | English
# Face Detection

Supported models:

|model name|task_name|model_id|
|:--:|:--:|:--:|
|[face-detection-keypoint-RetinaFace](#face-detection-keypoint-RetinaFace)|face-detection|damo/cv_resnet50_face-detection_retinaface|
|[face-detection-keypoint-SCRFD](#face-detection-keypoint-SCRFD)|face-detection|damo/cv_resnet_facedetection_scrfd10gkps|
|[face-detection-MogFace](#face-detection-MogFace)|face-detection|damo/cv_resnet101_face-detection_cvpr22papermogface|
|[face-detection-ULFD](#face-detection-ULFD)|face-detection|damo/cv_manual_face-detection_ulfd|
|[face-detection-keypoint-MTCNN](#face-detection-keypoint-MTCNN)|face-detection|damo/cv_manual_face-detection_mtcnn|

## 📌face-detection-keypoint-RetinaFace ##
### Introduction
This model detects the face and corresponding keypoints in the input image. RetinaFace is an accurate two-in-one method of face detection and face keypoint detection, and the paper is accepted by CVPR2020.

This model is trained on Wider Face dataset.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_resnet50_face-detection_retinaface'
```

### Performance
The performance on the WiderFace validation set:
| Method | Easy | Medium | Hard |
| ------------ | ------------ | ------------ | ------------ |
| RetinaFace | 94.8 | 93.8 | 89.6 |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_resnet50_face-detection_retinaface/summary)

### Citations

```BibTeX
@inproceedings{deng2020retinaface,
title={Retinaface: Single-shot multi-level face localisation in the wild},
author={Deng, Jiankang and Guo, Jia and Ververas, Evangelos and Kotsia, Irene and Zafeiriou, Stefanos},
booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
pages={5203--5212},
year={2020}
}
```


## 📌face-detection-keypoint-SCRFD ##
### Introduction
This model detects the face and corresponding keypoints in the input image. The main contribution of SCRFD is to improve the balance between efficiency and accuracy of the detector from two aspects: first, the face size distribution of training data is counted, and more small samples are added to train the shallow stage of the model; Second, simplify the search space, and use the idea of RegNet to search the network structure of backbone, neck and head.

This model is trained on Wider Face dataset.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_resnet_facedetection_scrfd10gkps'
```

### Performance
The performance, model size, and inference time(2080ti GPU) on the WiderFace dataset (VGA resolution):

| Name | Easy | Medium | Hard | FLOPS | Params(M) | Infer(ms) |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |------------ |
| SCRFD_10G_BNKPS | 95.40 | 94.01 | 82.80 | 10G | 4.23 | 5.0|
| SCRFD_34G_GNKPS_v2 | 96.17 | 95.19 | 84.88 | 34G | 9.84 | 11.8|

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_resnet_facedetection_scrfd10gkps/summary)

### Citations

```BibTeX
@article{guo2021sample,
  title={Sample and Computation Redistribution for Efficient Face Detection},
  author={Guo, Jia and Deng, Jiankang and Lattas, Alexandros and Zafeiriou, Stefanos},
  journal={arXiv preprint arXiv:2105.04714},
  year={2021}
}
```


## 📌face-detection-MogFace ##
### Introduction
This model detects the human face in the input image. MogFace is the SOTA face detection method, has topped the list of Wider Face in six categories for more than one year. The paper is accepted by CVPR2022.

This model is trained on Wider Face dataset.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_resnet101_face-detection_cvpr22papermogface'
```

### performance
The performance on the WiderFace validation set:
| Method | Easy | Medium | Hard |
| ------------ | ------------ | ------------ | ------------ |
| MogFace | 97.0 | 96.3 | 93.0 |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_resnet101_face-detection_cvpr22papermogface/summary)

### Citations

```BibTeX
@inproceedings{liu2022mogface,
title={MogFace: Towards a Deeper Appreciation on Face Detection},
author={Liu, Yang and Wang, Fei and Deng, Jiankang and Zhou, Zhipeng and Sun, Baigui and Li, Hao},
booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
pages={4093--4102},
year={2022}
}
```

## 📌face-detection-ULFD ##
### Introduction
This model detects the human face in the input image. ULFD ([code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB)) is a lightweight face detection method. The backbone structure is designed manually based on SSD framework. It is the first 1M face detection model in the open source industry.
This model is trained on Wider Face dataset.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_manual_face-detection_ulfd'
```

### Performance
The performance on the WiderFace validation set:
| Method | Easy | Medium | Hard |
| ------------ | ------------ | ------------ | ------------ |
| ULFD | 85.3 | 81.9 | 53.9 |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_manual_face-detection_ulfd/summary)


## 📌face-detection-keypoint-MTCNN ##
### Introduction
This model detects the human face in the input image. MTCNN is a two-in-one model of face detection and face keypoint detection, which is widely used in industry.
This model is trained on Wider Face dataset.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: True
vis_func: vis_face_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-detection'
  model_id: 'damo/cv_manual_face-detection_mtcnn'
```

### Performance
The performance on the WiderFace validation set:
| Method | Easy | Medium | Hard |
| ------------ | ------------ | ------------ | ------------ |
| MTCNN | 85.1 | 82.0 | 60.7 |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_manual_face-detection_mtcnn/summary)

### Citations

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
