import asyncio
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ChatAction

import app.keyboards as kb

router = Router()
    #НАЧАЛО 
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.reply('Я могу помочь тебе c выбором фильма на вечер', reply_markup=kb.films)

@router.message(F.text == "Детектив")
async def echo(message: Message):
    await message.reply("В основе сюжета жанра детектив лежит загадка. Обычно это преступление, но внимание читателя приковано, скорее, к загадочным обстоятельствам дела, нежели к самому преступлению. \nКульминация детектива — решение загадки; повествование привязано к логическому процессу, посредством которого расследователь по цепочке фактов приходит к раскрытию тайны.",
                        reply_markup=kb.langsDet)

    #ВЫБОР
@router.message(F.text == 'Ужасы')
async def echo(message: Message):
    await message.reply("Ужасы медленно и постепенно раскрывают и развивают сюжет через напряженность, колющие боли и атмосферу, держа зрителя в постоянном напряжении до конца фильма.",
                        reply_markup=kb.langsScar)
    
@router.message(F.text == 'Приключения')
async def echo(message: Message):
    await message.reply("Приключение — это захватывающее происшествие, неожиданное событие или случай в жизни, цепь нечаянных событий и непредвиденных случаев.",
                        reply_markup=kb.langsPC)
    
@router.message(F.text == 'Военные')
async def echo(message: Message):
    await message.reply("Военный фильм — это жанр, связанный с военными действиями, обычно о морских, воздушных или сухопутных сражениях, с боевыми сценами, занимающими центральное место в драме.",
                        reply_markup=kb.langsWar)
    
@router.message(F.text == 'Комедии')
async def echo(message: Message):
    await message.reply("Комедия — жанр художественного произведения, характеризующийся юмористическим или сатирическим подходом, и также вид драмы, в котором специфически разрешается момент действенного конфликта или борьбы.",
                        reply_markup=kb.langsComedy)
