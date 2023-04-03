# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

from adadet.deploy.deploy import deploy
from adadet.utils.config import Config

from modelscope.utils.test_utils import test_level


class SmokeDetDeployTest(unittest.TestCase):

    def setUp(self) -> None:
        self.config_path = 'configs/deploy/security/smoke_det_deploy.yaml'
        self.img_path = './test/data/images/smoke_a388.jpg'
        self.video_path = './test/data/videos/smoke_a388.mp4'

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_smoke_det_deploy_image(self):
        cfg = Config.from_file(self.config_path)
        cfg.vis_flag = False
        cfg.adadet_deploy.rules.is_video = False
        smoke_det_deploy = deploy(cfg)
        res = smoke_det_deploy(self.img_path)

        assert isinstance(res, dict) and len(res) == 1

    @unittest.skipUnless(test_level() >= 1, 'skip test in current test level')
    def test_smoke_det_deploy_video(self):
        cfg = Config.from_file(self.config_path)
        cfg.vis_flag = False
        cfg.adadet_deploy.rules.is_video = True
        cfg.adadet_deploy.rules.frame_rate = 1
        smoke_det_deploy = deploy(cfg)
        res = smoke_det_deploy(self.video_path)

        assert isinstance(res, dict) and len(res) == 50


if __name__ == '__main__':
    unittest.main()
