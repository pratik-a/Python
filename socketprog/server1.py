import socket

s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))

s.listen(3)
print("wating for connection")

while True:
    c, addr = s.accept()
    print("connected with add", addr)

    c.send(bytes("hello from server", "utf-8"))
    c.close()