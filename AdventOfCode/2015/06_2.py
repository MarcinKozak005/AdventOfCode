import numpy as np
import re

file = open('06data.txt', 'r')

grid = np.array([[0] * 1000] * 1000)

for line in file:
    x1, y1, x2, y2 = [int(x) for x in re.findall(r'\d+', line)]
    if line.startswith('turn on'):
        grid[y1:y2 + 1, x1:x2 + 1] += 1
    elif line.startswith('turn off'):
        grid[y1:y2 + 1, x1:x2 + 1] -= 1
        # grid[grid < 0] = 0
        grid[y1:y2 + 1, x1:x2 + 1][grid[y1:y2 + 1, x1:x2 + 1] < 0] = 0
    else:
        grid[y1:y2 + 1, x1:x2 + 1] += 2
print(f'# of light on is: {grid.sum()}')
