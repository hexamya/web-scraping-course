import requests
from bs4 import BeautifulSoup

data = {
    'search': 'operations research'
}
response = requests.get('https://data.mendeley.com/research-data/', params=data)

soup = BeautifulSoup(response.content, 'html5lib')


print(Fore.BLUE)
print(Style.RESET_ALL)

soup.prettify()

print("\n\n".join([i.getText() for i in soup.select('.item-title')]))

print('\n\n'.join([f"{i.getText()}\n{i['href']}" for i in soup.select('.item-title')]))


data = [{'search': 'operations research'},{'search': 'Statistical Optimization'},{'search': 'Industrial Engineering'}]

responses = []
for i in data:
    responses.append(requests.get('https://data.mendeley.com/research-data/', params=i))

def soups(res):
    soup = BeautifulSoup(res.content, 'html5lib')

    print("\n\n".join([i.getText() for i in soup.select('.item-title')]))

    print('\n\n'.join([f"{i.getText()}\n{i['href']}" for i in soup.select('.item-title')]))

for i in responses:
    soups(i)

