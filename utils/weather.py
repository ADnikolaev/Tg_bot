import requests
from config_reader import config
#import json




class Weather:
    
    @staticmethod
    def is_exists(city: str) -> bool:
        url = config.weather_url.replace('city', city)
        data = requests.get(url).json()
        if data['cod'] == 200:
            return True
        else:
            return False



    def __init__(self, city: str) -> None:
        url = config.weather_url.replace('city', city)
        self.weather_data = requests.get(url).json()
#       self.weather_data = json.dumps(weather_request, indent=2)
#    def __get_weather(self):

    
    def __temperature(self) -> str:
        temperature = round(self.weather_data['main']['temp'])
        if temperature > 0:
            return f'+{temperature}'
        else:
            return str(temperature)

    def __temperature_feels(self) -> str:
        temperature = round(self.weather_data['main']['feels_like'])
        if temperature > 0:
            return f'+{temperature}'
        else:
            return str(temperature)
        
    def answer(self) -> str:
        return  f"Температура <b>{self.__temperature()}</b>, \nОщущается как <b>{self.__temperature_feels()}</b>"