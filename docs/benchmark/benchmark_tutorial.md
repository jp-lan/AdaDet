简体中文 | [English](./benchmark_tutorial_EN.md)
# 效率评测功能使用文档

此文档用于介绍效率评测功能（benchmark）的使用方法、参数说明、输出说明。

效率评测功能用于评测场景化解决方案在硬件上的耗时。
该功能以配置文件指定的测试图片/视频为输入，经过预热阶段后，程序会统计正式效率测评阶段的耗时，评测结束后，把正式评测过程中处理单帧图片的平均耗时作为结果输出到终端日志中。


## ⚡️快速开始
该功能可通过[run_benchmark.sh](../../tools/run_benchmark.sh)运行体验，具体运行命令如下：
```python
python tools/benchmark.py \
  --config configs/deploy/human/break_in_det_deploy.yaml \
  --warmup_times 1 \
  --repeat_times 1
```
该命令需要把场景化解决方案的配置文件路径、预热阶段推理次数、正式效率评测阶段推理次数作为参数输入到[效率评测功能接口](../../tools/benchmark.py)中，具体参数说明和结果说明如下：

## 效率评测功能接口参数

|参数名称|类型|是否必须|说明|
| :--: | :-- | :--: | :--: |
|config|str|是|场景化解决方案配置文件路径|
|warmup_times|int|否|预热阶段推理次数|
|repeat_times|int|否|效率评测阶段重复推理次数|


## 评测结果说明

效率评测功能运行完成后将把评测结果以日志形式输出到终端，其评测时间返回的是处理单帧时的平均耗时（已毫秒为单位），输出样例如下：

```bash
2023-02-24 09:39:24,887 - AdaDet - tools/benchmark.py:56 - INFO - Averaged deploy time of BreakInDet per frame is : 18.05 ms
```

## 当前支持效率评测的场景化方案列表

| 场景化方案名称 | 每帧耗时| 配置文件 | 文档链接 |
| ------ | ------ | ------ | ------ |
|人流统计 | 82.78ms|[config](../../configs/deploy/human/mot_counting_deploy.yaml) | [文档](../../docs/deploy/human/mot_counting_deploy.md) |
|闯入检测 | 71.24ms | [config](../../configs/deploy/human/break_in_det_deploy.yaml) | [文档](../../docs/deploy/human/break_in_deploy.md) |
|抽烟检测 | 61.13ms | [config](../../configs/deploy/security/smoke_det_deploy.yaml) | [文档](../../docs/deploy/security/smoke_det_deploy.md) |

上述耗时数据在V100 GPU(16G)上测得。
