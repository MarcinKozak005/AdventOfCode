# https://adventofcode.com/2020/day/5
# I added a space at the end of the last line of 5data.txt

import re

# Part 2
seats = [i for i in range(0, 8*127)]

f = open('5data.txt', 'r')
lines = f.readlines()
f.close()

# Part 1
maxID = -1
# Part 2
taken = []

for line in lines:
    # '\n' is at the end of each line (last line has a space added by me)
    row = line[:-4]
    col = line[-4:]
    rowNum = int(re.sub('B', '1', re.sub('F', '0', row)), 2)
    colNum = int(re.sub('R', '1', re.sub('L', '0', col)), 2)

    # Part 1
    if rowNum*8 + colNum > maxID:
        maxID = rowNum*8 + colNum

    # Part 2
    taken.append(rowNum*8 + colNum)

# Part 1
print(maxID)

# Part 2
# and analyse the output list according to the info given in the task
print(set(seats) - set(taken))
