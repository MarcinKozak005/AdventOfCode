# https://adventofcode.com/2020/day/4
# 4data.txt was regexed

import re

requiredFields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

# Part 1
def condition1(line):
    for field in requiredFields:
        if(re.search(field, line) is None):
            return False
    return True

# Part 2
def condition2(line):
    result = []
    for field in requiredFields:
        m = re.search(field + r'([^ \n]*)', line)
        if(m):
            result.append(m.group(1))
        else:
            return []
    return result

# Part 2
def condition2_1(g):
    byr = int(g[0])
    iyr = int(g[1])
    eyr = int(g[2])
    hgt = g[3]
    if hgt[-2:] == 'cm':
        hgtC = int(hgt[:-2])
        hgtI = 59
    elif hgt[-2:] == 'in':
        hgtC = 150
        hgtI = int(hgt[:-2])
    else:
        hgtC = 0
        hgtI = 0
    hcl = g[4]
    ecl = g[5]
    pid = g[6]

    if(byr >= 1920 and byr <= 2002 and
       iyr >= 2010 and iyr <= 2020 and
       eyr >= 2020 and eyr <= 2030 and
       hgtC >= 150 and hgtC <= 193 and
       hgtI >= 59 and hgtI <= 76 and
       re.match(r'#[0-9a-f]{6}', hcl) and
       ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
       re.match(r'\d{9}', pid)
       ):
        return True
    return False


# Common
f = open('4data.txt', 'r')
lines = f.readlines()
f.close()
counter = 0

for line in lines:

    # Part 1
    if(condition1(line)):
        counter += 1

    # Part 2
    groups = condition2(line)
    if(len(groups) == 7):
        if(condition2_1(groups)):
            counter += 1

print(counter)
