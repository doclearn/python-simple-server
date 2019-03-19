import socket


try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 8000))
    server.listen(8)
    print("Server Started!")
except:
    print("Error starting server!")

while True:
    c, a = server.accept()
    print (a[0] + " connected!")
