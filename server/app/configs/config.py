# -*- coding: utf-8 -*-
"""
=======================================
Filename: config
Description: base config for Yogurt
=======================================
"""
import os
import yaml
import logging

logger = logging.getLogger(__name__)


def read_conf(conf, key1, key2=None, default=None):
    if default is not None:
        return default
    if type(conf) != dict:
        logger.warning('[Config] ConfError: config is illegal')
        return default
    if key1 not in conf.keys():
        logger.warning('[Config] KeyError: {}'.format(key1))
    else:
        if key2:
            if key2 not in conf[key1].keys():
                logger.warning('[Config] KeyError: {}'.format(key2))
                return default
            return conf[key1][key2]
        return conf[key1]


class Config:
    server_root = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-2])
    with open(f'{server_root}/app/configs/config.yaml') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    config = Config()
    print(config.server_root)
