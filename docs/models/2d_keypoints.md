简体中文 | [English](./2d_keypoints_EN.md)
# 2D关键点检测

当前支持的2D关键点检测模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[2D人体关键点检测-HRNet](#2D人体关键点检测-HRNet)|body-2d-keypoints|damo/cv_hrnetv2w32_body-2d-keypoints_image|
|[2D手部关键点检测-HRNet](#2D手部关键点检测-HRNet)|hand-2d-keypoints|damo/cv_hrnetw18_hand-pose-keypoints_coco-wholebody|
|[2D人脸关键点检测-MobileNetV2](#2D人脸关键点检测-MobileNetV2)|face-2d-keypoints|damo/cv_mobilenet_face-2d-keypoints_alignment|

## 📌2D人体关键点检测-HRNet ##
### 基本信息
输入一张人物图像，实现端到端的人体关键点检测，输出图像中所有人体的15点人体关键点坐标、点位置信度和人体检测框。
本模型是基于COCO/MPII/AI Challenger等开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'body-2d-keypoints'
  model_id: 'damo/cv_hrnetv2w32_body-2d-keypoints_image'
```

### 客观指标
COCO数据集上模型指标：
| Method | 输入大小 | AP | AP50 | AP75 | AR | AR50 |
| ------------ | ------------ | ------------ | ------------ | ------------ |------------ |------------ |
| SimpleBaseline2D | 256x192 | 0.717 | 0.898 | 0.793 | 0.772|0.936|
| HRformer | 256x192 | 0.738 | 0.904 | 0.811 | 0.792 |0.941|
| **HRNET-Ours** | 256x192 | **0.770** | 0.838 | 0.741 |  0.797 |**0.943**|

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_hrnetv2w32_body-2d-keypoints_image/summary)

### 相关论文
本模型主要参考论文如下：
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

## 📌2D手部关键点检测-HRNet ##
### 基本信息
输入一张手部图像，实现端到端的手部关键点检测，输出完整的手部21个关键点。
该模型采用自顶向下的Heatmap手部关键点检测框架，通过端对端的快速推理可以得到图像中的全部手部关键点。 本模型基于HRNetv2和DarkPose方法。本模型是基于[COCO-WholeBody](https://github.com/jin-s13/COCO-WholeBody/)开源数据训练得到。


### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'hand-2d-keypoints'
  model_id: 'damo/cv_hrnetw18_hand-pose-keypoints_coco-wholebody'
```

### 客观指标
COCO-Wholebody数据集上模型指标：

| Method | 输入大小 | PCK | AUC | NME |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| litehrnet_w18 | 256x256 | 0.8161 | 0.8393 | 4.3899 |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_hrnetw18_hand-pose-keypoints_coco-wholebody/summary)

### 相关论文
本模型主要参考论文如下：

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

## 📌2D人脸关键点检测-MobileNetV2 ##
### 基本信息
输入一张人脸图像，实现人脸关键点检测，输出图像中人脸的106点关键点坐标和人像姿态角度。
该模型主要用于人脸关键点检测和对齐任务，从包含人脸的图片中检测出人脸框、人脸关键点坐标和人脸姿态角。
本模型是基于COCO/AI Challenger等开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'face-2d-keypoints'
  model_id: 'damo/cv_mobilenet_face-2d-keypoints_alignment'
```

### 客观指标
模型在自研测试数据集上的评价指标、模型大小、参数量如下：

| 输入大小 | POINTS-ION-NME | POSE-ME | MFLOPS |  PARAMS |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| 96x96 | **0.0981** | **10.5242** | **7.456383** | **0.266427 M** |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_mobilenet_face-2d-keypoints_alignment/summary)

### 相关论文
本模型主要参考论文如下：

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
