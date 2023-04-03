[简体中文](./3d_keypoints.md) | English
# 3D Keypoint Detection

Supported models:

|model name|task_name|model_id|
|:--:|:--:|:--:|
|[body-3d-keypoints-TPNet](#body-3d-keypoints-TPNet)|body-3d-keypoints|damo/cv_canonical_body-3d-keypoints_video|
|[body-3d-keypoints-HDFormer](#body-3d-keypoints-HDFormer)|body-3d-keypoints|damo/cv_hdformer_body-3d-keypoints_video|

## 📌body-3d-keypoints-TPNet ##
### Introduction

This is an end-to-end human keypoint detection model, which takes a video as input and output the 3D keypoint detection results (17 keypoints) of each frame. The model is trained on [Human3.6M](http://vision.imar.ro/human3.6m).

### Inference

Please use model infer function to make predictions. Currently, the model suppport both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of configuration file should be modified as below:

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'body-3d-keypoints'
  model_id: 'damo/cv_canonical_body-3d-keypoints_video'
```

The video [here](https://dmshared.oss-cn-hangzhou.aliyuncs.com/maas/test/video/Walking.54138969.h264.mp4) can be used for testing.

### Performance
| MPJPE |    P-MPJPE |   N-MPJPE |   MPJVE |
|---|---|---|---|
| 40.400 |   29.400      |37.700 |   1.900 |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_canonical_body-3d-keypoints_video/summary)

### Citations

```BibTeX
@inproceedings{pavllo2019-3d,
  title = {3D Human Pose Estimation in Video with Temporal Convolutions and Semi-Supervised Training,
  author = {Pavllo, Dario and Feichtenhofer, Christoph and Grangier, David and Auli, Michael},
  year = {2019},
  eprint = {1811.11742},
  doi = {10.48550/arXiv.1811.11742},
}
```

## 📌body-3d-keypoints-HDFormer ##
### Introduction

This is an end-to-end human keypoint detection model, which takes a video as input and output the 3D keypoint detection results (17 keypoints) of each frame. HDFormer is a U-Shape 3D human pose estimation model, which consists of 3 stages: down-sampling stage, up-sampling stage and combine stage. Moreover, HDFormer explores different ways of feature interaction , including: joint<->joint, bone<->joint and hyperbone<->joint. Compared to transformer based methods, HDFormer achieves higher accuracy and efficiency. The model is trained on [Human3.6M](http://vision.imar.ro/human3.6m).

### Inference

Please use model infer function to make predictions. Currently, the model suppport both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of configuration file should be modified as below:

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'body-3d-keypoints'
  model_id: 'damo/cv_hdformer_body-3d-keypoints_video'
```

The video [here](https://dmshared.oss-cn-hangzhou.aliyuncs.com/maas/test/video/Walking.54138969.h264.mp4) can be used for testing.

### Performance

The performance on Human3.6M:

| MPJPE(mm) |    2d_gt(T=96) |   cpn(T=96) |     hrnet(T=96) |
 |---|---|---|---|
| HDFormer |     21.6    |42.6 |     40.3 |


### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_hdformer_body-3d-keypoints_video/summary)

### Citations

```BibTeX
@article{chen2023-hdformer,
  title = {HDFormer: High-order Directed Transformer for 3D Human Pose Estimation},
  author = {Chen, Hanyuan and He, Jun-Yan and Xiang, Wangmeng and Liu, Wei and Cheng, Zhi-Qi and Liu, Hanbing and Luo, Bin and Geng, Yifeng and Xie, Xuansong},
  year = {2023},
  eprint = {2302.01825},
  doi = {10.48550/arXiv.2302.01825},
}
```
