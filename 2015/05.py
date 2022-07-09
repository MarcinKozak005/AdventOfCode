
file = open('05data.txt','r')

nice = 0
for line in file:
    vowels = 0
    rule1 = False
    prev = ''
    rule2 = False
    # For rule3 it's easier to assume it is fulfilled, and check for the violations
    rule3 = True  
    for char in line:
        # rule 3 - is the most strict one, so check it first
        if prev+char in ['ab', 'cd', 'pq', 'xy']:
            rule3 = False
            break
        # rule 1
        if not rule1 and char in 'aeiou':
            vowels += 1
            if vowels == 3:
                rule1 = True
        # rule 2
        if not rule2 and char == prev:
            rule2 = True
        prev = char
    if rule1 and rule2 and rule3:
        nice += 1
print(f'Total number of nice strings: {nice}')