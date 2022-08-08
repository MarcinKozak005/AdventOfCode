import re

def get(key):
    try:
        return formulas[key]
    except KeyError:
        formulas[key] = []
        return formulas[key]

data = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'

formulas = {}
results = set()
file = open('19data.txt')

# Read data
for line in file:
    m = re.findall(r'[a-zA-Z]+', line)
    get(m[0]).append(m[1])

# Calculate
molecules = re.findall(r'[A-Z][a-z]?', data)

for i in range(len(molecules)):
    if molecules[i] in formulas:
        tmp = molecules[i]
        for f in formulas[molecules[i]]:
            molecules[i] = f
            results.add(''.join(molecules))
        molecules[i] = tmp

print(f'Distinct molecules: {len(results)}')
