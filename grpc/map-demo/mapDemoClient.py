# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 4:00 下午
# @Author  : chenxingyi
# @FileName: mapDemoClient.py
import logging

import grpc

import mapDemos_pb2
import mapDemos_pb2_grpc


def runClient():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mapDemos_pb2_grpc.GreeterMapStub(channel)
        msgVal1 = mapDemos_pb2.MapObject(mapObj={
            "key1": "val1",
            "key2": "val2",
        })
        msgVal2 = mapDemos_pb2.MapObject(mapObj={
            "key1-1": "val1",
            "key2-2": "val2",
        })
        msg = {
            "t1_key": msgVal1,
            "t1_key": msgVal2,
        }
        print("send msg")
        print(msg)
        response = stub.SayHello(mapDemos_pb2.MapRequest(map=msg))
    print("client receive:%s" % response.resp)


if __name__ == '__main__':
    logging.basicConfig()
    runClient()
