import requests
import json
from bs4 import BeautifulSoup
import glob, os, os.path
from datetime import datetime, timedelta
import re

directory = os.path.dirname(os.path.realpath(__file__))

class DateTimeAwareEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)
def getAllCompaniesFromZone(href):
	filePath = "{}{}{}.json".format(directory, "/menusjson",href)
	try:
		# dir_path bu kodun dizinidir.
		with open(filePath) as json_data:
			content = json.load(json_data)
	except EnvironmentError:  # Eger dosya yoksa ici bos bir obje yaratilir.
		content = {"menu":[], "comment":[]}
	if (len(content["comment"]) > 0):
		# json dosyasindaki en guncel yorumun tarihi
		lastCheckDate = datetime.strptime(content["comment"][0]["Date"], "%Y-%m-%d")
	else :
		# json dosyasinda hic comment yoksa son kontrol tarihi 1990 yapildi
		lastCheckDate = datetime.strptime("1990-01-01", "%Y-%m-%d")
	page = requests.get('https://www.yemeksepeti.com{}'.format(href))
	soup = BeautifulSoup(page.content, 'html.parser')
	#####Menu listing#####
	itemNameL, itemInfoL, itemPriceL = [],[],[]
	restDetailBox = soup.find_all('div', class_='listBody')
	for category in restDetailBox:
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
	#####comment listing####
	flavourL,speedL,servingL,noteL,dateL = [],[],[],[],[]
	#get total comment page number
	pageListNav = soup.find_all('nav', class_='ys-pagination')
	currentDate = datetime.now()
	isBreak = False
	for pageList in pageListNav:
		pageA  = pageList.find_all('a')
		for page in pageA:
			commentHref = page['href']
			commentPage = requests.get('https://www.yemeksepeti.com{}'.format(commentHref))
			commentSoup = BeautifulSoup(commentPage.content, 'html.parser')
			commentBodies = commentSoup.find_all('div', class_='comments-body')
			for comment in commentBodies:
				flavour = ""
				speedStringD = comment.find_all('div', class_='speed')
				for stre in speedStringD:
					speedString = stre.get_text()
					speed = re.sub("\D", "", speedString)
				servingStringD = comment.find_all('div', class_='serving')
				for stre in servingStringD:
					servingString = stre.get_text()
					serving = re.sub("\D", "", servingString)
				flavourStringD = comment.find_all('div', class_='flavour')
				for stre in flavourStringD:
					flavourString = stre.get_text()
					flavour = re.sub("\D", "", flavourString)
				noteP = comment.find_all('p')
				for stre in noteP:
					note = stre.get_text()
				dateStringDc = comment.find_all('div', class_='commentDate')
				for dateStringD in dateStringDc:
					dateString = dateStringD.find_all('div')
					for dateS in dateString:
						dateLast = dateS.get_text()
				dateNumber = re.sub("\D", "", dateLast)
				if ("bugün" in dateLast):
					date = currentDate
				elif ("ay" in dateLast):
					date = currentDate - timedelta(days=(int(dateNumber) * 30))
				else:
					date = currentDate - timedelta(days=int(dateNumber))
				date = date.replace(hour=0, minute=0, second=0, microsecond=0)
				# en son kontrolde okunan bir comment ise comment parse bitirilir.
				if(date <= lastCheckDate):
					isBreak = True
					break
				dateL.append(date.strftime("%Y-%m-%d"))
				if(bool(flavour)):
					flavourL.append(flavour)
					speedL.append(speed)
					servingL.append(serving)
					noteL.append(note)
			if isBreak:
				break
		if isBreak:
			break

	json_innerData = { "menu" : [{"ItemName" : n, "ItemInfo" : i, "ItemPrice" : p } for n,i,p in zip(itemNameL,itemInfoL,itemPriceL)],"comment" : [{"Date" : d, "Speed" : sp, "Serving" : sv, "Flavour" : f, "Comment" : c } for d,sp,sv,f,c in zip(dateL,speedL,servingL,flavourL,noteL)]}
	content["menu"] = json_innerData["menu"]
	# commentler onceden okunan commentlerin en basina insert edilir.
	content["comment"][0:0] = json_innerData["comment"]
	print(href)
	print(json_innerData["comment"])#sadece yeni okunan yorumlar print edilir
	with open(filePath, 'w') as f:
		json.dump(content, f, ensure_ascii=False, indent=4, sort_keys=True)

os.chdir("json")
processed_hrefs = set()
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
							if (zone['href'] in processed_hrefs):
								print("{} yolu zaten crawl edildi!\n".format(zone['href']))
							else:
								getAllCompaniesFromZone(zone['href'])
								processed_hrefs.add(zone['href'])
