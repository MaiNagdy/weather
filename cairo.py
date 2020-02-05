from flask import Flask,request,jsonify
import requests
import json


app1= Flask(__name__)




@app1.route('/weather', methods=['GET'])
def weather():
 q=input("enter a city..")
 api_address='22dc9f732f316339d81e20d9a93a8866'
 url ='http://api.openweathermap.org/data/2.5/weather?appid={}&q={}'.format(api_address,q)
 response =(requests.get(url).json())
 return response["weather"]
 

 
  


if __name__ == "__main__":
	app1.run(port=8000)