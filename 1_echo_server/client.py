from socket import *

class Client:
    def __init__(self):
        self.sock = socket(SOCK_DGRAM)
        self.port = self.get_port()
        self.host = self.get_host()
        self.pass_key = 0

    def get_port(self):
        while True:
            port = input("port -> ")
            if port == "def":
                port = 9090
                break
            elif port.isdigit() and 1023 < int(port) < 65535:
                break
            else:
                print("error!")
        return int(port)


    def get_host(self):
        while True:
            host = input("host -> ")
            if host == "":
                host = "localhost"
            try:
                print(host, self.port)
                self.sock.connect((host, int(self.port)))
                break
            except Exception as e:
                print(e)
                print("cannot connect :(")
        return host

    def listen(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print("data from server -> " + data.decode()[8:])
                    if data.decode()[8:] == "пароль неверен":
                        break
                    print(f"length of data: {len(data.decode()[8:])}")
                else:
                    print("server stopped")
                    break
                key = input("enter msg-> ")
                if key == "exit":
                    break
                self.sock.send("CLIENT 1:".encode() + key.encode())
            except:
                break

    def main(self):
        print("connected!")
        self.listen()
        print("disconnecting...")
        self.sock.close()

client = Client()
client.main()