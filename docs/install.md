简体中文 | [English](./install_EN.md)
# 环境安装指南
## 软硬件要求
本仓库全部运算功能支持在GPU环境下运行，在CPU环境下只支持部分场景化方案、单模型推理功能，不支持模型训练和评估。

建议运行的机器环境满足下列条件：
- 64位操作系统
- Python >= 3.7，64位版本

## 环境安装步骤
### 1. Git LFS安装
使用AdaDet，请确保您的环境中安装git和git-lfs。对于mac和linux操作系统，git是自带的，而git-lfs需要自行安装。
- MacOS安装git lfs
```shell
brew install git-lfs
```
- CentOS安装git lfs
    - 首先在[git-lfs](https://git-lfs.github.com/)官网下载对应的rpm包，然后运行：
```shell
sudo rpm -ivh \<包名\>.rpm
git lfs install
```

### 2. Conda环境配置
AdaDet的Python运行环境可以在Conda虚拟环境进行快速安装：

```python
conda create -n adadet python=3.7 -y
conda activate adadet

#install torch相关依赖，建议参考: https://pytorch.org/get-started/previous-versions/
#建议安装v1.11.0版本
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 -c pytorch

#install tensorflow，如不体验OCR模型可跳过此步骤
pip install --upgrade tensorflow==1.15 # 仅支持 CPU 的版本
# pip install --upgrade tensorflow-gpu==1.15 # GPU 版

#install modelscope
pip3 install "modelscope[cv]" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html

#install mmcv-full
pip3 install -U openmim
mim install mmcv-full

git clone https://github.com/modelscope/AdaDet.git
cd AdaDet

#install dependencies
pip3 install -r requirements.txt

# install AdaDet package
python setup.py develop
```

### 测试用例快速体验
可通过下列命令快速运行测试用例，检查环境是否配置成功。
```python
# run tests
python test/run.py
```
当运行日志显示测试结果均通过时，表面环境安装成功，成功日志示例如下：
```bash
# cpu 环境下会跳过一些测试用例
2023-02-25 23:33:45,003 - AdaDet - test/run.py:65 - INFO - SUCCESS (Runs=9,success=6,failures=0,errors=0,    skipped=3,expected failures=0,unexpected successes=0)

# gpu 环境下所有测试用例均会显示通过
2023-02-25 15:40:36,939 - AdaDet - test/run.py:65 - INFO - SUCCESS (Runs=9,success=8,failures=0,errors=0,    skipped=1,expected failures=0,unexpected successes=0)
```
