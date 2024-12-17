import re

file = open('03data.txt')

possible = 0
for line in file:
    sides = [int(i) for i in re.findall(r'\d+',line)]
    # sum(x) - y > y <=> sum(x) > 2*y
    if sum(sides) > 2*max(sides):
        possible += 1
print(f'Possible: {possible}')