import string


with open("ch_3", 'r') as f:
    data = f.read().splitlines()

priorities = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))

points_1, points_2, i = 0, 0, 0
for sack in data:
    comp1, comp2 = set(sack[0:len(sack) // 2]), set(sack[len(sack) // 2:])
    points_1 += priorities[comp1.intersection(comp2).pop()]

while i < len(data):
    sack_1, sack_2, sack_3 = set(data[i]), set(data[i + 1]), set(data[i + 2])
    points_2 += priorities[sack_1.intersection(sack_2).intersection(sack_3).pop()]
    i += 3

print(points_1, points_2)
