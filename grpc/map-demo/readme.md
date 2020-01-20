# 说明
安装
python -m pip install grpcio -i https://mirrors.aliyun.com/pypi/simple/
python -m pip install grpcio-tools -i https://mirrors.aliyun.com/pypi/simple/

## proto文件编译
```python
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. <proto_path>
```
参数说明
-I:
--python_out:
--grpc_python_out:


## python grpc message max size
```python
from concurrent import futures
import grpc
from grpc._cython import _cygrpc as cygrpc
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[(cygrpc.ChannelArgKey.max_send_message_length, -1),
                                                                              (cygrpc.ChannelArgKey.max_receive_message_length, -1)])
```


