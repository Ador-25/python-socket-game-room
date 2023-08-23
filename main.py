import json
import socket

def sort_json(json_data):
    sorted_data = sorted(json_data.values())
    return sorted_data

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening on {}:{}".format(host, port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)

        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(data)

        try:
            json_data = json.loads(data)
            sorted_values = sort_json(json_data)
            sorted_response = json.dumps(sorted_values)
            client_socket.send(sorted_response.encode('utf-8'))
        except Exception as e:
            print("Error:", e)
        print('came here')
        client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
