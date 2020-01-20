#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/10 2:35 下午
# @Author  : chenxingyi
# @FileName: HelloServer.py

from concurrent import futures
import logging

import grpc

import hello_pb2
import hello_pb2_grpc


class Greeter(hello_pb2_grpc.HelloWorldServicer):

    def SayHello(self, request, context):
        print("receive %s msg:%s" %(request.person.name, request.msg))
        return hello_pb2.Greeting(message="hi %s" % request.person.name)

def startServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloWorldServicer_to_server(Greeter(), server)
    ip_port = '[::]:50051'
    print("start listen %s" % ip_port)
    server.add_insecure_port(ip_port)
    server.start()
    print("server wait")
    server.wait_for_termination()
    print("server quit")

if __name__ == '__main__':
    startServer()