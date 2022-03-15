
from multiprocessing.sharedctypes import Value
from pickle import GET
from pickletools import read_unicodestringnl
from unicodedata import name
from unittest import result
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
#client = MongoClient("mongodb://157.55.164.231:27017")
#client = MongoClient("mongodb://seismic:27017")
#client = MongoClient("mongodb://10.0.45.171:27017")

client = MongoClient('mongo', 27017)
#client = MongoClient(port=27017)
db=client.pressure

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/receive', methods=['GET', 'POST'])
def receive():
    #result = "result"
    return jsonify({"Psi" : [3000]})
    

@app.route('/post', methods=['POST']) 
def post():

    print (request.data)
    #test = {
    #    'psi' : request.json['psi']
    #}
    #result=db.pressure.insert_one(test)
    #value = request.json['psi']
    #return value
    return request.json['psi']
    

if __name__ == "__main__":
    app.run(debug=True)