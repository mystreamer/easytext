## EasyText
### An exercise in gRPC

This is a simple project where I aim to learn the fundamentals of writing a gRPC API.

Running the RPC Server:

```
cd easytext/texttype && python texttype.py
```

**Don't forget to install the dependencies through:**

```
python -m pip install requirements.txt
```

Run:

```
python test.py
```

To verify that the server is running.


Rebuilding the proto buffers after changes to the .proto files:

```
cd texttype
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/texttype.proto

