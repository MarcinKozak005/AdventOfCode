import re
import numpy as np
from statistics import mode
from collections import Counter  # part2


file = open('06data.txt')
arr = np.array([re.split(r'',word) for word in re.split(r'\n',file.read())])

for i in range(1,9):
    print(mode(arr[:,i]),end='')
    print(Counter(arr[:,i]).most_common()[:-2:-1][0][0], end='') # part 2
