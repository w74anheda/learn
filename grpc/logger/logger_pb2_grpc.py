# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import logger_pb2 as logger__pb2


class LoggerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LogStore = channel.unary_stream(
                '/Logger/LogStore',
                request_serializer=logger__pb2.FRequest.SerializeToString,
                response_deserializer=logger__pb2.Log.FromString,
                )


class LoggerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LogStore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LoggerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LogStore': grpc.unary_stream_rpc_method_handler(
                    servicer.LogStore,
                    request_deserializer=logger__pb2.FRequest.FromString,
                    response_serializer=logger__pb2.Log.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Logger', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Logger(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LogStore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Logger/LogStore',
            logger__pb2.FRequest.SerializeToString,
            logger__pb2.Log.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
