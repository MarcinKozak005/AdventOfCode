# https://adventofcode.com/2020/day/7
"""
Regexes:
'bags?' -> ''
'contain' -> ','
'(?<=\d)' -> ','
'\.' -> ''
' ' -> '' // space -> nothing
"""

rules = {}
# Load rules
with open('7_2data.txt','r') as f:
    for line in f:
        parts = line[:-1].split(',')
        rules[parts[0]] = parts[1:]


sum = 0
tmp = ['shinygold']
while tmp != []:
    current = tmp.pop(0)
    value = rules[current]
    if value[0] != 'noother':
        for i in range(0,len(value),2):
            tmp += [value[i+1] for _ in range(0,int(value[i]))]
            sum += int(value[i])
print(sum)
    
