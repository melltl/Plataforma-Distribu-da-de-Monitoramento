import grpc
from proto import storage_pb2
from proto import storage_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = storage_pb2_grpc.StorageServiceStub(channel)
    
    try:
        response = stub.GetHistoricalData(storage_pb2.DataRequest(sensor_id="temp_001"))
        print("Historical data received: ", response.data)
    except grpc.RpcError as e:
        print(f"Error: {e.code()}: {e.details()}")

if __name__ == '__main__':
    run()