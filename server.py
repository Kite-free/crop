#coding = UTF-8
from socket import *
Host = 'localhost'
port = 6666
bufsiz = 1024
addr = (Host,port)
tcpclient = socket(AF_INET,SOCK_STREAM)
tcpclient.connect(addr)
while True:
    data = input('请输入')
    if not data:
        break
    tcpclient.send(data.encode())
    data = tcpclient.recv(bufsiz)
    if not data:
        break
    print(data.decode())
tcpclient.close()