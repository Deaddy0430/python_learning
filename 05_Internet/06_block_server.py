from socket import *
from time import sleep, ctime

s = socket()
s.bind(('localhost', 4001))
s.listen(3)
#将socket设置为非阻塞
s.setblocking(False)
while True:
    print('Waiting for connection...')
    #c, addr = s.accept()    #accpet会存在阻塞，所以可以设置为非阻塞状态
    #设置一下捕获error，这样不会直接程序报错结束
    try:
        c, addr = s.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue
    else:
        print("Connect from", addr)
        #c.setblocking(False)
        while True:
            try:
                data = c.recv(1024).decode()
            except BlockingIOError as ex:
                if str(ex) == '[Errno 35] Resource temporarily unavailable':
                    sleep(1)
                    continue
                raise ex

            if not data:
                break
            print(' ',data)
            c.send(ctime().encode())
        c.close()
s.close()