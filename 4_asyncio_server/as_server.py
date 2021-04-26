import asyncio


HOST='localhost'
PORT=9094
print('the port {} is available'.format(PORT))

async def handle_echo(reader, writer):
	'''
	функция обработки подключения
	'''
	while True:

		data = await reader.read(100)
		#print('<<<got something>>>')
		message = data.decode()

		print(message)

		if 'exit' in message:
			writer.close()
			print('client is disconnected')


		writer.write(data)
		await writer.drain()

async def main():
	'''
	запуск сервера
	'''
	server = await asyncio.start_server(handle_echo, HOST, PORT)
	await server.serve_forever()


try:
	print('i am alive...')
	asyncio.run(main())
except KeyboardInterrupt:
	pass

server.close()

