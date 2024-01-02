import requests
import json

print("***WEATHER***")
city=input("Weather for which city?")

api_key= 'h5vmpbrhoxkv1dgjoc8ebhmhzfxhcbml'

url= 'https://api.openweathermap.org/data/2.5/weather?'
full_url=url+"q="+city+"&appid="+api_key

response=requests.get(full_url)
#if __name__=="__main__":
data=response.json()
main=data['main']
temp=main['temp']
hum=main['humidity']
pres=main['pressure']
report=data['weather']

print(f"{city:-^30}")
print(f"Temperature: {temp}")
print(f"Humidity: {hum}")
print(f"Pressure: {pres}")
print(f"Weather report: {report[0]['description']}")