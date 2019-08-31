from pwn import *

if __name__ == '__main__':
    s = ssh(host='behemoth.labs.overthewire.org', port=2221, user='behemoth0', password='behemoth0')
    s.download('/behemoth/behemoth0')
