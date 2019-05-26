"""
Author: Rishikesh Vanarse

Test code for recieving audio file from Raspberry Pi

"""

import socket

port = 8000

audio_s = socket.socket()
server_host = '192.168.1.7'

audio_s.bind((server_host, port))

audio_s.listen(5)

while True:
	connection, address = audio_s.accept()
	print("Connection successful")
	data = connection.recv(1024)
	print("Recieved: ", repr(data))

	print('Done Sending')
	connection.close()