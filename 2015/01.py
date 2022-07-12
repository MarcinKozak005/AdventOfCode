data = open('01data.txt', 'r').read()
floor = 0
# part2 start
char_position = 1
first_entrance = True
# part2 end
for c in data:
    if c == '(':
        floor += 1
    else:
        floor -= 1
    # part2 start
    if floor < 0 and first_entrance:
        print(f'Basement entered with char at position {char_position}')
        first_entrance = False
    char_position += 1 
    # part2 end
print(f'Final floor: {floor}')
