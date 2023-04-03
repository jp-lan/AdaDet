简体中文 | [English](./video_object_detection_EN.md)
# 视频目标检测

当前支持的视频目标检测模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[视频目标检测-StreamYOLO](#视频目标检测-StreamYOLO)|video-object-detection|damo/cv_cspnet_video-object-detection_streamyolo|


## 📌视频目标检测-StreamYOLO ##
### 基本信息
本模型是基于[StreamYOLO](https://github.com/yancie-yjr/StreamYOLO)的实时通用检测模型，支持8类交通目标检测。StreamYOLO基于YOLOX模型，使用Dual-Flow Perception特征融合模块，learns 特征层面的时序关系，提高环境感知预测的能力。与此同时，StreamYOLO设计了一个Trend-Aware Loss 去感知物体运动变化强度，用以加权物体预测的回归，使运动剧烈变化物体获得更高的回归权重，从而获得更好的预测结果。
本模型是基于 Argoverse-HD数据集 训练得到，适用于自动驾驶场景物体检测。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'video-object-detection'
  model_id: 'damo/cv_cspnet_video-object-detection_streamyolo'
```

### 客观指标
模型在Argoverse-HD的验证集上客观指标如下：

|Model |size |velocity | sAP<br>0.5:0.95 | sAP50 |sAP75| weights | COCO pretrained weights |
| ------        |:---: | :---:       |:---:     |:---:  | :---: | :----: | :----: |
|[StreamYOLO-l](https://arxiv.org/pdf/2207.10433.pdf)    |600×960  |1x  |36.9 |58.1| 37.5 |[official](https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth) |[official](https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/yolox_l.pth) |



### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_cspnet_video-object-detection_streamyolo/summary)

### 相关论文
本模型主要参考论文如下：

```BibTeX
@inproceedings{streamyolo,
  title={Real-time Object Detection for Streaming Perception},
  author={Yang, Jinrong and Liu, Songtao and Li, Zeming and Li, Xiaoping and Sun, Jian},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={5385--5395},
  year={2022}
}

@article{yang2022streamyolo,
  title={StreamYOLO: Real-time Object Detection for Streaming Perception},
  author={Yang, Jinrong and Liu, Songtao and Li, Zeming and Li, Xiaoping and Sun, Jian},
  journal={arXiv preprint arXiv:2207.10433},
  year={2022}
}
```
