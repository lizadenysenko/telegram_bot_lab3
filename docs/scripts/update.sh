#!/bin/bash
echo "Оновлення коду та залежностей"
cd ~/telegram-movie-bot
git fetch --all
git reset --hard origin/main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart telegrambot
