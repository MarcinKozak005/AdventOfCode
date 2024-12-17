# https://adventofcode.com/2020/day/12
positionEast = 0
positionNorth = 0
directions = 'NESW'
direction = 1

with open('12data.txt', 'r') as f:
    for line in f:
        command = line[0]
        value = int(line[1:])

        if command == 'F':
            command = directions[direction]
        if command == 'N':
            positionNorth += value
        elif command == 'E':
            positionEast += value
        elif command == 'S':
            positionNorth -= value
        elif command == 'W':
            positionEast -= value
        elif command == 'R':
            direction += value//90
            direction %= 4
        elif command == 'L':
            direction -= value//90
            direction %= 4

print(abs(positionEast) + abs(positionNorth))
