file = open('08data.txt')

cic = 0  # chars in the code
cis = 0  # chars in the string

for line in file:
    i = 0
    while i < len(line):
        if line[i] == '\n':  # newline in file
            i += 1
            continue
        cic += 1
        cis += 1
        if line[i] == '\\':  # escape seq
            if line[i+1] == 'x':  # \x
                i += 3
                cic += 3
            else:
                i += 1
                cic += 1
        i += 1  # loop incrementation
    cis -= 2  # the start and end quote
print(f'The difference is: {cic}-{cis}={cic-cis}')

