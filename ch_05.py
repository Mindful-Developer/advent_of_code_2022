import re
from copy import deepcopy


with open("ch_05", 'r') as f:
    data = f.read().splitlines()

arr1 = [
    [*'cfbldpzs'],
    [*'bwhpgvn'],
    [*'gjbwf'],
    [*'scwlfnjg'],
    [*'hsmptljw'],
    [*'sfgwcb'],
    [*'wbqmpth'],
    [*'twsf'],
    [*'rcn']
]

arr2 = deepcopy(arr1)

for line in data[10:]:
    n1, n2, n3 = map(int, re.findall(r'\d+', line))

    for i in range(n1):
        arr1[n3 - 1].insert(0, arr1[n2 - 1].pop(0))

    temp = []
    for i in range(n1):
        temp.append(arr2[n2-1].pop(0))
    for i in range(n1):
        arr2[n3-1].insert(0, temp.pop())

for i in arr1:
    print(i[0], end='')

print()

for i in arr2:
    print(i[0], end='')
