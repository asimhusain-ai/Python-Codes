import socket
s = socket.socket()
print("Socket Is Created")
port = 12345
s.bind('',port)
print("Bind to %s"%(port))
s.listen(5)
print("Listening to ")
while True:
    addr = s.accept()
    print("",addr)
    s.send("Got Connection".encode())
    s.close()
    break