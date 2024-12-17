from itertools import groupby

data = '1113122113'
num_od_iters = 50

for i in range(num_od_iters):
    groups = [''.join(g) for _, g in groupby(data)]
    data = ''
    for group in groups:
        data += str(len(group))+group[0]

print(f'Length of the output: {len(data)}')