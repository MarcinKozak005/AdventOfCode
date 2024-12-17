import re

file = open('07data.txt', 'r')

# a: [b,c] means there is an instruction b X c -> a, where X is an operation
out_in = {}
mask = (1 << 16) - 1

for line in file:
    wires = re.findall(r'[a-z0-9]+', line)
    out = wires[-1]
    op  = re.search(r'[A-Z]+',line)
    # 'number -> wire' case
    if not op:
        out_in[out] = wires[0]
        continue

    op = op.group()
    if op == 'AND':
        out_in[out] = f'({wires[0]} & {wires[1]})'
    elif op == 'OR':
        out_in[out] = f'({wires[0]} | {wires[1]})'
    elif op == 'RSHIFT':
        out_in[out] = f'(({wires[0]} >> {wires[1]}) & {mask})'  # (1)
    elif op == 'LSHIFT':
        out_in[out] = f'(({wires[0]} << {wires[1]}) & {mask})'
    else: #  op == 'NOT':
        out_in[out] = f'({mask} - {wires[0]})'  # 2)
        
exp = 'h'
wires = re.findall(r'\b[a-z]+\b',exp)
while wires:
    for w in wires:
        exp = exp.replace(w,out_in[w])
    wires = re.findall(r'\b[a-z]+\b',exp)
print(exp)
print(eval(exp))


# (1): https://stackoverflow.com/questions/21405341/confusion-in-left-shift-operator-in-python
# (2): https://stackoverflow.com/questions/31151107/how-do-i-do-a-bitwise-not-operation-in-python
