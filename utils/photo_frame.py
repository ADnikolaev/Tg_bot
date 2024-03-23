from PIL import ImageOps, Image, ImageFilter
from config_reader import config
import requests
import io
import os
from faker import Faker

fake = Faker("ru_RU")

class Frame:


    def __init__(self, img_id) -> None:
        self.img_id = img_id
        self.img_name = fake.postcode()

    def __get_image(self) -> None:
        resp = requests.get(config.uri_info.replace('BOT_TOKEN', config.bot_token.get_secret_value()) + self.img_id)
        img_path = resp.json()['result']['file_path']
        self.img = requests.get(config.uri.replace('BOT_TOKEN', config.bot_token.get_secret_value()) + img_path)
        self.img = Image.open(io.BytesIO(self.img.content))

    def __img_save(self, img) -> None:
        if not os.path.exists('photos'):
            os.mkdir('photos')
        img.save(f'photos/{self.img_name}.png', format="PNG")

    def frame(self) -> None:
        self.__get_image()
        img = ImageOps.expand(self.img, border=25, fill='#ff0000cc')
        self.__img_save(img)


