# https://adventofcode.com/2020/day/8

# Modified first task's code
def runCode(code):
    pointer = 0
    acc = 0
    while True:
        try:
            operation = code[pointer][0]
            arg = code[pointer][1]
            visited = code[pointer][2]

            if visited:
                return (0, False)

            code[pointer] = (operation, arg, True)
            if operation == 'acc':
                acc += arg
                pointer += 1
            elif operation == 'jmp':
                pointer += arg
            else:
                pointer += 1
        except IndexError:
            return (acc, True)


codeMemory = []

# read data into code list
with open('8data.txt', 'r') as f:
    for line in f:
        # instruction = (operation, argument, visited)
        instruction = (line[:3], int(line[4:]), False)
        codeMemory.append(instruction)

code = []
for i in range(len(codeMemory)):
    code = codeMemory.copy()

    if code[i][0] == 'jmp':
        code[i] = ('nop', code[i][1], code[i][2])
    elif code[i][0] == 'nop':
        code[i] = ('jmp', code[i][1], code[i][2])
    else:
        continue

    result = runCode(code)
    if result[1]:
        print(result[0])
        break
