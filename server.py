from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import socketserver
from typing import Callable
import sys

from middleware import Database

HOST = "127.0.0.1"
PORT = 8081

db = Database("middleware_db.db")

# class Server(socketserver.TCPServer):
#     def __init__(self, server_address: tuple[str, int], RequestHandlerClass: Callable[..., socketserver.BaseRequestHandler], bind_and_activate: bool) -> None:
#         super().__init__(server_address, RequestHandlerClass, bind_and_activate=bind_and_activate)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def server(host, port):
    sock.bind((host, port))
    sock.listen()
    while True:
        try:
            conn, address = sock.accept()
            print(f"Connected to {address}")

            data = conn.recv(1024)
            if not data:
                print(f"Invalid data {data}")
        except KeyboardInterrupt:
            print("Exiting ...")
            break 
        pass


def query_database(query):
    query = query.decode('utf-8')
    db.perform_query(query)


if __name__ == "__main__":      

    # sock_server = Server((HOST, PORT), Callable[..., socketserver.BaseRequestHandler], True)  
    print("Server started http://%s:%s" % (HOST, PORT ))

    # db = Database("middleware_db.db")


   
    server(HOST, PORT)
   
    
    # del db
    print("Server stopped.")