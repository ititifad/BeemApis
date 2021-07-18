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
    apikey_and_apisecret = api_key + ':' + secret_key
    
    first_request = requests.post(url = URL,data = json.dumps({
    'website': website,
    }),
    
    headers = {
    'Content-Type': content_type,
    'Authorization': 'Basic ' + api_key + ':' + secret_key,
    'website':website,
    },
    
    auth=(keys.api_key,keys.secret_key),verify=False)
    
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