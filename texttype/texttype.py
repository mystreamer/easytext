from concurrent import futures
from typing import Text

import grpc

from texttype_pb2 import (
    TextType,
    TextTypeResponse,
)

import texttype_pb2_grpc

# NO DS DECLARATION

class TypesService(texttype_pb2_grpc.TypesServicer):

    def GetType(self, request, context):
        texttype = None

        if request.raw_text == "":
            context.abort(grpc.StatusCode.NOT_FOUND, "Empty string provided")
        elif "news" in request.raw_text:
            texttype = TextType.NEWS
        elif "good" in request.raw_text:
            texttype = TextType.OPINION
        elif "should" in request.raw_text:
            texttype = TextType.ADVICE

        return TextTypeResponse(type = texttype)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    texttype_pb2_grpc.add_TypesServicer_to_server(
        TypesService(), server
    )
    server.add_insecure_port("[::]:5005")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()