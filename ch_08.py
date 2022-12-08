with open("ch_08", 'r') as f:
    data = f.read().splitlines()

seen = set()
for i, line in enumerate(data):
    greatest = -1
    for j, num in enumerate(line):
        if int(num) > greatest:
            greatest = int(num)
            seen.add((i, j))
    greatest = -1
    for j, num in enumerate(line[::-1]):
        if int(num) > greatest:
            greatest = int(num)
            seen.add((i, len(line) - 1 - j))
for j, line in enumerate(zip(*data)):
    greatest = -1
    for i, num in enumerate(line):
        if int(num) > greatest:
            greatest = int(num)
            seen.add((i, j))
    greatest = -1
    for i, num in enumerate(line[::-1]):
        if int(num) > greatest:
            greatest = int(num)
            seen.add((len(line) - 1 - i, j))

print(len(seen))


best_score = 0
for i, line in enumerate(data):
    for j, num in enumerate(line):
        num_trees_left = 0
        for k in reversed(range(0, i)):
            if int(data[k][j]) < int(num):
                num_trees_left += 1
            else:
                num_trees_left += 1
                break
        num_trees_right = 0
        for k in range(i + 1, len(data)):
            if int(data[k][j]) < int(num):
                num_trees_right += 1
            else:
                num_trees_right += 1
                break
        num_trees_up = 0
        for k in reversed(range(0, j)):
            if int(data[i][k]) < int(num):
                num_trees_up += 1
            else:
                num_trees_up += 1
                break
        num_trees_down = 0
        for k in range(j + 1, len(data)):
            if int(data[i][k]) < int(num):
                num_trees_down += 1
            else:
                num_trees_down += 1
                break

        scenic_score = num_trees_left * num_trees_right * num_trees_up * num_trees_down
        if scenic_score > best_score:
            best_score = scenic_score

print(best_score)