import re

data = open('12data.txt')

data_string = data.read()

string_list = re.findall('-?\d+', data_string)
numbers_sum = sum([int(x) for x in string_list])

print(f'The sum of the numbers is {numbers_sum}')
