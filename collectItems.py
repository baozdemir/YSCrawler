#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import ast
import datetime

def getAllCompaniesFromZone():

	#json file company attrs
	DisplayName,CategoryName,CuisineNameList,DeliveryTime,MinimumDeliveryPrice,ImageFullPath,MainCuisineId,MainCuisineName,ServingText,href,SpeedText,FlavourText,AvgPoint,WorkHoursText = [], [], [], [], [], [], [], [], [], [], [], [], [], []

	#json file location attrs
	allZones,aCity, aZone, cityZones,zoneHref,aHref = [], [], [],[],[],[]

	with open('zonesAdiyaman.json', 'r') as f:
		zones_json = json.load(f)

			# count all city number
		length_cities = len(zones_json['allZones'])
		print ("Total City Numberrr: {}".format(length_cities))
		for count in range(length_cities):
			for (key, value) in zones_json['allZones'][count].items():
				length_outg = len(zones_json['allZones'][count][key])
				for count2 in range(length_outg):
					for (key2, value2) in zones_json['allZones'][count][key][count2].items():   
			# key -> city, key2 -> "tüm kampüsler"-"diğer bölgeler"...                        
			#print(zones_json['allZones'][count][key][count2][key2])
						city_zone_length = len(zones_json['allZones'][count][key][count2][key2])
						print("{} city have {} {}".format(key,city_zone_length,key2))
						print(zones_json['allZones'][count][key][count2][key2][0]['name'])
						hrefL = []
						for zone in zones_json['allZones'][count][key][count2][key2]:
							page = requests.get('https://www.yemeksepeti.com{}/#ors:false'.format(zone['url']))
							print(zone['url'])
							soup = BeautifulSoup(page.content, 'html.parser')
							companies = soup.find_all('a', class_='restaurantName')
							itemNameL = []
							uniqueItemList = []
							for company in companies:                       
								href = company['href']
								hrefL.append(href)
								print(href)
								page = requests.get('https://www.yemeksepeti.com{}'.format(href))
								soup = BeautifulSoup(page.content, 'html.parser')
								#####Menu listing#####
								itemName = ""
								restDetailBox = soup.find_all('div', class_='listBody')
								for category in restDetailBox:
										categoryItems = category.find_all('li')
										for item in categoryItems:
												itemNameSpan  = item.find_all('a')
												for names in itemNameSpan:
														if(len(names.get_text()) > 2):
																itemName=names.get_text()
																if(bool(itemName)):
																	if itemName not in itemNameL:
																		itemNameL.append(itemName)
																		print("{}".format(itemName))                              
							aHref.append({ "hrefs" : hrefL })
							zoneHref.append({zone['name'] : aHref})
							aZone.append({ "items" : itemNameL })
							cityZones.append({zone['name'] : aZone})
							aZone = []
							aHref = []
				aCity = ({ key : cityZones })
				cityZones = []    
				with open("allItems/{}_meals.json".format(key), 'w') as f:
					json.dump(aCity, f, ensure_ascii=False, indent=4, sort_keys=True)
				aCity = ({ key : zoneHref })
				zoneHref = []    
				with open("allItems/{}_hrefs.json".format(key), 'w') as f:
					json.dump(aCity, f, ensure_ascii=False, indent=4, sort_keys=True)
getAllCompaniesFromZone()
