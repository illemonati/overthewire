import base64

encoded = '3d3d516343746d4d6d6c315669563362'


def decode(og: str):
    a = bytes.fromhex(og).decode()
    b = a[::-1]
    c = base64.b64decode(b)
    return c


if __name__ == '__main__':
    print(decode(encoded))
