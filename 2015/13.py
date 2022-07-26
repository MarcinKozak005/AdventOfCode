from itertools import permutations
import math as m  # for infinity

file = open('13data.txt','r')

relationships = {}
initials = set()

# Load data
for line in file:
    words = line.split(' ')
    relationships[f'{words[0][0]}{words[-1][0]}'] = int(words[3]) * (-1 if 'lose' in words else 1)
    initials.add(words[0][0])

# Calculate
arrangements = list(permutations(initials))
num_of_seats = len(initials)

max_happiness = -m.inf

for arr in arrangements:
    happiness = 0
    # biggest_happiness_lost = m.inf  # part 2
    for i in range(num_of_seats):
        happiness += relationships[arr[i] + arr[i-1]] + relationships[arr[i-1] + arr[i]]
        # part 2 start
        # change = relationships[arr[i] + arr[i-1]] + relationships[arr[i-1] + arr[i]]
        # biggest_happiness_lost = min(biggest_happiness_lost, change)
        # happiness += change 
        # part 2 end
    max_happiness = max(max_happiness, happiness)
    # Part 2: Minimise happiness loss ~ raise happiness by sitting between the biggest quarrel
    # max_happiness = max(max_happiness, happiness - biggest_happiness_lost)  # part 2
print(f'Max happiness is {max_happiness}')

