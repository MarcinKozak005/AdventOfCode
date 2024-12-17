"""
Input modifications: add \n to the last line
"""
import numpy as np

def create_grid():
    grid = []
    data = open('08data.txt','r')
    for line in data:
        grid.append([int(x) for x in line[:-1]])
    return np.array(grid)

def scan(i, j_range, current_max, visibility_func):
    for j in j_range:
        current_max = visibility_func(i,j,current_max)
        if current_max == 9:
            break

def main():
    grid = create_grid()
    height, width = grid.shape
    visibles = np.zeros(grid.shape)

    def is_visible(i,j, current_max):
        if grid[i,j] > current_max:
            visibles[i,j] = 1
            current_max = grid[i,j]
        return current_max
    
    visibility_func = lambda i,j,m: is_visible(i,j,m)
    for i in range(1,height-1):
        scan(i,range(1,width-1), grid[i,0],visibility_func)
        scan(i,range(width-2,0,-1),grid[i,-1],visibility_func)
    visibility_func = lambda i,j,m: is_visible(j,i,m)
    for j in range(1,width-1):
        scan(j, range(1,height-1),grid[0,j],visibility_func)
        scan(j,range(height-2,0,-1),grid[-1,j],visibility_func)
    # add edges, subtract duplicated vertices
    print(visibles.sum() + 2*width + 2*height - 4)

if __name__ == '__main__':
    main()