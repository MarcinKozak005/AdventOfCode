# https://adventofcode.com/2020/day/6
# Input data was regexed so that each line is one group, and a '\n' was added in the last line

f = open('6_1data.txt', 'r')
lines = f.readlines()
f.close()

sum = 0
for line in lines:
    # last character in line is '\n'
    sum += len(set(line[:-1]))
print(sum)
