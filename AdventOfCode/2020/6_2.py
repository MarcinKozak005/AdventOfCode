# https://adventofcode.com/2020/day/6
# Input: two empty lines ('\n') were added at the end of the file

f = open('6_2data.txt', 'r')
lines = f.readlines()
f.close()

sum = 0
letters = 'abcdefghijklmnopqrstuvwxyz'
tmp = set(letters)
for line in lines:
    if line != '\n':
        tmp = tmp.intersection(set(line[:-1]))
    else:
        sum += len(tmp)
        tmp = set(letters)
print(sum)
