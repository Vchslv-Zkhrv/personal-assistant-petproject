from typing import NoReturn as _NoReturn
import asyncio
from aiogram import Bot as _Bot, Dispatcher as _Dispatcher, types as _types
from aiogram.filters.command import Command as _Cmd

from config import TOKEN, CHAT_ID



_bot = _Bot(TOKEN)
_dp = _Dispatcher()


class BotStopped(Exception):
    pass


@_dp.message(lambda msg: msg.chat.id != CHAT_ID)
async def on_intruder(message: _types.Message):
    await _bot.delete_message(message.chat.id, message.message_id)


@_dp.message(_Cmd("start"))
async def on_start(message: _types.Message):
    await message.answer(str(message.chat.id))


def run() -> _NoReturn:
    asyncio.run(_dp.start_polling(_bot))
    raise BotStopped
