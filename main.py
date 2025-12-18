import telebot

# Aapka API Key (Note: Isse baad mein badal lena, ye public hai abhi)
API_TOKEN = '8525540536:AAFPHx6q38Wk9Rm4wzvR5G9g2qHwK8nBkbY'

bot = telebot.TeleBot(API_TOKEN)

# Start Command ka Jawab
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaste! Aapka Bot Cloud se connect ho gaya hai aur chal raha hai! ✅")

# Koi bhi message likho, wahi wapas bolega
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Aapne kaha: " + message.text)

print("Bot Start Ho Gaya...")
bot.infinity_polling()
