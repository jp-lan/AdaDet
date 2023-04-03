# Copyright (c) Alibaba, Inc. and its affiliates.
import argparse
import time

import cv2
import torch
from adadet.deploy.deploy import deploy
from adadet.utils.config import Config
from adadet.utils.constants import StateCode

from modelscope.utils.logger import get_logger

logger = get_logger()


def parse_args():
    """
    args for benchmark.
    """
    parser = argparse.ArgumentParser(description='Parse args for benchmark')
    parser.add_argument('--config', type=str, help='yaml configure file name')
    parser.add_argument(
        '--warmup_times',
        type=int,
        default=1,
        help='number of warmup runs before official runs')
    parser.add_argument(
        '--repeat_times', type=int, default=1, help='number of official runs')
    args = parser.parse_args()

    return args


def benchmark_deploy(cfg: Config, warmup_times: int, repeat_times: int):
    deployer = deploy(cfg)
    input_path = cfg.input_path
    logger.info('Warmup runs started.')
    for i in range(warmup_times):
        deployer(input_path)
    logger.info('Warmup runs finished.')
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    start_time = time.perf_counter()
    for i in range(repeat_times):
        deployer(input_path)
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    end_time = time.perf_counter()

    if cfg['adadet_deploy']['rules']['is_video']:
        cap = cv2.VideoCapture(input_path)
        num_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if num_frame == 0:
            logger.error(f'Open video {input_path} Failed!')
            exit(StateCode.INVALID_VIDEO_PATH)
    else:
        num_frame = 1
    logger.info('Averaged deploy time of ' + cfg['adadet_deploy']['type']
                + ' per frame is : %.2f ms' % (
                    (end_time - start_time) / repeat_times / num_frame * 1000))


def main():
    logger.info('Benchmark started.')
    args = parse_args()
    cfg = Config.from_file(args.config)
    logger.info('Loaded config: ' + str(cfg))
    if cfg.get('adadet_deploy', None):
        benchmark_deploy(cfg, args.warmup_times, args.repeat_times)
    logger.info('Benchmark finished.')


if __name__ == '__main__':
    main()
