"""
Author: Rishikesh Vanarse

Test code for sending audio file from Raspberry Pi to remote server
"""

import socket

audio_s = socket.socket()
host = '192.168.1.7'
port = 8000


audio_s.connect((host, port))
audio_s.send("Test from Raspi")

audio_s.close()
print("Success")