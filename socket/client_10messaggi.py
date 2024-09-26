import socket

server_address = ("10.210.0.45", 8800)

BUFFER_SIZE = 4092

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for _  in range(10):
    
    message = "Messaggio"

    udp_client_socket.sendto(message.encode(), server_address)
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)

    print(f"Messaggio ritornato: {data.decode()}")
    
udp_client_socket.close()