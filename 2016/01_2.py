from collections import defaultdict

def move(side, x,y):
    if side == 0:
        y += n
    elif side == 1:
        x += n
    elif side == 2:
        y -= n
    else:
        x -= n
    return x,y


data = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5"
data = data.split(', ')


positions = defaultdict(lambda: False)
positions[(0,0)] = True

x = 0
y = 0
side = 0  # 0 - north, ..., 3 - west
found = False
for d in data:
    if found:
        break
    side = (side + (1 if d[0] == 'R' else -1)) % 4
    n = int(d[1:])
    for i in range(1,n+1):
        x,y = move(side,x,y)
        
        if positions[(x,y)]:
            found = True
            break
        positions[(x,y)] = True
        
print(f'Distance = {abs(x)+abs(y)}')
