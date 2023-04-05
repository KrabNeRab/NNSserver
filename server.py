import socket
import re

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 5050))
sock.listen(0)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024).decode()
    if 'end'.encode() in data.encode():
        break

    if '1'.encode() in data.encode():
        msg1 = conn.recv(1024).decode('utf-8')
        f = open('NNS.txt', 'a')
        f.writelines(msg1 + '\n')
        f.close()
    if '2'.encode() in data.encode():
        msg2 = conn.recv(1024).decode('utf-8')
        f = open('NNS.txt', 'r')
        file = f.read().splitlines()
        for i in file:
            if msg2 in i:
                conn.send(i.encode())
            else:
                no_data = 'no data'
                conn.send(no_data.encode())
                continue

        f.close()

conn.close()
