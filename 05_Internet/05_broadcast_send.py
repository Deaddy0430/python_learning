from socket import *
from time import sleep
#设置目标地址
dest = ('192.168.137.45', 9999)
s = socket(AF_INET, SOCK_DGRAM)
#设置发送广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    sleep(2)
    s.sendto("来呀，带你去看晴空万里".encode(), dest)
s.close()