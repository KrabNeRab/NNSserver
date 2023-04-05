import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(1)
sock.connect(('localhost', 5050))

msg = None

while msg != 'end':
    msg = str(input('1)Ввести новые данные 2)Поиск (end чтобы закончить работу сервера): '))
    sock.send(msg.encode())

    if msg == '1':
        nns = input('Введите ФИО: ')
        job = input('Место работы: ')
        job_title = input('Должность: ')
        msg1 = nns + ' ' + job + ' ' + job_title
        sock.send(msg1.encode('utf-8'))

    if msg == '2':
        nns = input('Введите ФИО: ')
        msg2 = nns
        sock.send(msg2.encode('utf-8'))
        data = sock.recv(1024)
        print(data)

print('Работа с сервером закончена')
sock.close()
