from pydantic import BaseModel
from typing import List
import os

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
	bot_token: str
	purchase_link: str = "https://example.com/purchase"
	half_link_template: str = "https://example.com/{webinar}-half"
	webinars: List[str] = [
		"Энергопоток",
		"Денежный рост",
		"Пакет сверхмощных практик",
	]

	@classmethod
	def from_env(cls) -> "Settings":
		return cls(
			bot_token=os.getenv("BOT_TOKEN", ""),
			purchase_link=os.getenv("PURCHASE_LINK", "https://example.com/purchase"),
			half_link_template=os.getenv("HALF_WEBINAR_LINK_TEMPLATE", "https://example.com/{webinar}-half"),
		)


settings = Settings.from_env()

if not settings.bot_token:
	raise RuntimeError("BOT_TOKEN не задан. Установите переменную окружения или .env файл.")
