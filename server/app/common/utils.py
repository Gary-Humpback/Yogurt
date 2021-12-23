# -*- coding: utf-8 -*-
"""
=======================================
Filename: utils
Description: tools for server
=======================================
"""
import json
import os
import traceback
from datetime import datetime
from functools import wraps
from dateutil import relativedelta
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from server.app.common.error_code import *
from server.app.configs.config import Config


def build_ret_data(ret_code, data=''):
    return {'code': ret_code, 'msg': ERR_CODE[ret_code], 'data': data}


def exec_service(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            ret_code, ret_data = func(*args, **kwargs)
            return_dict = build_ret_data(ret_code, ret_data)
        except Exception as ex:
            traceback.print_exc()
            return_dict = build_ret_data(THROW_EXP, str(ex))
        return return_dict

    return wrapper


def read_request(request, key):
    return request.get_json()[key]


def process_response(response):
    return json.dumps(response)


"""
======================================== scheduler task ========================================
"""


def clean_logs():
    # month job: clean logs once two month
    month_freq = 2
    condition = datetime.strftime(datetime.now() - relativedelta.relativedelta(month=month_freq), '%Y_%m')
    os.system(f'find {Config.server_root}/logs/ -name "{condition}_*"|xargs rm')


class SchedulerConf:
    JOBS = [
        {
            'id': 'clean_log',
            'func': clean_logs,
            'args': None,
            'trigger': 'corn',
            'day': 1,  # check job in every month 1st 4:00
            'hour': 4,
            'minute': 00
        }
    ]
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    SCHEDULER_API_ENABLED = True


def run_scheduler(app):
    app.config.from_object(SchedulerConf())
    scheduler = APScheduler(BackgroundScheduler(timezone='Asia/Shanghai'))
    scheduler.init_app(app)
    scheduler.start()
    return app
