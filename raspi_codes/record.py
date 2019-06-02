"""
Author: Rishikesh Vanarse

Record audio and sav to a wav file
Requires: souddevice, scipy
"""


import sounddevice as sd
import numpy as np 
import scipy.io.wavfile as wav



filename = 'recorded_audio'
sample_rate = 40000
duration = 5 #No. of seconds

recording = sd.rec(duration * sample_rate, samplerate = sample_rate, channels =2, dtype = 'float64')

print("Recording")
sd.wait()
print("recording complete")
#sd.play(recording, sample_rate)

f = open(filename, 'wb')
wav.write(filename, sample_rate, recording)
f.close()


#sd.wait()
print("Success")