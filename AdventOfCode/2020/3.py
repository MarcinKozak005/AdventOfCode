# https://adventofcode.com/2020/day/3
# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

f = open('3data.txt', 'r')
lines = f.readlines()
f.close()

pos = 0
counter = 0
# Part 2
part2 = True

# Common
for line in lines:

    right = 1
    # Part 1
    if(line[pos] == '#'):
        counter += 1
    pos += right
    pos = pos % 31

    # Part 2
    if(line[pos] == '#' and part2 == True):
        counter += 1
    if part2 == True:
        pos += right
        pos = pos % 31
    part2 = not part2

print(counter)
