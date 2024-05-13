from flask import Flask, request, redirect, url_for, render_template
from config import NOTES, GPIO
from gpiozero import DigitalOutputDevice as DOD
import time

app = Flask(__name__)


frets = [None] * 24


@app.route("/")
def index():
    return "Self-Playing Guitar"


@app.route("/initialize")
def initialize():
    for (string, fret), id_ in NOTES.items():
        pin_obj = DOD(GPIO[id_])
        pin_obj.off()
        frets[id_] = pin_obj
    return {"result": True}


@app.route("/play/<int:string>/<int:fret>/<int:time>")
def play(string: int, fret: int, time: int):
    pin_obj = frets[NOTES[string, fret]]
    if not pin_obj:
        return {"result": False}
    pin_obj.blink(on_time=time, off_time=0, n=1, background=True)
    return {"result": True}


if __name__ == "__main__":
    app.run(debug=True)
