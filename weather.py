import requests

city = input('Enter your city name: ')
url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=697ef311d890e8881867fa67b8312407'
data = requests.get(url)
read = data.json()

print('city name: {}'.format(read['name']))
print('temperature: {}'.format(read['main']['temp']))
print('pressure: {}'.format(read['main']['pressure']))
print('humidity: {}'.format(read['main']['humidity']))
print('min-temp: {}'.format(read['main']['temp_min']))
print('max-temp: {}'.format(read['main']['temp_max']))
