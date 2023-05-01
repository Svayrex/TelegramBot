import telebot
from telebot import types
bot = telebot.TeleBot('6236952582:AAEPeDuGFV_eX9kMGWOGzz21xtFAjuMo9iE')
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('D:\Новая папка\питон\ТГ бот\ТГ Бот\Z.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📋 Информация 📋")
    item2 = types.KeyboardButton("💎 О да, я хочу быть в топе! 💎")
    item3 = types.KeyboardButton("💻 Разработчики 💻")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, помогу тебе ворваться в хип-хоп!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '💎 О да, я хочу быть в топе! 💎':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("💸 Напишите крутой бит! 💸", callback_data='1')
            item2 = types.InlineKeyboardButton("⚡ Сделайте текст! ⚡", callback_data='2')
            item3 = types.InlineKeyboardButton("🎧 Сведите на высшем уровне! 🎧", callback_data='3')
            item4 = types.InlineKeyboardButton("🌟 Напишите трек! 🌟", callback_data='4')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Что вам нужно?', reply_markup=markup)
        elif message.text == "📋 Информация 📋":
            bot.send_message(message.chat.id, " 📃 Мы работаем с людьми которые хотят попасть в реки или зайти на высший уровень!" +
                " Я готов помочь вам с любыми музыкальными трудностями" + 
                " Наши услуги дают возможность максимально индивидуализировать продукт под себя.")
        elif message.text == "💻 Разработчики 💻":
            bot.send_message(message.chat.id, '🤖 Данный бот был разработан <b>TRAMPOR™️</b>', parse_mode='html')
        else:
            bot.send_message(message.chat.id, 'По другим вопросам пишите сюда → @TRAMPORT')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                bot.send_message(call.message.chat.id, '💥 Посмотрите это видео → https://www.youtube.com/watch?v=3vTnIVDTjsM')
            elif call.data == '2':
                bot.send_message(call.message.chat.id, '💥 Посмотрите это видео → https://www.youtube.com/watch?v=g1YO2ZSwjgA')
            elif call.data == '3':
                bot.send_message(call.message.chat.id, '💥 Посмотрите это видео → https://www.youtube.com/watch?v=jqmfA23jbyM')
            elif call.data == '4':
                bot.send_message(call.message.chat.id, '💥 Посмотрите это видео → https://www.youtube.com/watch?v=0xkt_58cXOA')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спасибо за обращение! 😘",
                reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Пишите, всегда поможем!")
    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)