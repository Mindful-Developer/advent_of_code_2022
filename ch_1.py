with open("ch_1", "r") as f:
    elves = f.read().split("\n\n")

elves = sorted(map(lambda x: sum(int(y) for y in x.split("\n")), elves))
print(f"Largest = {elves[-1]}", f"Largest 3 summed = {sum(elves[-3:])}")