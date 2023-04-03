简体中文 | [English](./infer_tutorial_EN.md)
# 单模型推理接口使用文档

单模型推理功能用于推理训练好的单个网络，并把推理结果和可视化结果保存到输出目录，可用于单模型结果确认和场景化应用效果调试。
此文档用于介绍单模型推理功能（infer）的配置文件和保存结果，并且给出了当前支持的模型列表。

## ⚡️快速开始
该功能可通过[run_infer.sh](../../tools/run_infer.sh)运行体验人体垂类目标检测单模型效果，具体运行命令如下：
```python
python tools/infer.py --config configs/infer/model_infer.yaml
```
该命令需要把[配置文件](../../configs/infer/model_infer.yaml)作为参数输入到[推理功能接口](../../tools/infer.py)中。

## 配置文件说明
单模型推理功能可以通过[配置文件](../../configs/infer/model_infer.yaml)进行参数配置，以人体垂类目标检测为例，主要配置参数说明如下：
```yaml
input_path:
  ./test/data/images/test_walker1.jpeg

output_path:
  ./infer_out

vis_flag: True
vis_func: vis_det_img

adadet_infer:
  type: 'ModelScopePipeline'
  task: 'domain-specific-object-detection'
  model_id: 'damo/cv_tinynas_human-detection_damoyolo'
```

### 参数说明

对配置文件中的参数说明如下：

