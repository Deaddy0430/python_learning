from socket import *

#create socket
sockfd = socket(AF_INET, SOCK_STREAM)
 
#commit connection
server_addr = ('localhost', 9897)
sockfd.connect(server_addr)

while True:
    #send & recv data
    data = input("发送>>")
    sockfd.send(data.encode())  #encode -> transfer to 'byte' type
    if data == '##':
        break
    data = sockfd.recv(1024)
    print(data.decode())

#close socket
sockfd.close() 