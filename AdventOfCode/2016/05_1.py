from hashlib import md5

password = ''
i = 0
key = 'ugkcyxxp'
while len(password) < 8:
    encoded = (key + str(i)).encode('utf-8')
    digest = md5(encoded).hexdigest()
    if digest[:5] == '00000':
        password += str(digest[5])
        print(password)
    i += 1