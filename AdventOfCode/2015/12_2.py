import json

data = open('12data.txt','r')

js_data = json.loads(data.read())

def sum_not_red(elem):
    result = 0
    if type(elem) is list:
        for e in elem:
            result += sum_not_red(e)
    elif type(elem) is dict:
        if 'red' in elem.values():
            return 0
        for e in elem.values():
            result += sum_not_red(e)
    elif type(elem) is str:
        return 0
    else:
        result += elem
    return result
        

result = 0

result += sum_not_red(js_data)
print(f'The sum (without dicts with "red") is: {result}')