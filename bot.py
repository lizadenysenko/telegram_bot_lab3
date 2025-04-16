"""Telegram-бот для пошуку фільмів за назвою, жанром чи ключовим словом"""

import os
from typing import Dict
from urllib.parse import quote
import requests
import telebot
from telebot import types
from telebot.types import Message, ReplyKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

API_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN')
OMDB_API_KEY: str = os.getenv('OMDB_API_KEY')

bot = telebot.TeleBot(API_TOKEN)
user_languages: Dict[int, str] = {}

def get_user_first_name(message: Message) -> str:
    """Повертає ім’я користувача або 'друг', якщо воно відсутнє."""
    return message.from_user.first_name if message.from_user.first_name else "друг"

def start_keyboard() -> ReplyKeyboardMarkup:
    """Створює клавіатуру з кнопкою /help."""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    help_button = types.KeyboardButton('/help')
    keyboard.add(help_button)
    return keyboard

def language_keyboard() -> ReplyKeyboardMarkup:
    """Створює клавіатуру для вибору мови."""
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    english_button = types.KeyboardButton('/lang_en')
    ukrainian_button = types.KeyboardButton('/lang_uk')
    keyboard.add(english_button, ukrainian_button)
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message: Message) -> None:
    """Обробляє команду /start."""
    user_name = get_user_first_name(message)
    user_languages.setdefault(message.from_user.id, 'uk')
    keyboard = start_keyboard()
    bot.reply_to(message, f"Привіт, {user_name}!\n"
                          f"Використовуйте кнопку нижче для отримання допомоги.", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_help(message: Message) -> None:
    """Обробляє команду /help."""
    language = user_languages.get(message.from_user.id, 'uk')
    if language == 'uk':
        help_text = (
            "Доступні команди:\n"
            "/start - Привітання і основні інструкції\n"
            "/find <назва фільму> - Знайти фільм за назвою\n"
            "/search <ключове слово> - Знайти фільми за ключовими словами\n"
            "/genre <жанр> - Знайти фільми за жанром\n"
            "/lang_en - Вибрати англійську мову"
        )
    else:
        help_text = (
            "Available commands:\n"
            "/start - Greeting and basic instructions\n"
            "/find <movie title> - Find a movie by title\n"
            "/search <keyword> - Find movies by keyword\n"
            "/genre <genre> - Find movies by genre\n"
            "/lang_uk - Switch to Ukrainian language"
        )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['find'])
def find_movie(message: Message) -> None:
    """Знаходить фільм за назвою."""
    user_name = get_user_first_name(message)
    language = user_languages.get(message.from_user.id, 'uk')
    try:
        search_query = message.text.split(' ', 1)[1]
    except IndexError:
        msg = (f"Будь ласка, {user_name}, надайте назву фільму після команди /find."
               if language == 'uk' else
               f"Please provide the movie title after the /find command, {user_name}.")
        bot.reply_to(message, msg)
        return

    encoded_query = quote(search_query)
    url = f'http://www.omdbapi.com/?t={encoded_query}&apikey={OMDB_API_KEY}'
    response = requests.get(url, timeout=5)
    data = response.json()

    if data.get('Response') == 'True':
        title = data.get('Title')
        year = data.get('Year')
        rating = data.get('imdbRating')
        director = data.get('Director')
        actors = data.get('Actors')
        genre = data.get('Genre')
        overview = data.get('Plot')
        poster = data.get('Poster')
        trailer_url = f"https://www.youtube.com/results?search_query={title}+trailer"

        response_message = (
            f"🎬 Назва: {title}\n"
            f"📅 Рік: {year}\n"
            f"⭐ Рейтинг IMDb: {rating}\n"
            f"🎥 Режисер: {director}\n"
            f"🎭 Актори: {actors}\n"
            f"📚 Жанр: {genre}\n"
            f"📝 Опис: {overview}\n"
            f"▶️ Трейлер на YouTube: {trailer_url}"
        )
        if poster != 'N/A':
            bot.send_photo(message.chat.id, poster, caption=response_message)
        else:
            bot.reply_to(message, response_message)
    else:
        bot.reply_to(message, f"Фільм не знайдено, {user_name}."
                     if language == 'uk' else f"Movie not found, {user_name}.")

@bot.message_handler(commands=['lang_en'])
def set_language_english(message: Message) -> None:
    """Встановлює англійську мову."""
    user_languages[message.from_user.id] = 'en'
    bot.reply_to(message, "Language set to English.")

@bot.message_handler(commands=['lang_uk'])
def set_language_ukrainian(message: Message) -> None:
    """Встановлює українську мову."""
    user_languages[message.from_user.id] = 'uk'
    bot.reply_to(message, "Мову змінено на українську.")

if __name__ == '__main__':
    bot.polling(none_stop=True)