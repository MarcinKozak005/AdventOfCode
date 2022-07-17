from itertools import permutations
import math as m  # for infinity

file = open('09data.txt','r')

distances = {}
cities = set()

def get_distance(x,y):
    try:
        return distances[f'{x}-{y}']
    except KeyError:
        return distances[f'{y}-{x}']

# Load data
for line in file:
    words = line.split(' ')
    distances[f'{words[0]}-{words[2]}'] = int(words[-1])
    cities.add(words[0])
    cities.add(words[2])

# Calculate
pathes = list(permutations(cities))

shortes_patch_length = m.inf
longest_patch_length = -m.inf  # part 2

for patch in pathes:
    current_patch_length = 0
    for i in range(len(patch)-1):
        current_patch_length += get_distance(patch[i], patch[i+1])
    shortes_patch_length = min(shortes_patch_length, current_patch_length)
    longest_patch_length = max(longest_patch_length, current_patch_length)  # part 2
print(f'Shortest path is {shortes_patch_length}')
print(f'Longest path is {longest_patch_length}')  # part 2 
