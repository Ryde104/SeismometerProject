
from multiprocessing.sharedctypes import Value
from pickle import GET
from pickletools import read_unicodestringnl
from unicodedata import name
from unittest import result
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(port=27017)
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

    test = {
        'psi' : request.json['psi']
    }
    result=db.pressure.insert_one(test)
    value = request.json['psi']
    return value
    

if __name__ == "__main__":
    app.run(debug=True)

