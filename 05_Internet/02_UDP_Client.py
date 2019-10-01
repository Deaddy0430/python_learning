from socket import *
import sys

if len(sys.argv) < 3:
    print('''
        argv is error!
        please try in format:
        python3 udp_client.py 127.0.0.1 8888
    ''')

host = sys.argv[1]
port = int(sys.argv[2])
addr = (host, port)

#create socket
sockfd = socket(AF_INET, SOCK_DGRAM)

#send/recv
while True:
    data = input("消息： ")
    if not data:
        break
    sockfd.sendto(data.encode(), addr)
    data, addr = sockfd.recvfrom(1024)
    print("从服务器收到： ", data.decode())
sockfd.close()