"""
Initial stack state:
- Replace ] with ',
- Replace [ with '
- Check possible column misalignment
- Copy each column (in VScode hold scroll button and drag)
- Paste the column in the different place and remove \n
- reverse the list
"""

import re

def main():
    stacks = [
        ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
        ['L', 'D', 'Z', 'Q', 'W', 'V'],
        ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
        ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
        ['Z', 'W', 'L', 'C'],
        ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
        ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
        ['D', 'P', 'J'],
        ['D', 'C', 'N', 'W', 'V']
    ]
    data = open('05data.txt','r')
    for line in data:
        num,source, target = [int(x) for x in re.findall(r'\d+',line)]
        move2(stacks, num, source, target)
    for s in stacks:
        print(s[-1],end='')


def move1(stacks, num, source, target):
    for _ in range(num):
        stacks[target-1].append(stacks[source-1].pop())

# part 2
def move2(stacks,num, source, target):
    stacks[target-1] += stacks[source-1][-num:]
    stacks[source-1] = stacks[source-1][:-num]


if __name__ == '__main__':
    main()
