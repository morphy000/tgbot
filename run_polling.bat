@echo off
setlocal enabledelayedexpansion

if not exist .env (
	if exist app.env.example copy app.env.example .env >nul
)

echo Installing deps...
pip install -r requirements.txt >nul

echo Starting bot in polling mode...
python bot.py
