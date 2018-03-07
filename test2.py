from urllib2 import urlopen
import json

url = 'http://jsonplaceholder.typicode.com/albums/'
response = urlopen(url)
json_obj = json.load(response)

for i in json_obj:
    print i['title']