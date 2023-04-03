简体中文 | [English](./3d_keypoints_EN.md)
# 3D关键点检测

当前支持的3D关键点检测模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[3D人体关键点检测-TPNet](#3D人体关键点检测-TPNet)|body-3d-keypoints|damo/cv_canonical_body-3d-keypoints_video|
|[3D人体关键点检测-HDFormer模型](#3d人体关键点检测-HDFormer)|body-3d-keypoints|damo/cv_hdformer_body-3d-keypoints_video|

## 📌3D人体关键点检测-TPNet ##
### 基本信息
输入一段包含人物的视频，实现端到端的人体关键点检测，输出视频中每一帧图像人体的17点人体3D关键点坐标。
本模型是基于[Human3.6M](http://vision.imar.ro/human3.6m)开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'body-3d-keypoints'
  model_id: 'damo/cv_canonical_body-3d-keypoints_video'
```

可使用的测试数据[视频](https://dmshared.oss-cn-hangzhou.aliyuncs.com/maas/test/video/Walking.54138969.h264.mp4)，可下载后把文件路径填入配置文件进行测试。

### 客观指标
| MPJPE |	 P-MPJPE |	 N-MPJPE |	 MPJVE |
|---|---|---|---|
| 40.400 |	 29.400 	 |37.700 |	 1.900 |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_canonical_body-3d-keypoints_video/summary)

### 相关论文
本模型主要参考论文如下：
```BibTeX
@inproceedings{pavllo2019-3d,
  title = {3D Human Pose Estimation in Video with Temporal Convolutions and Semi-Supervised Training,
  author = {Pavllo, Dario and Feichtenhofer, Christoph and Grangier, David and Auli, Michael},
  year = {2019},
  eprint = {1811.11742},
  doi = {10.48550/arXiv.1811.11742},
}
```

## 📌3D人体关键点检测-HDFormer ##
### 基本信息
输入一段包含人物的视频，实现端到端的人体关键点检测，输出视频中每一帧图像人体的17点人体3D关键点坐标。
本模型HDFormer是一种U-Shape结构的3D人体姿态估计模型，包含3个不同的stage：下采样阶段、上采样阶段和合并阶段。本模型结合了joint<->joint, bone<->joint 和 hyperbone<->joint的特征交互。HDFormer相比于Transformer结构的3D人体姿态估计模型，具有更高的预测精度和推理效率。本模型是基于[Human3.6M](http://vision.imar.ro/human3.6m)开源数据训练得到。


### 模型推理
可使用单模型推理功能进行效果体验，目前支持GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'body-3d-keypoints'
  model_id: 'damo/cv_hdformer_body-3d-keypoints_video'
```

可使用的测试数据[视频](https://dmshared.oss-cn-hangzhou.aliyuncs.com/maas/test/video/Walking.54138969.h264.mp4)，可下载后把文件路径填入配置文件进行测试。

### 客观指标
Human3.6M数据集中客观指标如下：

| MPJPE(mm) |	 2d_gt(T=96) |	 cpn(T=96) |	 hrnet(T=96) |
 |---|---|---|---|
| HDFormer |	 21.6 	 |42.6 |	 40.3 |


### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_hdformer_body-3d-keypoints_video/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{chen2023-hdformer,
  title = {HDFormer: High-order Directed Transformer for 3D Human Pose Estimation},
  author = {Chen, Hanyuan and He, Jun-Yan and Xiang, Wangmeng and Liu, Wei and Cheng, Zhi-Qi and Liu, Hanbing and Luo, Bin and Geng, Yifeng and Xie, Xuansong},
  year = {2023},
  eprint = {2302.01825},
  doi = {10.48550/arXiv.2302.01825},
}
```
