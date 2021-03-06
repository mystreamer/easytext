# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import texttype_pb2 as texttype__pb2


class TypesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetType = channel.unary_unary(
                '/Types/GetType',
                request_serializer=texttype__pb2.TextTypeRequest.SerializeToString,
                response_deserializer=texttype__pb2.TextTypeResponse.FromString,
                )


class TypesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TypesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetType': grpc.unary_unary_rpc_method_handler(
                    servicer.GetType,
                    request_deserializer=texttype__pb2.TextTypeRequest.FromString,
                    response_serializer=texttype__pb2.TextTypeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Types', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Types(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Types/GetType',
            texttype__pb2.TextTypeRequest.SerializeToString,
            texttype__pb2.TextTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
