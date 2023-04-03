[简体中文](./2d_keypoints.md) | English
# 2D Keypoint Detection

Supported models:

|model name|task_name|model_id|
|:--:|:--:|:--:|
|[body-2d-keypoints-HRNet](#body-2d-keypoints-HRNet)|body-2d-keypoints|damo/cv_hrnetv2w32_body-2d-keypoints_image|
|[hand-2d-keypoints-HRNet](#hand-2d-keypoints-HRNet)|hand-2d-keypoints|damo/cv_hrnetw18_hand-pose-keypoints_coco-wholebody|
|[face-2d-keypoints-MobileNetV2](#face-2d-keypoints-MobileNetV2)|face-2d-keypoints|damo/cv_mobilenet_face-2d-keypoints_alignment|

## 📌body-2d-keypoints-HRNet ##
### Introduction
This model performs end-to-end 2D body keypoint detection, which outputs the confidence score, bounding box, and the corresponding 15 body keypoints of each person.
This model is trained on datasets, such as COCO/MPII/AI Challenger.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'body-2d-keypoints'
  model_id: 'damo/cv_hrnetv2w32_body-2d-keypoints_image'
```

### Performance
The performance on the COCO dataset:
| Method | Input Resolution | AP | AP50 | AP75 | AR | AR50 |
| ------------ | ------------ | ------------ | ------------ | ------------ |------------ |------------ |
| SimpleBaseline2D | 256x192 | 0.717 | 0.898 | 0.793 | 0.772|0.936|
| HRformer | 256x192 | 0.738 | 0.904 | 0.811 | 0.792 |0.941|
| **HRNET-Ours** | 256x192 | **0.770** | 0.838 | 0.741 |  0.797 |**0.943**|

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_hrnetv2w32_body-2d-keypoints_image/summary)

### Citations

```BibTeX
@inproceedings{cheng2020bottom,
  title={HigherHRNet: Scale-Aware Representation Learning for Bottom-Up Human Pose Estimation},
  author={Bowen Cheng and Bin Xiao and Jingdong Wang and Honghui Shi and Thomas S. Huang and Lei Zhang},
  booktitle={CVPR},
  year={2020}
}

@inproceedings{SunXLW19,
  title={Deep High-Resolution Representation Learning for Human Pose Estimation},
  author={Ke Sun and Bin Xiao and Dong Liu and Jingdong Wang},
  booktitle={CVPR},
  year={2019}
}

@article{wang2019deep,
  title={Deep High-Resolution Representation Learning for Visual Recognition},
  author={Wang, Jingdong and Sun, Ke and Cheng, Tianheng and Jiang, Borui and Deng, Chaorui and Zhao, Yang and Liu, Dong and Mu, Yadong and Tan, Mingkui and Wang, Xinggang and Liu, Wenyu and Xiao, Bin},
  journal={TPAMI},
  year={2019}
}
```

## 📌hand-2d-keypoints-HRNet ##
### Introduction
This model performs end-to-end 2D hand keypoint detection, which outputs 21 hand keypoints. A top-down heatmap framework for hand keypoints detection is adopted. The model is based on HRNetv2 and DarkPose methods.
This model is trained on [COCO-WholeBody](https://github.com/jin-s13/COCO-WholeBody/) dataset.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'hand-2d-keypoints'
  model_id: 'damo/cv_hrnetw18_hand-pose-keypoints_coco-wholebody'
```

### Performance
The performance on the COCO-Wholebody dataset:
| Method | Input Resolution | PCK | AUC | NME |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| litehrnet_w18 | 256x256 | 0.8161 | 0.8393 | 4.3899 |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_hrnetw18_hand-pose-keypoints_coco-wholebody/summary)

### Citations

```BibTeX
@article{WangSCJDZLMTWLX19,
  title={Deep High-Resolution Representation Learning for Visual Recognition},
  author={Jingdong Wang and Ke Sun and Tianheng Cheng and
          Borui Jiang and Chaorui Deng and Yang Zhao and Dong Liu and Yadong Mu and
          Mingkui Tan and Xinggang Wang and Wenyu Liu and Bin Xiao},
  journal={TPAMI},
  year={2019}
}
@inproceedings{zhang2020distribution,
  title={Distribution-aware coordinate representation for human pose estimation},
  author={Zhang, Feng and Zhu, Xiatian and Dai, Hanbin and Ye, Mao and Zhu, Ce},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={7093--7102},
  year={2020}
}
```

## 📌face-2d-keypoints-MobileNetV2 ##
### Introduction

This model performs face keypoints detection, which outputs 106 keypoints and the angle of each face in the input image. The model is mainly used for face key point detection and face alignment tasks.
This model is trained on datasets, such as COCO and AI Challenger.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-2d-keypoints'
  model_id: 'damo/cv_mobilenet_face-2d-keypoints_alignment'
```

### Performance
The performance and model details on the private dataset:

| Input Resolution | POINTS-ION-NME | POSE-ME | MFLOPS |  PARAMS |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| 96x96 | **0.0981** | **10.5242** | **7.456383** | **0.266427 M** |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_mobilenet_face-2d-keypoints_alignment/summary)

### Citations

```BibTeX
@article{howard2017mobilenets,
  title={Mobilenets: Efficient convolutional neural networks for mobile vision applications},
  author={Howard, Andrew G and Zhu, Menglong and Chen, Bo and Kalenichenko, Dmitry and Wang, Weijun and Weyand, Tobias and Andreetto, Marco and Adam, Hartwig},
  journal={arXiv preprint arXiv:1704.04861},
  year={2017}
}

@inproceedings{sandler2018mobilenetv2,
  title={Mobilenetv2: Inverted residuals and linear bottlenecks},
  author={Sandler, Mark and Howard, Andrew and Zhu, Menglong and Zhmoginov, Andrey and Chen, Liang-Chieh},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={4510--4520},
  year={2018}
}
```
