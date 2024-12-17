# https://adventofcode.com/2020/day/9

from collections import deque


def checkNumber(number, queue):
    # 25 is the len of the queue in this example
    for i in range(24):
        for j in range(i+1, 25):
            if queue[i] + queue[j] == number and i != j:
                return True
    return False


queue = deque()
with open('9data.txt', 'r') as f:
    for i in range(25):
        queue.append(int(f.readline()))

    for line in f:
        current = int(line)
        if not checkNumber(current, queue):
            print(current)
            break
        queue.popleft()
        queue.append(current)
