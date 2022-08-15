from hashlib import md5

password = {}
i = 0
key = 'ugkcyxxp'
while len(password) < 8:
    encoded = (key + str(i)).encode('utf-8')
    digest = md5(encoded).hexdigest()
    if digest[:5] == '00000':
        try:
            p = int(digest[5])
        except ValueError:
            i += 1
            continue
        if p <= 7 and p not in password:
            password[p] = digest[6]
            print(f'{p}: {digest[6]}')
    i += 1
