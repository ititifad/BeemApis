from flask import Flask,request,jsonify,Response;
import json;
import requests;
import base64
import keys

 #import pyodbc;
app = Flask(__name__)
 
@app.route('/',methods=['GET','POST'])

def whitelist():
    URL = 'https://checkout.beem.africa/v1/whitelist/add-to-list'
    api_key ='30c8bfbb68caae0c'
    secret_key ='NTU1NjJhMjE2ZjVhYzkxZmZlODU1YmRjZGJlZDJlNDgxYTNhYWYzZTkzOTI4MWY4NDE2MDc4NWYxZTZhM2Y1Mg=='
    content_type = 'application/json'
    website = 'https://edukani.herokuapp.com/'
    
    headers = {
    'Content-Type': content_type,
    'Authorization': 'Basic ' + keys.api_key + ':' + keys.secret_key,
    },
    
    return whitelist()

 
if __name__ == '__main__':
 app.run(debug=True)