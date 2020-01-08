# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 12:44 下午
# @Author  : chenxingyi
# @FileName: processUtil.py

import typing
import multiprocessing


class ProcessUtil(object):
    def __init__(self, process_cnt):
        self.process_cnt = process_cnt
        self.pool = multiprocessing.Pool(processes=process_cnt)

    def doAsyncJob(self, job, args=()):
        self.pool.apply_async(job, args=args)
