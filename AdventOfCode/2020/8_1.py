# https://adventofcode.com/2020/day/8


code = []

# read data into code list
with open('8data.txt', 'r') as f:
    for line in f:
        # instruction = (operation, argument, visited)
        instruction = (line[:3], int(line[4:]), False)
        code.append(instruction)

pointer = 0
acc = 0
while True:
    operation = code[pointer][0]
    arg = code[pointer][1]
    visited = code[pointer][2]

    if visited:
        break

    code[pointer] = (operation, arg, True)
    if operation == 'acc':
        acc += arg
        pointer += 1
    elif operation == 'jmp':
        pointer += arg
    else:
        pointer += 1
print(acc)
