from flask import Flask, request, redirect, url_for, render_template
from config import NOTES, GPIO
from gpiozero import DigitalOutputDevice as Pin

app = Flask(__name__)

# Setup pins
frets: list[Pin] = [Pin(GPIO[id_]) for id_ in range(24)]

for f in frets:
    f.off()


@app.route("/")
def index():
    return "Self-Playing Guitar"


@app.route("/state")
def state():
    return {"state": [[frets[NOTES[string, fret]].value for fret in range(4)] for string in range(6)]}


@app.route("/play/<int:string>/<int:fret>/<int:time>")
def play(string: int, fret: int, time: int):
    pin: Pin = frets[NOTES[string, fret]]
    pin.blink(on_time=time, off_time=0, n=1, background=True)
    return {"result": True}


if __name__ == "__main__":
    app.run(debug=True)
