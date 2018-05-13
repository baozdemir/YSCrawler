#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import ast

def getAllCompaniesFromZone():
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
                            page = requests.get('https://www.yemeksepeti.com{}'.format(zone['url']))
                            soup = BeautifulSoup(page.content, 'html.parser')
                            companies = soup.find_all('a', class_='restaurantName')
                            for company in companies:
                                company_span = company.find('span')
                                company_name = company_span.get_text()
                                company_datatooltip =  json.loads(company_span['data-tooltip'])
                                print(company_datatooltip['CategoryName'])
                                '''for k,v in company_datatooltip.items():
                                    if(k is "CategoryName"):
                                        print(v)'''

getAllCompaniesFromZone()
            
            
'''<span data-tooltip="{ ;AreaName ;: ;Acıbadem ;, ;CatalogName ;: ;TR_ISTANBUL ;,
                             ;CategoryName ;: ;2b57297a-d0cc-433b-9163-49147e471d8d ;
                             , ;ClosedByParent ;:false, ;CuisineNameList ;:[ ;Kahvaltı ;, ;Cafe ;, ;Pasta \u0026 Tatlı ;],
                              ;DeliveryFee ;:0, ;DeliveryTime ;:45, ;DisplayName ;: ;G&#246;reme Muhallebicisi, Acıbadem ;
                              , ;Flavour ;:9.24, ;HasDVDPromotion ;:false, ;ImageLabel ;:null, ;ImageLabelList ;:[ ;cc_genel.gif ;], 
                              ;ImagePath ;: ;/CategoryImages/TR_ISTANBUL/goreme_muhalllebicisi_kurtulus.gif ;
                              , ;ImageFullPath ;: ;http://images.yemeksepeti.com//CategoryImages/TR_ISTANBUL/goreme_muhalllebicisi_kurtulus_big.gif ;
                              , ;ImageLabelListFullPath ;:[ ;http://images.yemeksepeti.com/Labels/Restaurant/cc_genel.gif ;],
                               ;IsOpen ;:true, ;IsRestaurantOpen ;:true, ;MainCuisineId ;: ;96f07b33-348d-4848-b428-005cf224f9c3 ;,
                                ;MainCuisineLabelName ;: ;Pasta.jpg ;, ;MainCuisineName ;: ;Pasta
                                 \u0026 Tatlı ;, ;MinimumDeliveryPrice ;:5.0, ;Oid ;:0, ;OpenRestaurantCount ;:0,
                                  ;PaymentMethodsText ;: ;Ticket Restaurant Yemek Kartı^Nakit^Multinet^Online Kredi/Banka Kartı^Ticket Restaurant Yemek
                                   &#199;eki^SetCard^MetropolCard^Sodexo Yemek &#199;eki^Sodexo Yemek Kartı^Kredi Kartı^ ;, ;PaymentMethodsList ;:
                                   [ ;Ticket Restaurant Yemek Kartı ;, ;Nakit ;, ;Multinet ;, ;Online Kredi/Banka Kartı ;, ;Ticket Restaurant Yemek &#199;eki ;, ;SetCard ;, ;MetropolCard 
                                   ;, ;Sodexo Yemek &#199;eki ;, ;Sodexo Yemek Kartı ;, ;Kredi Kartı ;], ;PrimaryParentCategory ;: ; 
                                   ;, ;PromotionInfoForFOC ;:null, ;PromotionInfo ;:[{ ;DiscountId ;:6150170, ;PromotionImageUrl ;: ;genelpromosyon.gif ;, ;PromotionText ;: 
                                   ;Sadece Yemeksepeti\u0027nde, \u0027Se&#231;ilmiş Men&#252; (Et D&#246;ner D&#252;r&#252;m - 70 gr.)\u0027 22 TL yerine 19,5 TL! ;},
                                   { ;DiscountId ;:6150171, ;PromotionImageUrl ;: ;null ;, ;PromotionText ;: ;Sadece Yemeksepeti\u0027nde, \u0027Se&#231;ilmiş Men&#252; 
                                   (Kaşarlı K&#246;fte)\u0027 30 TL yerine 26,9 TL! ;}], ;PromotionInfoForPopup ;: ; ;, ;RestaurantSubState ;: ; ;, ;Serving ;:9.37, ;
                                    Slug ;:null, ;Speed ;:9.09, ;WorkHoursText ;: ;08:00-23:59 ;, ;Refiners ;:{ ;AreasCount ;:[], ;CuisinesCount ;:[], ;HasDvdPromotionCount ;:0, 
                                    ;HasPromotionCount ;:0, ;OpenRestaurantCount ;:0}, ;AvgPoint ;: ;9,2 ;, ;ImagePathSmall ;: 
                                    ;/CategoryImages/TR_ISTANBUL/goreme_muhalllebicisi_kurtulus_small.gif ;, ;ImageFullPathSmall ;: ;
                                    http://images.yemeksepeti.com//CategoryImages/TR_ISTANBUL/goreme_muhalllebicisi_kurtulus_small.gif ;, ;
                                    SeoUrl ;: ;/goreme-muhallebicisi-acibadem-istanbul ;, ;CuisineImageList ;:[ ;Pasta.jpg ;, ;kahvalti.png ;, ;Cafe.jpg ;],
                                     ;AllPromotionImageList ;:[ ;genelpromosyon.gif ;, ;cc_genel.gif ;], ;ServingText ;: ;9,4 ;, ;SpeedText ;: ;9,1 ;, ;FlavourText ;: ;9,2 ;,
                                      ;AvgRestaurantScore ;: ;9,2 ;, ;AvgRestaurantScorePoint ;:9.2, ;MinimumDeliveryPriceText ;: ;5,00 ;, ;RestaurantSubStateText ;:null
                                      , ;AvgPointHtmlClass ;: ;point11 ;, ;FlavourPointHtmlClass ;: ;nopoint ;, ;HasCampusDiscount ;:false, ;IsFreezoneRestaurant ;:false,
                                       ;IsNew ;:false, ;IsYSDeliveryRestaurant ;:false, ;HasPromotion ;:true}">G&#246;reme Muhallebicisi, Acıbadem</span>'''