from pydantic import BaseModel
from typing import List
import os

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
	bot_token: str
	fake_account: str = "@cuute_kira"
	webinar_links: dict = {
		"Денежный рост": "https://t.me/+mnY-SrO2MuUzNDc6",
		"СНОВИДЕНИЯ ч.1": "https://t.me/+HUUzs1zzXp9iMzJi", 
		"ПАКЕТ СВЕРХМОЩНЫХ ПРАКТИК": "https://t.me/+gxnBxZ-A3rE0MGYy",
		"Энергопоток": "https://example.com/energopotok"  # placeholder
	}
	webinars: List[str] = [
		"Энергопоток",
		"Денежный рост",
		"СНОВИДЕНИЯ ч.1",
		"ПАКЕТ СВЕРХМОЩНЫХ ПРАКТИК",
	]

	@classmethod
	def from_env(cls) -> "Settings":
		return cls(
			bot_token=os.getenv("BOT_TOKEN", ""),
			fake_account=os.getenv("FAKE_ACCOUNT", "@cuute_kira"),
		)


settings = Settings.from_env()

if not settings.bot_token:
	raise RuntimeError("BOT_TOKEN не задан. Установите переменную окружения или .env файл.")
