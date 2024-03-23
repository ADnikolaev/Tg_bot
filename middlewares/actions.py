from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery

from utils.logger import logger

from utils.weather import Weather


class SaveMessageInLogMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        """Сохранение сообщений пользователя и бота в лог"""
        logger.info(f'Сообщение от пользователя: {event.from_user.username}/{event.from_user.id}')
        if True:
            logger.info(f'{event.from_user.username}/BOT: {event.html_text}')
            await handler(event, data)
            logger.info(f'BOT/{event.from_user.username}: response 200')
        else:
            return await handler(event, data)

class IsItCityMiddleware(BaseMiddleware):
    """
    я считаю что это лишнее. Ты делаешь два запроса для одного и того же действия
    Вместо мидлвари лучше обрабатывай эксепшн WeatherException, который я дописал
    """

    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        if Weather.is_exists(f'{event.html_text}'):
            await handler(event, data)
        else:
            return await handler(event, data)
