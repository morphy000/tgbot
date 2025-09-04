@echo off
echo ========================================
echo Загрузка Telegram Bot на GitHub
echo ========================================
echo.

echo Введите ваш GitHub username:
set /p github_username=

echo Введите название репозитория (например: telegram-webinar-bot):
set /p repo_name=

echo.
echo Создаем репозиторий на GitHub...
echo.

echo Пожалуйста, выполните следующие шаги:
echo.
echo 1. Откройте браузер и перейдите на: https://github.com/new
echo 2. Заполните форму:
echo    - Repository name: %repo_name%
echo    - Description: Telegram bot for selling webinars with Flask webhook
echo    - Выберите Public или Private
echo    - НЕ ставьте галочки на README, .gitignore, license
echo 3. Нажмите "Create repository"
echo.
echo После создания репозитория нажмите любую клавишу для продолжения...
pause

echo.
echo Подключаем локальный репозиторий к GitHub...
git remote add origin https://github.com/%github_username%/%repo_name%.git

echo Переименовываем ветку в main...
git branch -M main

echo Отправляем код на GitHub...
git push -u origin main

echo.
echo ========================================
echo Готово! Репозиторий загружен на GitHub!
echo ========================================
echo.
echo URL вашего репозитория:
echo https://github.com/%github_username%/%repo_name%
echo.
pause
