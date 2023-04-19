[简体中文](./video_object_tracking.md) | English
# Video Object Tracking

Supported models:

|model name|task_name|model_id|
|:--:|:--:|:--:|
|[video-object-tracking-FairMOT](#video-object-tracking-FairMOT)|video-multi-object-tracking|damo/cv_yolov5_video-multi-object-tracking_fairmot|

## 📌video-object-tracking-FairMOT ##
### Introduction
Multi-object tracking(MOT) algorithm usually consists of an object detection module and an object re-identification module. This model is based on FairMOT, which simultaneously performs object detection and re-identification in a single module and runs in real time.

This model is trained on [CrowdHuman](https://www.crowdhuman.org/)/[MIX](https://github.com/Zhongdao/Towards-Realtime-MOT/blob/master/DATASET_ZOO.md)/[MOT17](https://motchallenge.net/data/MOT17/) datasets, and aims to track pedestrians in street-view. Also, the model achieves SOTA performance on the 2DMOT15 dataset, while obtaining reasonable performance on MOT16, MOT17, and MOT20 datasets.

### Inference
Please use the model infer function to make predictions. Currently, the model supports both CPU and GPU inference, more details are in [infer tutorial](../infer/infer_tutorial_EN.md) and [infer configuration file](../../configs/infer/model_infer.yaml). Important parameters of the configuration file should be modified as below:

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'video-multi-object-tracking'
  model_id: 'damo/cv_yolov5_video-multi-object-tracking_fairmot'
```

### Performance
The performance on the MOT17 test set:
| Method    |  MOTA |
|--------------|-----------|
|FairMOT  | 68.5 |

### Demo Links
[ModelCard & demo](https://modelscope.cn/models/damo/cv_yolov5_video-multi-object-tracking_fairmot/summary)

### Citations

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
