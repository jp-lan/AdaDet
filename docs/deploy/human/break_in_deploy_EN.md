[简体中文](./break_in_deploy.md) | English
# Industrial Solution -- break-in Detection
This solution aims to detect the break-in behavior by connecting human detection and area break-in judgement modules in series.

## Introduction
The pipeline of this solution is illustrated as:
<img src='../../assets/breaking_in_pipeline_en.png' width=700>

The module of human detection performs the human-body detection based on [DAMOYOLO](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary), and then the  results will be passed into the module of [Area break-in Judgement](../../adadet/deploy/break_in_det_deploy.py) to decide whether break-in or not.

## Configurations
[configuration file example](../../../configs/deploy/human//break_in_det_deploy.yaml)
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

### Parameters

- `input_path` (str): Input video path
- `output_path` (str): Output path for files including inference results and visualization results
- `vis_flag` (bool): whether to show the detection results
- `adadet_deploy`: specific parameters for this solution
  - `type` (str): default, type of the solution
  - `model_id` (str): ModelScope ID of human detection model
  + `rules`: rules for break-in
      * `is_video` (bool): whether the input is a video or not
      * `region_polygon` (list): polygon region for break-in detection, the list should contain more than 3 points, and the 3 points are not on the same line
      * `frame_rate` (int): frame extraction rate for detection, valid when `is_video==True`, e.g. 5 represents that one frame is extracted at intervals of 5 frames for processing
      * `det_thres` (float): human detection confidence threshold


### Returns
```python
{
    0: { # detection result of frame 0. If the input is an image, only return the result of frame 0
          "scores": [float, float, ...], # confidences of the detection boxes
          "labels": [str, str, ...], # type of the detection boxes
          "boxes": [[float, float, float, float], ...] # coordinates of the detection boxes，[x1, y1, x2, y2]
          "alarms": [[bool, bool, bool, bool], ...] # Ture if the human detection box is in the defined region or area, otherwise, Flase
        }
    },
    1: {
        ...
    },
    ...
}

```


## Performance Evaluation
The performance evaluation on NVIDIA V100 GPU(16G)、32 core Xeon CPU:
| Solution | Inference time (single frame) | Model Size |
| :---: | :---: | :---: |
| break-in Detection | 71.24ms | 130M |


## ⚡️Quick-Start
Inference for this solution：
```python
python tools/deploy.py --config configs/deploy/human/break_in_det_deploy.yaml
```

## Finetune/Customize your model
For this solution, you can finetune/customize your model with specific datasets.

1. Human detection model: fine-tuning this model, please refer to [training docs](../../train/detection/damoyolo_trainer_EN.md) for details
