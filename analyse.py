import json
import glob, os, os.path
from datetime import datetime, timedelta
import re

directory = os.path.dirname(os.path.realpath(__file__))
os.chdir("menusjson")
for file in glob.glob("*ankara.json"):
    commentCounts = {}
    averagePoints = {}
    with open(file, 'r') as f:
        #print(file)
        companies_json = json.load(f)
        for count in range(len(companies_json["menu"])):
            item=companies_json["menu"][count]
            sitemName=item["ItemName"].lower()
            commentCounts[item["ItemName"]] = 0
            averagePoints[item["ItemName"]] = 0
            for tmp in range(len(companies_json["comment"])):
                comment = companies_json["comment"][tmp]
                for word in sitemName.split(" "):
                    if word in comment["Comment"].lower():
                        commentCounts[item["ItemName"]] = commentCounts[item["ItemName"]]+1
                        if re.match("^\d+?\.\d+?$",  comment["Flavour"]) is None:
                            avg = 0
                        else:
                       		avg = ((float(comment["Flavour"]) + float(comment["Serving"]) + float(comment["Speed"])) / 3)
                        averagePoints[item["ItemName"]] = round(((averagePoints[item["ItemName"]] * (commentCounts[item["ItemName"]] - 1)) + avg) / commentCounts[item["ItemName"]])
        print("yemek bazlı ortalama puanlar :")
        print(averagePoints)
        print("\n")
        print("yemek bazlı yapılan ortalama yorum sayıları :")
        print(commentCounts)
    with open(directory + "/analysis/" + file, 'w') as write:
        obj = { "commentCount": commentCounts, "averageScore": averagePoints}
        json.dump(obj, write, ensure_ascii=False, indent=4, sort_keys=True)
