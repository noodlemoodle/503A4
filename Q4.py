# import wave as wave
# wave_read = wave.open('MoodyLoop.wav', 'r')
# c = wave_read.getnchannels()
# print(wave_read)
# wave_write = wave.open('MoodyLoop.wav', 'w')
import numpy as np
import scipy.io.wavfile
from matplotlib.pyplot import *

rate, data = scipy.io.wavfile.read('MoodyLoop.wav')
sin_data = np.sin(data)
print(rate)
print(data)
print(data.size)
plot(data)
show()
