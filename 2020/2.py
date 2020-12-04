# https://adventofcode.com/2020/day/2

import re

counter = 0
f = open('2data.txt', 'r')
lines = f.readlines()
f.close()

for line in lines:
    result = re.match(r'(\d+)-(\d+) (.): (.*)', line)

    a = int(result.group(1))
    b = int(result.group(2))
    letter = result.group(3)
    phrase = result.group(4)

    # Part 1
    letterCounts = phrase.count(letter)
    if(letterCounts <= int(b) and letterCounts >= int(a)):
        counter += 1

    # Part 2
    if((phrase[a-1] == letter) ^ (phrase[b-1] == letter)):
        counter += 1

print(counter)
