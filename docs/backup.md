# Інструкція з резервного копіювання Telegram FilmInfo Bot

Цей документ описує процедури резервного копіювання та відновлення проєкту для release engineer / DevOps спеціалістів.

---

## 1. Стратегія резервного копіювання

### 1.1 Типи резервних копій

- **Повне (full):** Бекап всього каталогу проєкту + середовище.
- **Інкрементальне:** Зберігаються лише зміни з моменту останнього бекапу (можна реалізувати rsync/rsnapshot).
- **Диференціальне:** Між двома точками full-бекапу (не обов’язково для даного проєкту).

### 1.2 Частота

- **Повний бекап**: 1 раз на тиждень (наприклад, у неділю о 03:00)
- **Інкрементальний**: щодня о 03:00 (rsync)

### 1.3 Зберігання та ротація

- Місце: `/backups/telegram-movie-bot/`
- Ротація: зберігати 7 інкрементальних і 4 повні копії (1 міс.)

---

## 2. Процедура резервного копіювання

### 2.1 Бекап файлів проєкту

```bash
tar -czf /backups/telegram-movie-bot/project_$(date +%F).tar.gz ~/telegram-movie-bot
```

### 2.2 Бекап конфігурацій

```bash
cp ~/telegram-movie-bot/.env /backups/telegram-movie-bot/.env_$(date +%F)
```

### 2.3 Логи

```bash
cp ~/telegram-movie-bot/bot.log /backups/telegram-movie-bot/log_$(date +%F).log
```

---

## 3. Перевірка цілісності резервних копій

```bash
tar -tzf /backups/telegram-movie-bot/project_$(date +%F).tar.gz > /dev/null
if [ $? -eq 0 ]; then echo "✅ Архів цілий"; else echo "❌ Помилка архіву"; fi
```

---

## 4. Автоматизація резервного копіювання

`backup.sh` (в `docs/scripts/backup.sh`)

```bash
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
```

Додати у `cron`:

```bash
crontab -e
# Щоденний запуск о 03:00
0 3 * * * /home/telegrambot/telegram-movie-bot/docs/scripts/backup.sh
```

---

## 5. Процедура відновлення з резервних копій

### 5.1 Повне відновлення

```bash
tar -xzf /backups/telegram-movie-bot/project_дата.tar.gz -C ~
cp /backups/telegram-movie-bot/.env_дата ~/telegram-movie-bot/.env
cp /backups/telegram-movie-bot/log_дата.log ~/telegram-movie-bot/bot.log
```

### 5.2 Вибіркове відновлення

Наприклад, лише `.env`:

```bash
cp /backups/telegram-movie-bot/.env_дата ~/telegram-movie-bot/.env
```

### 5.3 Тестування

Після відновлення:

```bash
sudo systemctl restart telegrambot
journalctl -u telegrambot -f
```

Надішліть боту `/start` і перевірте відповідь.




