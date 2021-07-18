from flask import Flask,request,jsonify,Response;
import json;
import requests;
import base64
 #import pyodbc;
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])

def getCheckout():
    checkout_url = 'https://checkout.beem.africa/v1/checkout'
    api_key ='30c8bfbb68caae0c'
    secret_key = 'NTU1NjJhMjE2ZjVhYzkxZmZlODU1YmRjZGJlZDJlNDgxYTNhYWYzZTkzOTI4MWY4NDE2MDc4NWYxZTZhM2Y1Mg=='
    content_type = 'application/json'
    apikey_and_apisecret = api_key + ':' + secret_key
    
    payload = {
    "amount": "200",
    "reference_number": "SOKO-12345",
    "mobile": "255683869602",
    "sendSource": "true",
    "transaction_id": "96f9cc09-afa0-40cf-928a-d7e2b27b2408",
    }
    
    first_request = requests.get(url = checkout_url, params=payload,
    headers = {
    'Content-Type': content_type,
    'Authorization': 'Basic ' + api_key + ':' + secret_key,
    },
    auth=(api_key,secret_key),verify=False)
    print(first_request.status_code)
    print(first_request.json())
    return (first_request.json())

    @app.errorhandler(500)
    def server_error(e):
        errorName='Error'
        return Response(
            json.dumps(errorName),
            status=500,
            )
if __name__ == '__main__':
    app.run(debug=True)