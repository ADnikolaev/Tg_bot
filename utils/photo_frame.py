from PIL import ImageOps, Image, ImageFilter
from config_reader import config
import requests
import io
import os
from faker import Faker


class Frame:


    def __init__(self, img_id) -> None:
        self.img_id = img_id
        self.img_name = Faker("ru_RU").postcode() # Нет смысла объявлять фейкер за пределами класса

    def __get_image(self) -> bytes:
        # resp = requests.get(config.uri_info.replace('BOT_TOKEN', config.bot_token.get_secret_value()) + self.img_id)
        # img_path = resp.json()['result']['file_path']
        # self.img = requests.get(config.uri.replace('BOT_TOKEN', config.bot_token.get_secret_value()) + img_path)
        # self.img = Image.open(io.BytesIO(self.img.content))
        """
        Вот здесь лучше просто сделать http запрос. Без открытия в PIL.
        Так будет соблюден принцип единой ответственности
        self.img ну и делать атрибутом класса как будто бы лишнее. Лучше просто вернуть результат
        """
        resp = requests.get(config.uri_info.replace('BOT_TOKEN', config.bot_token.get_secret_value()) + self.img_id)
        img_path = resp.json()['result']['file_path']
        img = requests.get(config.uri.replace('BOT_TOKEN', config.bot_token.get_secret_value()) + img_path)
        return img.content

    def __img_save(self, img) -> str:
        # if not os.path.exists('photos'):
        #     os.mkdir('photos')
        # img.save(f'photos/{self.img_name}.png', format="PNG")
        """
        Будет лучше если все опереции которые ты делаешь через PIL будут в одном методе
        Так же лучше явно возвращать путь к файлу,
        чтобы в месте где ты вызываешь метод не пришлось его опять генерировать
        Избежишь места с потенциальными ошибками и трудностями в понимании
        """
        img = Image.open(io.BytesIO(img))
        img = ImageOps.expand(img, border=25, fill='#ff0000cc')
        os.makedirs("photos", exist_ok=True)
        img_path = f'photos/{self.img_name}.png'
        img.save(img_path, format="PNG")
        return img_path

    def frame(self) -> str:
        img = self.__get_image()
        img_path = self.__img_save(img)
        return img_path


