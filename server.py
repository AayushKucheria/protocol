import socket

s = socket.socket()

# Hostname is a label assigned to a device connected to a network
host = socket.gethostname()

# Port identifies a specific process
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you fro connecting'.encode())
    c.close()

