from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import socketserver
from typing import Callable
import sys

from middleware import Database



db = Database("middleware_db.db")

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address

HOST = get_ip_address()
PORT = 8081

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

            # Sends the queried results back to the client
            send_response(conn, query_results)

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

def send_response(conn, query_results):
     scholars = []
     for result in query_results:
         scholars.append(result)

     scholars = bytes(str(scholars), 'utf-8')
     conn.sendall(scholars)

if __name__ == "__main__":      

    print(f"Server started   {HOST} {PORT}")

    db = Database("middleware_db.db")

    server(HOST, PORT)
    
    del db
    print("Server stopped.")
    