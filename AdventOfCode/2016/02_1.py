file = open('02data.txt')

"""
Keypad - coordinates maping
  1     2     3
(0,2) (1,2) (2,2)
  4     5     6
(0,1) (1,1) (2,1)
  7     8     9
(0,0) (1,0) (2,0)
"""

code = ''
x = 1
y = 1
for line in file:
    for c in line:
        y = min(2,y+1) if c == 'U' else y
        y = max(0,y-1) if c == 'D' else y
        x = min(2,x+1) if c == 'R' else x
        x = max(0,x-1) if c == 'L' else x
    code += f'{7 + x - 3*y}'  # calculate number based on coordinates
print(f'Code is: {code}')    
