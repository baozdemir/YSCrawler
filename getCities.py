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
	city_data = {}
	names.append(city_name)
	hrefs.append(city_href)
json_data = [{"name" : n, "href" : h} for n,h in zip(names,hrefs)]	
#city_data['city_name'] = city_name
#city_data['city_href'] = city_href
#json_data = json.dumps(city_data)
with open('cities.json', 'w') as f:
    json.dump(json_data, f)



