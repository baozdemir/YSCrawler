#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup


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
                        #print(zones_json['allZones'][count][key][count2][key2])
                        city_zone_length = len(zones_json['allZones'][count][key][count2][key2])
                        print("{} city have {} {}".format(key,city_zone_length,key2))


getAllCompaniesFromZone()
