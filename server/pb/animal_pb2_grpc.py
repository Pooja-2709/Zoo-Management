# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
from pb import grpc

from pb import animal_pb2 as animal__pb2


class AnimalServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/animal.AnimalService/create',
                request_serializer=animal__pb2.CreateAnimalRequest.SerializeToString,
                response_deserializer=animal__pb2.CreateAnimalResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/animal.AnimalService/update',
                request_serializer=animal__pb2.UpdateAnimalRequest.SerializeToString,
                response_deserializer=animal__pb2.UpdateAnimalResponse.FromString,
                )
        self.delete = channel.unary_unary(
                '/animal.AnimalService/delete',
                request_serializer=animal__pb2.DeleteAnimalRequest.SerializeToString,
                response_deserializer=animal__pb2.DeleteAnimalResponse.FromString,
                )


class AnimalServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnimalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=animal__pb2.CreateAnimalRequest.FromString,
                    response_serializer=animal__pb2.CreateAnimalResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=animal__pb2.UpdateAnimalRequest.FromString,
                    response_serializer=animal__pb2.UpdateAnimalResponse.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=animal__pb2.DeleteAnimalRequest.FromString,
                    response_serializer=animal__pb2.DeleteAnimalResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'animal.AnimalService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AnimalService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/animal.AnimalService/create',
            animal__pb2.CreateAnimalRequest.SerializeToString,
            animal__pb2.CreateAnimalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/animal.AnimalService/update',
            animal__pb2.UpdateAnimalRequest.SerializeToString,
            animal__pb2.UpdateAnimalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/animal.AnimalService/delete',
            animal__pb2.DeleteAnimalRequest.SerializeToString,
            animal__pb2.DeleteAnimalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)