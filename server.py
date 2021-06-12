from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import socketserver
from typing import Callable
import sys

from middleware import Database

HOST = "localhost"
PORT = 8080
exit = False

db = Database("middleware_db.db")

class Server(socketserver.TCPServer):
    def __init__(self, server_address: tuple[str, int], RequestHandlerClass: Callable[..., socketserver.BaseRequestHandler], bind_and_activate: bool) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate=bind_and_activate)

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()

    conn, address = sock.accept()
    print(f"Connected to {address}")

    try:
        while True :
            data = conn.recv(1024)
            if not data:
                break
    except KeyboardInterrupt:
        sys.exit()


def query_database(query):
    db.perform_query(query)


if __name__ == "__main__":      

    # sock_server = Server((HOST, PORT), Callable[..., socketserver.BaseRequestHandler], True)  
    print("Server started http://%s:%s" % (HOST, PORT + 1))

    db = Database("middleware_db.db")


    try:
        # socket_server.serve_forever()
        server(HOST, PORT)
        pass
    except KeyboardInterrupt:
        pass
    
    del db
    exit = True
    print("Server stopped.")