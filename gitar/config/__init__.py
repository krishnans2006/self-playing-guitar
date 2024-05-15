NOTES = {(i % 6, i // 6): i for i in range(24)}  # (string,fret): id

GPIO = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]


if __name__ == "__main__":
    for (string, fret), id_ in NOTES.items():
        print(f"ID {id_:2} | String: {string}, Fret: {fret}, GPIO Pin: {GPIO[id_]}")
