import requests

api_address = 'https://openweathermap.org/data/2.5/weather?appid=1fdfa3874cc07dedf321967cfd339def&q='
city = input('City Name: ')

url = api_address + city

json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['main']
print(formatted_data)