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
    
def server(host: str = "0.0.0.0", port: int = 8000):
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listen on port {port}...")

    while True:
        response = """\
        HTTP/1.1 200 OK
        Content-Type: text/html; charset=utf-8

        <html>
            <body>
                <h1>Hello from raw socket HTTP server!</h1>
            </body>
        </html>
        """
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode('utf-8'))
                conn.sendall(response.encode("utf-8"))
            conn.close()
            
def main():
    args = argument()
    server(port=args.p)
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutdown...")