- `input_path` (str): 输入图片/视频路径。
- `output_path` (str): 输出目录路径，存放日志、推理结果、可视化结果等文件。
- `vis_flag` (bool): 是否对推理结果进行可视化。
- `vis_func` (str): 可视化函数名，函数位于"adadet/utils/visualization.py"中，用于生成可视化效果图/视频。
- `adadet_infer`: 推理功能主要配置参数部分
    + `type` (str): infer节点的类别，当前为'ModelScopePipeline'，无需改动。
    + `task` (str): ModelScope对应Task的名称，可从[相应文件](https://github.com/modelscope/modelscope/blob/master/modelscope/metainfo.py)查询获得。当前使用的人体检测垂类目标检测模型对应值为:'domain-specific-object-detection'。
    + `model_id` (str): ModelScope中模型库的模型id名称，以人体垂类目标检测为例，model_id为'damo/cv_tinynas_human-detection_damoyolo',可从对应[模型库](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary)介绍中获得。


## 保存结果说明

单模型推理将把推理结果和可视化结果（若有）保存在配置文件中的output_path下，若未设置output_path，将默认保存在'./infer_output'文件夹中。
若输入的文件为test_walker1.jpeg, 则在output_path下将保存生成下列文件：

```bash
  ├── test_walker1.jpeg.json
  ├── vis
  │   ├── test_walker1.jpeg
```

其中test_walker1.jpg.json为图片输出结果，以人体垂类目标检测为例，其输出内容字段为：
```python

{
    "scores": [
        0.8139657378196716,
        0.7489762306213379,
        ...
    ],
    "labels": [
        "person",
        "person",
        ...
    ],
    "boxes": [
        [
            561.63720703125,
            377.2309265136719,
            622.9022827148438,
            488.0690002441406
        ],
        [
            371.8719177246094,
            203.49237060546875,
            387.8343200683594,
            253.65220642089844
        ],
        ...
    ]
}

```

可视化文件'${output_path}/vis/test_walker1.jpg'如下：

<img src='../assets/test_walker1_vis.jpeg' width=400>


## 当前支持单模型推理的模型列表

| 任务-模型名称 | task | model_id | 模型介绍链接 |
| ------ | ------ | ------ | ------ |
|通用目标检测-YOLOX-S|image-object-detection|damo/cv_cspnet_image-object-detection_yolox|[链接](../models/object_detection.md)|
|通用目标检测-YOLOX-Nano|image-object-detection|damo/cv_cspnet_image-object-detection_yolox_nano_coco|[链接](../models/object_detection.md)|
|通用目标检测-DINO|image-object-detection|damo/cv_swinl_image-object-detection_dino|[链接](../models/object_detection.md)|
|通用目标检测-DAMOYOLO-S|image-object-detection|damo/cv_tinynas_object-detection_damoyolo|[链接](../models/object_detection.md)|
|通用目标检测-DAMOYOLO-M|image-object-detection|damo/cv_tinynas_object-detection_damoyolo-m|[链接](../models/object_detection.md)|
|通用目标检测-DAMOYOLO-T|image-object-detection|damo/cv_tinynas_object-detection_damoyolo-t|[链接](../models/object_detection.md)|
|通用目标检测-ViTDet|image-object-detection|damo/cv_vit_object-detection_coco|[链接](../models/object_detection.md)|
|通用目标检测-AIRDet-S|image-object-detection|damo/cv_tinynas_detection|[链接](../models/object_detection.md)|
|人体检测-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_human-detection_damoyolo|[链接](../models/domain_specific_object_detection.md)|
|人头检测-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_head-detection_damoyolo|[链接](../models/domain_specific_object_detection.md)|
|手部检测-YOLOX-PAI|domain-specific-object-detection|damo/cv_yolox-pai_hand-detection|[链接](../models/domain_specific_object_detection.md)|
|口罩检测-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_facemask|[链接](../models/domain_specific_object_detection.md)|
|安全帽检测-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_safety-helmet|[链接](../models/domain_specific_object_detection.md)|
|香烟检测-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_cigarette|[链接](../models/domain_specific_object_detection.md)|
|手机检测-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_phone|[链接](../models/domain_specific_object_detection.md)|
|交通标识检测-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_traffic_sign|[链接](../models/domain_specific_object_detection.md)|
|车辆检测-YOLOX-PAI|image-object-detection|damo/cv_yolox_image-object-detection-auto|[链接](../models/domain_specific_object_detection.md)|
|烟火检测-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_smokefire|[链接](../models/domain_specific_object_detection.md)|
|高性能通用小目标检测-MaskScoring模型|image-object-detection|damo/cv_resnet50_object-detection_maskscoring|[链接](../models/small_object_detection.md)|
|人脸检测关键点-RetinaFace|face-detection|damo/cv_resnet50_face-detection_retinaface|[链接](../models/face_detection.md)|
|人脸检测关键点-SCRFD|face-detection|damo/cv_resnet_facedetection_scrfd10gkps|[链接](../models/face_detection.md)|
|人脸检测-MogFace|face-detection|damo/cv_resnet101_face-detection_cvpr22papermogface|[链接](../models/face_detection.md)|
|人脸检测-ULFD|face-detection|damo/cv_manual_face-detection_ulfd|[链接](../models/face_detection.md)|
|人脸检测关键点-MTCNN|face-detection|damo/cv_manual_face-detection_mtcnn|[链接](../models/face_detection.md)|
|文字检测-行检测-中英-SegLink++|ocr-detection|damo/cv_resnet18_ocr-detection-line-level_damo|[链接](../models/ocr_detection.md)|
|文字检测-单词检测-英文-SegLink++|ocr-detection|damo/cv_resnet18_ocr-detection-word-level_damo|[链接](../models/ocr_detection.md)|
|视频目标检测-StreamYOLO|video-object-detection|damo/cv_cspnet_video-object-detection_streamyolo|[链接](../models/video_object_detection.md)|
|2D人体关键点检测-HRNet|body-2d-keypoints|damo/cv_hrnetv2w32_body-2d-keypoints_image|[链接](../models/2d_keypoints.md)|
|2D手部关键点检测-HRNet|hand-2d-keypoints|damo/cv_hrnetw18_hand-pose-keypoints_coco-wholebody|[链接](../models/2d_keypoints.md)|
|2D人脸关键点检测-MobileNetV2|face-2d-keypoints|damo/cv_mobilenet_face-2d-keypoints_alignment|[链接](../models/2d_keypoints.md)|
|3D人体关键点检测-TPNet|body-3d-keypoints|damo/cv_canonical_body-3d-keypoints_video|[链接](../models/3d_keypoints.md)|
|3D人体关键点检测-HDFormer模型|body-3d-keypoints|damo/cv_hdformer_body-3d-keypoints_video|[链接](../models/3d_keypoints.md)|
|视频多目标跟踪-FairMOT|video-multi-object-tracking|damo/cv_yolov5_video-multi-object-tracking_fairmot|[链接](../models/video_object_tracking.md)|
