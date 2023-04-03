# Copyright (c) Alibaba, Inc. and its affiliates.
import argparse
import os
from importlib import import_module

import cv2
from adadet.infer.infer import infer
from adadet.utils.config import Config
from adadet.utils.io import dump

from modelscope.utils.logger import get_logger

init_loggers = {}
logger = get_logger()


def parse_args():
    """
    args for infer.
    """
    parser = argparse.ArgumentParser(description='Parse args for infer')
    parser.add_argument('--config', type=str, help='yaml configure file name')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    cfg = Config.from_file(args.config)
    logger.info('Loaded config: ' + str(cfg))
    inference = infer(cfg)
    input_path = cfg.get('input_path', './infer_input')
    output_path = cfg.get('output_path', './infer_output')
    os.makedirs(output_path, exist_ok=True)
    if not os.path.isfile(input_path):
        logger.error('Invalid input_path: ' + input_path)

    res = inference(input_path)
    output_name = os.path.basename(input_path) + '.json'
    dump(res, os.path.join(output_path, output_name))
    if cfg.vis_flag:
        vis_func = getattr(
            import_module('adadet.utils.visualization'), cfg.vis_func)
        vis_img = vis_func(input_path, res)
        os.makedirs(os.path.join(output_path, 'vis'), exist_ok=True)
        output_img = os.path.join(output_path, 'vis',
                                  os.path.basename(input_path))
        cv2.imwrite(output_img, vis_img)
    logger.info('Infer finished!')


if __name__ == '__main__':
    main()
