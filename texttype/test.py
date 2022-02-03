import grpc
from texttype_pb2_grpc import TypesStub
from texttype_pb2 import TextTypeRequest, TextType
channel = grpc.insecure_channel("localhost:5005")
client = TypesStub(channel)
request = TextTypeRequest(raw_text="This good !")
ret = client.GetType(request)

print(ret)
