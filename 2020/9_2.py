# https://adventofcode.com/2020/day/9

from collections import deque

sol1 = 552655238
numbers = []
with open('9data.txt', 'r') as f:
    for line in f:
        numbers.append(int(line))


for i in range(len(numbers)-1):
    queue = deque()
    for j in range(i, len(numbers)):
        queue.append(numbers[j])
        if sum(queue) >= sol1:
            break
    if sum(queue) == sol1:
        print(min(queue) + max(queue))
        break
