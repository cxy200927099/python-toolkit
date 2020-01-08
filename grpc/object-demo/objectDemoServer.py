# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 10:30 上午
# @Author  : chenxingyi
# @FileName: objectDemoServer.py

from concurrent import futures
import logging

# from utils import logUtil
import grpc
import sys
import objectDemos_pb2_grpc
import objectDemos_pb2

import typing
import threading
import os
import psutil
import time
import warnings
import processUtil
import multiprocessing

def init_log():
    # ignore spleeter warning
    warnings.filterwarnings('ignore')

    # init log
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(filename)s:%(lineno)d:%(message)s",
        level=logging.DEBUG)
    logging.info("log init!")

def getThreadInfo() -> typing.Tuple[str, str]:
    t = threading.currentThread()
    return t.ident, t.name

def getProcessInfo() -> typing.Tuple[str, str]:
    pid = os.getpid()
    p = psutil.Process(pid)
    return p.pid, p.name()

def doTimeConsumingTask(tag:str, data:typing.Dict[str, typing.List[str]]):
    t_id, t_name = getThreadInfo()
    p_id, p_name = getProcessInfo()
    logging.info("thread id:%d pid:%d doTimeConsumingTask receive %s" %
                 (t_id, p_id, tag))
    time.sleep(5)
    logging.info("thread id:%d pid:%d doTimeConsumingTask done %s" %
                 (t_id, p_id, tag))

class UpdateUser(objectDemos_pb2_grpc.UpdateUserModelServicer):

    def UpdateUserModel(self, request, context):
        recv_data_map = request.usersAttr
        t_id, t_name = getThreadInfo()
        p_id, p_name = getProcessInfo()
        logging.info("thread id:%d pid:%d UpdateUserModel receive data" %
                     (t_id, p_id))
        # multiProcess.doAsyncJob(doTimeConsumingTask, args=(recv_data_map,))
        pass_data = {}
        start_ms = int(round(time.time() * 1000))
        for (_k, _v) in recv_data_map.items():
            tmp_list = []
            for i in range(len(_v.userData)):
                tmp_list.append(_v.userData[i])
            pass_data[_k] = tmp_list
        ts = int(round(time.time() * 1000)) - start_ms
        # logging.info("convert data ts:%d ms" % ts)
        tag = int(round(time.time() * 1000))
        # 异步执行，这里比较坑，当传递的args类型，参数个数有所不同，doTimeConsumingTask不会被执行
        # 推测可能是内部抛异常了，当时没有任何反馈，可以传入error_callback
        pool.apply_async(doTimeConsumingTask, args=(str(tag), pass_data,))
        resp = objectDemos_pb2.UserRawDataResponse(code=0, errMsg='')
        return resp


def startServer():
    # global multiprocess
    # multiProcess = processUtil.ProcessUtil(process_cnt=2)
    global pool
    pool = multiprocessing.Pool(processes=2)
    logging.info("main pool:%s" % pool.__str__())

    _OPTION = [
        ('grpc.max_send_message_length', 16 * 1024 * 1024),
        ('grpc.max_receive_message_length', 16 * 1024 * 1024)
    ]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=_OPTION)
    objectDemos_pb2_grpc.add_UpdateUserModelServicer_to_server(UpdateUser(), server)

    t_id, t_name = getThreadInfo()
    p_id, p_name = getProcessInfo()
    logging.info("thread id:%d name:%s process id:%d name:%s" % (
    t_id, t_name, p_id, p_name))

    ip_port = '[::]:50052'
    logging.info("start listen %s" % ip_port)
    server.add_insecure_port(ip_port)
    server.start()
    logging.info("server wait")
    server.wait_for_termination()
    logging.info("server quit")

if __name__ == '__main__':
    init_log()
    startServer()