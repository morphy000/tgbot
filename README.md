# Telegram Bot (Polling only)

Улучшенный стабильный Telegram-бот на pyTelegramBotAPI. Работает только в режиме long polling — идеально для постоянного запуска на виртуальной машине без публичного IP и HTTPS.

## ✨ Возможности
- Диалоговые воронки с кнопками (`ReplyKeyboardMarkup`)
- Markdown форматирование (жирный текст, эмодзи)
- Конфигурация через `.env` (без хардкода токена)
- Чистый polling: минимум зависимостей, максимум стабильности

## 📦 Установка

1) Клонируйте репозиторий или скопируйте файлы на ВМ
2) Установите Python 3.10+
3) Установите зависимости:
```bash
pip install -r requirements.txt
```
4) Создайте файл `.env` (на основе примера):
```bash
# Windows PowerShell
Copy-Item app.env.example .env
# Или используйте уже подготовленный файл
Copy-Item app.env.local .env
```
5) В файле `.env` укажите токен бота от BotFather:
```env
BOT_TOKEN=123456:AAA...
# Необязательно: переопределите ссылки
PURCHASE_LINK=https://example.com/purchase
HALF_WEBINAR_LINK_TEMPLATE=https://example.com/{webinar}-half
```

## ▶️ Запуск

```bash
python bot.py
```
После запуска в консоли появится лог:
```
[INFO] tgbot: Starting bot in polling mode...
```
Откройте Telegram и отправьте боту команду `/start`.

## ⚙️ Настройка контента
- Измените список вебинаров в `config.py` → `settings.webinars`
- Ссылки можно задать в `.env` или изменить значения по умолчанию в `config.py`

## 🔁 Автозапуск на ВМ

### Вариант A. Windows (Планировщик задач)
1. Откройте «Планировщик заданий» → «Создать задачу»
2. Вкладка «Триггеры» → «При входе в систему» (или «При запуске»)
3. Вкладка «Действия» → Добавить:
   - Программа/скрипт: `python`
   - Аргументы: `bot.py`
   - Рабочая папка: путь к проекту (например, `D:\tgbot`)
4. Вкладка «Параметры» → Разрешить запуск по требованию
5. Сохраните и протестируйте запуск вручную

### Вариант B. Linux (systemd, если будете переносить)
`/etc/systemd/system/tgbot.service`:
```ini
[Unit]
Description=Telegram Bot (Polling)
After=network.target

[Service]
WorkingDirectory=/opt/tgbot
ExecStart=/usr/bin/python3 bot.py
Restart=always
EnvironmentFile=/opt/tgbot/.env

[Install]
WantedBy=multi-user.target
```
Команды:
```bash
sudo systemctl daemon-reload
sudo systemctl enable tgbot
sudo systemctl start tgbot
sudo systemctl status tgbot
```

## 🧪 Тестирование
- Запустите `python bot.py`
- В Telegram отправьте `/start`
- Пройдите сценарии: «Хочу вебинар!», «Все еще сомневаюсь», «Остались сомнения»

## 🛠️ Троблшутинг
- Бот не отвечает:
  - Проверьте, что процесс `python bot.py` запущен
  - Проверьте токен в `.env`
  - Убедитесь, что интернет соединение есть на ВМ
- Ошибка про токен: убедитесь, что `.env` существует и содержит `BOT_TOKEN`
- Консоль «молчит»: добавьте временно уровень логирования DEBUG в `bot.py`

## 📁 Структура
```
.
├─ bot.py               # Основная логика бота (polling)
├─ config.py            # Конфигурация (Pydantic + .env)
├─ requirements.txt     # Зависимости
├─ app.env.example      # Пример .env
├─ app.env.local        # Локальный .env с токеном (не коммитить!)
└─ README.md            # Эта инструкция
```

## 📝 Заметки по безопасности
- Никогда не коммитьте реальный токен в публичный репозиторий
- Храните `.env` вне VCS или добавьте его в `.gitignore`

## 📣 Поддержка
Нужны автозапуск как сервис, логи в файл, ротация логов или интеграция с Supabase? Напишите — добавлю. 
