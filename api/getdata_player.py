import http.client
import json

import pandas as pd

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token' : 'a5138360d35743f1961282ccb58f088f' }
r = '/v4/persons/'
name = []

for i in range(10):
    r = r + str(i)
connection.request('GET', '/v4/persons/{i}', None, headers)
response = json.loads(connection.getresponse().read().decode())
    
print(response)