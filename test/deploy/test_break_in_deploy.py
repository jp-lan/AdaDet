# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

from adadet.deploy.deploy import deploy
from adadet.utils.config import Config

from modelscope.utils.test_utils import test_level


class BreakInDeploy(unittest.TestCase):

    def setUp(self) -> None:
        self.input_image = './test/data/images/test_walker1.jpeg'
        self.input_video = './test/data/videos/MOT17-03-partial.mp4'
        self.config_path = 'configs/deploy/human/break_in_det_deploy.yaml'
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_break_in_det_deploy_image(self):
        cfg = Config.from_file(self.config_path)
        cfg.adadet_deploy.rules.is_video = False
        break_in_det_deploy = deploy(cfg)
        res = break_in_det_deploy(self.input_image)
        assert isinstance(res, dict) and res[0]['alarms'].sum() == 1

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_break_in_det_deploy_video(self):
        cfg = Config.from_file(self.config_path)
        cfg.adadet_deploy.rules.is_video = True
        break_in_det_deploy = deploy(cfg)
        res = break_in_det_deploy(self.input_video)
        assert isinstance(res, dict) and res[0]['alarms'].sum() == 20


if __name__ == '__main__':
    unittest.main()
