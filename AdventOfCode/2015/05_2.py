file = open('05data.txt', 'r')

nice = 0
for line in file:
    prev = ''
    rule1_dict = {}
    rule1 = False
    char_2 = ''
    rule2 = False
    for i in range(len(line)):
        char = line[i]
        # rule 1
        if not rule1:
            if prev + char not in rule1_dict.keys():
                rule1_dict[prev + char] = i
            elif i - rule1_dict[prev + char] >= 2:
                rule1 = True
        # rule 2
        if not rule2 and char_2 == char:
            rule2 = True
        char_2 = prev
        prev = char
    if rule1 and rule2:
        nice += 1
print(f'Total number of nice strings: {nice}')
