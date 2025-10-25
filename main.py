import telebot,requests
import secret
from for_sql1 import ddb
bot = telebot.TeleBot(secret.TOKEN)

m = 'message'
gr = 0
ddb()
@bot.message_handler(commands=['start'])
def hellow(m):
    bot.send_message(m.chat.id, "Нужно заменить")
    bot.send_message(m.chat.id, "Из какой ты группы?(ИСП-?)")

@bot.message_handler()
def us_group(m):
    global gr
    bot.register_next_step_handler(m,bot.send_message(m.chat.id,f"Хорошо буду присылать расписание для {m.text} группы"))
    gr = int(m.text)

@bot.message_handler(func=lambda message:True)
def text_message(m):
    if m.text == 'Группа':
        bot.reply_to(m.chat.id, f"вот твоя группа {gr}")













bot.infinity_polling() 