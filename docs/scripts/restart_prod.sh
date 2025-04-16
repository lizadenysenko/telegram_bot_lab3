#!/bin/bash

echo "Перезапуск Telegram FilmInfo Bot..."
pkill -f bot.py
sleep 2
source ~/telegram-filminfo-bot/venv/bin/activate
nohup python ~/telegram-filminfo-bot/bot.py > bot.log 2>&1 &

echo "Перезапуск завершено"
