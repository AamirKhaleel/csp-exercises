#import socket library
import socket
#create socket object using socket method
sckt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print message to show if socket is created
print ("Socket created successfully")
#declare a port value
port=1025
#bind function accepts 2 parameters which is a host and port number
sckt.bind(('',port))
#print a message if binded successfully
print ("socket binded to %s" %(port))
#put socket into listening mode
sckt.listen(5)
#print a message if listening succesfully
print ("socket is listening")
#while statement while true server accept the client socket and address
while True:
    client,address=sckt.accept()
    #print a message if connected to the address
    print ('Got connection from', address)

    #sent message to client
    client.send(bytes("Connected to client", "utf-8"))

    #close the connection with the client
    client.close()
