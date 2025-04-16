# 🎬 FilmInfo Bot — Telegram Movie Search Bot

**FilmInfo Bot** is a Telegram bot that allows users to search for movies by title, genre, 
or keyword using the [OMDb API](http://www.omdbapi.com/).  
The bot supports both **Ukrainian 🇺🇦** and **English 🇬🇧** languages.

---

## Features

- Search movies by:
  - Title (`/find`)
  - Genre (`/genre`)
  - Keyword (`/search`)
- Display information including:
  - Title, Year, Genre
  - Director, Actors
  - IMDb rating, Plot
  - Poster image
  - YouTube trailer link
- Language switching between 🇬🇧 and 🇺🇦

---

## Technologies

- Python 3.x
- `telebot` (pyTelegramBotAPI) library
- OMDb API (The Open Movie Database)

---

## Installation & Running the Bot

1. **Clone the Repository**
    ```bash
    git clone https://github.com/lizadenysenko/film_info_telegram_bot_2025.git
    cd movie-bot


2. **Install Dependencies**
    (Recommended) Create a virtual environment:
    python -m venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    
    Install Python packages:
    pip install -r requirements.txt


3. **Configure Environment Variables**
    Create a .env file based on the example:
    cp .env.example .env
    
    Fill in your API keys inside .env:
    API_TOKEN=your_telegram_bot_token
    OMDB_API_KEY=your_omdb_api_key


4. **Start the Bot**
    python bot.py


## Available Bot Commands
    Command	Description
    /start	Welcome message with help button
    /help	Instructions and command list
    /find <title>	Find a specific movie by title
    /search <keyword>	Search movies by keyword
    /genre <genre>	Search movies by genre
    /lang_en	Switch language to English
    /lang_uk	Switch language to Ukrainian


## Project Structure
    movie-bot/
    ├── bot.py             # Main bot script
    ├── .env.example       # Example for environment variables
    ├── .gitignore         # Git ignored files
    ├── requirements.txt   # Python dependencies
    ├── LICENSE            # MIT License
    └── README.md          # Project documentation

## Security Notice
    Keep all API tokens and secrets in the .env file.
    The .env file is listed in .gitignore to prevent sensitive data from being uploaded to public repositories.
    Never share your API keys publicly.

## License
    This project is licensed under the MIT License.

## Author
    Developer: Liza Denysenko
    GitHub: lizadenysenko
    Telegram: @lvanilka