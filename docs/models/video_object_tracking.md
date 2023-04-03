简体中文 | [English](./video_object_tracking_EN.md)
# 视频目标跟踪

当前支持的视频目标跟踪模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[视频多目标跟踪-FairMOT](#视频多目标跟踪-FairMOT)|video-multi-object-tracking|damo/cv_yolov5_video-multi-object-tracking_fairmot|

## 📌视频多目标跟踪-FairMOT ##
### 基本信息
多目标跟踪算法通常由目标检测和目标重识别两个模块构成，本模型基于FairMOT算法，在单个网络中同时完成目标检测和重识别模块，可满足实时性要求。
本模型是基于[CrowdHuman](https://www.crowdhuman.org/)/[MIX](https://github.com/Zhongdao/Towards-Realtime-MOT/blob/master/DATASET_ZOO.md)/[MOT17](https://motchallenge.net/data/MOT17/)开源数据训练得到，适用于视频多目标跟踪行人场景，目前在2DMOT15数据集达到SOTA，在MOT16, MOT17, MOT20数据集上达到不错的效果。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'video-multi-object-tracking'
  model_id: 'damo/cv_yolov5_video-multi-object-tracking_fairmot'
```

### 客观指标
模型在MOT17的测试集集上客观指标如下：
| Method    |  MOTA |
|--------------|-----------|
|FairMOT  | 68.5 |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_yolov5_video-multi-object-tracking_fairmot/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@article{zhang2021fairmot,
  title={Fairmot: On the fairness of detection and re-identification in multiple object tracking},
  author={Zhang, Yifu and Wang, Chunyu and Wang, Xinggang and Zeng, Wenjun and Liu, Wenyu},
  journal={International Journal of Computer Vision},
  volume={129},
  pages={3069--3087},
  year={2021},
  publisher={Springer}
}
```
