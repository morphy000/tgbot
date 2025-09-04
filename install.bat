@echo off
echo Установка зависимостей для Telegram бота...
echo.

echo Устанавливаем pyTelegramBotAPI...
pip install pyTelegramBotAPI==4.14.0

echo Устанавливаем Flask...
pip install Flask==3.0.0

echo Устанавливаем requests...
pip install requests==2.31.0

echo.
echo Все зависимости установлены!
echo.
echo Следующие шаги:
echo 1. Отредактируйте config.py с вашими настройками
echo 2. Получите токен бота у @BotFather
echo 3. Настройте webhook URL
echo 4. Запустите бота командой: python main.py
echo.
pause
