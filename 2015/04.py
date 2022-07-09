import hashlib  # for hashlib.md5

key = 'bgvyzdsv'
i = 0
while True:
    encoded = (key + str(i)).encode('utf-8')
    digest = hashlib.md5(encoded).hexdigest()
    if digest[0:5] == '00000':
    # if digest[0:6] == '000000':  # part2 
        break
    i += 1
print(f'The answer is {i}')
