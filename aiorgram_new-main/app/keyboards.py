from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


films = ReplyKeyboardMarkup(keyboard= [
    [KeyboardButton(text ='Детектив')],
    [KeyboardButton(text ='Ужасы')],
    [KeyboardButton(text ='Приключения')],
    [KeyboardButton(text ='Военные')],
    [KeyboardButton(text= 'Комедии')],
    [KeyboardButton(text= 'Свяжитесь со мной', request_contact=True)],
], resize_keyboard=True,
input_field_placeholder="Выберите пункт меню"
)


langsDet = InlineKeyboardMarkup(inline_keyboard= [ #Детектив
    [InlineKeyboardButton(text ='Новинки', url = 'https://www.kinopoisk.ru/lists/movies/genre--mystery/?sort=date')],
    [InlineKeyboardButton(text ='Популярное', url = 'https://www.kinopoisk.ru/lists/movies/genre--mystery/?b=top')],
    [InlineKeyboardButton(text='Зарубежные', url = 'https://www.kinopoisk.ru/lists/movies/genre--mystery/?b=foreign')],
])
#
langsScar = InlineKeyboardMarkup(inline_keyboard= [ #ужасы
    [InlineKeyboardButton(text ='Новинки', url = 'https://www.kinopoisk.ru/lists/movies/genre--horror/?b=released&sort=date')],
    [InlineKeyboardButton(text ='Популярное', url = 'https://www.kinopoisk.ru/lists/movies/genre--horror/?sort=date&b=released&b=top')],
    [InlineKeyboardButton(text='Зарубежные', url = 'https://www.kinopoisk.ru/lists/movies/genre--horror/?sort=date&b=released&b=foreign')],
])
  
langsPC = InlineKeyboardMarkup(inline_keyboard= [ #Приключения
    [InlineKeyboardButton(text ='Новинки', url = 'https://www.kinopoisk.ru/lists/movies/genre--adventure/?sort=date&b=released')],
    [InlineKeyboardButton(text ='Популярное', url = 'https://www.kinopoisk.ru/lists/movies/genre--adventure/?sort=date&b=released&b=top')],
    [InlineKeyboardButton(text='Зарубежные', url = 'https://www.kinopoisk.ru/lists/movies/genre--adventure/?sort=date&b=released&b=foreign')],
])

langsWar = InlineKeyboardMarkup(inline_keyboard= [ #военные
    [InlineKeyboardButton(text ='Новинки', url = 'https://www.kinopoisk.ru/lists/movies/genre--war/?sort=date&b=released')],
    [InlineKeyboardButton(text ='Популярное', url = 'https://www.kinopoisk.ru/lists/movies/genre--war/?b=released&b=top')],
    [InlineKeyboardButton(text='Зарубежные', url = 'https://www.kinopoisk.ru/lists/movies/genre--war/?b=released&b=foreign')],
])

langsComedy = InlineKeyboardMarkup(inline_keyboard= [ #Комедии
    [InlineKeyboardButton(text ='Новинки', url = 'https://www.kinopoisk.ru/lists/movies/genre--comedy/?b=released&sort=date')],
    [InlineKeyboardButton(text ='Популярное', url = 'https://www.kinopoisk.ru/lists/movies/genre--comedy/?b=released&b=top')],
    [InlineKeyboardButton(text='Зарубежные', url = 'https://www.kinopoisk.ru/lists/movies/genre--comedy/?b=released&b=foreign')],
])