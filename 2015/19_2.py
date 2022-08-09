import re
from collections import deque

def get(key):
    try:
        return past[key]
    except KeyError:
        return True

def find():
    while True:
        data,n_oper = queue.popleft()
        print(f'L: {len(data)} N: {n_oper}')
        if data == ['e']:
            return n_oper
        for i in range(len(data)):
            for j in range(1,10):
                compound = ''.join(data[i:i+j])
                if compound in reversed_formulas:
                    x = data[:i] + [reversed_formulas[compound]] + data[i+j:]
                    if get(str(x)):
                        queue.append((x, n_oper+1))
                        past[str(x)] = False

data = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'

past = {}
reversed_formulas = {}
file = open('19data.txt')

queue = deque([(re.findall(r'[A-Z][a-z]?', data),0)])

# Read data
for line in file:
    m = re.findall(r'[a-zA-Z]+', line)
    reversed_formulas[m[1]] = m[0]

print(f'Result: {find()}')
