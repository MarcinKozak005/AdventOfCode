import re

file = open('07data.txt')

def getABA(s):
    result = []
    for i in range(0,len(s)-2):
        if s[i] == s[i+2] and s[i+1] != s[i]:
            result.append(s[i:i+3])
    return result

count = 0
for line in file:
    normal = [x[1] for x in re.findall(r'(^|\])([a-zA-Z]+)($|\[)', line)]
    brackets = re.findall(r'\[.*?\]', line)
    normal_aba = []
    # find all ABA strings
    for n in normal:
        normal_aba.extend(getABA(n))
    # check all bracket strings 
    sentinel = True
    for n in normal_aba:
        for b in brackets:
            if n[1]+n[0]+n[1] in b:
                count += 1
                sentinel = False
                break
        if not sentinel:
            break
print(count)