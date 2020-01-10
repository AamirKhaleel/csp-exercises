#import socket module
import socket
#create socket object using socket method
sckt_client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#define port
port=1025
#client connect to server
sckt_client.connect(('127.0.0.1',port))

#recieve data from the server
print (sckt_client.recv(1024))
#close the connection
sckt_client.close()
