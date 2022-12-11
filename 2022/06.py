
def main():
    data = open('06data.txt').read()
    # num_of_last_char = 4
    num_of_last_char = 14  # part 2
    pos = num_of_last_char
    while True:
        if len(set(data[(pos-num_of_last_char):pos])) == num_of_last_char:
            print(pos)
            return
        pos += 1
    


if __name__ == '__main__':
    main()