import socket, json, requests
import api_request

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

def write_data(data, auth_token):
    with open("input.txt", "w+") as f:
        f.write(data+"\n")
        f.write(auth_token)

while True:    
    client_connection, client_address = server_socket.accept()

    req = client_connection.recv(1024).decode()

    data = json.loads(req.split("\n")[-1])
    query = data["inputs"]
    AUTH = data["auth"]
    
    write_data(query, AUTH)
    ret = api_request.main()

    response = f'HTTP/1.0 200 OK\n\n{ret}'
    client_connection.sendall(response.encode())
    client_connection.close()

server_socket.close()
