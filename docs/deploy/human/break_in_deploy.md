简体中文 | [English](./break_in_deploy_EN.md)
# 人员闯入场景解决方案
此解决方案采用了人体检测和闯入区域判断模块实现闯入行为检测。
## 解决方案介绍
解决方案整体流程图如下：

<img src='../../assets/break_in_pipeline.jpg' width=700>

整个解决方案使用了的人体算法基于[DAMOYOLO](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary)进行人体检测，获得人体检测结果后会经过[区域闯入模块](../../adadet/deploy/break_in_det_deploy.py)实现区域闯入判断功能。
## 配置文件
人员闯入解决方案可以通过[配置文件](../../../configs/deploy/human//break_in_det_deploy.yaml)进行参数配置，主要配置参数说明如下：
```yaml
input_path:
  'test/data/videos/MOT17-03-partial.mp4'

output_path:
  ./deploy_res

vis_flag:
  True

adadet_deploy:
  type: BreakInDet
  model_id: 'damo/cv_tinynas_human-detection_damoyolo'
  rules:
    is_video: True
    region_polygon: [[710, 0],[1172,0],[1638,1080],[805, 1080]]
    frame_rate: 5
    det_thres: 0.5
```

### 参数说明

对配置文件中的参数说明如下：

- `input_path` (str): 输入视频路径。
- `output_path` (str): 输出目录路径，存放推理结果、可视化结果等文件。
- `vis_flag` (bool): 输入对检测结果进行可视化。
- `deploy`: 解决方案主要配置参数部分
- `type` (str): 方案的类别名称，无需改动。
- `model_id` (str): 人体检测模型对应的ModelScope模型id。
    + `rules`: 人员闯入检测规则
        * `is_video` (bool): 输入是否为视频。
        * `region_polygon` (list): 闯入区域多边形规则区域，需要大于等于3个坐标点，并且3个点不在同一直线上。
        * `frame_rate` (int): 抽帧的检测，只有在`is_video==True`时生效，比如：5表示间隔5帧抽取一帧进行处理。
        * `det_thres` (float): 人体检测置信度阈值，只有大于等于该阈值时，判定为人体。


### 返回结果

解决方案返回结果的格式如下：

```python

{
    0: { # 第0帧的检测结果，如果输入为图片，只有第0帧结果
          "scores": [float, float, ...], # 每个检测结果的置信度
          "labels": [str, str, ...], # 每个检测结果的类别
          "boxes": [[float, float, float, float], ...] # 每个检测结果的坐标信息，[x1, y1, x2, y2]
          "alarms": [[bool, bool, bool, bool], ...] # 每个人体检测框是否在规则区域里面，是则为True，否则为False
        }
    },
    1: {
        ...
    },
    ...
}

```


## 性能评估
该解决方案在NVIDIA V100 GPU(16G)、32 core Xeon CPU上性能如下表：

| 场景化方案名称 | 每帧使用耗时 | 模型体积 |
| :---: | :---: | :---: |
| 人员闯入 | 71.24ms | 130M |


## ⚡️快速开始
使用下面命令可快速跑通该解决方案：
```python
python tools/deploy.py --config configs/deploy/human/break_in_det_deploy.yaml
```

## 二次开发
本场景化方案中，支持二次开发（单模型训练）的模型为：

1. 人体检测模型，具体的二次开发流程可参考对应的[训练文档](../../train/detection/damoyolo_trainer.md)。
