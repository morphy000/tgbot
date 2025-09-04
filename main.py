from flask import Flask, request
import telebot
from telebot import types
import os
from config import BOT_TOKEN, WEBHOOK_URL, WEBINARS, PURCHASE_LINK, HALF_WEBINAR_LINK_TEMPLATE

app = Flask(__name__)

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# Функция /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(types.KeyboardButton("Хочу вебинар!"))
    markup.add(types.KeyboardButton("Все еще сомневаюсь"))
    
    welcome_text = """🎉 **Привет! Мы знаем, зачем ты здесь!** 🎉

🔥 **Что произошло?**
Мы раздобыли эксклюзивный доступ к полным записям вебинаров Анны Тельновой по нумерологии! «Энергопоток», «Денежный рост», «Пакет сверхмощных практик» — и это только начало! Готов к мощным знаниям?

💡 **Как это работает?**
Мы не можем просто раздать платный контент направо и налево. Но у нас есть честная сделка:
Ты делаешь символическое пожертвование всего **500 рублей** на поддержку нашего канала (чтобы мы продолжали находить для тебя крутые штуки). А мы дарим тебе полную запись любого вебинара на твой выбор!

🌟 **Что ты получишь?**
✅ Тот же топовый контент от эксперта Анны Тельновой.
✅ Полную видео- или аудиозапись в топовом качестве.
✅ Экономию до **3000 рублей** с каждого вебинара!
✅ Шанс наконец разобраться в своих цифрах и изменить жизнь к лучшему."""
    
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)

# Обработка "Хочу вебинар!"
@bot.message_handler(lambda message: message.text == "Хочу вебинар!")
def send_webinar_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    
    # Добавляем кнопки для каждого вебинара
    for webinar in WEBINARS:
        markup.add(types.KeyboardButton(webinar))
    
    markup.add(types.KeyboardButton("Назад"))
    
    bot.send_message(message.chat.id, "Выбери свой вебинар:", reply_markup=markup)

# Обработка "Все еще сомневаюсь"
@bot.message_handler(lambda message: message.text == "Все еще сомневаюсь")
def send_doubts(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(types.KeyboardButton("Хочу вебинар!"))
    markup.add(types.KeyboardButton("Остались сомнения"))
    
    doubts_text = """⚡ **Не переживай, всё по-честному!** ⚡

Ты не покупаешь пиратку — ты жертвуешь на развитие наших проектов и получаешь ценный подарок в благодарность. Всё легально и прозрачно!

Это лучшая инвестиция в себя за **500 рублей вместо 3500**. Давай, решайся!"""
    
    bot.send_message(message.chat.id, doubts_text, parse_mode="Markdown", reply_markup=markup)

# Обработка "Остались сомнения"
@bot.message_handler(lambda message: message.text == "Остались сомнения")
def send_free_half(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    
    # Добавляем кнопки для бесплатной половины каждого вебинара
    for webinar in WEBINARS:
        markup.add(types.KeyboardButton(f"{webinar} (половина бесплатно)"))
    
    markup.add(types.KeyboardButton("Назад"))
    
    free_half_text = """🎁 **Супер-фишка для самых упорных!** 🎁

Для тех, кто всё ещё думает, — получи половину вебинара **БЕСПЛАТНО** на выбор! Выбери один из трёх и убедись в качестве сам."""
    
    bot.send_message(message.chat.id, free_half_text, parse_mode="Markdown", reply_markup=markup)

# Обработка "Назад"
@bot.message_handler(lambda message: message.text == "Назад")
def go_back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(types.KeyboardButton("Хочу вебинар!"))
    markup.add(types.KeyboardButton("Все еще сомневаюсь"))
    
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработка выбора бесплатной половины вебинара
@bot.message_handler(lambda message: any(webinar in message.text and "половина бесплатно" in message.text for webinar in WEBINARS))
def send_free_half_link(message):
    # Извлекаем название вебинара из текста
    webinar = None
    for w in WEBINARS:
        if w in message.text:
            webinar = w
            break
    
    if webinar:
        # Формируем ссылку на половину вебинара
        webinar_slug = webinar.lower().replace(' ', '-')
        half_link = HALF_WEBINAR_LINK_TEMPLATE.format(webinar=webinar_slug)
        
        bot.send_message(message.chat.id, f"Вот ссылка на половину вебинара **{webinar}**: {half_link}", parse_mode="Markdown")
        
        # Добавляем кнопку для полного доступа
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        markup.add(types.KeyboardButton("Хочу полный доступ"))
        markup.add(types.KeyboardButton("Назад"))
        
        bot.send_message(message.chat.id, "Хотите полный доступ?", reply_markup=markup)

# Обработка "Хочу полный доступ"
@bot.message_handler(lambda message: message.text == "Хочу полный доступ")
def send_purchase(message):
    bot.send_message(message.chat.id, f"Перейдите по ссылке для покупки: {PURCHASE_LINK}")
    
    # Возвращаем к основному меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(types.KeyboardButton("Хочу вебинар!"))
    markup.add(types.KeyboardButton("Все еще сомневаюсь"))
    
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработка выбора полного вебинара
@bot.message_handler(lambda message: any(webinar == message.text for webinar in WEBINARS))
def send_full_webinar_link(message):
    webinar = message.text
    
    bot.send_message(message.chat.id, f"Отлично! Вы выбрали вебинар **{webinar}**. Перейдите по ссылке для покупки: {PURCHASE_LINK}", parse_mode="Markdown")
    
    # Возвращаем к основному меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(types.KeyboardButton("Хочу вебинар!"))
    markup.add(types.KeyboardButton("Все еще сомневаюсь"))
    
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Webhook endpoint
@app.route('/bot', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.get_json())
    bot.process_new_updates([update])
    return 'OK', 200

# Главная страница для проверки работы сервера
@app.route('/', methods=['GET'])
def index():
    return 'Telegram Bot is running!'

if __name__ == '__main__':
    # Удаляем старый webhook и устанавливаем новый
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    
    print(f"Bot started! Webhook URL: {WEBHOOK_URL}")
    print("Make sure your server is accessible from the internet!")
    
    # Запускаем Flask приложение
    app.run(host='0.0.0.0', port=80, debug=False)
