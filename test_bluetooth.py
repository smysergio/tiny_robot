import bluetooth #https://people.csail.mit.edu/albert/bluez-intro/x232.html

MAC = "B4:9D:0B:5F:C1:3E"

# initialize bluetooth communication
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind((MAC,1))
server_sock.listen(1)
while(1):
	# wait for a client to connect
	client_sock,address = server_sock.accept()
	while(client_sock):
		# listen for message
		try:
			msg = client_sock.recv(8)
		except bluetooth.btcommon.BluetoothError:
			break
		print msg
		time.sleep(10)