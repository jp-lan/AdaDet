[简体中文](./mot_counting_deploy.md) | English
# Industrial Solution -- MOT & Counting
This solution aims to count or estimate the number of people (crowd counting) by connecting pedestrian multi-object tracking (MOT) and MOT counting modules in series.
## Introduction
The pipeline of this solution is illustrated as:

<img src='../../assets/mot_counting_pipeline_en.png' width=800>

The module of pedestrian multi-object tracking (MOT) performs multiple pedestrian tracking based on [FairMOT](https://modelscope.cn/models/damo/cv_yolov5_video-multi-object-tracking_fairmot/summary), and then the  results will be passed into the module of [MOT Counting](../../adadet/deploy/mot_counting_deploy.py) to estimate the number of people.

## Configurations
[configuration file example](../../../configs/deploy/human/mot_counting_deploy.yaml)
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

### Parameters

- `input_path` (str): Input video path
- `output_path` (str): Output path for files including inference results and visualization results
- `vis_flag` (bool): whether to show the detection results
- `deploy`:  specific parameters for this solution
    + `type` (str): default, type of the solution
    + `model_id` (str):  ModelScope ID of FairMOT model
    + `rules`: rules for MOT counting
        * `is_video` (bool): whether the input is a video or not
        * `horizontal` (bool): the direction of crossing line，True represents horizontal，False represents vertical
        * `coord` (int): the coordinate of crossing line in the frame. If horizontal, it represents the coordinate in axis-y, else, coordinate in axis-x
        * `in_flag` (bool): Inside or outside, True represents the human cross outside the line from the upper left to lower right and inside the line from lower right to upper left, False if otherwise

### Returns

```python
{
  'mot_res': { # output of the pedestrian MOT module
    'boxes': [
                [
                  [int, int, int, int],
                  ...
                ], # detected pedestrian boxes in frame 0, [x1, x2, y1, y2]
                [
                  [int, int, int, int],
                  ...
                ], # detected pedestrian boxes in frame 1, [x1, x2, y1, y2]
              ...
              ], # total pedestrian boxes within all frames
    'labels': [
                [int, ...], # id for each pedestrian box in frame 0
                [int, ...], # id for each pedestrian box in frame 1
                ...
              ] # all the ids for each pedestrian box within all frames
  },
  'final_res': # final results of pedestrian MOT counting
    [(int, int), (int, int), (int, int), (int, int), (int, int), ...] # the number of crossing-line (inside, outside)， length of list should be equal to number of frames, each tuple represents the number of (inside, outside)
}
```

## Performance Evaluation
The performance evaluation on NVIDIA V100 GPU(16G)、32 core Xeon CPU:

| Solution | Inference time (single frame) | Model Size |
| :---: | :---: | :---: |
| MOT & Counting | 82.78ms |  67M |


## ⚡️Quick-Start
Inference for this solution：
```python
python tools/deploy.py --config configs/deploy/human/mot_counting_deploy.yaml
```
