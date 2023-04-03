[简体中文](./benchmark_tutorial.md) | English
# Benchmark Tutorial

This doc introduces the benchmark function, including parameters and outputs.

The benchmark function is used to test the speed of industrial solutions on a particular hardware.

The benchmark function takes the test image/video specified in the configuration file as input. After the warm-up stage, it will calculate the average time cost for each frame during the formal test stage and the result will be shown in the log.


## ⚡️Quick Start
Execute [run_benchmark.sh](../../tools/run_benchmark.sh) script to get the result of the benchmark function.
```python
python tools/benchmark.py \
  --config configs/deploy/human/break_in_det_deploy.yaml \
  --warmup_times 1 \
  --repeat_times 1
```
The command takes the configuration file path, warmup_times, and repeat_times as the input parameter to the [benchmark API](../../tools/benchmark.py). The parameters are introduced in the following table.

## Parameters

|parameter name|type|required|details|
| :--: | :-- | :--: | :--: |
|config|str|yes|Configuration file path of the industrial solution|
|warmup_times|int|no|The number of running times during the warm-up stage|
|repeat_times|int|no|The number of running times during the formal test stage|


## Benchmark Results

The benchmark result, which is the average time cost in processing a single frame (in milliseconds), will be shown on the terminal. The output sample is as follows:
```bash
2023-02-24 09:39:24,887 - AdaDet - tools/benchmark.py:56 - INFO - Averaged deploy time of BreakInDet per frame is : 18.05 ms
```

## Benchmark Results of Supported Industrial Solutions

| Industrial Solutions | Time Cost (per frame)| Configuration File | Tutorial |
| ------ | ------ | ------ | ------ |
|MOT & Counting | 82.78ms|[config](../../configs/deploy/human/mot_counting_deploy.yaml) | [tutorial](../../docs/deploy/human/mot_counting_deploy_EN.md) |
|Break-In Detection | 71.24ms | [config](../../configs/deploy/human/break_in_det_deploy.yaml) | [tutorial](../../docs/deploy/human/break_in_deploy_EN.md) |
|Smoking Detection | 61.13ms | [config](../../configs/deploy/security/smoke_det_deploy.yaml) | [tutorial](../../docs/deploy/security/smoke_det_deploy_EN.md) |

The above data is obtained on a V100 GPU(16G).
