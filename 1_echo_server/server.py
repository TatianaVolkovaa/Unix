import socket
import logging
from datetime import datetime

class Server:
    def __init__(self):
        self.users = {}
        self.logger = self.get_logger()
        self.sock = socket.socket()
        self.port = 9090
        self.conn = None
        self.pass_key = 0
        self.k = 1

    def get_users(self):
        try:
            f = open("users.txt")
            for line in f:
                rr = line.split(":")
                spis = []
                spis.append(rr[1])
                spis.append(rr[2][:len(rr[2]) - 1])
                self.users[rr[0]] = spis
            f.close()
        except:
            self.users = {}

    def get_logger(self):
        logger = logging.getLogger("server")
        logger.setLevel(logging.INFO)
        file_hanlder = logging.FileHandler("server.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_hanlder.setFormatter(formatter)
        logger.addHandler(file_hanlder)
        return logger

    def set_port(self):
        while True:
            port = input("введите порт -> ")
            if port == "def":
                port = 9090
                break
            elif port.isdigit() and 0 < int(port) < 65535:
                break
            else:
                print("ошибка!")
        self.port = int(port)
        while self.port < 65535:
            if self.port >= 65535:
                raise AssertionError("все порты заняты")
            try:
                self.sock.bind(('', int(self.port)))
                break
            except socket.error:
                self.port += 1

    def write_users(self):
        try:
            f = open("users.txt", "w")
            for line in self.users.items():
                f.write(str(line[0]) + ":" + str(line[1][0]) + ":" + str(line[1][1]) + "\n")
            f.close()
        except:
            pass

    def listen(self):
        while True:
            self.write_users()
            if self.k == 1:
                self.conn, addr = self.sock.accept()
                user_port = addr[0]
                if user_port in self.users:
                    self.conn.send("SERVER -> привет, ".encode() + self.users[user_port][0].encode() + "\n введите пароль -> ".encode())
                else:
                    self.conn.send("SERVER -> привет! введи имя и пароль через пробел:".encode())
                self.logger.info(f'клиент {str(addr)} подключен')
                print(f'клиент {str(addr)} подключен')
                self.k = 0
            else:
                try:
                    data = self.conn.recv(1024)
                    if not data:
                        self.logger.info("отключение клиента...")
                        print("клиент отключился")
                        self.k = 1
                        self.pass_key = 0
                        self.conn.close()
                    elif self.pass_key == 0:
                        if user_port in self.users:
                            if str(data.decode()[9:]) == self.users[addr[0]][1]:
                                self.conn.send("SERVER -> пароль верен".encode())
                                self.pass_key = 1
                            else:
                                self.pass_key = 0
                                self.k = 1
                                self.conn.send("SERVER -> пароль неверен".encode())
                                self.conn.close()
                        else:
                            info = str(data.decode())[9:]
                            r = []
                            try:
                                r.append(info.split()[0])
                                r.append(info.split()[1])
                                self.users[addr[0]] = r
                                print("новый пользователь " + str(info.split()[0]))
                                self.conn.send("SERVER -> пользователь зарегистрирован".encode())
                                self.pass_key = 1
                            except IndexError:
                                self.conn.send("SERVER -> введите имя и пароль через пробел!".encode())
                                self.pass_key = 0

                    else:
                        key = input("для выключения сервера, напишите что-то кроме enter")
                        info = data.decode()[9:]
                        print("данные получены: " + info)
                        print(f"длина данных: {len(data.decode()[9:])}")
                        self.logger.info("данные получены:")
                        self.conn.send("SERVER -> ".encode() + info.upper().encode())
                        self.logger.info("отправка данных клиенту...")
                        if key != "":
                            break
                except ConnectionError:
                    print("клиент отключен")
                    self.logger.info("отключение клиента...")
                    self.k = 1
                    self.pass_key = 0
                    self.conn.close()

    def main(self):
        self.get_users()
        self.set_port()
        print(f"пользователи: {self.users}")
        print("сервер запущен!")
        self.logger.info("сервер запущен!")
        self.logger.info(f'начало прослушивание порта {str(self.port)}')
        self.sock.listen(1)
        self.listen()
        self.logger.info("соединение закрыто!")
        print("закрыли соединение")

        self.logger.info("остановка сервера...")
        self.conn.send("SERVER -> ".encode() + "отключение...".encode())
        self.conn.close()
        self.sock.close()

server = Server()
server.main()
