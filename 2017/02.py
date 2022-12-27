import re as r

def main():
    data = open('02data.txt','r')
    check_sum = 0
    for line in data:
        numbers = [int(x) for x in r.split(r'\t',line)]
        check_sum += diff_max_min(numbers)
        # check_sum += get_evenly_divisable_number(numbers) # part 2
    print(check_sum)

def diff_max_min(numbers):
    minim = numbers[0]
    maxim = numbers[0]
    for n in numbers:
        minim = min(n,minim)
        maxim = max(n,maxim)
    return maxim - minim

# part 2
def get_evenly_divisable_number(numbers):
    is_evenly_divisable = lambda x,y: numbers[x] // numbers[y] == numbers[x] / numbers[y]
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if is_evenly_divisable(i,j):
                return numbers[i]/numbers[j]
            if is_evenly_divisable(j,i):
                return numbers[j]/numbers[i]

if __name__ == '__main__':
    main()