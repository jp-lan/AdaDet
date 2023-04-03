简体中文 | [English](./mot_counting_deploy_EN.md)
# 人群跟踪与计数场景解决方案
此解决方案采用了行人多目标跟踪模型和穿线计数模块实现人群计数。
## 解决方案介绍
解决方案整体流程图如下：

<img src='../../assets/mot_counting_pipeline.jpg' width=800>

整个解决方案使用了多目标跟踪算法[FairMOT](https://modelscope.cn/models/damo/cv_yolov5_video-multi-object-tracking_fairmot/summary)进行多目标跟踪，获得跟踪结果后会经过[计数模块](../../adadet/deploy/mot_counting_deploy.py)实现计数功能。
## 配置文件
人群跟踪与计数场景解决方案可以通过[配置文件](../../../configs/deploy/human/mot_counting_deploy.yaml)进行参数配置，主要配置参数说明如下：
```yaml
input_path:
  'test/data/videos/MOT17-03-partial.mp4'

output_path:
  ./deploy_res

vis_flag:
  True

adadet_deploy:
  type: MOTCounting
  model_id: 'damo/cv_yolov5_video-multi-object-tracking_fairmot'
  rules:
    is_video: True
    horizontal: True
    coord: 200
    in_flag: True
```

### 参数说明

对配置文件中的参数说明如下：

- `input_path` (str): 输入视频路径。
- `output_path` (str): 输出目录路径，存放推理结果、可视化结果等文件。
- `vis_flag` (bool): 输入对检测结果进行可视化。
- `deploy`: 解决方案主要配置参数部分
    + `type` (str): 方案的类别名称，无需改动。
    + `model_id` (str): 视频多目标跟踪模型对应的ModelScope模型id。
    + `rules`: 穿线计数模块规则
        * `is_video` (bool): 输入是否为视频。
        * `horizontal` (bool): 线的方向定义，True为水平方向，False为竖直方向
        * `coord` (int): 线位于视频帧的坐标位置，水平线为y方向坐标，竖直线为x方向坐标。
        * `in_flag` (bool): 内外空间的定义，True表示目标从左上往右下穿线为走出，从右下往左上穿线为走入；反之为False。

### 返回结果

解决方案返回结果的格式如下：

```python
{
  'mot_res': { # 保存行人多目标跟踪算法的输出结果
    'boxes': [
                [
                  [int, int, int, int],
                  ...
                ], # 第0帧检测出来的行人box, [x1, x2, y1, y2]
                [
                  [int, int, int, int],
                  ...
                ], # 第1帧检测出来的行人box, [x1, x2, y1, y2]
              ...
              ], # 视频所有帧检测出来的所有行人box
    'labels': [
                [int, ...], # 第0帧检测出来的每个行人box对应的id
                [int, ...], # 第1帧检测出来的每个行人box对应的id
                ...
              ] # 视频所有帧检测出来的每个行人box对应的id
  },
  'final_res': # 行人计数的最终输出结果
    [(int, int), (int, int), (int, int), (int, int), (int, int), ...] # 返回每帧图片穿线计数的数量， list长度与视频帧数相等，每个tuple为（穿线走入的数目, 穿线走出的数目）。
}
```

## 性能评估
该解决方案在NVIDIA V100 GPU(16G)、32 core Xeon CPU上性能如下表：

| 场景化方案名称 | 每帧使用耗时 |  模型体积 |
| :---: | :---: | :---: |
| 人群跟踪与计数 | 82.78ms |  67M |


## ⚡️快速开始
使用下面命令可快速跑通该解决方案：
```python
python tools/deploy.py --config configs/deploy/human/mot_counting_deploy.yaml
```
