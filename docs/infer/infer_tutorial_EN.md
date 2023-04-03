[简体中文](./infer_tutorial.md) | English
# Single Model Inference Tutorial

'Single Model Inference' is the inference of a single trained model, which generates the inference results and visualized results in the output directory for debugging. This document will introduce the details (configuration file and work directory structure) of 'Single Model Inference' and provide a list of currently supported models.

## ⚡️Quick Start

The startup script [run_infer.sh](../../tools/run_infer.sh) is as below:

```python
python tools/infer.py --config configs/infer/model_infer.yaml
```

The command takes [inference configuration file](../../configs/infer/model_infer.yaml) as input parameter to [infer API](../../tools/infer.py).

## Configuration
The contents of [inference configuration file](../../configs/infer/model_infer.yaml) are as follows (take human detection model as an example):

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

### Parameters

- `input_path` (str): The path of input image/video.
- `output_path` (str): The output path, which contains log file, inference resuts, visualization results, etc.
- `vis_flag` (bool): Whether to visualize the inference results.
- `vis_func` (str): The visualization function, which is defined in "adadet/utils/visualization.py". It's used to generate the visualization reults of image/video.
- `adadet_infer`: The parameters about inference.
    + `type` (str): The type of infer node. Default: 'ModelScopePipeline', no changes required.
    + `task` (str): The task name in ModelScope. Refer to [metainfo file](https://github.com/modelscope/modelscope/blob/master/modelscope/metainfo.py) for more details, e.g., 'domain-specific-object-detection' for human detection model.
    + `model_id` (str):The model_id in ModelScope, e.g., `'damo/cv_tinynas_human-detection_damoyolo'` for human detection model. Please refer to [modelcard](https://modelscope.cn/models/damo/cv_tinynas_human-detection_damoyolo/summary) for the model_id of a specific model.

## Inference Results

The inference results are saved in `output_path`. If `output_path` is not set, the results will be saved in `'./infer_output'`. Suppose the input file is test_walker1.jpeg, then the directory structure of `output_path` is as below:

```bash
  ├── test_walker1.jpeg.json
  ├── vis
  │   ├── test_walker1.jpeg
```

test_walker1.jpg.json is the inference output file. Take human detection model as an example:

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

The visuaized image '${output_path}/vis/test_walker1.jpg' is shown as below

<img src='../assets/test_walker1_vis.jpeg' width=400>


## Supported Models

| model name | task | model_id | related link |
| ------ | ------ | ------ | ------ |
|general-object-detection-YOLOX-S|image-object-detection|damo/cv_cspnet_image-object-detection_yolox|[link](../models/object_detection_EN.md)|
|general-object-detection-YOLOX-Nano|image-object-detection|damo/cv_cspnet_image-object-detection_yolox_nano_coco|[link](../models/object_detection_EN.md)|
|general-object-detection-DINO|image-object-detection|damo/cv_swinl_image-object-detection_dino|[link](../models/object_detection_EN.md)|
|general-object-detection-DAMOYOLO-S|image-object-detection|damo/cv_tinynas_object-detection_damoyolo|[link](../models/object_detection_EN.md)|
|general-object-detection-DAMOYOLO-M|image-object-detection|damo/cv_tinynas_object-detection_damoyolo-m|[link](../models/object_detection_EN.md)|
|general-object-detection-DAMOYOLO-T|image-object-detection|damo/cv_tinynas_object-detection_damoyolo-t|[link](../models/object_detection_EN.md)|
|general-object-detection-ViTDet|image-object-detection|damo/cv_vit_object-detection_coco|[link](../models/object_detection_EN.md)|
|general-object-detection-AIRDet-S|image-object-detection|damo/cv_tinynas_detection|[link](../models/object_detection_EN.md)|
|human-detection-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_human-detection_damoyolo|[link](../models/domain_specific_object_detection_EN.md)|
|head-detection-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_head-detection_damoyolo|[link](../models/domain_specific_object_detection_EN.md)|
|hand-detection-YOLOX-PAI|domain-specific-object-detection|damo/cv_yolox-pai_hand-detection|[link](../models/domain_specific_object_detection_EN.md)|
|facemask-detection-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_facemask|[link](../models/domain_specific_object_detection_EN.md)|
|safety-helmet-detection-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_safety-helmet|[link](../models/domain_specific_object_detection_EN.md)|
|cigarette-detection-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_cigarette|[link](../models/domain_specific_object_detection_EN.md)|
|phone-detection-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_phone|[link](../models/domain_specific_object_detection_EN.md)|
|traffic-sign-detection-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_traffic_sign|[link](../models/domain_specific_object_detection_EN.md)|
|vehicle-detection-YOLOX-PAI|image-object-detection|damo/cv_yolox_image-object-detection-auto|[link](../models/domain_specific_object_detection_EN.md)|
|smokefire-detection-DAMOYOLO|domain-specific-object-detection|damo/cv_tinynas_object-detection_damoyolo_smokefire|[link](../models/domain_specific_object_detection_EN.md)|
|small-object-detection-MaskScoring|image-object-detection|damo/cv_resnet50_object-detection_maskscoring|[link](../models/small_object_detection_EN.md)|
|face-detection-keypoint-RetinaFace|face-detection|damo/cv_resnet50_face-detection_retinaface|[link](../models/face_detection_EN.md)|
|face-detection-keypoint-SCRFD|face-detection|damo/cv_resnet_facedetection_scrfd10gkps|[link](../models/face_detection_EN.md)|
|face-detection-MogFace|face-detection|damo/cv_resnet101_face-detection_cvpr22papermogface|[link](../models/face_detection_EN.md)|
|face-detection-ULFD|face-detection|damo/cv_manual_face-detection_ulfd|[link](../models/face_detection_EN.md)|
|face-detection-keypoint-MTCNN|face-detection|damo/cv_manual_face-detection_mtcnn|[link](../models/face_detection_EN.md)|
|text-detection-line-detection-CN/EN-SegLink++|ocr-detection|damo/cv_resnet18_ocr-detection-line-level_damo|[link](../models/ocr_detection_EN.md)|
|text-detection-word-detection-EN-SegLink++|ocr-detection|damo/cv_resnet18_ocr-detection-word-level_damo|[link](../models/ocr_detection_EN.md)|
|video-object-detection-StreamYOLO|video-object-detection|damo/cv_cspnet_video-object-detection_streamyolo|[link](../models/video_object_detection_EN.md)|
|body-2d-keypoints-HRNet|body-2d-keypoints|damo/cv_hrnetv2w32_body-2d-keypoints_image|[link](../models/2d_keypoints_EN.md)|
|hand-2d-keypoints-HRNet|hand-2d-keypoints|damo/cv_hrnetw18_hand-pose-keypoints_coco-wholebody|[link](../models/2d_keypoints_EN.md)|
|face-2d-keypoints-MobileNetV2|face-2d-keypoints|damo/cv_mobilenet_face-2d-keypoints_alignment|[link](../models/2d_keypoints_EN.md)|
|body-3d-keypoints-TPNet|body-3d-keypoints|damo/cv_canonical_body-3d-keypoints_video|[link](../models/3d_keypoints_EN.md)|
|body-3d-keypoints-HDFormer|body-3d-keypoints|damo/cv_hdformer_body-3d-keypoints_video|[link](../models/3d_keypoints_EN.md)|
|video-object-tracking-FairMOT|video-multi-object-tracking|damo/cv_yolov5_video-multi-object-tracking_fairmot|[link](../models/video_object_tracking_EN.md)|
