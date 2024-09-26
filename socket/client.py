import socket

server_address = ("192.168.1.124", 8800)

BUFFER_SIZE = 4092

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Messaggio"

udp_client_socket.sendto(message.encode(), server_address)
data, address = udp_client_socket.recvfrom(BUFFER_SIZE)

print(f"Messaggio ritornato: {data.decode()}")