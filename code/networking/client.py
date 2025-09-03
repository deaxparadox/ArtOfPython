import argparse
import socket

def argument():
    arg = argparse.ArgumentParser()
    arg.add_argument(
        "-p",
        type=int,
        default=8000,
        help="Port number to listen"
    )
    return arg.parse_args()

def main(*, host: str = "localhost", port: int = 8000):
    payload = """
    GET / HTTP/1.1
    Host: localhost:8080
    User-Agent: ...
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(payload.encode('utf-8'))
    response = client_socket.recv(4096)
    print(response.decode())
    client_socket.close()
    
if __name__ == '__main__':
    args = argument()
    main(port=args.p)