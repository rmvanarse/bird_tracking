"""
Author: Rishikesh Vanarse

Test code for recieving audio file from Raspberry Pi

"""

import socket

s = socket.socket()
server_host = '192.168.1.8'
port = 8000

s.bind((server_host, port))

filename = 'audio_copy.mp3'

f= open(filename, 'wb')
s.listen(5)

while True:
	conn, addr = s.accept()
	print("Connection Recieved from ", addr)
	print("Listening...")

	l = conn.recv(1024)

	while (l) :
		f.write(l)
		l = conn.recv(1024)

	f.close()
	print("Recieved")
	conn.send("Completed")
	conn.close()