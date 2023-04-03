# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

from adadet.infer.infer import infer
from adadet.utils.config import Config

from modelscope.utils.test_utils import test_level


class DetInfer(unittest.TestCase):

    def setUp(self) -> None:
        self.config_path = 'configs/infer/model_infer.yaml'
        self.input_path = './test/data/images/test_walker1.jpeg'
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_infer_det(self):
        cfg = Config.from_file(self.config_path)
        inference = infer(cfg)
        res = inference(self.input_path)
        assert isinstance(res, dict) and 'labels' in res.keys(
        ) and 'boxes' in res.keys() and 'scores' in res.keys()


if __name__ == '__main__':
    unittest.main()
