# Copyright (c) Alibaba, Inc. and its affiliates.
class DatasetMode(object):
    """ Dataset mode
    """
    dataset_offline = 'dataset_offline'
    dataset_online = 'dataset_online'


class StateCode:
    ERROR = -1
    SUCCESS = 1
    INVALID_REGION_POLYGON_FORMAT = 201
    INVALID_REGION_POLYGON_VALUE = 202
    INVALID_VIDEO_PATH = 203
    INVALID_IMAGE_PATH = 204
    INVALID_SUFFIX = 205
