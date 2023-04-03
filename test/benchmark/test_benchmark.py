# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

from adadet.utils.config import Config
from tools.benchmark import benchmark_deploy

from modelscope.utils.test_utils import test_level


class BenchmarkTest(unittest.TestCase):

    def setUp(self) -> None:
        self.config_path = 'configs/deploy/security/smoke_det_deploy.yaml'
        self.img_path = './test/data/images/smoke_a388.jpg'

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_smoke_det_benchmark_image(self):
        cfg = Config.from_file(self.config_path)
        cfg.input_path = self.img_path
        cfg.adadet_deploy.rules.is_video = False
        benchmark_deploy(cfg, 1, 1)


if __name__ == '__main__':
    unittest.main()
