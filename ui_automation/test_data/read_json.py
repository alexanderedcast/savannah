# coding=utf-8
import json
import os

import yaml


def read_json(file_name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '%s.json' % file_name)) as f:
        data = json.load(f)
    return data


def read_config_file():
    with open(os.getcwd() + os.path.sep + "ui_automation/env_config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)
    return config
