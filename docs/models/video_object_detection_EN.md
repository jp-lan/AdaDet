[简体中文](./video_object_detection.md) | English
# Video Object Detection

The current list of supported video object detection models is as follows:

|model name|task_name|model_id|
|:--:|:--:|:--:|
|[video-object-detection-StreamYOLO](#video-object-detection-StreamYOLO)|video-object-detection|damo/cv_cspnet_video-object-detection_streamyolo|


## 📌video-object-detection-StreamYOLO ##
### Introduction
This model is a real-time general detection model based on [StreamYOLO](https://github.com/yancie-yjr/StreamYOLO)，and supports detection of8 types of traffic objects. Based on the YOLOX model, it uses the Dual-Flow Perception feature fusion module to learn temporal relationships at the feature level to improve environmental perception and prediction. Additionally, StreamYOLO employs a Trend-Aware Loss to perceive the intensity of object motion changes, which is used to weigh object prediction regression. This allows objects with more severe motion changes to receive higher regression weights, resulting in better prediction results. This model is trained on the Argoverse-HD dataset and is suitable for object detection in autonomous driving scenarios.

### Inference
You can experience the effect using the single-model inference function, currently supporting CPU/GPU inference. Please refer to the [inference documentation](../infer/infer_tutorial_EN.md)和[inference configuration example](../../configs/infer/model_infer.yaml)，please modify the key parameters of the configuration file as follows：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'video-object-detection'
  model_id: 'damo/cv_cspnet_video-object-detection_streamyolo'
```

### Performance
The performance of the model on the validation set of Argoverse-HD are as follows:

|Model |size |velocity | sAP<br>0.5:0.95 | sAP50 |sAP75| weights | COCO pretrained weights |
| ------        |:---: | :---:       |:---:     |:---:  | :---: | :----: | :----: |
|[StreamYOLO-l](https://arxiv.org/pdf/2207.10433.pdf)    |600×960  |1x  |36.9 |58.1| 37.5 |[official](https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth) |[official](https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/yolox_l.pth) |



### Demo Links
[ModelCard & demo experience](https://modelscope.cn/models/damo/cv_cspnet_video-object-detection_streamyolo/summary)

### Citations
The main reference papers of this model are as follows:

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
