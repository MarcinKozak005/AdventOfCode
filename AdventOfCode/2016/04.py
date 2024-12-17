from itertools import groupby
import re


def shift(c, n):
    """
    ord(c)                              --> ASCII code of c. c in (a-z), so ord(c) in (97-122)
    ord(c) - 97                         --> changes range from 97-122 to 0-25
    ord(c) - 97 + n                     --> applies shift 
    ( (ord(c) - 97 + n) % 26)           --> maps the value after the shift to range 0-25
    (97 + ( (ord(c) - 97 + n) % 26))    --> maps the value range to 97-122 (a-z)
    chr(97 + ( (ord(c) - 97 + n) % 26)) --> returns the char for specific ASCII code
    """
    return chr(97 + ( (ord(c) - 97 + n) % 26))

file = open('04data.txt')

count = 0
for line in file:
    m = re.match(f'(.*?)-(\d+)\[(.*)\]',line)
    m1 = ''.join(sorted(m.group(1)))  # sorts alphabetically
    letters = [''.join(g) for _, g in groupby(m1)][1:]
    letters.sort(key=lambda x: len(x), reverse=True)  # Timsort is stable
    calculated = ''.join([letters[i][0] for i in range(5)]) 
    if calculated == m.group(3):
        count += int(m.group(2))
        # part 2
        # print(f'{"".join([shift(c,int(m.group(2))) for c in m.group(1)])} - {m.group(2)}')
        # manually search in the results for 'north'
print(f'Result is {count}')
