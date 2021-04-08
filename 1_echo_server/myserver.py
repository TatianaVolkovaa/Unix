import socket

print("Запуск сервера...")
sock = socket.socket()
print("Начало прослушивания порта...")
sock.bind(('', 9090))
sock.listen(1)
print("Подключение клиента...")
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	print("Прием данных от клиента...")
	data = conn.recv(1024)
	if not data or data == "":
		break
	msg += data.decode()
	print("Отправка данных клиенту...")
	conn.send(data.upper())

print(msg)

print("Отключение клиента и oстановка сервера")
conn.close()


