# import wave as wave
# wave_read = wave.open('MoodyLoop.wav', 'r')
# c = wave_read.getnchannels()
# print(wave_read)
# wave_write = wave.open('MoodyLoop.wav', 'w')
from numpy import *
from scipy import *
from pywt import *
import scipy.io.wavfile
from matplotlib.pyplot import *

rate, data = scipy.io.wavfile.read('MoodyLoop.wav')
sin_data = data
data_vec = sin_data.ravel()
print(rate)
print(data_vec)
print(data_vec.size)


def cmorlet(data, freqs, tstep, Fs):
    out = zeros((size(freqs), 10 + round(size(data)/tstep)), dtype = complex128)
    j = 0
    for f in freqs:
        nmax = int(round(2*Fs/f))
        s = linspace(-nmax*f/Fs, nmax*f/Fs, 2*nmax + 1)
        window = exp(-(s**2)/4)*exp(-2*pi*1j*s)
        k = 0
        while(k*tstep+size(window) <= size(data)):
            out[j,k] = abs(f)*sum(window*data[(k*tstep):(k*tstep + size(window))])
            k = k+1
        j= j+1
    return out

y = cmorlet(data_vec, linspace(100, 3000, 1), 128, 8000)

f, arr = subplots(2, 1)
arr[0].plot(sin_data)
arr[1].plot(y)
f.subplots_adjust(hspace = 0.5, wspace = 0.4)
f.set_figwidth(8)
f.set_figheight(8)
show()
imshow(abs(y), 'gray', aspect = 'auto', extent = (0,5, 3000, 100))
show()
