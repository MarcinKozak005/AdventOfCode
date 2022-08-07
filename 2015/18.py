import numpy as np

def get(array: np.ndarray, i, j):
    # prevent 'looping': tab[-1] = last element of tab
    if i < 0 or j < 0:
        return 0
    try:
        return array[i,j]
    except IndexError:
        return 0

def calculate_next_val(array: np.ndarray, i, j):
    s = get(array,i-1,j-1) + get(array,i-1,j) + get(array,i-1,j+1) + \
        get(array,i,j-1)            +           get(array,i,j+1) + \
        get(array,i+1,j-1) + get(array,i+1,j) + get(array,i+1,j+1)
    if array[i,j] == 1:
        return 1 if s in (2,3) else 0
    else:
        return 1 if s == 3 else 0

file = open('18data.txt')
size = 100
n_iter = 100

current = np.empty(shape=(size,size), dtype='int8')
next = np.empty(shape=(size,size), dtype='int8')

# Load data
line = file.readline()
line_counter = 0
while line:
    for i in range(size):
        current[line_counter,i] = 1 if line[i] == '#' else 0
    line = file.readline()
    line_counter += 1

# Calculate the state of the grid
for _ in range(n_iter):
    for i in range(size):
        for j in range(size):
            next[i,j] = calculate_next_val(current, i, j)
    current, next = next, current
    # part 2
    # current[0,0], current[0,size-1], current[size-1,0], current[size-1, size-1] = 1,1,1,1
print(f'Sum: {sum(sum(current))}')