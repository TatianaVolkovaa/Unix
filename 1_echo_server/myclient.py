import socket
from time import sleep

sock = socket.socket()
#sock.setblocking(1)
print("Соединение с сервером...")
sock.connect(('localhost', 9090))

msg = input("Введите сообщение: ")
print("Отправка данных серверу")
sock.send(msg.encode())
print("Прием данных от сервера")
data = sock.recv(1024)

print("Разрыв соединения с сервером")
sock.close()

print(data.decode())


