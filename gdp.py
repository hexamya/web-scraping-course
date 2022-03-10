import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.worldometers.info/gdp/gdp-by-country/')

soup = BeautifulSoup(response.content, 'html5lib')

print(Fore.BLUE)
print(Style.RESET_ALL)

requests.utils.default_headers()

# for id selection -----> #
# for class selection -----> .

table = soup.select_one('#example2')

HEADER = [ i.getText() for i in table.thead.tr.findAll('th') ]

LIST = [[i.getText() for i in j.findAll('td')] for j in table.tbody.findAll('tr')]

STR = "\n".join([" - ".join([i.getText() for i in j.findAll('td')]) for j in table.tbody.findAll('tr')])

print(STR)

with open('gdp.txt', 'w', encoding='utf-8') as fp:
    fp.write(STR)

{ i[0]: i[1:]  for i in LIST }

GDP = pd.DataFrame({HEADER[j]:[ i[j] for i in LIST] for j in range(len(HEADER))})

GDP.to_excel('gdp.xlsx')