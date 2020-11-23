import socket

socket = socket.socket()
socket.bind(('127.0.0.1', 8080))
socket.listen(5)

while True:
    conn, addr = socket.accept()
    data = conn.recv(8096)
    print(data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    conn.send(b'123')
    conn.close()
