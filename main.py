import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('Русский')
    item2 = types.KeyboardButton('English')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 
        'Дамы и господа приветствуем'.format(
        message.from_user, 
        bot.get_me()), 
        parse_mode='html', 
        reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Русский':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            item1 = types.KeyboardButton('🛒 Магазин')
            item2 = types.KeyboardButton('💵 Баланс')
            item3 = types.KeyboardButton('☎️ Поддержка')
            item4 = types.KeyboardButton('📝 Промокод')
            item5 = types.KeyboardButton('👥 Реферальная программа')
            item6 = types.KeyboardButton('📋 Наличие')
            item7 = types.KeyboardButton('Диспут/ненаход')
            item8 = types.KeyboardButton('Отзывы')
            item9 = types.KeyboardButton('Поддержка и правила')
            item10 = types.KeyboardButton('Обменки')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
            bot.send_message(message.chat.id, 'Русский:', reply_markup=markup)


        elif message.text == '🛒 Магазин': 


                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                item1 = telebot.types.InlineKeyboardButton('🧇🧇Cookies🧇🧇', callback_data='Cookies')
                markup.add(item1)
                        
                        
                bot.send_message(message.chat.id,
                "🛒 Магазин", reply_markup=markup)

        elif message.text == '💵 Баланс': 


                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                item1 = telebot.types.InlineKeyboardButton('⏳ История', callback_data='his')
                item2 = telebot.types.InlineKeyboardButton('📤 LTC Пополнить', callback_data='popolnit') 
                markup.add(item1, item2)
                        
                        
                bot.send_message(message.chat.id,
                '''💵 Баланс:

    🌞 Актуальный курс LTC: 1 LTC = 123 usd

    Баланс вашего кошелька: 0 LTC (0 usd)
    Всего загружено: 0 LTC (0 usd)
    Всего потрачено: 0 LTC (0 usd)''', reply_markup=markup)

        elif message.text == '☎️ Поддержка': 


                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                item1 = telebot.types.InlineKeyboardButton('Связатся', url="https://t.me/weed_support_bot", callback_data='Svazatsa')
                markup.add(item1)
                        
                        
                bot.send_message(message.chat.id,
                "☎️ Поддержка", reply_markup=markup)


        elif message.text == '👥 Реферальная программа': 
                
                                        
                bot.send_message(message.chat.id,
                '''Приглашайте друзей и получайте бонусы за их покупки
                👥 Ваших рефералов: 0
                🎁 Заработано на рефералах:
                BTC - 0
                Всего - 0 USD''')
                bot.send_message(message.chat.id,
                "➰ Ваша реферальная ссылка: https://t.me/MyrzaGeroybot?start=658365722")

        elif message.text == '📝 Промокод': 


            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            item1 = telebot.types.InlineKeyboardButton('❌ Отмена', callback_data='Cencel')
            markup.add(item1)
                    
            bot.send_message(message.chat.id,
            "Введите промокод:", reply_markup=markup)


        elif message.text == '📋 Наличие': 


                bot.send_message(message.chat.id,
                '''Наличие товаров:



    🧇🧇Cookies🧇🧇

        🧇🧇Cookies🧇🧇: 7 → 20.00 usd''')

        elif message.text == 'Диспут/ненаход': 


                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                item1 = telebot.types.InlineKeyboardButton('❌ Отмена', callback_data=' Cencel')
                item2 = telebot.types.InlineKeyboardButton('✅ Отправить репорт', callback_data='good')            
                markup.add(item1, item2)
                        
                        
                bot.send_message(message.chat.id,
                '''Обязательно к прочтению ПРАВИЛА:
    
    Гарантия на любую моментальную покупку после выдачи адреса - 5 часов. 
    Гарантия на покупку по предзаказу с момента выдачи адреса - 4 часа. 
    По истечении этого времени претензии по отсутствию или качеству товара не принимаются.


    Отправте все фото и видео фиксацию с метса ненахода 
    Подробно опишите ситуацию . 
    После чего Вам не обходимо нажмить на кнопку 
    "отправить репорт"

    С Уважением, "Family Weed"...
    Приносим извинения за не удобства .''', reply_markup=markup)

        elif message.text == 'Отзывы': 


                bot.send_message(message.chat.id,'''Отзывы:

    02.11.2020 18:04:02 @CALILIFE0312 - TOURIST: Trip report special for family weed
    сорт: Purple
    Кладмен respect (ps: касание)
    Толлер : как космос
    Кросстоллер :
    Cheese
    Purple
    Orange bud
    OG
    Руч
    Варя
    Лёд

    Сами шишки понравились очень уже подымал не раз 😅
    Вкус и запах топ 🔥🔥
    Стоун: 4 из 5
    Благодарю шоп и его команду за фастовое решение диспута,
    Famal благодарю за поддержку
    Всем peace
    09.06.2021 14:44:53 @Ppcmt - m - Only: Бот не пополняет хотя пожверждения все прошли более 6 confirms. Прошу решить в срочном порядке
    01.06.2021 22:10:55 Salam - Aleikum: Мы сделали покупку 2 гр приехали на место а Клада нету можете пожалуйста принять меры?!
    09.06.2021 13:03:06 JZ: Всем салют. Вчера приобрел OG KUSH и сказать что я о.уел, все равно что ничего не сказать. Такого стаффа по правде я давно не пробовал, если даже вообще не пробовал. Для тех у кого толлер на уровне, слабые складутся на раз два)) всем добра ✌🏼 ☮️
    25.05.2021 23:58:17 @cr0ss - 😎 - 🤓: Просто Топ''')

        elif message.text == 'Поддержка и правила': 


                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                item1 = telebot.types.InlineKeyboardButton('Связаться', url="https://t.me/weed_support_bot", callback_data='good')
                markup.add(item1)
                        
                        
                bot.send_message(message.chat.id,
                "❓ Поддержка", reply_markup=markup)

        elif message.text == 'Обменки': 
                bot.send_message(message.chat.id,
                '''    @fast24bot

    ответственности за обмен валют не несем !!!''')

        else:
            bot.send_message(message.chat.id,"Комманда не распознана")






    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.message:
            if call.data == 'his':
                bot.send_message(call.message.chat.id, '''⏳ Ваши последние транзакции:

    🚫 У вас нет транзакций''')
            elif call.data == 'popolnit':


                markup = telebot.types.InlineKeyboardMarkup(row_width=1)
                item1 = telebot.types.InlineKeyboardButton('❌ Отмена', callback_data='Cencel')
                markup.add(item1)


                bot.send_message(call.message.chat.id, '''💵 Баланс

    Ваш личный адрес LTC для пополнения кошелька ниже.

    Баланс вашего кошелька будет обновлен после подтверждения сети (обычно в течение часа).
    Адрес одноразовый, не используйте его повторно.''')
                bot.send_message(call.message.chat.id, "LgWM85uwgLNgtZfdhc4zeMMD2E1yqJBqGr", reply_markup=markup)
            elif call.data == 'Cencel':

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item1 = types.KeyboardButton('🛒 Магазин')
                item2 = types.KeyboardButton('💵 Баланс')
                item3 = types.KeyboardButton('☎️ Поддержка')
                item4 = types.KeyboardButton('📝 Промокод')
                item5 = types.KeyboardButton('👥 Реферальная программа')
                item6 = types.KeyboardButton('📋 Наличие')
                item7 = types.KeyboardButton('Диспут/ненаход')
                item8 = types.KeyboardButton('Отзывы')
                item9 = types.KeyboardButton('Поддержка и правила')
                item10 = types.KeyboardButton('Обменки')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
                bot.send_message(message.chat.id, '❌ Отмена', reply_markup=markup)


            
                        
                        



# запуск бота
bot.polling(none_stop=True)
