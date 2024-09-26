import socket

server_address = ("10.210.0.45", 8800)

BUFFER_SIZE = 4092

udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    message = input("CLIENT: ")
    final_message = "CLIENT:" + message
    
    
    udp_client_socket.sendto(final_message.encode(), server_address)
    
    if message == "break":
        print("CHIUDO LA CHAT...")
        break
    
    data, address = udp_client_socket.recvfrom(BUFFER_SIZE)
    
    print(data.decode())
    
udp_client_socket.close()