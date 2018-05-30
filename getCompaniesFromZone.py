import requests
import json
from bs4 import BeautifulSoup
def getAllCompaniesFromZones ():
	DisplayName=[]
	with open('json/Adana_companies.json', 'r') as f:
    		companies_json = json.load(f)
	length_cities = len(companies_json['Adana'])
	for count in range(length_cities):
		#print(count) #semt sayısı
		for (key, value) in companies_json['Adana'][count].items():
			#print(companies_json['Adana'][count].items())	#comps un içeriği
			#print(value)	#tüm bölgeler
			#alttaki satırda Adana_companies.json dan 100.yıl ve comps tagleri içine girerek DisplayName kısmını almaya çalıştım
			#key,value çiftindeki value comps tagının içeriğini alıyor
			#bu içerikten DisplayName kısmını almam lazım.Alttaki satırdan mantıgını anlamışsındır
                	DisplayName.append(value['DisplayName'])	

	for dname in DisplayName:
		print(dname)
	
getAllCompaniesFromZones()
