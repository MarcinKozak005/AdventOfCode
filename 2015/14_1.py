import re
import math as m  # for infinity 

data = open('14data.txt','r')

reindeers = [] 

for line in data:
    numbers = re.findall(r'\d+', line)
    reindeers.append([int(i) for i in numbers])

time = 2503
max_distance = - m.inf

for r in reindeers:
    distance = (time // (r[1]+r[2]) ) * r[0] * r[1]
    time_left = time % (r[1]+r[2])
    distance += (min(time_left, r[1]) * r[0])
    max_distance = max(max_distance, distance)

print(f'Winning reindeer traveled: {max_distance}')

