from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/1plot')
def plot1():
    return render_template('1plot.html')