import requests
from config_reader import config
#import json


class WeatherException(Exception):
    """Исключение для ошибок апи погоды"""


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
        self.url = config.weather_url.replace('city', city)
        # self.weather_data = requests.get(url).json()
        #self.weather_data = json.dumps(weather_request, indent=2)
        #def __get_weather(self):

    def __http_get(url: str) -> dict:
        """Http запрос лучше делать в отдельном методе и возвращать ексепшн в случае ошибки"""
        data = requests.get(url).json()
        if data.status_code == 200:
            return data
        else:
            raise WeatherException

    
    def __temperature_info(self) -> tuple:
        """Всю информацию из ответа апи погоды лучше сделать в одном месте"""
        weather_data = self.__http_get(self.url)
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(self.weather_data['main']['feels_like'])
        if temperature > 0:
            temperature = f'+{temperature}'
        if temperature_feels > 0:
            temperature_feels = f'+{temperature}'
        return str(temperature), str(temperature_feels)

    # Нафиг его вообще
    # def __temperature_feels(self) -> str:
    #     temperature = round(self.weather_data['main']['feels_like'])
    #     if temperature > 0:
    #         return f'+{temperature}'
    #     else:
    #         return str(temperature)

        
    def answer(self) -> str:
        temperature, temperature_feels = self.__temperature_info()
        return  f"Температура <b>{temperature}</b>, \nОщущается как <b>{temperature_feels}</b>"