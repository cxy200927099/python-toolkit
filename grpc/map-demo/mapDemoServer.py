# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 3:30 下午
# @Author  : chenxingyi
# @FileName: mapDemoServer.py

from concurrent import futures
import logging

import grpc

import mapDemos_pb2
import mapDemos_pb2_grpc

class Greeter(mapDemos_pb2_grpc.GreeterMapServicer):

    def SayHello(self, request, context):
        recvMap = request.map
        print("receive map count:%d" % len(recvMap))
        print(recvMap)
        return mapDemos_pb2.MapResponse(resp="success accept map")

def startServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mapDemos_pb2_grpc.add_GreeterMapServicer_to_server(Greeter(), server)
    ip_port = '[::]:50051'
    print("start listen %s" % ip_port)
    server.add_insecure_port(ip_port)
    server.start()
    print("server wait")
    server.wait_for_termination()
    print("server quit")

if __name__ == '__main__':
    logging.basicConfig()
    startServer()