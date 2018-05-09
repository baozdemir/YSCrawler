import requests
import json
from bs4 import BeautifulSoup
def getAllZones ():
	with open('cities.json', 'r') as f:
    		cities_json = json.load(f)
	zoneNames , zoneUrls, zone, zoneInfo = [], [], [], []
	cityName , cityZoneInfo = [], []
	for city in cities_json['cities']:
		print('{} city is parsing by https://www.yemeksepeti.com{}'.format(city['name'],city['href']))
		page = requests.get('https://www.yemeksepeti.com{}'.format(city['href']))
		soup = BeautifulSoup(page.content, 'html.parser')
		optgroups = soup.find_all('optgroup')
		for opt in optgroups:
			zones = opt.find_all('option')
			for zone in zones :
				zone_url = zone['data-url']
				zone_name = zone.get_text()
				zoneNames.append(zone_name)
				zoneUrls.append(zone_url)							
			json_innerData = { opt['label'] : [{"name" : n, "url" : u} for n,u in zip(zoneNames,zoneUrls)]}
			zoneInfo.append(json_innerData)
		cityZoneInfo.append( {city['name'] :[json_innerData]}) 
	json_data = { "allZones" : [cityZoneInfo]}		
	with open('zones.json', 'w') as f:
    		json.dump(json_data, f,ensure_ascii=False)


def getZone (city_name):
	with open('cities.json', 'r') as f:
    		cities_json = json.load(f)
	for city in cities_json['cities']:
		if(city['name']==city):
			print('{} city is parsing by https://www.yemeksepeti.com{}'.format(city['name'],city['href']))
			page = requests.get('https://www.yemeksepeti.com{}'.format(city['href']))
			soup = BeautifulSoup(page.content, 'html.parser')
			return city
getAllZones()
