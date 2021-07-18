from flask import Flask,request,jsonify,Response;
import json;
import requests;
import base64
import keys

 #import pyodbc;
app = Flask(__name__)
 
@app.route('/',methods=['GET','POST'])

def send_sms():
    URL = 'https://apisms.beem.africa/v1/send'
    api_key =keys.api_key
    secret_key = keys.secret_key
    content_type = 'application/json'
    source_addr = 'Kanyasu'
    apikey_and_apisecret = keys.api_key + ':' + keys.secret_key

    first_request = requests.post(url = URL,data = json.dumps({
    'source_addr': source_addr,
    'schedule_time': '',
    'encoding': '0',
    'message': 'Hello, Glory.',
    'recipients': [
    {
    'recipient_id': 1,
    'dest_addr': '255752585587',
    },
    ],
    }),
 
    headers = {
    'Content-Type': content_type,
    'Authorization': 'Basic ' + keys.api_key + ':' + keys.secret_key,
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