import re

file = open('03data.txt')

tabs = [[],[],[]]
possible = 0
for line in file:
    sides = re.findall(r'\d+',line)
    for i in range(0,3):
        tabs[i].append(int(sides[i]))

    if len(tabs[0]) == 3:
        for i in range(0,3):
            # sum(x) - y > y <=> sum(x) > 2*y
            possible += 1 if sum(tabs[i]) > 2*max(tabs[i]) else 0
        tabs = [[],[],[]]
print(f'Possible: {possible}')