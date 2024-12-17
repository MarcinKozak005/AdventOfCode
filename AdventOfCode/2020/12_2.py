# https://adventofcode.com/2020/day/12
positionEast = 0
positionNorth = 0
wpE = 10
wpN = 1

with open('12data.txt', 'r') as f:
    for line in f:
        command = line[0]
        value = int(line[1:])

        if command == 'L':
            command = 'R'
            # There are no rotate values above 360
            value = 360 - value

        if command == 'F':
            positionNorth += value*wpN
            positionEast += value*wpE
        elif command == 'N':
            wpN += value
        elif command == 'E':
            wpE += value
        elif command == 'S':
            wpN -= value
        elif command == 'W':
            wpE -= value
        elif command == 'R':
            for i in range(value//90):
                wpE, wpN = wpN, -wpE

print(abs(positionEast) + abs(positionNorth))
