import re

file = open('07data.txt')

def isABBA(s):
    for i in range(0,len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False

count = 0
for line in file:
    normal = [x[1] for x in re.findall(r'(^|\])([a-zA-Z]+)($|\[)', line)]
    brackets = re.findall(r'\[.*?\]', line)
    normal_sat, brackets_sat = False, True
    # check cond in non brackets strings
    for n in normal:
        if isABBA(n):
            normal_sat = True
            break
    # check cond in brackets strings
    for b in brackets:
        if isABBA(b):
            brackets_sat = False
            break
    if brackets_sat and normal_sat:
        count += 1
print(count)