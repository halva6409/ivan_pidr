import telebot,requests
import secret

bot = telebot.TeleBot(secret.TOKEN)

@bot.message_handler(commands=['start'])
def hellow(message):
    bot.reply_to(message, "Привет, я бот, который поможет тебе в колледже, я могу напомнить вам о следующей паре,в каком она кабинет и во сколько звонок. Еще я могу помочь тебе с какими либо заданиями.")

bot.infinity_polling()