import socket

HOST = '127.0.0.1'  
PORT = 8081  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def conect_server(host, port):
    sock.connect((host, port))

def send_data(data):
    data = bytes(data, "utf-8")
    sock.sendall(data)

def receive_data():
    data = sock.recv(1024)
    return data

if __name__ == "__main__":
    conect_server(HOST, PORT)
    send_data("SELECT * FROM HallOfFame")
    data = receive_data()

    print(data)
