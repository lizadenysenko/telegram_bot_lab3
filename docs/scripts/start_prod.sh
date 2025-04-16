#!/bin/bash

echo "Запуск Telegram FilmInfo Bot у PRODUCTION..."

cd ~/telegram-movie-bot
source venv/bin/activate
nohup python bot.py > bot.log 2>&1 &

echo "Бот запущено у фоновому режимі"
