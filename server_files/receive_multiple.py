"""
Author: Rishikesh Vanarse

Test code for recieving multiple audio files from Raspberry Pi
Current version: Copy of rec_audio.py

Plan: Receive --> Process --> Delete

"""

import socket

s = socket.socket()
server_host = '192.168.1.6'
port = 8000

s.bind((server_host, port))

base_filename = 'current_audio_copy'

f= open(base_filename, 'wb')
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
	#conn.send("Completed")
	conn.close()