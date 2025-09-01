import socket

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server_socket.bind(('0.0.0.0', 9000))
server_socket.listen(5)


print("Server listen on port 8080...")


while True:
    client, addr = server_socket.accept()
    print(client, addr)
    print(f"Connection from {addr}")
    client.sendall(b"Hello from server\n")
    client.close()