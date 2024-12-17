divisors = {
    1:[1],
    2:[1,2]
    }

def get_divisors(num):
    i = num -1
    while True:
        if num % i == 0:
            result = []
            y = divisors[i]
            try:
                z = divisors[int(num/i)]
            except KeyError:
                z = []
            for e in y+z:
                if num % e == 0:
                    result.append(e)
                    result.append(int(num/e))
            divisors[num] = list(set(result))
            return divisors[num]
        i -= 1


i = 2
while True:
    print(i)
    if sum(get_divisors(i)) >= 3400000:
        break
    i += 1
print(f'Lowest house number is: {i}') 
