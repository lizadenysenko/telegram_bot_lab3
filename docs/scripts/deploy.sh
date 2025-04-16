#!/bin/bash
echo "Розгортання Telegram Movie Bot"
cd ~/telegram-movie-bot
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart telegrambot
echo "Бот оновлено і перезапущено"
