import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template

app = Flask(__name__)      # app får nemmere ved at finde ud af hvor resourcer er på systemet og kan nemmere tilgås

def stue_temp():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def stue_hum():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([2, 1])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stue')
def stue():
    stue_temperature = stue_temp()
    stue_humidity = stue_hum()
    #print(stue_temperature)
    return render_template('stue.html', stue_temperature = stue_temperature, stue_humidity = stue_humidity)

app.run(debug=True)            # denne funktion genstarter vores flask.py hvergang vi har lavet ændringer



