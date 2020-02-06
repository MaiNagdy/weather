from flask import Flask,request,jsonify
import requests
import json


app1= Flask(__name__)




@app1.route('/weather', methods=['GET'])
def weather():
 response={}
 q = request.args.get('q', default=None, type=str)
 
 appid=request.args.get('appid',default=None,type=str)
 url ='http://api.openweathermap.org/data/2.5/weather?appid={}&q={}'.format(appid,q)
 response =(requests.get(url).json())
 return jsonify(response)

 
  


if __name__ == "__main__":
	app1.run(port=8000)
