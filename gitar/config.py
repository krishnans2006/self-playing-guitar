NOTES = {(i % 6, i // 6): i for i in range(24)}  # (string,fret): id

GPIO = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

LAYOUT = [
    {"string": "E", "notes": ["F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"]},
    {"string": "B", "notes": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]},
    {"string": "G", "notes": ["G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]},
    {"string": "D", "notes": ["D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"]},
    {"string": "A", "notes": ["A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"]},
    {"string": "E", "notes": ["F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"]},
]

AVAILABLE_FRETS = list(range(4))

CHORDS = {
    "G": [(0, 2), (4, 1), (5, 2)],
    "C": [(1, 0), (3, 1), (4, 2)],
    "D": [(0, 1), (1, 2), (2, 1)],
    "E": [(2, 0), (3, 1), (4, 1)],
    "A": [(1, 1), (2, 1), (3, 1)],
}


if __name__ == "__main__":
    for (string, fret), id_ in NOTES.items():
        print(f"ID {id_:2} | String: {string}, Fret: {fret}, GPIO Pin: {GPIO[id_]}")
