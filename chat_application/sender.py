import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = "172.20.10.4"
port_number = 9999 # 0 - 65536
target_add = (ip_address,port_number)
message = input("kya msg kroge: ")
message.encode('ascii')
encripted_message = message.encode('ascii')
s.sendto(encripted_message,target_add)

# port dynamic nature (change hote rhte hai )