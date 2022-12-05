with open("ch_04", 'r') as f:
    data = f.read().splitlines()

total_contained, total_overlapping = 0, 0
for line in data:
    e1, e2 = line.split(',')
    e1_s, e1_f = map(int, e1.split('-'))
    e2_s, e2_f = map(int, e2.split('-'))

    if e1_s >= e2_s and e1_f <= e2_f or e2_s >= e1_s and e2_f <= e1_f:
        total_contained += 1

    if e1_s <= e2_s <= e1_f or e2_s <= e1_s <= e2_f:
        total_overlapping += 1

print(total_contained, total_overlapping)
