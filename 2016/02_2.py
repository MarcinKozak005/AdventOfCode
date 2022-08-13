file = open('02data.txt')

"""
Keypad - coordinates maping
                   1      
                (+0,+2)
          2        3       4
        (-1,+1) (+0,+1) (+1,+1)
   5       6       7       8       9
(-2,+0) (-1,+0) (+0,+0) (+1,+0) (+2,+0)
           A       B       C
        (-1,-1) (+0,-1) (+1,-1)
                   D      
                (+0,-2)
"""

code = ''
x = -2
y = 0
for line in file:
    for c in line:
        # max/min values of y-coordinate depends on x-coordinate and vice versa 
        y = min(2 - abs(x), y+1) if c == 'U' else y
        y = max(abs(x) - 2, y-1) if c == 'D' else y
        x = min(2 - abs(y), x+1) if c == 'R' else x
        x = max(abs(y) - 2, x-1) if c == 'L' else x
    # calculate number based on coordinates
    key = 7 + x - (3 if abs(y) == 2 else 4) * y
    code += f'{key if key < 10 else chr(key+55)}'
print(f'Code is: {code}')    
