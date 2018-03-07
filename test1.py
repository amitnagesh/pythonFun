from urllib import urlopen
import json
u = urlopen('http://jsonplaceholder.typicode.com/albums/')
resp = json.loads(u.read().decode('utf-8'))

from pprint import pprint
pprint ("---------")
pprint (resp)
pprint ("---------")

for i in resp:
    if "adipisci laborum fuga laboriosam" in i["title"]:
        print i["id"]
    if "adipisci laborum fuga laboriosam" not in i["title"]:
        continue
pprint ("---------")        

        
        