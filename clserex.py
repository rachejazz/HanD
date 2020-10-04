import socket

#creating socket
serverSocket=socket.socket()
print("ServerSocket created")

#Linking with IP and port
ip="127.0.0.1"
port=3300#change if occupied
serverSocket.bind((ip,port))
print("Server socket bound with ip {} port {}".format(ip, port))

#Listening
serverSocket.listen()

#Server incomeing connections one by one"
count=0
while(True):
	(clientConnection, clientAddress)=serverSocket.accept()
	count=count+1
	print("Accepted {} connections".format(count))

	#reading client connection
	while(True):
		data=clientConnetion.recv(1024)
		print(data)

		if(data!=b''):
			msg1="Acknowledeged sent data"
			msg1Bytes=str.encode(msg1)

			msg2="Closing connection"
			msg2Bytes=str.encode(msg2)

			clientConnection.send(msg1Bytes)
			clientConnection.send(msg2Bytes)

			print("Connection closed")
			break

