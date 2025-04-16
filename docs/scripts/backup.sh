#!/bin/bash

DATE=$(date +%F)
BACKUP_DIR="/backups/telegram-movie-bot"

mkdir -p $BACKUP_DIR

echo "Повне резервне копіювання..."
tar -czf $BACKUP_DIR/project_$DATE.tar.gz ~/telegram-movie-bot

echo "Копіювання .env..."
cp ~/telegram-movie-bot/.env $BACKUP_DIR/.env_$DATE

echo "Копіювання логів..."
cp ~/telegram-movie-bot/bot.log $BACKUP_DIR/log_$DATE.log

echo "Завершено!"
