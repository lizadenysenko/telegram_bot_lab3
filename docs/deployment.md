# Інструкція з розгортання Telegram FimInfo Bot у production

Цей документ містить покрокову інструкцію для DevOps або release-інженера з розгортання проєкту у виробничому середовищі.

---

## Вимоги до апаратного забезпечення

- **Архітектура:** x86_64
- **ОС:** Ubuntu 22.04 LTS або інша Linux-based система
- **CPU:** мінімум 1 vCPU (рекомендовано 2+)
- **RAM:** мінімум 512 MB (рекомендовано 1 GB)
- **Disk:** мінімум 1 GB вільного простору
- **Постійне з’єднання з інтернетом**

---

##  Необхідне програмне забезпечення

- Python 3.10+
- pip
- Git
- systemd (для автозапуску)
- (Опційно) Docker та Docker Compose

---

## Налаштування мережі

- Відкрити порт 443 або 80 (у разі використання webhook-режиму)
- Або забезпечити вихід в інтернет для polling-режиму
- Налаштувати firewall: дозволити `https`, `dns`, `outbound 443`

---

## Конфігурація серверів

1. Створіть окремого користувача:
```bash
sudo adduser telegrambot
```

2. Склонуйте репозиторій:
```bash
sudo -u telegrambot -i
git clone https://github.com/lizadenysenko/film_info_telegram_bot_2025
cd telegram-movie-bot
```

3. Створіть і активуйте віртуальне середовище:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Додайте .env з необхідними ключами.

---

## Розгортання коду

### Через systemd
1.Створіть юніт-файл `/etc/systemd/system/telegrambot.service`:
```ini
[Unit]
Description=Telegram FilmInfo Bot
After=network.target

[Service]
User=telegrambot
WorkingDirectory=/home/telegrambot/telegram-filminfo-bot
ExecStart=/home/telegrambot/telegram-filminfo-bot/venv/bin/python bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

2. Активуйте службу:
```bash
sudo systemctl daemon-reexec
sudo systemctl enable telegrambot
sudo systemctl start telegrambot
```

---

## Перевірка працездатності

- Перевірити логи:

```bash
journalctl -u telegrambot -f
```

- У Telegram: знайти вашого бота та надіслати команду `/start`
- Переконатись, що бот відповідає і знаходить фільми