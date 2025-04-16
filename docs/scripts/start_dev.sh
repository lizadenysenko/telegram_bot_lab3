#!/bin/bash

echo "Запуск Telegram FilmInfo Bot у DEV-режимі..."

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "Залежності встановлено. Запускаємо бот..."
python bot.py
