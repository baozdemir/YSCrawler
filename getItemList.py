import requests
import json
from bs4 import BeautifulSoup
import glob, os

def getAllCompaniesFromZone(href):
	page = requests.get('https://www.yemeksepeti.com{}'.format(href))
	soup = BeautifulSoup(page.content, 'html.parser')

	#//f = open ('out.txt', 'w')
	#f.write(soup.prettify())
	itemNames = soup.find_all('a', class_='getProductDetail')
	productInfos = soup.find_all('span', class_='productInfo')
	prices = soup.find_all('span', class_='pull-right newPrice')

	names, hrefs = [], []
	product_info=[]
	price_info=[]
	i=0
	for itemName in itemNames:
		item_name = itemName.get_text()
		for productInfo in productInfos:
			product_info_p = productInfo.find('p')
			product_info.append(product_info_p.get_text())
			for price in prices:	
				price_info.append(price.get_text())
		print('{}'.format(item_name))
		print('{}'.format(product_info[i]))
		print('{}{}'.format(price_info[i],"\n"))
		i=i+1
os.chdir("json")
for file in glob.glob("*.json"):
	with open(file, 'r') as f:
		companies_json = json.load(f)
		city_name = file.split("_")[0]
		length_cities = len(companies_json[city_name])
		for count in range(length_cities):
			for (key, value) in companies_json[city_name][count].items():
				length_outg = len(companies_json[city_name][count][key])
				for count2 in range(length_outg):
					for (key2, value2) in companies_json[city_name][count][key][count2].items():   
			# key -> city, key2 -> "tüm kampüsler"-"diğer bölgeler"...                        
			#print(companies_json[city_name][count][key][count2][key2])
						city_zone_length = len(companies_json[city_name][count][key][count2][key2])
						print("{} city have {} {}".format(key,city_zone_length,key2))
						for zone in companies_json[city_name][count][key][count2][key2]:
							getAllCompaniesFromZone(zone['href'])
			
			
			
