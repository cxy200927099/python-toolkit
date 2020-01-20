#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/20 2:44 下午
# @Author  : Chenxingyi
# @FileName: dependency_b.py

# from dependency_a import *
# from dependency.dependency_a import *
from utils.logUtil import *

def dependency_b():
    print("init logging")
    init_log()
    logging.info("init done!")
    print("package dependency b was called")
    # dependency_a()

if __name__ == '__main__':
    dependency_b()
