import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.yemeksepeti.com/sehir-secim")
soup = BeautifulSoup(page.content, 'html.parser')

f = open ('out.txt', 'w')
f.write(soup.prettify())

cities = soup.find_all('a', class_='cityLink')

for city in cities:
	city_name = city.find_all('span', class_='name')
	print('{}{}'.format(city_name,"\n"))


