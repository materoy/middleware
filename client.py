import socket
import scholars
import sys
import re

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
    data = data.decode('utf-8')
    data_list =  eval(data)
    return data_list

def ip_address_validator(raw_ip):
    address = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", raw_ip)
    if address:
        HOST = address.group()
        return HOST
    else:
        print("Please provide a valid IP address")
        prompt_ip()
    
def prompt_ip():
    raw_ip = input("Enter the IP address or hostname of the server:\t")
    return ip_address_validator(raw_ip)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        HOST = ip_address_validator(sys.argv[1])  
        
    else:
        HOST = prompt_ip

    conect_server(HOST, PORT)
    send_data("SELECT * FROM HallOfFame")
    data = receive_data()
    data_list =  eval(data)

    for entity in data_list:
        scholar = scholars.Scholar(entity)
        print(scholar)

