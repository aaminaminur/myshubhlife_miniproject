# Necessary imports
# Here BeautifulSoup from bs4 library is used

import requests
import bs4

# Hardcoding the URL, will work to take it dynamically later
url = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"

# Making request and making soup using BeautifulSoup and html-parser
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# print(type(soup))

# Storing all URLS in an Array named urls
urls = []
for link in soup.select('a'):
    titleName = link.get('title')
    refLink = link.get('href')
    # There are many links without title (i.e. Title coming out as None).
    # So, eliminating links without Title
    if titleName:
        urls.append([titleName, refLink])

# Printing all URLS for test purpose
for item in urls:
    print(item)
