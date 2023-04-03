[简体中文](./install.md) | English
# Environment Installation Guide
## Software and Hardware Requirements
All computational functions in this repository are supported to run on GPU environment. Only partial scenario-based solutions and single-model inference functions are supported to run on CPU environment. Model training and evaluation are not supported on CPU.

It is recommended to run on a machine environment that meets the following conditions:
- 64-bit operating system
- Python >=3.7,64-bit version

## Environment Installation Steps
### 1. Git LFS Installation
To use AdaDet, make sure that git and git-lfs are installed in your environment. For MacOS and Linux operating systems, git is included by default, but git-lfs needs to be installed separately.
- Install git-lfs on MacOS
```shell
brew install git-lfs
```
- Install git lfs on CentOS
		- Firstly, download the corresponding rpm package from the [git-lfs](https://git-lfs.github.com/) official website, and then run:
```shell
sudo rpm -ivh \<package name\>.rpm
git lfs install
```

### 2. Conda Environment Setup
The Python runtime environment of AdaDet can be quickly installed in a Conda virtual environment：

```python
conda create -n adadet python=3.7 -y
conda activate adadet

#install dependencies of torch，please refer to: https://pytorch.org/get-started/previous-versions/
#v1.11.0 is recommended
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 -c pytorch

#install tensorflow，If you do not want to experience the OCR model, you can skip this step.
pip install --upgrade tensorflow==1.15 # only CPU version is supported
# pip install --upgrade tensorflow-gpu==1.15 # GPU version

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

### Quick experience of test cases
You can quickly run the test cases and check if the environment is configured successfully by using the following command.
```python
# run tests
python test/run.py
```
When the running log shows that all test results have passed, it means that the environment installation is successful. A successful log example is shown below:
```bash
# Under CPU environment, some test cases will be skipped
2023-02-25 23:33:45,003 - AdaDet - test/run.py:65 - INFO - SUCCESS (Runs=9,success=6,failures=0,errors=0,    skipped=3,expected failures=0,unexpected successes=0)

# Under GPU environment, all test cases will show as pass
2023-02-25 15:40:36,939 - AdaDet - test/run.py:65 - INFO - SUCCESS (Runs=9,success=8,failures=0,errors=0,    skipped=1,expected failures=0,unexpected successes=0)
```
