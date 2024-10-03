import socket
import threading
from threading import Thread

SERVER_ADDRESS=("localhost", 8800) #indirizzo_ip, porta

BUFFER_SIZE = 4092 #massima dimensione trasmissibile

def main():
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #..., socket di tipo UDP

    udp_server_socket.bind(SERVER_ADDRESS) #vado a legare il socket all'ip e alla porta del server, in questo caso accetta connessioni a qualsiasi ip del pc

    data, client_address = udp_server_socket.recvfrom(BUFFER_SIZE)
    print(data.decode())
    
    threadInvio = threading.Thread(target = invio, args=(udp_server_socket, client_address), daemon=True)
    threadRicezione = threading.Thread(target = ricezione, args=(udp_server_socket,), daemon=True)
    
    threadInvio.start()
    threadRicezione.start()
    threadInvio.join()
    threadRicezione.join()
    
    
def invio(udp_server_socket, client_address):
    while True:
        data = input("")
        udp_server_socket.sendto(data.encode(), client_address)
        
def ricezione(udp_server_socket):
    while True:
        data, client_address = udp_server_socket.recvfrom(BUFFER_SIZE)
        print(data.decode())

if  __name__ == "__main__":
    main()
