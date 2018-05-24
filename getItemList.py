import requests
import json
from bs4 import BeautifulSoup

page = requests.get("https://www.yemeksepeti.com/korykos-mersin-tantuni-besevler-ankara")
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
	#names.append(city_name)
	#hrefs.append(city_href)
#json_data = { "cities" : [{"name" : n, "href" : h} for n,h in zip(names,hrefs)]}

#with open('cities.json', 'w') as f:
 #   json.dump(json_data, f,ensure_ascii=False)



