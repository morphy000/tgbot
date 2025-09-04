@echo off
echo Запуск Telegram бота...
echo.

echo Проверяем наличие config.py...
if not exist config.py (
    echo ОШИБКА: Файл config.py не найден!
    echo Создайте файл config.py с настройками бота
    pause
    exit /b 1
)

echo Проверяем наличие main.py...
if not exist main.py (
    echo ОШИБКА: Файл main.py не найден!
    pause
    exit /b 1
)

echo Запускаем бота...
python main.py

pause
