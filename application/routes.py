from application import app
from flask import render_template
from Signal import Signal
import json
import plotly
import plotly.express as px


@app.route('/')
def index():
    return render_template('index.html', title='home')

@app.route('/audio')
def audio():
    return render_template('audio.html', title='audio')

@app.route('/1plot')
def plot1():
    # Graph 1 -> input signal after lowpass filter
    signal = Signal()
    signal.get_signal('C:/Users/marce/PycharmProjects/ADK/application/static/nagranie_1.wav')
    signal.normalize_signal()
    signal.reconstruction()
    signal_reconstructed = signal.recon_sig
    x = signal.x
    list_sig = list(signal_reconstructed)

    fig1 = px.line(x=x, y=list_sig,
                   labels={
                       'x': 'Czas [ms]',
                       'y': 'Amplituda'},
                   title="Wykres sygnału fonokardiograficznego po filtrze lowpass")



    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph 2 -> signal after FFT
    signal2 = Signal()
    signal2.get_signal('C:/Users/marce/PycharmProjects/ADK/application/static/nagranie_1.wav')
    signal2.normalize_signal()
    signal2.reconstruction()
    signal_reconstructed = signal2.recon_sig
    fs = signal2.sample_rate
    freq, power = signal2.fft_power_freq(fs, signal_reconstructed)
    sig_freq = list(freq[:1000])
    sig_power = list(power[:1000])

    fig2 = px.line(x=sig_freq, y=sig_power,
                   labels={
                       'x': 'Częstotliwość [Hz]',
                       'y': 'Moc'},
                   title='Widmo sygnału fonokardiograficznego')

    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('1plot.html', title='plots', graph1JSON=graph1JSON,
                                                        graph2JSON=graph2JSON)


