import socket  # socket library in Python is used for network communication,allowing programs to communicate with each other over a network. 
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #  Used for IPv4 addresses. This is the most commonly used address family and is represented by a 32-bit address. 
    # SOCK_DGRAM: This type of socket is used for connectionless, unreliable messages. This means that data is sent as individual packets (datagrams) and no connection is established between the client and server. 
    ip_address = "172.20.10.4"
    port_number = 9999 # 0 - 65536
    target_add = (ip_address,port_number)
    message = input("kya msg kroge: ")
    message.encode('ascii')
    encripted_message = message.encode('ascii')
    s.sendto(encripted_message,target_add)
except Exception as e:
    print("bhaii kya huwa msg nhi kiya ")

# port dynamic nature (change hote rhte hai )