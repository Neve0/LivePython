import socket
import threading


HOST = 'localhost'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
table = {}
lock = threading.Lock()


def runServer():
    while True: 
        connected_adress, connected_ip = server.accept()
        formatted_ipAdress = str(connected_ip[0]) + ":" + str(connected_ip[1]) 
        table[formatted_ipAdress] = connected_adress
        print(f"Connected to {formatted_ipAdress}")

        message = ""
        while (message.lower() != "quit"):
            
            message = connected_adress.recv(1024).decode('utf-8')

            print(f"The message is {message} from {formatted_ipAdress}")
            
            lock.acquire()
            for ip in table.keys():
                if ip != formatted_ipAdress:
                    table[ip].send(message.encode())
            lock.release()
                
            
            
        
        connected_adress.close()
        lock.acquire()
        table.pop(formatted_ipAdress)
        lock.release()
        print(f"Connection closed")

thread_list = []

for _ in range(2):
    thread = threading.Thread(None, runServer)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
