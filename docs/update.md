# Інструкція з оновлення Telegram FilmInfo Bot

Цей документ описує кроки для безпечного оновлення Telegram-бота у production-середовищі, включаючи відкат у разі невдалого розгортання.

---

## 1. Підготовка до оновлення

### 1.1 Створення резервних копій

Перед будь-яким оновленням створіть резервні копії:

```bash
# Бекап каталогу проєкту
tar -czf ~/backup/telegram-movie-bot_$(date +%F).tar.gz ~/telegram-movie-bot

# Бекап віртуального середовища (опціонально)
tar -czf ~/backup/venv_backup_$(date +%F).tar.gz ~/telegram-movie-bot/venv
```

### 1.2 Перевірка сумісності

- Ознайомтесь із changelog (якщо є)
- Переконайтесь, що версія Python сумісна
- Перевірте залежності (`requirements.txt`) — оновлювати краще у віртуальному середовищі тестового сервера

### 1.3 Планування часу простою (якщо потрібно)

- У polling-режимі просто зупиняється бот (1-2 хв).
- Якщо бот критичний — повідомте відповідальних.

---

## 2. Процес оновлення

### 2.1 Зупинка служби

```bash
sudo systemctl stop telegrambot
```

### 2.2 Розгортання нового коду

```bash
cd ~/telegram-movie-bot
git pull origin main
```

### 2.3 Оновлення конфігурацій

- Оновіть `.env`, якщо були додані нові змінні
- Перевірте `requirements.txt`:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

---

## 3. Перевірка після оновлення

### 3.1 Запуск служби

```bash
sudo systemctl start telegrambot
```

### 3.2 Перевірка працездатності

- Використовуйте `/start` і `/find` для перевірки
- Перегляньте логи:

```bash
journalctl -u telegrambot -f
```

---

## 4. Відкат (Rollback)

У разі проблем з оновленням:

### Кроки:

1. Зупиніть бота:

```bash
sudo systemctl stop telegrambot
```

2. Відновіть бекап:

```bash
rm -rf ~/telegram-movie-bot
tar -xzf ~/backup/telegram-movie-bot_дата.tar.gz -C ~
```

3. (Опційно) Відновіть стару версію віртуального середовища:

```bash
rm -rf ~/telegram-movie-bot/venv
tar -xzf ~/backup/venv_backup_дата.tar.gz -C ~/telegram-movie-bot
```

4. Перезапустіть:

```bash
sudo systemctl start telegrambot
```

