from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import bs4
import pymongo
import requests
app = Flask(__name__)

titleAndLink = []

app.config['MONGO_DBNAME'] = 'wikiscrap'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/wikiscrap'

mongo = PyMongo(app)


def scrapURL(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for link in soup.select('a'):
        titleName = link.get('title')
        refLink = link.get('href')
        if titleName:
            templink = "https://wikipedia.org"+refLink
            titleAndLink.append([titleName, templink])
            testcollection.insert_one(
                {"keyword": titleName, "reflink": templink})


dburl = "mongodb://localhost:27017/"
mydbclient = pymongo.MongoClient(dburl)
testdatabase = mydbclient["wikiscrap"]
testdatabase.drop_collection("keywords")
testcollection = testdatabase["keywords"]


@app.route('/scrapurl', methods=["POST"])
def scrap_wiki_url():
    req_json = request.json
    scrapurl = req_json['scrapurl']
    titleAndLink.append(["dummy", scrapurl])
    i = 0
    while len(titleAndLink) < 5000:
        scrapURL(titleAndLink[i][1])
        i += 1

    return jsonify({"response": "Entered url " + scrapurl + " is scrapped and data saved in database!!!"})


@app.route('/allurls', methods=['GET'])
def get_all_urls():
    keyword = mongo.db.keywords
    output = []
    for item in keyword.find():
        output.append({'keyword': item['keyword'], 'reflink': item['reflink']})
    return jsonify({'result': output})


@app.route('/allurls/<searchkey>', methods=["GET"])
def get_related_keywords(searchkey):
    keyword = mongo.db.keywords
    output = []
    searchkey = searchkey.lower()
    for item in keyword.find():
        output.append({'keyword': item['keyword'], 'reflink': item['reflink']})
    if not output:
        output = "No result found!!!"
        return jsonify({'result': output})

    finalResult = []

    for item in output:
        if searchkey in item['keyword'].lower():
            finalResult.append(
                {'keyword': item['keyword'], 'reflink': item['reflink']})

    displayResult = []

    for item in finalResult:
        if item not in displayResult and len(displayResult) < 10:
            displayResult.append(item)

    return jsonify({'result': displayResult})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
