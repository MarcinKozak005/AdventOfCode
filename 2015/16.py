import re

file = open('16data.txt')

target = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

# part 2 start
# group1 = ('cats','trees')
# group2 = ('pomeranians', 'goldfish')
# group3 = set(target.keys()) - set (group1) - set(group2)
# part 2 end

for line in file:
    fulfills = True
    for a in list(target.keys()):
        attr_match = re.search(f'{a}: (\d+)', line)
        if attr_match and int(attr_match.group(1)) != target[a]:
        # part 2 start
        # if attr_match and (
        #     (a in group1 and int(attr_match.group(1)) <= target[a]) or
        #     (a in group2 and int(attr_match.group(1)) >= target[a]) or
        #     (a in group3 and int(attr_match.group(1)) != target[a])
        # ):
        # part 2 end
            fulfills = False
            break
    if fulfills:
        print(f'Probable solution: {line}',end='')
