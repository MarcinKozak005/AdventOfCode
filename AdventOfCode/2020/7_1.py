# https://adventofcode.com/2020/day/7
"""
Regexes:
'bags?' -> ''
'contain' -> ','
'\d' -> ''
'\.' -> ''
' ' -> '' // space -> nothing
"""

rules = {}
# Load rules
with open('7_1data.txt','r') as f:
    for line in f:
        parts = line[:-1].split(',')
        rules[parts[0]] = parts[1:]


memory = []
tmp = ['shinygold']
while tmp != []:
    current = tmp.pop(0)
    for key, value in rules.items():
        if current in value:
            # cycle prevention
            if key not in memory:
                tmp.append(key)
                memory.append(key)
print(len(memory))
    
