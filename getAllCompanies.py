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
    allZones,aCity, aZone, cityZones = [], [], [],[]

    with open('zones.json', 'r') as f:
        zones_json = json.load(f)

            # count all city number

        length_cities = len(zones_json['allZones'])
        print ("Total City Number: {}".format(length_cities))
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
                        for zone in zones_json['allZones'][count][key][count2][key2]:
                            page = requests.get('https://www.yemeksepeti.com{}/#ors:false'.format(zone['url']))
                            print(zone['url'])
                            soup = BeautifulSoup(page.content, 'html.parser')
                            companies = soup.find_all('a', class_='restaurantName')
                            for company in companies:
                                company_span = company.find('span')
                                company_name = company_span.get_text()
                                company_datatooltip =  json.loads(company_span['data-tooltip'])
                                DisplayName.append(company_datatooltip['DisplayName'])
                                CategoryName.append(company_datatooltip['CategoryName'])
                                CuisineNameList.append(company_datatooltip['CuisineNameList'])
                                DeliveryTime.append(company_datatooltip['DeliveryTime'])
                                MinimumDeliveryPrice.append(company_datatooltip['MinimumDeliveryPrice'])
                                ImageFullPath.append(company_datatooltip['ImageFullPath'])
                                MainCuisineId.append(company_datatooltip['MainCuisineId'])
                                MainCuisineName.append(company_datatooltip['MainCuisineName'])
                                ServingText.append(company_datatooltip['ServingText'])
                                SpeedText.append(company_datatooltip['SpeedText'])
                                FlavourText.append(company_datatooltip['FlavourText'])
                                AvgPoint.append(company_datatooltip['AvgPoint'])
                                WorkHoursText.append(company_datatooltip['WorkHoursText'])
                                href.append(company['href'])                       
                            aZone.append({ "comps" : [{"DisplayName" : dn, "CategoryName" : cn,"CuisineNameList" : cnl, "DeliveryTime" : dt,"MinimumDeliveryPrice" : mdp, "ImageFullPath" : ifp,"MainCuisineId" : mci, "MainCuisineName" : mcn,"ServingText": st, "SpeedText": spt,"FlavourText": ft,"AvgPoint" : ap, "WorkHoursText":wht, "href" : h} for dn,cn,cnl,dt,mdp,ifp,mci,mcn,st,spt,ft,ap,wht,h in zip(DisplayName,CategoryName,CuisineNameList,DeliveryTime,MinimumDeliveryPrice,ImageFullPath,MainCuisineId,MainCuisineName,ServingText,SpeedText,FlavourText,AvgPoint,WorkHoursText,href)]})
                            DisplayName,CategoryName,CuisineNameList,DeliveryTime,MinimumDeliveryPrice,ImageFullPath,MainCuisineId,MainCuisineName,ServingText,href,SpeedText,FlavourText,AvgPoint,WorkHoursText = [], [], [], [], [], [], [], [], [], [], [], [], [], []
                            cityZones.append({zone['name'] : aZone})
                            aZone = []
                aCity = ({ key : cityZones })
                cityZones = []    
                with open("json/{}_companies.json".format(key), 'w') as f:
                    json.dump(aCity, f, ensure_ascii=False, indent=4, sort_keys=True)

getAllCompaniesFromZone()
