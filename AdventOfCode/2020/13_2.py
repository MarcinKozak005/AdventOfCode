# https://adventofcode.com/2020/day/12
import sys

with open('13data.txt','r') as f:

    data = f.readlines()[1].split(',')

busses = []
for i in range(len(data)):
    if data[i] != 'x':
        busses.append((int(data[i]),i))

i = 0
look = True
while look:
    look = False
    i += busses[0][0]
    for (line,index) in busses:
        if (i+index) % line:
            look = True
            break
    print(i)

print(i)


    