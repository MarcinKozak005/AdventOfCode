from itertools import groupby
data = 'hepxcrrq'
# data = 'hepxxyzz'  # part 2

def increment(string):
    i = len(string) - 1
    while True:
        if string[i] != 'z':
            return string[:i] + chr(ord(string[i])+1) + string[i+1:]
        else:
           string = string[:i] + 'a' + string[i+1:]
           i -= 1


while True:
    rule1, rule2, rule3 = False, False, False
    data = increment(data)
    # rule 2 - the most strict one
    for c in data:
        if c == 'i' or c == 'o' or c == 'l':
            continue
    rule2 = True
    #
    diff_tab = [ord(data[i+1]) - ord(data[i]) for i in range(len(data)-1)]
    groups = [list(x) for _,x in groupby(diff_tab)]
    pairs_counter = 0
    for g in groups:
        if len(g) >= 2 and g[0] == 1:
            rule1 = True
        elif g[0] == 0:
            pairs_counter += 1
    if pairs_counter >= 2:
        rule3 = True
    if rule1 and rule2 and rule3:
        break
print(f'Next password is {data}')
    
        
