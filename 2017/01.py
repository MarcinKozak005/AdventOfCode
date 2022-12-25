
def main():
    number = open('01data.txt','r').readline()
    result = 0 
    step = 1
    # step = int(len(number)/2)  # part 2 
    for i in range(len(number)):
        result += int(number[i]) if number[i] == number[(i + step) % len(number)] else 0
    print(result)



if __name__ == '__main__':
    main()