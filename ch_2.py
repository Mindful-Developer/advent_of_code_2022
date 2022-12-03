pw = {"X": 1, "Y": 2, "Z": 3}

standard = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

win = {
    "A": {"X": 0 + 3, "Y": 3 + 1, "Z": 6 + 2},
    "B": {"X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3},
    "C": {"X": 0 + 2, "Y": 3 + 3, "Z": 6 + 1},
}

with open("ch_2", 'r') as f:
    games = f.read().splitlines()

p1, p2 = 0, 0
for game in games:
    o, p = game.split()
    p1 += pw[p] + standard[o][p]
    p2 += win[o][p]

print(p1, p2)