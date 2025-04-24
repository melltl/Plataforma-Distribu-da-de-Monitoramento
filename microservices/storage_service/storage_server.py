from concurrent import futures
import grpc
from proto import storage_pb2
from proto import storage_pb2_grpc


class StorageServicer(storage_pb2_grpc.StorageServiceServicer):
    def GetHistoricalData(self, request, context):
        return storage_pb2.DataResponse(data=["Dummy Data 1", "Dummy Data 2"])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    storage_pb2_grpc.add_StorageServiceServicer_to_server(StorageServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()