"""
Author: Rishikesh Vanarse

Record audio and sav to a wav file
Requires: souddevice, scipy
"""


import sounddevice as sd
import numpy as np 
import scipy.io.wavfile as wav 

import socket

filename = 'recorded_audio'
sample_rate = 40000
duration = 5 #No. of seconds
num_files = 5 #No. of files to send (temp)

#recording = sd.rec(duration * sample_rate, samplerate = sample_rate, channels =2, dtype = 'float64')

#Establish Connection
audio_s = socket.socket()
host = '192.168.1.6'  #Change IP
port = 8000

audio_s.connect((host, port))
#audio_s.send("Connection Etablished")
print("Connection Established")

#Record and Send
i=1
while True:
	
	#Record
	recording = sd.rec(duration * sample_rate, samplerate = sample_rate, channels =2, dtype = 'float64')

	print("Recording", i)
	sd.wait()
	print("recording complete")
	
	f = open(filename + str(i), 'wb')
	wav.write(filename+ str(i), sample_rate, recording)
	f.close()

	#Send
	f= open(filename + str(i), 'rb')
	print("Sending...")
	l = f.read(1024)
	
	while (l):
		audio_s.send(l)
		l = f.read(1024)
	f.close()
	print("Done sending: audio #"+ str(i+1))
	#audio_s.close()

	#Random exit condition
	if i >= num_files:
		break
	i = i+1

audio_s.close()


#sd.play(recording, sample_rate)




#sd.wait()
print("Success")