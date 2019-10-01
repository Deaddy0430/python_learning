#============================================可循环收发============================================

#wildcard import
from socket import *
#create a socket
sockfd = socket(AF_INET, SOCK_STREAM)

#bind the address
sockfd.bind(( '0.0.0.0', 9896))  #addr -> (ip, port)

#setup listen
sockfd.listen(5)

#waiting for accept for connection
while True:
    print("WAITING FOR CONNECT...")
    connfd, addr = sockfd.accept()
    print("Connect from", addr)
    while True:
        #recv&send
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        n = connfd.send(b'Receive your message')
        print("%d of bytes was sent" % n)
#close socket
    connfd.close()
sockfd.close()