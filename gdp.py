import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.worldometers.info/gdp/gdp-by-country/')

soup = BeautifulSoup(response.content, 'html5lib')

print(Fore.BLUE)
print(Style.RESET_ALL)


# for id selection -----> #
# for class selection -----> .

table = soup.select_one('#example2')

[ i.getText() for i in table.thead.tr.findAll('th') ]

[[i.getText() for i in j.findAll('td')] for j in table.tbody.findAll('tr')]
