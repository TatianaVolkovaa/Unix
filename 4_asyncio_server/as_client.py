import asyncio
from re import match


def check_ip(ip):
	'''
	функция проверки вводимого айпи
	'''
	if ip=='localhost':
		return False
	else:
		host_ch=r'[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]'
		if ip and match(host_ch, ip):
			return False
		else:
			return True

def check_port(port):
	'''
	функция проверки вводимого порта
	'''
	if 1024<=int(port)<=65525:
		return False
	else:
		return True


async def main(host, port):
	'''
	функция открытия и закрытия соединения с сервером
	'''

	reader, writer = await asyncio.open_connection(host, port)
	
	while True:
		message=input('you: ')
		writer.write(message.encode())

		if 'exit' in message:
			write.close()
			print('disconnected')
			break

		data = await reader.read(100)
		print('S: server got {}'.format(data.decode() ))


if __name__ == '__main__':

	while True:
		'''
		ввод хоста
		'''
		host = input('input your host: ')
		C=check_ip(host)
		if C==False:
			break
		else:
			print('try again')

	while True:	
		'''
		ввод порта
		'''
		port = input('input your port: ')
		C2=check_port(port)
		if C2==False:
			break
		else:
			print('try again')

	try:
		asyncio.run(main(host,port))
		print('the message is sent...')
	except:
		print('connection is lost')

