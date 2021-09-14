import requests

response = requests.request('GET', 'https://www.hltv.org/events#tab-ALL')

print(response)