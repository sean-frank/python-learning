import requests, json

api_key = 'null'
query = input("Enter the city in which you would like to get the current forecast: ")
link = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={query}&aqi=no"
results = requests.get(link).json()
current_weather_data = results['current' ]['condition']['text']).lower().strip('"')
region_data = results['location']['region']).strip('"')
name_data = results['location']['name']).strip('"')

print(f"The current weather in {name_data}, {region_data} is {current_weather_data}.")