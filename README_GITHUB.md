# 🤖 Telegram Webinar Bot

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-4.14.0-red.svg)](https://github.com/eternnoir/pyTelegramBotAPI)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Telegram-бот для продажи вебинаров с использованием pyTelegramBotAPI и Flask webhook. Бот реализует полный сценарий продаж с приветственным сообщением, выбором вебинаров и предложением бесплатных пробных версий.

## ✨ Особенности

- 🎯 **Полный сценарий продаж** - от приветствия до покупки
- 🎁 **Бесплатные пробные версии** - для привлечения клиентов
- 🔄 **Webhook поддержка** - для стабильной работы
- 🎨 **Красивый интерфейс** - с кнопками и форматированием
- ⚙️ **Гибкая конфигурация** - легко настраиваемые вебинары и ссылки
- 🔒 **Безопасность** - поддержка переменных окружения

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/your-username/telegram-webinar-bot.git
cd telegram-webinar-bot
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка конфигурации
Отредактируйте `config.py` или создайте файл `.env`:
```python
BOT_TOKEN = "ваш_токен_бота"
WEBHOOK_URL = "https://ваш_ipv4_адрес/bot"
PURCHASE_LINK = "https://ваш_сайт.com/purchase"
```

### 4. Запуск бота
```bash
python main.py
```

## 📋 Сценарий работы бота

1. **`/start`** - Приветственное сообщение с описанием предложения
2. **"Хочу вебинар!"** - Выбор конкретного вебинара для покупки
3. **"Все еще сомневаюсь"** - Дополнительная информация для сомневающихся
4. **"Остались сомнения"** - Предложение бесплатной половины вебинара
5. **Выбор вебинара** - Отправка ссылки на покупку или бесплатную половину

## 🛠️ Структура проекта

```
telegram-webinar-bot/
├── main.py              # Основной файл бота
├── bot.py               # Альтернативная версия
├── bot_advanced.py      # Продвинутая версия с .env
├── config.py            # Конфигурация
├── requirements.txt    # Зависимости
├── README.md           # Документация
├── LICENSE             # Лицензия
├── .gitignore          # Git исключения
├── install.bat         # Установка для Windows
├── run.bat             # Запуск для Windows
└── env_example.txt     # Пример переменных окружения
```

## ⚙️ Конфигурация

### Настройка вебинаров
```python
WEBINARS = [
    "Энергопоток",
    "Денежный рост", 
    "Пакет сверхмощных практик"
]
```

### Настройка ссылок
```python
PURCHASE_LINK = "https://ваш_сайт.com/purchase"
HALF_WEBINAR_LINK_TEMPLATE = "https://ваш_сайт.com/{webinar}-half"
```

## 🌐 Настройка webhook

### Вариант A: ngrok (для тестирования)
```bash
ngrok http 80
```

### Вариант B: VPS сервер
1. Разверните сервер с публичным IP
2. Настройте домен (опционально)
3. Обновите WEBHOOK_URL в конфигурации

## 📝 Примеры использования

### Создание бота
1. Найдите @BotFather в Telegram
2. Отправьте `/newbot`
3. Следуйте инструкциям
4. Скопируйте токен в конфигурацию

### Запуск на Windows
```bash
install.bat  # Установка зависимостей
run.bat      # Запуск бота
```

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для подробностей.

## 🆘 Поддержка

Если у вас возникли проблемы:

1. Проверьте правильность токена бота
2. Убедитесь, что webhook URL доступен из интернета
3. Проверьте логи сервера
4. Убедитесь, что все зависимости установлены

## 📞 Контакты

- **Автор:** [Ваше имя]
- **Email:** [ваш@email.com]
- **Telegram:** [@ваш_username]

---

⭐ Если этот проект вам понравился, поставьте звездочку!
