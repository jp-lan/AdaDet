简体中文 | [English](./ocr_detection_EN.md)
# OCR检测

当前支持的OCR检测模型列表如下：

|任务-模型名称|task_name|model_id|
|:--:|:--:|:--:|
|[文字检测-行检测-中英-SegLink++](#文字检测-行检测-中英-SegLink++)|ocr-detection|damo/cv_resnet18_ocr-detection-line-level_damo|
|[文字检测-单词检测-英文-SegLink++](#文字检测-单词检测-英文-SegLink++)|ocr-detection|damo/cv_resnet18_ocr-detection-word-level_damo|

## 📌文字检测-行检测-中英-SegLink++
### 基本信息
文字检测，即给定一张图片，检测出图中所含文字的外接框的端点的坐标值。文字行检测即检测给定图片中文字行的外接框。
本模型是以自底向上的方式，先检测文本块和文字行之间的吸引排斥关系，然后对文本块聚类成行，最终输出文字行的外接框的坐标值。
本模型是基于MTWI/RECTS/SROIE/LSVT开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'ocr-detection'
  model_id: 'damo/cv_resnet18_ocr-detection-line-level_damo'
```

### 客观指标
模型在MTWI测试集上测试，结果如下：

| Backbone |  Recall   | Precision |  F-score |
|:--------:|:---------:|:---------:|:--------:|
| ResNet18 |   68.1    |   84.9    |   75.6   |

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_resnet18_ocr-detection-line-level_damo/summary)

### 相关论文
本模型主要参考论文如下：
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

## 📌文字检测-单词检测-英文-SegLink++
### 基本信息
文字检测，即给定一张图片，检测出图中所含文字的外接框的端点的坐标值。英文单词检测即检测给定图片英文单词的外接框。
本模型是基于MLT17/MLT19/IC15/TextOCR/HierText开源数据训练得到。

### 模型推理
可使用单模型推理功能进行效果体验，目前支持CPU/GPU推理，可参考[推理文档](../infer/infer_tutorial.md)和[推理配置样例](../../configs/infer/model_infer.yaml)，配置文件关键参数作如下对应修改：

```yaml
vis_flag: False
adadet_infer:
  type: 'ModelScopePipeline'
  task: 'ocr-detection'
  model_id: 'damo/cv_resnet18_ocr-detection-word-level_damo'
```

### 客观指标

### 相关链接
[ModelCard & demo体验](https://modelscope.cn/models/damo/cv_resnet18_ocr-detection-word-level_damo/summary)

### 相关论文
本模型主要参考论文如下：

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
