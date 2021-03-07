# Necessary imports
# Here BeautifulSoup from bs4 library is used
import requests
import bs4

import pymongo

dburl = "mongodb://localhost:27017/"
mydbclient = pymongo.MongoClient(dburl)
testdatabase = mydbclient["wikiscrap"]
testcollection = testdatabase["keywords"]

# Hardcoding the URL, will work to take it dynamically later
url = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"
# Making request and making soup using BeautifulSoup and html-parser
# print(type(soup))
# Storing all URLS in an Array named urls
titleAndLink = []
titleAndLink.append(["dummy", url])


def scrapURL(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for link in soup.select('a'):
        titleName = link.get('title')
        refLink = link.get('href')
        # There are many links without title (i.e. Title coming out as None).
        # So, eliminating links without Title
        if titleName:
            templink = "https://wikipedia.org"+refLink
            titleAndLink.append([titleName, templink])


# if titleName:
#     templink = "https://wikipedia.org"+refLink
#     titleAndLink.append({"_id": titleName, "refLink": templink})

i = 0
while len(titleAndLink) < 5000:
    scrapURL(titleAndLink[i][1])
    i += 1
# Printing all URLS for test purpose
print(len(titleAndLink))

linksToStoreInDB = []

for items in titleAndLink:
    dict = {"_id": items[0], "reflink": items[1]}
    linksToStoreInDB.append(dict)

# print(linksToStoreInDB)

x = testcollection.insert_many(linksToStoreInDB)

if x:
    print("Success!!!")
