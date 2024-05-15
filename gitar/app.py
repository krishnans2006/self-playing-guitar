from flask import Flask, render_template
import config
from gpiozero import DigitalOutputDevice as Pin

app = Flask(__name__)

# Setup pins
frets: list[Pin] = [Pin(config.GPIO[id_]) for id_ in range(24)]

for f in frets:
    f.off()


@app.route("/")
def index():
    return render_template("index.html", layout=config.LAYOUT, available_frets=config.AVAILABLE_FRETS, chords=config.CHORDS)


@app.route("/state")
def state():
    return {"state": [[frets[config.NOTES[string, fret]].value for fret in range(4)] for string in range(6)]}


@app.route("/play/<int:string>/<int:fret>/<int:time>")
def play(string: int, fret: int, time: int):
    pin: Pin = frets[config.NOTES[string, fret]]
    pin.blink(on_time=time, off_time=0, n=1, background=True)
    return {"result": True}


@app.route("/play-chord/<chord>/<int:time>")
def play_chord(chord: str, time: int):
    if chord == "all":
        for pin in frets:
            pin.blink(on_time=time, off_time=0, n=1, background=True)
    elif chord not in config.CHORDS:
        return {"result": False}
    else:
        for string, fret in config.CHORDS[chord]:
            pin: Pin = frets[config.NOTES[string, fret]]
            pin.blink(on_time=time, off_time=0, n=1, background=True)
    return {"result": True}


if __name__ == "__main__":
    app.run(debug=True)
