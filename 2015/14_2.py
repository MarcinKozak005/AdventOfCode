import re
import numpy as np

data = open('14data.txt','r')

reindeers = [] 

for line in data:
    numbers = re.findall(r'\d+', line)
    reindeers.append([int(i) for i in numbers])

time = 2503

distances = np.array([0] * len(reindeers))
scores = [0] * len(reindeers)

for i in range(time):
    for j in range(len(reindeers)):
        r = reindeers[j]
        if i % (r[1] + r[2]) < r[1]:
            distances[j] += r[0]
    round_results = list(distances == distances.max())
    scores = [x + y for x,y in zip(scores, round_results)]
        
print(f'Max # of points is: {max(scores)}')
