def main():
    data = open('03data.txt','r')
    result = first_part(data)
    # result = second_part(data)
    data.close()
    print(result)

def first_part(data):
    result = 0
    for line in data:
        middle = int(len(line)/2)
        char = set(line[:middle]).intersection(set(line[middle:]))
        if len(char) != 0:
            result += get_char_priority(char.pop())
    return result

# part 2
def second_part(data):
    result = 0
    line1 = data.readline()
    while line1:
        line2 = data.readline()
        line3 = data.readline()
        char = set(line1).intersection(set(line2)).intersection(set(line3))
        char = [x for x in char if x!='\n'][0]
        result += get_char_priority(char)
        line1 = data.readline()
    return result

def get_char_priority(char):
    return ord(char) - (96 if char >= 'a' and char<='z' else 38)

if __name__ == '__main__':
    main()