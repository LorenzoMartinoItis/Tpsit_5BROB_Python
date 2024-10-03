import socket
import threading
from threading import Thread

SERVER_ADDRESS=("localhost", 8800) #indirizzo_ip, porta

BUFFER_SIZE = 4092 #massima dimensione trasmissibile

def main():
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #..., socket di tipo UDP

    data="Mi sto connettendo..."
    udp_client_socket.sendto(data.encode(),  SERVER_ADDRESS)
    print(data)

    threadInvio = threading.Thread(target = invio, args=(udp_client_socket,), daemon=True)
    threadRicezione = threading.Thread(target = ricezione, args=(udp_client_socket,), daemon=True)
    
    threadInvio.start()
    threadRicezione.start()
    threadInvio.join()
    threadRicezione.join()
    
    
def invio(udp_client_socket):
    while True:
        data=input("")
        udp_client_socket.sendto(data.encode(), SERVER_ADDRESS)
        
def ricezione(udp_client_socket):
    while True:
        data, _ = udp_client_socket.recvfrom(BUFFER_SIZE)
        print(data.decode())

if  __name__ == "__main__":
    main()
