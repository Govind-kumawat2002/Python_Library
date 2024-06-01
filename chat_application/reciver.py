import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = "172.20.10.4"
port_number = 9999 # 0 - 65536
complete_add = (ip_address,port_number)
s.bind(complete_add)
while True:
    message = s.recvfrom(120)
    print(message)
    data = message[0]
    data = "\n"
    print(data.encode("ascii"))
    # with open(ip_address,'a+') as file:
    #     file.write(data)

    

