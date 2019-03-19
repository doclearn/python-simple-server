#client side
import socket#inport the socket library

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Defines servers characteristics
#AF_INET means it uses ip4 address to connect
#SOCK_STREAM means it uses tcp connections


ip = input("Enter IP Address: ") #ask the user the ip address of the host.
port = 8000
#pre defined port
try:
    server.connect((ip, port)) #connects to the server
    print("Connected to " + ip)#prints if connection is successful
except:
    print("Error")#print if cnnection is unsuccessful







