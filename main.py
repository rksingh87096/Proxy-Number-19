import telebot
import os
from flask import Flask
from threading import Thread

# --- SETUP: API KEY ---
# (Apna API Token yahan dalein)
API_TOKEN = '8525540536:AAFPHx6q38Wk9Rm4wzvR5G9g2qHwK8nBkbY'

bot = telebot.TeleBot(API_TOKEN)

# --- JUGAAD: FAKE WEBSITE (FOR RENDER) ---
app = Flask('')

@app.route('/')
def home():
    return "I am alive! Bot chal raha hai."

def run_http():
    # Render jo PORT dega uspar chalega, nahi toh 8080 par
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run_http)
    t.start()

# --- BOT COMMANDS ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaste! Main ab Render par 24/7 chalunga. ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Reply: " + message.text)

# --- START EVERYTHING ---
if __name__ == "__main__":
    keep_alive()  # Pehle server start hoga
    print("Bot start ho raha hai...")
    bot.infinity_polling() # Fir bot start hoga
