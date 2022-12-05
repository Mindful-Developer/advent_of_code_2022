import re
from copy import deepcopy


with open("ch_05", 'r') as f:
    data = f.read().splitlines()

arr1 = [
    "c,f,b,l,d,p,z,s".split(','),
    "b,w,h,p,g,v,n".split(','),
    'g,j,b,w,f'.split(','),
    's,c,w,l,f,n,j,g'.split(','),
    'h,s,m,p,t,l,j,w'.split(','),
    's,f,g,w,c,b'.split(','),
    'w,b,q,m,p,t,h'.split(','),
    't,w,s,f'.split(','),
    'r,c,n'.split(',')]

arr2 = deepcopy(arr1)

for line in data[10:]:
    n1, n2, n3 = map(int, re.findall(r'\d+', line))

    for i in range(n1):
        arr1[n3 - 1].insert(0, arr1[n2 - 1].pop(0))

    temp = []
    for i in range(n1):
        temp.append(arr2[n2-1].pop(0))
    for i in range(len(temp)):
        arr2[n3-1].insert(0, temp.pop())

for i in arr1:
    print(i[0], end='')

print()

for i in arr2:
    print(i[0], end='')
