[简体中文](./quick_start.md) | English
# Quick Start
This quick start tutorial takes the human detection single model and the break-in detection scenario as examples, allowing customers to quickly familiarize themselves with the usage and workflow of AdaDet.

## 1. Model Inference
```python
# Perform quick model inference using the trained human detection model.
python tools/infer.py --config configs/infer/model_infer.yaml
```
The inference results will be saved in the "./infer_out" directory, and the following files will be generated:

```bash
  ├── test_walker1.json
  ├── vis
  │   ├── test_walker1.jpeg
```

The fields of the output content for "test_walker1.jpg.json" image are:
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

The visualization result is shown below.

<img src='./assets/test_walker1_vis.jpeg' width=400>

## 2. Model Training and Evaluation (Secondary Development)
If the model performance is not satisfactory, the model can be further developed (finetuned) by preparing data for training.

Note: A GPU environment is required for this section.

### 1. Data Preparation
Data preparation is detailed in the parameter settings of the[training document](./train/detection/damoyolo_trainer_EN.md). Here, we use the prepared [online dataset](https://modelscope.cn/datasets/modelscope/person_detection_for_train/summary) as an example for model training (refer to the [training document](./train/detection/damoyolo_trainer_EN.md) for offline data preparation).

### 2. Training
Based on the selected model type and prepared data, fill in the corresponding parameters in the [training configuration file](../configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml). The finetuning process can be run directly with the following command:


```python
python tools/train.py --config configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml
```

The default save directory for training results is `./workdirs`. After completing the training, the directory structure of the working directory is as follows:

```bash
  ├── epoch_xxx_ckpt.pth # Model file
  ├── latest_ckpt.pth # Latest model file
  ├── train_log.txt # Training log file
  ├── inference
  │   ├── bbox.json # Prediction box file
  │   ├── coco_results.pth # COCO eval results file
  │   ├── predictions.pth # Prediction results file

```

### 3. Evaluation
During the training process mentioned above, the model is evaluated on the validation set. If you want to evaluate a specific model separately, you can use the following command for model evaluation:
```python
python tools/eval.py --config configs/train/detection/domain_specific_object_detection_damoyolo_online.yaml \
                     --checkpoint the/path/to/your/checkpoint.pth
```
Note that if the `checkpoint` parameter is not specified, the evaluation will use the pre-trained model that comes with the trainer by default.

## 3. Experience of Industrial Solution Performance
Industrial Solutions are practical applications for the industry. The [break-in detection](./deploy/human/break_in_deploy_EN.md) industrial solution links the human detection model node and the region break-in judgment node.

You can quickly run this solution using the following command:
```python
python deploy.py --config configs/deploy/human/break_in_det_deploy.yaml
```
The results are saved by default in `./deploy_res`, where you can view the relevant output results and visual results. If you need to fine-tune the human detection model in the break-in detection scenario, please refer to [Model Training and Evaluation](#2.Model-Training-and-Evaluation-(Secondary-Development)).
