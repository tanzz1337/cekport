import socket

ip = input("Masukkan IP target: ")
port = int(input("Masukkan port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)

def portscanner(port):
    if client.connect_ex((ip, port)):
        print("Port", port, "closed")
    else:
        print("Port", port, "open")

for port in range(1, 65535):
    portscanner(port)
