[简体中文](./object_detection.md) | English
# General Object Detection

The current list of supported general object detection models is as follows:

|model name|task_name|model_id|
|:--:|:--:|:--:|
|[general-object-detection-YOLOX-S](#general-object-detection-YOLOX-S)|image-object-detection|damo/cv_cspnet_image-object-detection_yolox|
|[general-object-detection-YOLOX-Nano](#general-object-detection-YOLOX-nano)|image-object-detection|damo/cv_cspnet_image-object-detection_yolox_nano_coco|
|[general-object-detection-DINO](#general-object-detection-DINO)|image-object-detection|damo/cv_swinl_image-object-detection_dino|
|[general-object-detection-DAMOYOLO-S](#general-object-detection-DAMOYOLO-S)|image-object-detection|damo/cv_tinynas_object-detection_damoyolo|
|[general-object-detection-DAMOYOLO-M](#general-object-detection-DAMOYOLO-M)|image-object-detection|damo/cv_tinynas_object-detection_damoyolo-m|
|[general-object-detection-DAMOYOLO-T](#general-object-detection-DAMOYOLO-T)|image-object-detection|damo/cv_tinynas_object-detection_damoyolo-t|
|[general-object-detection-ViTDet](#general-object-detection-ViTDet)|image-object-detection|damo/cv_vit_object-detection_coco|
|[general-object-detection-AIRDet-S](#general-object-detectionAIRDet-S)|image-object-detection|damo/cv_tinynas_detection|


## 📌general-object-detection-YOLOX-S ##
### Introduction
This model is trained based on the small model of the [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) model, the latestenhanced version of the YOLO detection series. In real-time general detection models, YOLO series models have made significant progress, greatly promoting the development of the community. This model is trained based on [COCO2017](https://cocodataset.org/#detection-2017) and is suitable for object detection in natural scenes.


### Inference
The single model inference function can be used for effect experience, and CPU/GPU inference is currently supported. Please refer to the [inference document](../infer/infer_tutorial_EN.md) and [inference configuration sample](../../configs/infer/model_infer.yaml)，please modify the key parameters in the configuration file as follows：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_cspnet_image-object-detection_yolox'
```

### Performance
The performance of the model on the COCO2017 validation set are as follows:

|Model |size |mAP<sup>val<br>0.5:0.95 |mAP<sup>test<br>0.5:0.95 | Speed V100<br>(ms) | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---: | :---:    | :---:       |:---:     |:---:  | :---: | :----: |
|YOLOX-S    |640  |40.5 |40.5      |9.8      |9.0 | 26.8 | [Official](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.pth)


### Demo Links
[ModelCard & Demo Experience](https://modelscope.cn/models/damo/cv_cspnet_image-object-detection_yolox/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
@article{yolox2021,
  title={{YOLOX}: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```


## 📌general-object-detection-YOLOX-nano ##
### Introduction
This model is based on the nano model of the [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) model, which is the latest enhanced version of the YOLO detection series. In real-time general detection models, the YOLO series models have made significant progress, greatly promoting community development.
This model is trained based on [COCO2017](https://cocodataset.org/#detection-2017) and is suitable for natural scene object detection.

### Inference
The single-model inference function can be used for performance experience, and CPU/GPU inference is currently supported. Please refer to the [inference documentation](../infer/infer_tutorial_EN.md)和[inference configuration sample](../../configs/infer/model_infer.yaml)，and modify the key parameters of the configuration file as follows:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_cspnet_image-object-detection_yolox_nano_coco'
```

### Performance
The performance of the model on the validation set of COCO2017 are as follows:

|Model |size |mAP<sup>val<br>0.5:0.95 | Params<br>(M) |FLOPs<br>(G)| weights |
| ------        |:---:  |  :---:       |:---:     |:---:  | :---: |
| YOLOX-Nano |416  |25.8  | 0.91 |1.08 | [github](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_nano.pth) |


### Demo links
[ModelCard & demo experience](https://modelscope.cn/models/damo/cv_cspnet_image-object-detection_yolox_nano_coco/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
@article{yolox2021,
  title={{YOLOX}: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```


## 📌general-object-detection-DINO ##
### Introduction
This model is trained based on the [DINO](https://github.com/alibaba/EasyCV/tree/master/configs/detection/dino) model, which is an improved version of the DETR series model. This model is trained based on [COCO2017](https://cocodataset.org/#detection-2017) and is suitable for object detection in natural scenes.


### Inference
The single-model inference function can be used for performance evaluation. Currently, CPU/GPU inference is supported. Please refer to the[inference document](../infer/infer_tutorial_EN.md)和[inference configuration example](../../configs/infer/model_infer.yaml)，modify the key parameters in the configuration file as follows:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_swinl_image-object-detection_dino'
```

### Training evaluation
The single-model training/evaluation function can be used for fine-tuning and optimizing the model. Refer to the [training documentation](../train/detection/dino_trainer.md)和[training configuration examples](../../configs/train/detection/general_object_detection_dino.yaml)，modify the key parameters in the configuration file as follows：

```yaml
adadet_train:
  ...
  model_id: 'damo/cv_swinl_image-object-detection_dino'
  ...
```

### Performance
The objective metrics of the model on the validation set of COCO2017 are as follows:

| Method | bbox_mAP| AP@0.5 | inference time(V100)| Parameters (backbone/total)|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| DINO | 63.39 | 80.25 | 325ms | 195M/218M  |


### Demo Links
[ModelCard & Demo Experience](https://modelscope.cn/models/damo/cv_swinl_image-object-detection_dino/summary)

### Citations
The main reference papers for this model are as follows:

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


## 📌general-object-detection-DAMOYOLO-S ##
### Introduction
This model is trained based on the[DAMOYOLO](https://github.com/tinyvision/DAMO-YOLO)model's small model. DAMO-YOLOis an object detection framework aimed at industrial applications, balancing model speed and accuracy. Its trained model outperforms the current YOLO series methods while still maintaining high inference speed.
This model is trained based on [COCO2017](https://cocodataset.org/#detection-2017) and is suitable for object detection in natural scenes.


### Inference
The model can be tested using the single-model inference function. It currently supports CPU/GPU inference and can refer to the[inference document](../infer/infer_tutorial_EN.md)和[inference configuration example](../../configs/infer/model_infer.yaml)，The key parameters in the configuration file can be modified as follows:：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo'
```

### Training Evaluation
The single-model training/evaluation function can be used for fine-tuning and optimizing the model. Please refer to the [training document](../train/detection/damoyolo_trainer.md)和[training configuration example](../../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml)，modify the key parameters in the configuration file as follows:

```yaml
adadet_train:
  ...
  model_id: 'damo/cv_tinynas_object-detection_damoyolo'
  ...
```

### Performance
The performance of the model on the COCO2017 validation set are as follows:

|Model |size |mAP<sup>val<br>0.5:0.95 | Latency(ms)<br>T4-TRT-FP16| FLOPs<br>(G)| Parameters(M)|
| ------        |:---: | :---: |:---:|:---: | :---: |
|YOLOX-S        | 640  | 40.5  | 3.20| 26.8 | 9.0   |
|YOLOv5-S       | 640  | 37.4  | 3.04| 16.5 | 7.2   |
|YOLOv6-S       | 640  | 43.5  | 3.10| 44.2 | 17.0  |
|PP-YOLOE-S     | 640  | 43.0  | 3.21| 17.4 | 7.9   |
|**DAMO-YOLO-S** | 640  | 46.8  | 3.83| 37.8 | 16.3  |

- The mAP reported in the table is the result on the COCO2017 validation set.
- The latency reported in the table does not include the post-processing (nms) time. The testing conditions are T4 GPU, TensorRT=7.2.1.6, CUDA=10.2, CUDNN=8.0.0.1.


### Demo links:
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo/summary)

### Citations:
The main reference paper of this model is as follows:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌general-object-detection-DAMOYOLO-M ##
### Introduction
This model is trained based on the medium model of [DAMOYOLO](https://github.com/tinyvision/DAMO-YOLO)，which is an object detection framework designed for industrial applications. It balances model speed and accuracy, and its trained model's performance surpasses that of the current YOLO series methods while still maintaining extremely high inference speed.
This model is trained on [COCO2017](https://cocodataset.org/#detection-2017) and is suitable for object detection in natural scenes。

### Inference
The single-model inference function can be used for performance testing, and currently supports CPU/GPU inference. Please refer to the [inference documentation](../infer/infer_tutorial_EN.md)和[inference configuration examples](../../configs/infer/model_infer.yaml) for corresponding modifications to the key parameters in the configuration file:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo-m'
```

### Performance
The performance of the model on the validation set of COCO2017 are as follows:

|Model |size |mAP<sup>val<br>0.5:0.95 | Latency(ms)<br>T4-TRT-FP16| FLOPs<br>(G)| Parameters(M)|
| ------        |:---: | :---: |:---:|:---: | :---: |
|YOLOX-M        | 640  | 46.9  | 6.46| 73.8 | 25.3  |
|YOLOv5-M       | 640  | 45.4  | 5.71| 49.0 | 21.2   |
|YOLOv6-M       | 640  | 49.5  | 5.72| 82.2 | 34.3  |
|YOLOv7       | 640  | 51.2  | 9.08| 104.7 | 36.9   |
|PP-YOLOE-M     | 640  | 49.0  | 6.67|49.9 |23.4   |
|**DAMO-YOLO-M** | 640  | 50.0  | 5.62| 61.8 | 28.2  |

- The mAP reported in the table is the result on the COCO2017 validation set.
- The latency reported in the table does not include post-processing (nms) time and was tested under the following conditions: T4 GPU, TensorRT=7.2.1.6, CUDA=10.2, CUDNN=8.0.0.1.


### Demo Links
[ModelCard & Demo Experience](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo-m/summary)

### Citations
This model is mainly based on the following papers:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌general-object-detection-DAMOYOLO-T  ##
### Introduction
This model is trained based on the tiny version of[DAMOYOLO](https://github.com/tinyvision/DAMO-YOLO)，DAMO-YOLO is an object detection framework designed for industrial applications, which balances model speed and accuracy. The model trained by DAMOYOLO outperforms current YOLO series methods in terms of model performance and still maintains high inference speed.
This model is trained on [COCO2017](https://cocodataset.org/#detection-2017) dataset and is suitable for detecting objects in natural scenes.


### Inference
Single model inference function can be used to experience the model performance. Currently, CPU/GPU inference is supported. Please refer to the[inference documents](../infer/infer_tutorial_EN.md)和[examples for inference configuration](../../configs/infer/model_infer.yaml). The following key parameters in the configuration file should be modified accordingly

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_tinynas_object-detection_damoyolo-t'
```

### Performance
The performance of the model on the COCO2017 validation set are as follows:

|Model |size |mAP<sup>val<br>0.5:0.95 | Latency(ms)<br>T4-TRT-FP16| FLOPs<br>(G)| Parameters(M)|
| ------        |:---: | :---: |:---:|:---: | :---: |
|YOLOX-T | 416  | 32.8  | 1.78| 6.5 | 5.1  |
|YOLOv5-N | 640  | 28.0  | 2.23| 4.5 |1.9  |
|YOLOv5-S | 640  | 37.4  | 3.04| 16.5 | 7.2  |
|YOLOv6-T | 640  | 40.3  | 2.53| 36.7 | 15.0  |
|YOLOv7-T | 640  | 38.7  | 3.13|13.7 | 6.2  |
|**DAMO-YOLO-T** | 640  | 43.0  | 2.78| 18.1 | 8.5  |

- The mAP reported in the table is the result on the COCO2017 validation set.
- The latency reported in the table does not include post-processing (nms) time, and the testing conditions are: T4 GPU, TensorRT=7.2.1.6, CUDA=10.2, CUDNN=8.0.0.1.


### Demo Links:
[ModelCard & demo experience](https://modelscope.cn/models/damo/cv_tinynas_object-detection_damoyolo-t/summary)

### Citations:
This model is mainly based on the following papers:

```BibTeX
 @article{damoyolo,
  title={DAMO-YOLO: A Report on Real-Time Object Detection Design},
  author={Xianzhe Xu, Yiqi Jiang, Weihua Chen, Yilun Huang, Yuan Zhang and Xiuyu Sun},
  journal={arXiv preprint arXiv:2211.15444v2},
  year={2022}
}
```


## 📌general-object-detection-ViTDet ##
### Introduction:
This model is trained based on the [ViTDet](https://arxiv.org/abs/2203.16527)，which is a simple detection framework based on ViT without feature hierarchy.
This model is trained on [COCO2017](https://cocodataset.org/#detection-2017) and is suitable for object detection in natural scenes.

### Inference:
The single-model inference function can be used for testing the effectiveness. Currently, CPU/GPU inference is supported. Please refer to the[inference document](../infer/infer_tutorial_EN.md) and [example configuration](../../configs/infer/model_infer.yaml)for key parameter modifications in the configuration file:

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_vit_object-detection_coco'
```

### Performance
The performance of the model on the COCO2017 validation set are as follows:

| Backbone |  Pretrain   | box mAP | mask mAP |   Remark   |
|:--------:|:-----------:|:-------:|:--------:| ---------- |
| ViT-Base | ImageNet-1k |  51.6   |   45.9   | [official](https://github.com/facebookresearch/detectron2/tree/main/projects/ViTDet) |
| ViT-Base | ImageNet-1k |  51.1   |   45.5   | [unofficial](https://github.com/ViTAE-Transformer/ViTDet) |
| ViT-Base | ImageNet-1k |  51.4   |   45.7   | modelscope |


### Demo Links
[ModelCard & demo experience](https://modelscope.cn/models/damo/cv_vit_object-detection_coco/summary)

### Citations
The main reference papers for this model are as follows:

```BibTeX
@article{Li2022ExploringPV,
  title={Exploring Plain Vision Transformer Backbones for Object Detection},
  author={Yanghao Li and Hanzi Mao and Ross B. Girshick and Kaiming He},
  journal={ArXiv},
  year={2022},
  volume={abs/2203.16527}
}
```


## 📌general-object-detectionAIRDet-S ##
### Introduction
This model is trained based on the small model of AIRDet, using techniques such as Giraffe Neck, GFLv2 Head, AutoAugmentation, etc., which surpasses the current YOLO models (YOLOX-s, YOLOv6-s, YOLOe-s) in accuracy while maintaining high inference speed. This model is trained based on [COCO2017](https://cocodataset.org/#detection-2017) and is suitable for object detection in natural scenes.

### Inference
You can use the single-model inference function to experience the effect. Currently, CPU/GPU inference is supported. Please refer to the[inference documnet](../infer/infer_tutorial_EN.md)和[inference configuration example](../../configs/infer/model_infer.yaml) for modification of key parameters in the configuration file:：

```yaml
vis_flag: True
vis_func: vis_det_img
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'image-object-detection'
  model_id: 'damo/cv_tinynas_detection'
```

### Performance
The performance of the model on the COCO2017 validation set are as follows:

|Model |size |mAP<sup>val<br>0.5:0.95 | Latency V100<br>TRT-FP32-BS32| Latency V100<br>TRT-FP16-BS32| FLOPs<br>(G)| weights |
| ------        |:---: | :---:     |:---:|:---: | :---: | :----: |
|Yolox-S   | 640 | 40.5 | 3.4 | 2.3 | 26.81 | [link]() |
|AIRDet-S | 640 | 44.2 | 4.4 | 2.8 | 27.56 | [link](https://drive.google.com/file/d/119W87oZ4zcJvvjzYCmBudX38cRpZbQc4/view?usp=sharing) |


### Demo links
[ModelCard & demo experience](https://modelscope.cn/models/damo/cv_tinynas_detection/summary)

### Citations
The main reference papers for this model are as follows:

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
