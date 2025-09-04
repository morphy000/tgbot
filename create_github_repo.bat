@echo off
echo ========================================
echo Создание GitHub репозитория для Telegram Bot
echo ========================================
echo.

echo Введите название репозитория (например: telegram-webinar-bot):
set /p repo_name=

echo Введите описание репозитория:
set /p repo_description=

echo Введите ваш GitHub username:
set /p github_username=

echo.
echo Создаем репозиторий на GitHub...
echo.

REM Создаем репозиторий через GitHub CLI (если установлен)
gh repo create %repo_name% --description "%repo_description%" --public --source=. --remote=origin --push

if %errorlevel% neq 0 (
    echo GitHub CLI не установлен или произошла ошибка.
    echo.
    echo Пожалуйста, создайте репозиторий вручную:
    echo 1. Перейдите на https://github.com/new
    echo 2. Название репозитория: %repo_name%
    echo 3. Описание: %repo_description%
    echo 4. Выберите Public или Private
    echo 5. НЕ ставьте галочки на README, .gitignore, license
    echo 6. Нажмите "Create repository"
    echo.
    echo После создания репозитория выполните:
    echo git remote add origin https://github.com/%github_username%/%repo_name%.git
    echo git branch -M main
    echo git push -u origin main
) else (
    echo Репозиторий успешно создан!
    echo URL: https://github.com/%github_username%/%repo_name%
)

echo.
echo Готово! Репозиторий создан и файлы загружены.
pause
