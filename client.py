#coding = UTF-8
from socket import *
from time import ctime
Host = '127.0.0.1'
Port = 6666
Bufsiz = 1024
addrs = (Host, Port)
tcpserver = socket(AF_INET,SOCK_STREAM)
tcpserver.bind(addrs)
tcpserver.listen(5)

while True:
    print('waiting for connection...')
    tcpclient, addrc = tcpserver.accept()
    print('..connected by ',addrc)
    while True:
        data = tcpclient.recv(Bufsiz)
        if not data:
            break
        print(ctime())
        a = 'Nihao'
        b = 'danshi'
        tcpclient.send(a.encode())
    tcpclient.close()

