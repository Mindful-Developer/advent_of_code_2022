with open("ch_06", 'r') as f:
    data = f.read()

found = False
for i in range(len(data)):
    if len(set(data[i:i+4])) == 4 and not found:
        print(i+4)
        found = True
    if len(set(data[i:i+14])) == 14:
        print(i+14)
        break