# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 10:32 上午
# @Author  : chenxingyi
# @FileName: logUtil.py

import logging
import warnings


def init_log():
    # ignore spleeter warning
    warnings.filterwarnings('ignore')

    # init log
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(filename)s:%(lineno)d:%(message)s",
        level=logging.DEBUG)
    logging.info("log init!")