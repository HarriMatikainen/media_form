from bson import ObjectId
from flask import Flask, render_template, request, url_for
import pymongo
from werkzeug.utils import redirect

app = Flask(__name__)

uri = "mongodb://127.0.0.1:27017"
# käynnistetään tietokannan asiakas
client = pymongo.MongoClient(uri)
# tietokannan nimi
# database = client['Kirjasto']
# "taulukon" nimi
# collection = database['kirjat']

# database = client['menu']
# collection = database['bills']

# collection.insert({"Testi": 12345})

# rows = collection.find({}) # 4 objects
# for row in rows:
#    print(row)

@app.route('/media_form')
def open_media_form():
    return render_template("mediaFormNew.html")

@app.route('/action', methods=['POST'])
def tee_jotain():
    return "Teen jotain!"

if __name__ == "__main__":
    app.run()