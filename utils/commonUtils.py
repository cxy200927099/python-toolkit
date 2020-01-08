#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 11:02 上午
# @Author  : chenxingyi
# @FileName: commonUtils.py

import typing
import threading
import os
import psutil
# from multiprocessing import Pool
import multiprocessing
import time

def getThreadInfo() -> typing.Tuple[str, str]:
    t = threading.currentThread()
    return t.ident, t.name

def getProcessInfo() -> typing.Tuple[str, str]:
    pid = os.getpid()
    p = psutil.Process(pid)
    return p.pid, p.name()

def doSomeWork(msg: str):
    # print("msg:%s" % msg)
    t_id, t_name = getThreadInfo()
    p_id, p_name = getProcessInfo()
    print("doSomeWork receive %s thread id:%d name:%s process id:%d name:%s" % (msg, t_id, t_name, p_id, p_name))
    time.sleep(1)
    print("doSomeWork %s done thread id:%d name:%s process id:%d name:%s" % (msg, t_id, t_name, p_id, p_name))

def doTimeConsumingTask(data:typing.Dict[str, typing.List[str]]):
    t_id, t_name = getThreadInfo()
    p_id, p_name = getProcessInfo()
    print("doTimeConsumingTask receive data thread id:%d name:%s process id:%d name:%s" %
                 (t_id, t_name, p_id, p_name))
    time.sleep(1)
    print("doTimeConsumingTask done thread id:%d name:%s process id:%d name:%s" %
                 (t_id, t_name, p_id, p_name))

def doThreadFunc():
    t_id, t_name = getThreadInfo()
    p_id, p_name = getProcessInfo()
    print("doThreadFunc receive thread id:%d name:%s process id:%d name:%s" % ( t_id, t_name, p_id, p_name))
    pool.apply_async(doTimeConsumingTask, args=("test",))
    print("doThreadFunc done thread id:%d name:%s process id:%d name:%s" % ( t_id, t_name, p_id, p_name))


def mycallback(x):
    global blah
    blah = "called back"
    print("My callback " + str(x))


def myerrorcallback(r):
    print("My errorcallback " + str(r))


if __name__ == '__main__':
    t_id, t_name = getThreadInfo()
    p_id, p_name = getProcessInfo()
    print("main start thread id:%d name:%s process id:%d name:%s" %
                 (t_id, t_name, p_id, p_name))
    global pool
    pool = multiprocessing.Pool(processes=3)
    # 这里args参数多传了一个，导致doSomeWork不会被执行，但是没有任何错误提示
    # 添加callback就可以监控到错误的日志
    pool.apply_async(doSomeWork, args=("hello", "hello1"), callback=mycallback, error_callback=myerrorcallback)
    pool.apply_async(doSomeWork, args=("python",))
    pool.apply_async(doSomeWork, args=("world",))

    pool.close()
    pool.join()
    # time.sleep(4)
    # t1 = threading.Thread(target=doThreadFunc)
    # t1.start()
    # t1.join()
    # time.sleep(2)
    print("main quit thread id:%d name:%s process id:%d name:%s" %
                 (t_id, t_name, p_id, p_name))
