# Copyright (c) Alibaba, Inc. and its affiliates.
import argparse

from adadet.train import train_manager
from adadet.utils.config import Config

from modelscope.utils.logger import get_logger

logger = get_logger()


def parse_args():
    """
    args for evaluation.
    """
    parser = argparse.ArgumentParser(description='Parse args for evaluation')
    parser.add_argument('--config', type=str, help='yaml configure file path')
    parser.add_argument(
        '--checkpoint', type=str, default=None, help='the checkpoint path')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    cfg = Config.from_file(args.config)
    trainer = train_manager(cfg)

    if args.checkpoint is None:
        ckpt_path = trainer.get_default_model_path()
    else:
        ckpt_path = args.checkpoint

    res = trainer.evaluate(checkpoint_path=ckpt_path)

    if res is not None:
        print(f'Evaluate results:{res}')


if __name__ == '__main__':
    main()
