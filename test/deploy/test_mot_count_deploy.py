# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

from adadet.deploy.deploy import deploy
from adadet.utils.config import Config

from modelscope.utils.test_utils import test_level


class MotCountDeploy(unittest.TestCase):

    def setUp(self) -> None:
        self.config_path = 'configs/deploy/human/mot_counting_deploy.yaml'
        self.video_path = './test/data/videos/MOT17-03-partial.mp4'
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_mot_counting_deploy(self):
        cfg = Config.from_file(self.config_path)
        mot_counting_deploy = deploy(cfg)
        res = mot_counting_deploy(self.video_path)
        assert isinstance(res, dict) and len(res['final_res']) == 60


if __name__ == '__main__':
    unittest.main()
