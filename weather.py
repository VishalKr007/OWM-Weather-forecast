import requests

def weather(city):
    print("Fetching weather data....\n")
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=697ef311d890e8881867fa67b8312407'
    data = requests.get(url)
    read_data = data.json()
    print('city name: {}'.format(read_data['name']))
    print('temperature: {}'.format(read_data['main']['temp']))
    print('pressure: {}'.format(read_data['main']['pressure']))
    print('humidity: {}'.format(read_data['main']['humidity']))
    print('min-temp: {}'.format(read_data['main']['temp_min']))
    print('max-temp: {}'.format(read_data['main']['temp_max']))
#    print('sunset: {}'.format(read_data['main']['sunset']))

def main():
    yourcity()


def yourcity():
    cityname = input('Please enter your city: ')
    print('your city name is: ', cityname)
    print("")
    print('Do you want to proceed (y/n)')
    x = input()
    if x=="y":
        weather(cityname)
    else:
        print('process terminated!!!')





if __name__=='__main__':
    main()
