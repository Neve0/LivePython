import socket

HOST = 'localhost'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = ""
response = ""
while (message.lower() != 'quit'):
    message = input()
    client.send(message.encode())
    response = client.recv(1024).decode("utf-8")
    print(f"                                 {response}")
    
    