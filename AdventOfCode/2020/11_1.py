# https://adventofcode.com/2020/day/11
"""
Regexes:
'(?<=.)' -> ','
"""

"""
Seats legend:
# -> was occupied is occupied
- -> was occupied is free
L -> was free     is free
+ -> was free     is occupied

ppp
pxc
ccc

p - previous fields
c - current fields

By using such technique I don't have to use second table to store the results
"""
prevFields = [(-1, -1), (-1, 0), (-1, 1), (0, -1)]
currFields = [(0, 1), (1, -1), (1, 0), (1, 1)]


def checkFields(fields, row, col, tab):
    result = []
    for f in fields:
        try:
            tmpR = row+f[0]
            tmpC = col+f[1]
            if tmpR >= 0 and tmpC >= 0:
                result.append(tab[tmpR][tmpC])
        except IndexError:
            pass
    return result


def numberOfOccupied(row, col, tab):
    prev = checkFields(prevFields, row, col, tab)
    curr = checkFields(currFields, row, col, tab)
    return prev.count('-') + prev.count('#') + curr.count('#') + curr.count('+')


tab = []
with open('11data.txt', 'r') as f:
    for line in f:
        tab.append(line.split(',')[:-1])

numOfCol = len(tab[0])
numOfRow = len(tab)
changed = True

while changed:
    changed = False
    for i in range(numOfRow):
        for j in range(numOfCol):
            numOfOcc = numberOfOccupied(i, j, tab)
            if tab[i][j] in ['-', 'L'] and numOfOcc == 0:
                tab[i][j] = '+'
                changed = True
            elif tab[i][j] in ['+', '#'] and numOfOcc >= 4:
                tab[i][j] = '-'
                changed = True
            elif tab[i][j] == '-':
                tab[i][j] = 'L'
            elif tab[i][j] == '+':
                tab[i][j] = '#'

result = 0
for t in tab:
    result += t.count('#')
print(result)
