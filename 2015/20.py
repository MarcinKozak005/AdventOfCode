from math import sqrt

def get_divisors(num):
    result = []
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            result.append(num/i)
    return result


i = 10
while True:
    print(i)
    if sum(get_divisors(i)) >= 3400000:
        break
    i += 1
print(f'Lowest house number is: {i}') 
