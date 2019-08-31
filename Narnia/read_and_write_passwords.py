import json
from prettytable import PrettyTable
import sys

pfile = open('passwords.json', 'r+')
pdic = dict(json.load(pfile))
if len(sys.argv) > 1:
    if sys.argv[1] == 'd':
        pdic.pop('narnia' + str(len(pdic)))
    else:
        pdic['narnia' + str(len(pdic) + 1)] = sys.argv[1]
    pfile.seek(0)
    pfile.truncate()
    json.dump(pdic, pfile)
pfile.close()

table = PrettyTable()
table.field_names = ['level', 'password']
for (k, v) in pdic.items():
    table.add_row([k, v])
print(table)
