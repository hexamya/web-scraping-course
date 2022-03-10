import requests

response = requests.get('https://docs.djangoproject.com/en/4.0/')

c = response.content

with open('index.html', 'wb') as fp:
    fp.write(c)