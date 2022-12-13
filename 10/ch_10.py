with open("ch_10", 'r') as f:
    data = f.read().splitlines()

cycle = 1
x = 1

def cycler(*nums):
    global cycle
    global x
    image = [[]]
    def increase_cycle():
        global cycle
        global x
        nonlocal j
        register = [x - 1, x, x + 1]
        if cycle % 40 in register:
            image[j].append("#")
        else:
            image[j].append(".")
        cycle += 1
        if cycle % 40 + 1 == 1:
            j += 1
        if cycle in nums:
            val_dict[cycle] = x * cycle

    i = 0
    j = 0
    val_dict = {}
    while i < len(data):
        if j == len(image):
            image.append([])
        if data[i].startswith("addx "):
            val = int(data[i].split()[1])
            increase_cycle()
            x += val
        if j == len(image):
            image.append([])
        increase_cycle()
        i += 1
    return val_dict, image


p1, p2 = cycler(20, 60, 100, 140, 180, 220)

print(sum(p1.values()))
for i in p2:
    print(i)

