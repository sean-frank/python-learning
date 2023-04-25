import requests, json
ip_addr = requests.get('http://checkip.amazonaws.com/').text.strip('\n')
results = requests.get(f"http://ip-api.com/json/{ip_addr}").json()
lon = results['lon']
lat = results['lat']
api_finder_weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}").json()
found_api = requests.get(api_finder_weather['properties']['forecast']).json()
print(f"The current weather in your location {results['city']},{results['region']} is {found_api['properties']['periods'][0]['shortForecast'].lower()}.")