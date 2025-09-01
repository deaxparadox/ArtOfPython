import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9000))
client_socket.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
response = client_socket.recv(4096)
print(response.decode())
client_socket.close()