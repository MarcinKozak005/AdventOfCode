import re

def main():
    data = open('04data.txt','r')
    result = 0
    for line in data:
        ranges = [int(x) for x in re.split(r'[,-]',line)]
        # result = result + (1 if fully_contains(ranges) else 0)
        result = result + (1 if overlaps(ranges) else 0)
    print(result)

def fully_contains(r):
    return (r[0]>=r[2] and r[1]<=r[3]) or (r[2]>=r[0] and r[3]<=r[1])

# part 2
def overlaps(r):
    return not(
        (r[0] < r[2] and r[1] < r[2]) or 
        (r[0] > r[3] and r[1] > r[3]) or 
        (r[2] < r[0] and r[3] < r[0]) or 
        (r[2] > r[1] and r[3] > r[1])
        )

if __name__ == '__main__':
    main()