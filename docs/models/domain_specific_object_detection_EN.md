[简体中文](./domain_specific_object_detection.md) | English
# Domain Specific Object Detection

The current list of supported domain-specific object detection models is as follows:

|model Name|task_name|model_id|
|:--:|:--:|:--:|
|[human-detection-DAMOYOLO](#human-detection-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_human-detection_damoyolo|
|[head-detection-DAMOYOLO](#head-detection-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_head-detection_damoyolo|
|[hand-detection-YOLOX-PAI](#hand-detection-YOLOX-PAI)|domain-specific-object-detection|damo/cv_yolox-pai_hand-detection|
|[facemask-detection-DAMOYOLO](#facemask-detection-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_facemask|
|[safety-helmet-detection-DAMOYOLO](#safety-helmet-detection-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_safety-helmet|
|[cigarette-detection-DAMOYOLO](#cigarette-detection-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_cigarette|
|[phone-detection-DAMOYOLO](#phone-detection-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_phone|
|[traffic-sign-detection-DAMOYOLO](#traffic-sign-detection-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_traffic_sign|
|[vehicle-detection-YOLOX-PAI](#vehicle-detection-YOLOX-PAI)|image-object-detection|damo/cv_yolox_image-object-detection-auto|
|[smokefire-detection-DAMOYOLO](#smokefire-detection-DAMOYOLO)|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_smokefire|


## 📌human-detection-DAMOYOLO ##
### Introduction
This model is a real-time human detection model based on the [DAMO-YOLO-S](https://github.com/tinyvision/DAMO-YOLO) framework, which is a target detection framework designed for industrial applications. The model balances both speed and accuracy, and has achieved better detection results than other YOLO-based methods while still maintaining high inference speed. The model was trained on the [COCO2017 human dataset](https://cocodataset.org/#detection-2017), the [Object365 human dataset](http://www.objects365.org/overview.html), and internal accumulated data, and is suitable for human detection in natural scenes.

### Inference
You can use the single-model inference function for performance testing. The model supports CPU/GPU inference, and you can refer to the [inference documentation](../infer/infer_tutorial_EN.md) and the [inference configuration sample](../../configs/infer/model_infer.yaml) to modify the following key parameters in the configuration file:


```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_human-detection_damoyolo'
```

### Train/Eval
You can use the single-model training/evaluation function for fine-tuning the model. You can refer to the [training documentation](../train/detection/damoyolo_trainer_EN.md) and the [training configuration sample](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) to modify the following key parameters in the configuration file:


```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_human-detection_damoyolo'
  ...
```

### Performance
The model achieves the following objective metrics on the COCO2017 validation set:

| Method | AP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.837 | 3.83 | 37.8 | 16.3  |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary)

### Citations
The main reference paper for this model is:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌head-detection-DAMOYOLO ##
### Introduction
This model is a real-time head detection model based on the [DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO) model. DAMO-YOLO is an industrial-grade object detection framework that balances model speed and accuracy. The model trained by DAMO-YOLO surpasses various YOLO methods currently and still maintains high inference speed. This model is trained on the [Safety Helmet Wearing Dataset (SHWD)](https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset)/internal accumulated data and is suitable for head detection in natural scenes.

### Inference
The single-model inference function can be used to experience the effect of the model. CPU/GPU inference is currently supported. Please refer to the [Inference Document](../infer/infer_tutorial_EN.md) and [Inference Configuration Example](../../configs/infer/model_infer.yaml). The key parameters in the configuration file are modified as follows:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_head-detection_damoyolo'
```

### Train/Eval
The single-model training/evaluation function can be used for fine-tuning and optimization of the model. Please refer to the [Training Document](../train/detection/damoyolo_trainer_EN.md) and [Training Configuration Example](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml). The key parameters in the configuration file are modified as follows:

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_head-detection_damoyolo'
  ...
```

### Performance
The model achieves the following objective metrics on the SHWD validation set:

| Method | AP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.934 | 3.83 | 37.8 | 16.3  |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_tinynas_head-detection_damoyolo/summary)

### Citations
The main reference paper for this model is:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌hand-detection-YOLOX-PAI ##
### Introduction
This model is a real-time hand detection model based on the [YOLOX-PAI](https://github.com/alibaba/EasyCV/blob/master/docs/source/tutorials/yolox_EN.md) model. YOLOX-PAI is an industrial-level object detection framework that is an improved and upgraded version of [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX). This model is trained on the COCO-HAND_Big/TV_HAND dataset and is suitable for hand detection in natural scenes.


### Inference
The model can be used for single-model inference, which currently supports CPU/GPU inference. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Examples](../../configs/infer/model_infer.yaml) for details on how to modify the configuration file as follows:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_yolox-pai_hand-detection'
```

### Performance
The evaluation metrics, model size, and number of parameters of the model on the public test dataset are as follows:

| Input Size | AR@1 | AR@10 | AR@100 |  AR@100 (small) | AR@100(medium) | AR@100(large) |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| 640x640x3 | **0.2454** | **0.4295** | **0.4334** | **0.3884** | **0.5154** | **0.4978** |

| Input Size | mAP | mAP@.50IOU | mAP@.75IOU |  mAP (small) | mAP (medium) | mAP(large) |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| 640x640x3 | **0.3526** | **0.7294** | **0.3035** | **0.3002** | **0.4414** | **0.4218** |


### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_yolox-pai_hand-detection/summary)

### Citations
The main reference paper for this model is as follows:

```BibTeX
@article{DBLP:journals/corr/abs-2208-13040,
  title     = {YOLOX-PAI: An Improved YOLOX Version by PAI[J]},
  author    = {Zou X, Wu Z, Zhou W, et al.},
  journal   = {arXiv preprint arXiv:2208.13040},
  year      = {2022}
}
```


## 📌facemask-detection-DAMOYOLO ##
### Introduction
This model is a real-time face mask detection model based on the [DAMO-YOLO-S](https://github.com/tinyvision/DAMO-YOLO) framework, which is designed for industrial application and balances model speed and accuracy. The trained model surpasses other YOLO-based methods in terms of performance while maintaining high inference speed. The model was trained on the [FaceMaskDetection dataset](https://github.com/AIZOOTech/FaceMaskDetection) as well as internal data and is suitable for face mask detection in natural scenes.


### Inference
The single-model inference feature can be used to experience the effect of the model, and CPU/GPU inference is currently supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Example](../../configs/infer/model_infer.yaml) for key parameter modifications, as shown below:


```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_facemask'
```

### Train/Eval
The single-model training/evaluation feature can be used to fine-tune and optimize the model. Please refer to the [Training Documentation](../train/detection/damoyolo_trainer_EN.md) and [Training Configuration Example](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) for key parameter modifications, as shown below:


```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_facemask'
  ...
```

### Performance
The model achieved the following objective metrics on the FaceMaskDetection validation set:

| Method | mAP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.932 | 3.83 | 37.8 | 16.3  |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_facemask/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌safety-helmet-detection-DAMOYOLO ##
### Introduction
This model is a real-time safety helmet detection model based on the [DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO) framework, which is designed for industrial application and balances model speed and accuracy. The trained model surpasses other YOLO-based methods in terms of performance while maintaining high inference speed. The model was trained on the [Safety Helmet Wearing Dataset (SHWD)](https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset) as well as internal data and is suitable for face mask detection in natural scenes.

### Inference
The single-model inference feature can be used to experience the effect of the model, and CPU/GPU inference is currently supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Example](../../configs/infer/model_infer.yaml) for key parameter modifications, as shown below:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_safety-helmet'
```

### Train/Eval
The single-model training/evaluation feature can be used to fine-tune and optimize the model. Please refer to the [Training Documentation](../train/detection/damoyolo_trainer_EN.md) and [Training Configuration Example](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) for key parameter modifications, as shown below:


```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_safety-helmet'
  ...
```

### Performance
The model achieved the following objective metrics on the SHWD validation set:


| Method | mAP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.935 | 3.83 | 37.8 | 16.3  |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_safety-helmet/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌cigarette-detection-DAMOYOLO ##
### Introduction
This model is a real-time cigarette detection model based on the [DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO) framework, which is designed for industrial application and balances model speed and accuracy. The trained model surpasses other YOLO-based methods in terms of performance while maintaining high inference speed. The model was trained on internal data and is suitable for face mask detection in natural scenes.


### Inference
The single-model inference feature can be used to experience the effect of the model, and CPU/GPU inference is currently supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Example](../../configs/infer/model_infer.yaml) for key parameter modifications, as shown below:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_cigarette'
```

### Train/Eval
The single-model training/evaluation feature can be used to fine-tune and optimize the model. Please refer to the [Training Documentation](../train/detection/damoyolo_trainer_EN.md) and [Training Configuration Example](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) for key parameter modifications, as shown below:

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_cigarette'
  ...
```

### Performance
The model achieved the following objective metrics on the cigarette-internal validation set:

| Method | AP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.770 | 3.83 | 37.8 | 16.3  |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_cigarette/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```

## 📌phone-detection-DAMOYOLO ##
### Introduction
This model is a real-time phone detection model based on the [DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO) framework, which is designed for industrial application and balances model speed and accuracy. The trained model surpasses other YOLO-based methods in terms of performance while maintaining high inference speed. The model was trained on internal data and is suitable for face mask detection in natural scenes.

### Inference
The single-model inference feature can be used to experience the effect of the model, and CPU/GPU inference is currently supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Example](../../configs/infer/model_infer.yaml) for key parameter modifications, as shown below:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_phone'
```

### Train/Eval
The single-model training/evaluation feature can be used to fine-tune and optimize the model. Please refer to the [Training Documentation](../train/detection/damoyolo_trainer_EN.md) and [Training Configuration Example](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) for key parameter modifications, as shown below:

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_phone'
  ...
```

### Performance
The model achieved the following objective metrics on the FaceMaskDetection validation set:

| Method | AP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.888 | 3.83 | 37.8 | 16.3  |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_phone/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌traffic-sign-detection-DAMOYOLO ##
### Introduction
This model is a real-time traffic sign detection model based on the [DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO) framework, which is designed for industrial application and balances model speed and accuracy. The trained model surpasses other YOLO-based methods in terms of performance while maintaining high inference speed. The model was trained on the [BDD100K dataset](https://www.bdd100k.com/) and is suitable for face mask detection in natural scenes.

### Inference
The single-model inference feature can be used to experience the effect of the model, and CPU/GPU inference is currently supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Example](../../configs/infer/model_infer.yaml) for key parameter modifications, as shown below:


```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo_traffic_sign'
```

### Train/Eval
The single-model training/evaluation feature can be used to fine-tune and optimize the model. Please refer to the [Training Documentation](../train/detection/damoyolo_trainer_EN.md) and [Training Configuration Example](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) for key parameter modifications, as shown below:

```yaml
train:
  ...
  model:
    model_id: 'damo/cv_tinynas_object-detection_damoyolo_traffic_sign'
  ...
```

### Performance
The model achieved the following objective metrics on the FaceMaskDetection validation set:

| Method | mAP@0.5 | Latency(ms)<br>T4-TRT-FP16| FLOPs (G)| Parameters (M)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| **DAMO-YOLO-S** | 0.665 | 3.83 | 37.8 | 16.3  |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_traffic_sign/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌vehicle-detection-YOLOX-PAI ##
### Introduction
This model is a real-time vehicle detection model based on the [YOLOX-PAI](https://github.com/alibaba/EasyCV/blob/master/docs/source/tutorials/yolox_EN.md) model. YOLOX-PAI is an industrial-grade object detection framework, which is an improved and upgraded version of [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX).
This model is trained on Waymo/Nuimage100K/BDD100K and is suitable for vehicle detection in autonomous driving scenarios.

### Inference
The single-model inference feature can be used to experience the effect of the model, and CPU/GPU inference is currently supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Example](../../configs/infer/model_infer.yaml) for key parameter modifications, as shown below:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_yolox_image-object-detection-auto'
```

### Performance
The model achieved the following objective metrics on the FaceMaskDetection validation set:

|Model |size |mAP<sup>val<br>0.5:0.95 | Speed V100<br>(ms) fp16 bs32 | Params<br>(M) |FLOPs<br>(G)|
| ------        |:---:  | :---:       |:---:     |:---:  | :---: |
| YOLOX-PAI   |640  |43.9 |1.15      |23.7 | 49.9 |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_yolox_image-object-detection-auto/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
@article{DBLP:journals/corr/abs-2208-13040,
  title     = {YOLOX-PAI: An Improved YOLOX Version by PAI[J]},
  author    = {Zou X, Wu Z, Zhou W, et al.},
  journal   = {arXiv preprint arXiv:2208.13040},
  year      = {2022}
}
```

## 📌smokefire-detection-DAMOYOLO ##
### Introduction
This model is a real-time smokefire detection model based on the [DAMOYOLO-S](https://github.com/tinyvision/DAMO-YOLO) framework, which is designed for industrial application and balances model speed and accuracy. The trained model surpasses other YOLO-based methods in terms of performance while maintaining high inference speed.
The model is suitable for smokefire detection.

### Inference
The single-model inference feature can be used to experience the effect of the model, and CPU/GPU inference is currently supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Example](../../configs/infer/model_infer.yaml) for key parameter modifications, as shown below:


```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'cv_tinynas_object-detection_damoyolo_smokefire'
```

### Train/Eval
The single-model training/evaluation feature can be used to fine-tune and optimize the model. Please refer to the [Training Documentation](../train/detection/damoyolo_trainer_EN.md) and [Training Configuration Example](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml) for key parameter modifications, as shown below:

```yaml
train:
  ...
  model:
    model_id: 'cv_tinynas_object-detection_damoyolo_smokefire'
  ...
```

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo_smokefire/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```
