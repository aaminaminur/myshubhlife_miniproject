from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'wikiscrap'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/wikiscrap'

mongo = PyMongo(app)


@app.route('/allurls', methods=['GET'])
def get_all_urls():
    keyword = mongo.db.keywords
    output = []
    for item in keyword.find():
        output.append({'keyword': item['_id'], 'reflink': item['reflink']})
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
