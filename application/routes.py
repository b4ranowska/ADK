from application import app
from flask import render_template, url_for
from Signal import Signal
import pandas as pd
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

    # Graph One
    df = px.data.medals_wide()
    fig1 = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('1plot.html', title='plots', graph1JSON=graph1JSON)

