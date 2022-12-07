with open("ch_07", 'r') as f:
    data = f.read().splitlines()

fs = {}
pos = []
for ln in data:
    if ln.startswith('$ cd '):
        if '..' in ln:
            dir_size = fs['/'.join(pos)]['size']
            pos.pop()
            fs['/'.join(pos)]['size'] += dir_size
        else:
            pos.append(ln.split()[-1])
            fs['/'.join(pos)] = {'size': 0}
    elif ln == '$ ls' or ln.startswith('dir '):
        continue
    else:
        fs['/'.join(pos)]["size"] += int(ln.split()[0])

for _ in range(len(pos)-1):
    dir_size = fs['/'.join(pos)]['size']
    pos.pop()
    fs['/'.join(pos)]['size'] += dir_size

total_up_to_100000 = 0
amount_to_delete = 30000000 - (70000000 - fs['/']['size'])
smallest_dir = None
for _, v in fs.items():
    if v["size"] <= 100000:
        total_up_to_100000 += v["size"]
    elif v["size"] >= amount_to_delete:
        if smallest_dir is None or v["size"] < smallest_dir["size"]:
            smallest_dir = v

print(total_up_to_100000, smallest_dir["size"])