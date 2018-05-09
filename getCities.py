import requests
import json
from bs4 import BeautifulSoup

page = requests.get("https://www.yemeksepeti.com/sehir-secim")
soup = BeautifulSoup(page.content, 'html.parser')

f = open ('out.txt', 'w')
f.write(soup.prettify())

cities = soup.find_all('a', class_='cityLink')

names, hrefs = [], []
for city in cities:
	city_name_span = city.find('span', class_='name')
	city_name = city_name_span.get_text()
	city_href = city['href']	
	print('{}{}'.format(city_name,"\n"))
	names.append(city_name)
	hrefs.append(city_href)
json_data = { "cities" : [{"name" : n, "href" : h} for n,h in zip(names,hrefs)]}	

with open('cities.json', 'w') as f:
    json.dump(json_data, f,ensure_ascii=False)



