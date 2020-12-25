# https://adventofcode.com/2020/day/10

adapters = {}
maxJoltage = 0
with open('10data.txt','r') as f:
    for line in f:
        number = int(line)
        adapters[number] = True
        if number > maxJoltage:
            maxJoltage = number

diff1 = 0
diff3 = 0
acc = 0

# I assume that there IS such chain of adapters for the given input
for i in range(maxJoltage+1):
    try:
        adapters[i]
        if  i - acc == 1:
            diff1 += 1
            acc = i
        elif i - acc == 3:
            diff3 += 1
            acc = i
        else:
            acc = i
    except KeyError:
        continue

# my device's joltage
diff3 += 1
print(diff1*diff3)