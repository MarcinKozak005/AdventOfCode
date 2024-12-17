file = open('08data.txt')

cic = 0  # chars in the code
cie = 0  # chars in the encoded string

for line in file:
    i = 0
    while i < len(line):
        if line[i] == '\n':  # newline in file
            i += 1
            continue
        cic += 1
        cie += 1
        if line[i] == '\\' or line[i] == '"':
            cie += 1
        i += 1  # loop incrementation
    cie += 2  # the start and end quote
print(f'The difference is: {cie}-{cic}={cie-cic}')

