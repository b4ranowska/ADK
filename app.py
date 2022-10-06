from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/1plot')
def plot1():
    return render_template('1plot.html')

# @app.route('/2plot')
# def plot2():
#     return render_template('2plot.html')
#
# @app.route('/3plot')
# def plot3():
#     return render_template('3plot.html')


if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/wejsciowy')
# def index():