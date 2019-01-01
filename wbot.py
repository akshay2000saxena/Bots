import requests

city = input('City Name: ')

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=1fdfa3874cc07dedf321967cfd339def' 

json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['main']
print(formatted_data)