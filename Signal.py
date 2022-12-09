import numpy as np
import pywt
from numpy.fft import fftfreq
from scipy import signal
from scipy.fftpack import fft
from scipy.io import wavfile



class Signal:
    signal = None
    data = None
    sample_rate = None
    start_second = 5
    end_second = 6
    x = None
    y = None
    title_plot = None
    normalized_sig = None
    signal_enve = None
    fftff = None
    recon_sig = None

    def get_signal(self, file_loc):
        self.signal = file_loc
        self.sample_rate, self.data = wavfile.read(self.signal)
        data0 = self.data[:, 0]
        start_time = self.start_second * self.sample_rate
        end_time = self.end_second * self.sample_rate
        time = (len(data0[start_time:end_time]) / self.sample_rate) * 1000
        t = time / (len(data0[start_time:end_time]))
        self.x = [i * t for i in range(len(data0[start_time:end_time]))]
        self.y = data0[start_time:end_time] * t

    def normalize_signal(self):
        avg_sample = np.mean(self.y)
        self.normalized_sig = (self.y - avg_sample) / (max(abs(self.y - avg_sample)))


    def reconstruction(self):
        temp = pywt.wavedec(self.normalized_sig, 'haar', level=4)
        for i in range(1, len(temp)):
            temp[i] = pywt.threshold(temp[i], 0.3 * max(temp[i]), mode='soft')
        self.recon_sig = pywt.waverec(temp, 'haar')


    def env(self):
        absoluteSignal = []
        for sample in self.recon_sig:
            if sample == 0:
                absoluteSignal.append (0)
            else:
                absoluteSignal.append (sample)

        intervalLength = 1
        outputSignal = []

        for baseIndex in range (intervalLength, len (absoluteSignal)):
            maximum = 0
            for lookbackIndex in range (intervalLength):
                maximum = max (absoluteSignal [baseIndex - lookbackIndex], maximum)
            outputSignal.append (maximum)
        self.signal_enve = outputSignal



    def fft_power_freq(self, fs, signal):
        n = signal.shape[0]
        freq, power = fftfreq(n, 1 / fs)[:signal.shape[0] // 2], \
           np.square(np.abs(fft(signal)[:n // 2] / n))
        return freq, power/np.max(power)

    def spektogram(self):

        fs = 1
        f, t, Sxx = signal.spectrogram(self.recon_sig, fs, return_onesided=False)

        return f, t




