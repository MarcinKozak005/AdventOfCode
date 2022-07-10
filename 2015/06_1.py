import numpy as np
import re


file = open('06data.txt','r')

grid = np.array([[False] * 1000] * 1000)

for line in file:
    x1,y1,x2,y2 = [int(x) for x in re.findall('\d+', line)]
    if line.startswith('turn on'):
        grid[y1:y2+1, x1:x2+1] = True
    elif line.startswith('turn off'):
        grid[y1:y2+1, x1:x2+1] = False
    else:
        grid[y1:y2+1, x1:x2+1] = ~grid[y1:y2+1, x1:x2+1]
print(f'# of light on is: {grid.sum()}')

