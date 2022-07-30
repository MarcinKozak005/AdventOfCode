import re
import itertools
import math as m

data = open('15data.txt','r')

# pairs: (ingredient id, ingredient properties) 
ingredients = {}

for line in data:
    ingredients[line[0:3]] = [int(i) for i in re.findall(r'-?\d+',line)]

# Generate all possible recipes
possibilities = []
for p in list(itertools.combinations_with_replacement(ingredients.keys(),100)):
    tmp = {}
    for i in ingredients.keys():
        tmp[i] = p.count(i)
    possibilities.append(tmp)


max_score = - m.inf
for p in possibilities:
    properties = [0] * len(ingredients[list(ingredients.keys())[0]])
    for i in ingredients:
        next = list(map(lambda x: x*p[i], ingredients[i]))
        properties = [x + y for x,y in zip(properties, next)]
    if all(list(map(lambda x: x >0, properties))):
    # if all(list(map(lambda x: x >0, properties))) and properties[-1] == 500:  # part 2
        max_score = max(max_score, m.prod(properties[:-1]))

print(f'Max score is {max_score}')