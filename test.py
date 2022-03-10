from bs4 import BeautifulSoup
from colorama import Style, Fore, Back

with open('test.html', 'r', encoding='utf-8') as fp:
    htmldoc = fp.read()

print(Fore.RED+ htmldoc +Style.RESET_ALL)

soup = BeautifulSoup(htmldoc, 'html.parser')

print(Fore.BLUE)
soup.findAll('p')

soup.find('h1')

soup.h1.getText()
soup.h1.string

soup.find(id='text')

soup.findAll(class_='t')

soup.h1['id']