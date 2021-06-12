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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def server(host, port):
    sock.bind((host, port))
    sock.listen()
    while True:
        try:
            conn, address = sock.accept()
            print(f"Connected to {address}")

            data = conn.recv(1024)
            print(f"Received query {data}")
            query_results = query_database(data)
            query_results = bytes(query_results, 'utf-8')
            conn.sendall(query_results)

            if not data:
                print(f"Invalid data {data}")
                break
        except KeyboardInterrupt:
            print("Exiting ...")
            break 
        pass


def query_database(query):
    query = query.decode('utf-8')
    return db.perform_query(query)


if __name__ == "__main__":      

    print(f"Server started   {HOST} {PORT}")

    db = Database("middleware_db.db")

    server(HOST, PORT)
   
    
    del db
    print("Server stopped.")