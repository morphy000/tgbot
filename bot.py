import logging
import telebot
from telebot import types
from config import settings

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("tgbot")

bot = telebot.TeleBot(settings.bot_token, parse_mode="Markdown")

MAIN_BUTTONS = ["Хочу вебинар!", "Все еще сомневаюсь"]
BACK_BUTTON = "Назад"
FULL_ACCESS_BUTTON = "Хочу полный доступ"


def make_kb(labels: list[str]) -> types.ReplyKeyboardMarkup:
	kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
	for label in labels:
		kb.add(types.KeyboardButton(label))
	return kb


@bot.message_handler(commands=["start"])  # список строк
def start_handler(message: types.Message) -> None:
	kb = make_kb(MAIN_BUTTONS)
	text = (
		"🎉 **Привет! Мы знаем, зачем ты здесь!** 🎉\n\n"
		"🔥 **Что произошло?**\n"
		"Мы раздобыли эксклюзивный доступ к полным записям вебинаров Анны Тельновой по нумерологии! «Энергопоток», «Денежный рост», «Пакет сверхмощных практик» — и это только начало! Готов к мощным знаниям?\n\n"
		"💡 **Как это работает?**\n"
		"Мы не можем просто раздать платный контент направо и налево. Но у нас есть честная сделка:\n"
		"Ты делаешь символическое пожертвование всего **500 рублей** на поддержку нашего канала. А мы дарим тебе полную запись любого вебинара на твой выбор!\n\n"
		"🌟 **Что ты получишь?**\n"
		"✅ Тот же топовый контент от эксперта Анны Тельновой.\n"
		"✅ Полную видео- или аудиозапись в топовом качестве.\n"
		"✅ Экономию до **3000 рублей** с каждого вебинара!\n"
		"✅ Шанс наконец разобраться в своих цифрах и изменить жизнь к лучшему."
	)
	bot.send_message(message.chat.id, text, reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == "Хочу вебинар!")
def handle_want_webinar(message: types.Message) -> None:
	kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
	for w in settings.webinars:
		kb.add(types.KeyboardButton(w))
	kb.add(types.KeyboardButton(BACK_BUTTON))
	
	text = (
		f"Выбери свой вебинар:\n\n"
		f"📞 **Для получения доступа напишите:** {settings.fake_account}\n"
		f"Мы свяжемся с вами и предоставим доступ к выбранному вебинару."
	)
	bot.send_message(message.chat.id, text, reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == "Все еще сомневаюсь")
def handle_doubts(message: types.Message) -> None:
	kb = make_kb(["Хочу вебинар!", "Остались сомнения"])
	text = (
		"⚡ **Не переживай, всё по-честному!** ⚡\n\n"
		"Ты не покупаешь пиратку — ты жертвуешь на развитие наших проектов и получаешь ценный подарок. Всё легально и прозрачно!\n\n"
		"Это лучшая инвестиция в себя за **500 рублей вместо 3500**. Давай, решайся!"
	)
	bot.send_message(message.chat.id, text, reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == "Остались сомнения")
def handle_still_doubts(message: types.Message) -> None:
	kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
	for w in settings.webinars:
		kb.add(types.KeyboardButton(f"{w} (половина бесплатно)"))
	kb.add(types.KeyboardButton(BACK_BUTTON))
	text = (
		"🎁 **Супер-фишка для самых упорных!** 🎁\n\n"
		"Получите половину вебинара **БЕСПЛАТНО** на выбор и убедитесь в качестве."
	)
	bot.send_message(message.chat.id, text, reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == BACK_BUTTON)
def handle_back(message: types.Message) -> None:
	kb = make_kb(MAIN_BUTTONS)
	bot.send_message(message.chat.id, "Выберите действие:", reply_markup=kb)


@bot.message_handler(func=lambda m: any(w == m.text for w in settings.webinars))
def handle_full_webinar_choice(message: types.Message) -> None:
	webinar = message.text
	link = settings.webinar_links.get(webinar, "https://example.com/not-found")
	
	text = (
		f"🎉 **Отлично! Вы выбрали вебинар: {webinar}**\n\n"
		f"📱 **Ссылка на канал:** {link}\n\n"
		f"📞 **Для активации доступа напишите:** {settings.fake_account}\n"
		f"Мы предоставим вам полный доступ к выбранному вебинару."
	)
	
	kb = make_kb([FULL_ACCESS_BUTTON, BACK_BUTTON])
	bot.send_message(message.chat.id, text)
	bot.send_message(message.chat.id, "Хотите полный доступ?", reply_markup=kb)


@bot.message_handler(func=lambda m: any((w in m.text and "половина бесплатно" in m.text) for w in settings.webinars))
def handle_half_choice(message: types.Message) -> None:
	webinar = next((w for w in settings.webinars if w in message.text), None)
	if webinar:
		link = settings.webinar_links.get(webinar, "https://example.com/not-found")
		text = (
			f"🎁 **Пробный доступ к вебинару: {webinar}**\n\n"
			f"📱 **Ссылка на канал:** {link}\n\n"
			f"📞 **Для полного доступа напишите:** {settings.fake_account}\n"
			f"Мы предоставим вам полную версию вебинара."
		)
		bot.send_message(message.chat.id, text)
		kb = make_kb([FULL_ACCESS_BUTTON, BACK_BUTTON])
		bot.send_message(message.chat.id, "Хотите полный доступ?", reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == FULL_ACCESS_BUTTON)
def handle_full_access(message: types.Message) -> None:
	kb = make_kb(MAIN_BUTTONS)
	text = (
		f"💎 **Полный доступ к вебинарам**\n\n"
		f"📞 **Для получения полного доступа напишите:** {settings.fake_account}\n"
		f"Мы предоставим вам доступ ко всем вебинарам Анны Тельновой.\n\n"
		f"💰 **Стоимость:** 500 рублей (экономия до 3000 рублей!)"
	)
	bot.send_message(message.chat.id, text)
	bot.send_message(message.chat.id, "Выберите действие:", reply_markup=kb)


def main() -> None:
	logger.info("Starting bot in polling mode...")
	bot.remove_webhook()
	bot.infinity_polling(timeout=60, long_polling_timeout=30)


if __name__ == "__main__":
	main()
