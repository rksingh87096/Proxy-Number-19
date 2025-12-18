import telebot
import requests
import os
from flask import Flask
from threading import Thread

# --- API KEY ---
API_TOKEN = '8525540536:AAFPHx6q38Wk9Rm4wzvR5G9g2qHwK8nBkbY'

bot = telebot.TeleBot(API_TOKEN)

# --- FLASK SERVER (RENDER KE LIYE) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running! Premium Lookup Active."

def run_http():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run_http)
    t.start()

# --- ⚙️ MAIN LOGIC: YAHAN APNA API JODNA HAI ---
def fetch_data_from_api(mobile_number):
    try:
        # ⚠️ YAHAN DHYAN DEIN:
        # Agar aapke paas koi Website/API link hai jo data deti hai, usse yahan likhein.
        # Example: url = f"https://api.yoursite.com/get_info?num={mobile_number}"
        
        # Abhi main dummy data return kar raha hoon taaki aap format dekh sakein.
        # Jab aapka API lag jayega, toh niche wala part hatakar real response use karein.
        
        # --- (Aapka API Code Yahan Aayega) ---
        # response = requests.get(f"YOUR_API_LINK_HERE/{mobile_number}")
        # data = response.json()
        
        # Niche woh format hai jo aapne manga tha:
        # Maan lo API se ye data aaya:
        data = {
            "name": "Data Not Found (API Connect Karein)",
            "mobile": mobile_number,
            "father": "---",
            "location": "India",
            "circle": "Unknown",
            "id": "---",
            "address": "API connect karne ke baad yahan asli address aayega."
        }
        
        # Agar aapke GitHub me koi script hai (jaise 'data.py'), toh usse import karke data lein.
        
        return data
    except Exception as e:
        return None

# --- MESSAGE HANDLER ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaste! 🔍\nNumber bhejein, main details nikalunga.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_msg = message.text
    
    # Check agar number valid lag raha hai (10 digits)
    if len(user_msg) >= 10 and any(char.isdigit() for char in user_msg):
        
        processing_msg = bot.reply_to(message, "🔄 Searching Data... Please wait.")
        
        # Data fetch karein
        info = fetch_data_from_api(user_msg)
        
        if info:
            # --- 🎨 AAPKA EXACT FORMAT YAHAN HAI ---
            reply_text = (
                f"📱 **Mobile Details Found**\n\n"
                f"👤 **Name:** {info['name']}\n"
                f"📞 **Mobile:** {info['mobile']}\n"
                f"👨 **Father's Name:** {info['father']}\n"
                f"📍 **Location:** {info['location']}\n"
                f"⭕ **Circle:** {info['circle']}\n"
                f"🆔 **ID:** {info['id']}\n"
                f"🏠 **Address:** {info['address']}\n\n"
                f"👇 **Full API Response**\n"
                f"Live locations"
            )
            
            # Message edit karke result dikhayein
            bot.edit_message_text(reply_text, chat_id=message.chat.id, message_id=processing_msg.message_id, parse_mode="Markdown")
        else:
            bot.edit_message_text("❌ Data nahi mila ya API error hai.", chat_id=message.chat.id, message_id=processing_msg.message_id)
            
    else:
        bot.reply_to(message, "Kripya sahi Mobile Number bhejein.")

# --- RUN ---
if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
