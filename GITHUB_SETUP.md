# 📚 Инструкция по созданию GitHub репозитория

## 🚀 Быстрый способ (с GitHub CLI)

Если у вас установлен GitHub CLI:

1. **Установите GitHub CLI** (если не установлен):
   ```bash
   # Windows (через winget)
   winget install GitHub.cli
   
   # Или скачайте с https://cli.github.com/
   ```

2. **Авторизуйтесь в GitHub**:
   ```bash
   gh auth login
   ```

3. **Запустите скрипт**:
   ```bash
   create_github_repo.bat
   ```

## 🔧 Ручной способ

### Шаг 1: Создание репозитория на GitHub

1. Перейдите на [GitHub](https://github.com/new)
2. Заполните форму:
   - **Repository name**: `telegram-webinar-bot` (или другое название)
   - **Description**: `Telegram bot for selling webinars with Flask webhook`
   - **Visibility**: Public или Private (по вашему выбору)
   - **НЕ ставьте галочки** на README, .gitignore, license (у нас уже есть эти файлы)
3. Нажмите "Create repository"

### Шаг 2: Подключение к удаленному репозиторию

```bash
# Добавляем удаленный репозиторий
git remote add origin https://github.com/YOUR_USERNAME/telegram-webinar-bot.git

# Переименовываем ветку в main (современный стандарт)
git branch -M main

# Отправляем код на GitHub
git push -u origin main
```

### Шаг 3: Настройка репозитория

После создания репозитория:

1. **Переименуйте README_GITHUB.md в README.md**:
   ```bash
   git mv README_GITHUB.md README.md
   git commit -m "Update README for GitHub"
   git push
   ```

2. **Добавьте теги и релизы** (опционально):
   ```bash
   git tag -a v1.0.0 -m "First release"
   git push origin v1.0.0
   ```

## 📋 Структура файлов в репозитории

```
telegram-webinar-bot/
├── 📄 README.md              # Основная документация
├── 🤖 main.py                # Основной файл бота
├── 🔧 config.py              # Конфигурация
├── 📦 requirements.txt       # Зависимости
├── 📜 LICENSE                # Лицензия MIT
├── 🚫 .gitignore             # Git исключения
├── 🎯 bot.py                 # Альтернативная версия
├── ⚡ bot_advanced.py         # Продвинутая версия
├── 🛠️ install.bat            # Установка для Windows
├── ▶️ run.bat                # Запуск для Windows
├── 📝 env_example.txt        # Пример переменных окружения
└── 📚 README_GITHUB.md       # GitHub README (временно)
```

## 🎯 Рекомендуемые настройки репозитория

### Topics (теги)
Добавьте следующие теги в настройках репозитория:
- `telegram-bot`
- `python`
- `flask`
- `webhook`
- `webinar-sales`
- `pytelegrambotapi`

### Описание
```
Telegram bot for selling webinars with Flask webhook. Features: sales funnel, free trials, customizable webinars, secure configuration.
```

## 🔗 Полезные ссылки

- [GitHub CLI документация](https://cli.github.com/)
- [Git команды](https://git-scm.com/docs)
- [GitHub Pages](https://pages.github.com/) (для документации)

## 📝 Следующие шаги

После создания репозитория:

1. **Настройте GitHub Pages** (опционально):
   - Settings → Pages → Source: Deploy from a branch
   - Branch: main, folder: / (root)

2. **Добавьте Issues и Projects**:
   - Создайте шаблоны для issues
   - Настройте проекты для отслеживания задач

3. **Настройте Actions** (опционально):
   - Автоматические тесты
   - Автоматическое развертывание

4. **Добавьте Contributors**:
   - Пригласите соавторов в репозиторий

## 🎉 Готово!

Ваш Telegram Webinar Bot теперь доступен на GitHub! 🚀
