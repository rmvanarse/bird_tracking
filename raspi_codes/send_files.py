"""
Author: Rishikesh Vanarse

Test code for sending audio file from Raspberry Pi to remote server
"""

import socket

audio_s = socket.socket()
host = '192.168.1.6'
port = 8000

audio_s.connect((host, port))
#audio_s.send("Connection Etablished")
print("Connection Etablished")

filename = 'test_audio.mp3'

f= open(filename, 'rb')
print("Sending...")
l = f.read(1024)

while (l):
	audio_s.send(l)
	l = f.read(1024)
f.close()
print("Done sending")
audio_s.close()