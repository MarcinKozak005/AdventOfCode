from itertools import combinations


file = open('17data.txt')

containers = []

for line in file:
    containers.append(int(line))


counter = 0
for i in range(1, len(containers)):
    possibilities = list(combinations(containers, i))
    for p in possibilities:
        if sum(p) == 150:
            counter += 1
    # part 2 start
    # if counter > 0:
    #     break
    # part 2 end
print(f'There are {counter} possible container combinations')
