import json
import socket

data = {
    "first": 2,
    "second": 3,
    "third": 1,
    "fourth": 4
}

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

json_data = json.dumps(data)
client_socket.send(json_data.encode('utf-8'))

sorted_response = client_socket.recv(1024).decode('utf-8')
sorted_values = json.loads(sorted_response)

print("Sorted values:", sorted_values)

client_socket.close()
