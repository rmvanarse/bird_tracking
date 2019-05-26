"""
Author: Rishikesh Vanarse

Test code for sending audio file from Raspberry Pi to remote server
"""

import socket

audio_s = socket.socket()
host = '192.168.1.7'
port = 8000


audio_s.connect((host, port))
audio_s.send("Connection Established")

filename = 'TestFile'
f = open(filename, 'rb')
l = f.read(1024)

while (l):
	audio_s.send(l)
	print("sent:", l)
	l = f.read(1024)
f.close()
print("Done Sending")

audio_s.close()
print("Success")