[简体中文](./ocr_detection.md) | English
# OCR Detection

The Current list of supported OCR detection models is as follows:

|model Name|task_name|model_id|
|:--:|:--:|:--:|
|[text-detection-line-detection-CN/EN-SegLink++](#text-detection-line-detection-CN/EN-SegLink++)|ocr-detection|damo/cv_resnet18_ocr-detection-line-level_damo|
|[text-detection-word-detection-EN-SegLink++](#text-detection-word-detection-EN-SegLink++)|ocr-detection|damo/cv_resnet18_ocr-detection-word-level_damo|

## 📌 text-detection-line-detection-CN/EN-SegLink++
### Introduction
Text detection refers to detecting the coordinates of the bounding box of the text contained in an image. Text line detection refers to detecting the bounding box of the text line in a given image. This model detects the attractive and repulsive relationships between text blocks and text lines from the bottom up, then clusters text blocks into lines, and finally outputs the coordinates of the bounding box of the text lines. This model was trained on open source data from MTWI/RECTS/SROIE/LSVT.


### Inference
Single-model inference can be used for performance testing. Currently, CPU/GPU inference is supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Sample](../../configs/infer/model_infer.yaml) for modification of the key parameters in the configuration file:

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'ocr-detection'
  model_id: 'damo/cv_resnet18_ocr-detection-line-level_damo'
```

### Performance
The model was tested on the MTWI test set, and the results are as follows:

| Backbone |  Recall   | Precision |  F-score |
|:--------:|:---------:|:---------:|:--------:|
| ResNet18 |   68.1    |   84.9    |   75.6   |

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_resnet18_ocr-detection-line-level_damo/summary)

### Citations
The main reference paper for this model is as follows:

```BibTex
@article{tang2019seglink++,
  title={Seglink++: Detecting dense and arbitrary-shaped scene text by instance-aware component grouping},
  author={Tang, Jun and Yang, Zhibo and Wang, Yongpan and Zheng, Qi and Xu, Yongchao and Bai, Xiang},
  journal={Pattern recognition},
  volume={96},
  pages={106954},
  year={2019},
  publisher={Elsevier}
}
```

## 📌 text-detection-word-detection-EN-SegLink++
### Introduction
Text detection refers to detecting the coordinates of the bounding box of the text contained in an image. English word detection refers to detecting the bounding box of the English words in a given image. This model was trained on open source data from MLT17/MLT19/IC15/TextOCR/HierText.

### Inference
Single-model inference can be used for performance testing. Currently, CPU/GPU inference is supported. Please refer to the [Inference Documentation](../infer/infer_tutorial_EN.md) and [Inference Configuration Sample](../../configs/infer/model_infer.yaml) for modification of the key parameters in the configuration file:

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'ocr-detection'
  model_id: 'damo/cv_resnet18_ocr-detection-word-level_damo'
```

### Performance

### Demo Links
[ModelCard & Demo](https://modelscope.cn/models/damo/cv_resnet18_ocr-detection-word-level_damo/summary)

### Citations
The main reference paper for this model is as follows:

```BibTeX
@article{tang2019seglink++,
  title={Seglink++: Detecting dense and arbitrary-shaped scene text by instance-aware component grouping},
  author={Tang, Jun and Yang, Zhibo and Wang, Yongpan and Zheng, Qi and Xu, Yongchao and Bai, Xiang},
  journal={Pattern recognition},
  volume={96},
  pages={106954},
  year={2019},
  publisher={Elsevier}
}
```
