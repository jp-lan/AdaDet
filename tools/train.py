# Copyright (c) Alibaba, Inc. and its affiliates.
import argparse

from adadet.train import train_manager
from adadet.utils.config import Config

from modelscope.utils.logger import get_logger

logger = get_logger()


def parse_args():
    """
    args for train.
    """
    parser = argparse.ArgumentParser(description='Parse args for train')
    parser.add_argument('--config', type=str, help='yaml configure file path')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    cfg = Config.from_file(args.config)
    trainer = train_manager(cfg)
    trainer.train()


if __name__ == '__main__':
    main()
