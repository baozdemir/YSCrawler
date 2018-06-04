import requests
import json
from bs4 import BeautifulSoup
import glob, os, os.path

def getAllCompaniesFromZone(href):
	if(not(os.path.isfile("{}{}.json".format("/home/knetwork/Desktop/YSCrawler/menusjson",href)))):
		page = requests.get('https://www.yemeksepeti.com{}'.format(href))
		soup = BeautifulSoup(page.content, 'html.parser')

		#//f = open ('out.txt', 'w')
		#f.write(soup.prettify())
		
		'''itemNames = soup.find_all('a', class_='getProductDetail')
		productInfos = soup.find_all('span', class_='productInfo')
		prices = soup.find_all('span', class_='pull-right newPrice')
		
		names, hrefs = [], []
		item_names=[]
		product_info=[]
		price_info=[]
		i=0
		for itemName in itemNames:
			item_name = itemName.get_text()
			item_names.append(item_name)
			for productInfo in productInfos:
				product_info_p = productInfo.find('p')
				product_info.append(product_info_p.get_text())
				for price in prices:	
					price_info.append(price.get_text())
			print('{}'.format(item_name))
			print('{}'.format(product_info[i]))
			print('{}{}'.format(price_info[i],"\n"))
			i=i+1'''
		itemNameL, itemInfoL, itemPriceL = [],[],[]
		restDetailBox = soup.find_all('div', class_='listBody')
		for category in restDetailBox:
			#categoryNameB = category.find('b')
			#print(categoryNameB)
			#if (not (categoryNameB is None)):
			#	break
			#categoryName = categoryNameB.get_text();
			categoryItems = category.find_all('li')
			for item in categoryItems:
				itemNameSpan  = item.find_all('a')
				for names in itemNameSpan:
					if(len(names.get_text()) > 2):
						itemName=names.get_text()
				itemInfo  = item.find('p').get_text()
				itemPriceSpan = item.find('span', class_='newPrice')
				itemPrice = itemPriceSpan.get_text()
				itemNameL.append(itemName)
				#categoryNameL.append(categoryName)
				itemInfoL.append(itemInfo)
				itemPriceL.append(itemPrice)				
				#print("{} {} {}".format(itemName,itemInfo,itemPrice))
		json_innerData = { "menu" : [{"ItemName" : n, "ItemInfo" : i, "ItemPrice" : p } for n,i,p in zip(itemNameL,itemInfoL,itemPriceL)]}
		#dirname=os.path.dirname("menusjson{}.json".format(href))
		#if not os.path.exists(dirname):
		#	os.makedirs(dirname)
		#open("/home/user/YSCrawler/menusjson/")
		print(href)
		if(len(json.dumps(json_innerData))>30):
			with open("{}{}.json".format("/home/knetwork/Desktop/YSCrawler/menusjson",href), 'w') as f:
				json.dump(json_innerData, f, ensure_ascii=False, indent=4, sort_keys=True)

os.chdir("json")
for file in glob.glob("*.json"):
	with open(file, 'r') as f:
		companies_json = json.load(f)
		city_name = file.split("_")[0]
		length_cities = len(companies_json[city_name])
		for count in range(length_cities):
			for (key, value) in companies_json[city_name][count].items():
				print(key)
				length_outg = len(companies_json[city_name][count][key])
				for count2 in range(length_outg):
					for (key2, value2) in companies_json[city_name][count][key][count2].items():   
			# key -> city, key2 -> "tüm kampüsler"-"diğer bölgeler"...                        
			#print(companies_json[city_name][count][key][count2][key2])
						city_zone_length = len(companies_json[city_name][count][key][count2][key2])
						#print("{} city have {} {}".format(key,city_zone_length,key2))
						for zone in companies_json[city_name][count][key][count2][key2]:
							getAllCompaniesFromZone(zone['href'])
