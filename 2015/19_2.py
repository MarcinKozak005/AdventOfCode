import re
from collections import deque

def get(key):
    try:
        return formulas[key]
    except KeyError:
        formulas[key] = []
        return formulas[key]

def find():
    while True:
        print(f'Queue length: {len(queue)}')
        e,c = queue.popleft()
        molecules = re.findall(r'[A-Z][a-z]?',e)
        for i in range(len(molecules)):
            if molecules[i] in formulas:
                tmp = molecules[i]
                for f in formulas[molecules[i]]:
                    molecules[i] = f
                    new_molecule = ''.join(molecules)
                    if new_molecule == data:
                        return c+1
                    if len(new_molecule) <= result_length:
                        queue.append((new_molecule,c+1))
                molecules[i] = tmp

data = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'
result_length = len(data)

formulas = {}
file = open('19data.txt')

# Read data
for line in file:
    m = re.findall(r'[a-zA-Z]+', line)
    get(m[0]).append(m[1])

# Calculate
queue = deque([(x,1) for x in formulas['e']])

print(f'Result {find()}')



