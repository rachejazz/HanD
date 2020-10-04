import socket

#creating socket instance
socketObject=socket.socket()

#Connecting to server
socketObject.connect(("localhost",3300))
print("Connected to localhost")

#Requests sent to webpage
HTTPMessage= "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"
bytes=str.encode(HTTPMessage)
socketObject.sendall(bytes)

#Receiving data
while(True):
	data=socketObject.recv(1024)
	print(data)

	if(data==b''):
		print("Connection closed")
		break
socketObject.close()

