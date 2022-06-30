
file = open('02data.txt', 'r')

paper = 0
ribbon = 0

for line in file:
    dims = [int(x) for x in line.split('x')]
    dims.sort()
    a,b,c = dims
    paper += 2* (a*b + b*c + a*c) + a*b
    # part 2 start
    ribbon += 2*(a+b)
    ribbon += a*b*c
    # part 2 end
print(f'Elves should order {paper} feet of wrapping paper')
print(f'Elves should order {ribbon} feet of ribbon') # part 2

