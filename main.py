import requests

response = requests.get('https://docs.djangoproject.com/en/4.0/')

c = response.content

with open('index.html', 'wb') as fp:
    fp.write(c)

# string
response.text
# binary
response.content



response2 = requests.get('https://api.agify.io/?name=amin')

response2.text


# ageDict = {'ali': 50, 'hasan': 30}
# ageDict['hasan']

agify = response2.json()
agify['name']

###

response3 = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

bpi = response3.json()

bpi.keys()

print(bpi['chartName'])
print(bpi['time']['updated'])

c = bpi['bpi']['USD']
print('\n'.join([f"{i}: {c[i]}" for i in c]))