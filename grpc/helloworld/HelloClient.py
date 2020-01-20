#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/10 2:41 下午
# @Author  : chenxingyi
# @FileName: HelloClient.py

import logging

import grpc

import hello_pb2
import hello_pb2_grpc
# from google.protobuf.wrappers_pb2 import StringValue

def runClient():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.HelloWorldStub(channel)
        person = hello_pb2.Person(name="cxy")
        # msg = StringValue(value="greeter")
        print("send msg")
        # print(msg)
        response = stub.SayHello(hello_pb2.ToBeGreeted(person=person, msg="greeter"))
    print("client receive:%s" % response.message)


if __name__ == '__main__':
    runClient()