# Copyright (c) Alibaba, Inc. and its affiliates.
import argparse
import os

from adadet.deploy.deploy import deploy
from adadet.utils.config import Config
from adadet.utils.io import dump

from modelscope.utils.logger import get_logger

logger = get_logger()


def parse_args():
    """
    args for deploy.
    """
    parser = argparse.ArgumentParser(description='Parse args for deploy')
    parser.add_argument('--config', type=str, help='yaml configure file name')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    cfg = Config.from_file(args.config)
    logger.info('Loaded config: ' + str(cfg))
    input_path = cfg.get('input_path', './deploy_input')
    output_path = cfg.get('output_path', './deploy_output')
    deployer = deploy(cfg)
    os.makedirs(output_path, exist_ok=True)
    if not os.path.isfile(input_path):
        logger.error('Invalid input_path: ' + input_path)
    res = deployer(input_path)
    output_name = os.path.basename(input_path) + '.json'
    dump(res, os.path.join(output_path, output_name))
    if cfg.vis_flag:
        vis_path = os.path.join(output_path, 'vis',
                                os.path.basename(input_path))
        if cfg['adadet_deploy']['rules']['is_video']:
            vis_path = os.path.splitext(vis_path)[0] + '.avi'
        os.makedirs(os.path.join(output_path, 'vis'), exist_ok=True)
        deployer.visualize(input_path, res, vis_path)
    logger.info('final res = ' + str(res))


if __name__ == '__main__':
    main()
