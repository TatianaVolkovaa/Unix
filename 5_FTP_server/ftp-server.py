import socket
import os
import shutil

'''
+pwd - показывает название рабочей директории
+ls - показывает содержимое текущей директории
+exit - выход
+createdir <dirname> - создает новую папку
+deletefile <filename> - удаляет файл
+deletedir <dirname> - удаляет папку
+send <filename> - копирует файл с клиента на сервер
+get <filename> - копирует файл с сервера на клиент
'''

dirname = os.path.join(os.getcwd(), 'docs')

def process(req):

    if req == 'pwd':
        return dirname

    elif req == 'ls':
        return '; '.join(os.listdir(dirname))

    elif req == 'exit':
        return req

    elif req[:9] == 'createdir':
        s = os.path.join(os.getcwd(), 'docs', req[10::])
        if os.path.isdir(s) == False:
            os.mkdir(s)
            return("Created a directory")
        else:
            return("Directory with such name already exists")

    elif req[:10] == 'deletefile':
        s = os.path.join(os.getcwd(), 'docs', req[11::])
        try:
            os.remove(s)
            return("Deleted the file")
        except:
            return("There's no such file in the directory")

    elif req[:9] == 'deletedir':
        s = os.path.join(os.getcwd(), 'docs', req[10::])
        try:
            os.rmdir(s)
        except:
            return("The directory is not empty")
        else:
            return("The directory has been deleted")

    elif req[:4] == 'send':
        s = os.path.join(os.getcwd(), 'docs', req[5::])
        a = os.getcwd()
        try:
            shutil.copy(s, a)
            return("The file was copied to the server")
        except:
            return("There's no such file in the directory")

    elif req[:3] == 'get':
        s = os.path.join(os.getcwd(), 'docs')
        a = os.path.join(os.getcwd(), req[4::])
        try:
            shutil.copy(a, s)
            return("The file was copied from the server")
        except:
            return("There's no such file on the server")


PORT = 8888

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
print("Прослушиваем порт", PORT)

while True:
    conn, addr = sock.accept()
    
    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)
    conn.send(response.encode())

conn.close()
