import telebot

TOKEN = '7538153158:AAFAfuK-7CHDJ3LKnVXKjW5EC9uwxwW1L7A'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, 'مرحباً! أنا بوت تلجرام بسيط.')

@bot.message_handler(commands=['help'])
def send_message(message):
    bot.send_message(message.chat.id, 'أنا بوت تلجرام بسيط. يمكنك استخدام الأوامر التالية:')
    bot.send_message(message.chat.id, '/start - لبدء المحادثة')
    bot.send_message(message.chat.id, '/help - للحصول على مساعدة')

@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
