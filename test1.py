from urllib import urlopen
import json
u = urlopen('http://jsonplaceholder.typicode.com/albums/')
resp = json.loads(u.read().decode('utf-8'))

from pprint import pprint
pprint (resp)

for i in resp:
    print i["userId"]