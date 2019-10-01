from socket import *

#创建套接字
s = socket(AF_INET, SOCK_DGRAM)
#设置套接字可以发送接收广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
