import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '8183348642:AAGFoYQh58pHNbTJDbJ8--rn_VeYI6XA3a0'
bot = telebot.TeleBot(TOKEN)

def get_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(KeyboardButton("/start — Bosh sahifa"))
    markup.add(KeyboardButton("🏢 Kompaniya haqida"), KeyboardButton("🔧 Xizmatlarimiz"))
    markup.add(KeyboardButton("📞 Aloqa va telefon"), KeyboardButton("👨‍💻 Yaratuvchi haqida"))
    markup.add(KeyboardButton("🆘 Maslahat olish"))
    return markup

def send_welcome_message(chat_id):
    welcome_text = (
        "*Assalomu alaykum! SmartXizmat IT botiga xush kelibsiz!*\n\n"
        "Men sizga har qanday IT va dasturlash savollarida yordam beraman:\n"
        "• Python dasturlash\n"
        "• Windows/Linux o'rnatish\n"
        "• Microsoft Office (Excel, Word)\n"
        "• Telegram bot yaratish\n"
        "• Kompyuter muammolari\n\n"
        "Savolingizni yozing — batafsil javob beraman! 👇"
    )
    bot.send_message(chat_id, welcome_text, parse_mode='Markdown', reply_markup=get_main_menu())

@bot.message_handler(commands=['start'])
def start(message):
    send_welcome_message(message.chat.id)

@bot.message_handler(func=lambda message: True)
def all_messages(message):
    lower_text = message.text.lower().strip() if message.text else ""

    if lower_text in ["/start", "/start — bosh sahifa"]:
        send_welcome_message(message.chat.id)
        return

    response = ""

    # Python bo'yicha savollar
    if any(word in lower_text for word in ["python", "pyt hon", "payton", "python nima", "python dastur"]):
        response = (
            "🐍 *Python dasturlash tili bo'yicha yordam:*\n\n"
            "Python — eng mashhur va oson dasturlash tillaridan biri. Veb-sayt, bot, AI, avtomatlashtirish va ilmiy hisoblarda ishlatiladi.\n\n"
            "*Pythonni qanday o'rnatish kerak?*\n"
            "1. python.org saytiga kiring\n"
            "2. \"Downloads\" → Windows/Mac/Linux uchun versiyani yuklang\n"
            "3. O'rnatishda \"Add Python to PATH\" ni belgilang!\n"
            "4. Terminalda `python --version` deb tekshiring\n\n"
            "*Birinchi dastur:*\n"
            "```python\n"
            "print(\"Salom, Python!\")\n"
            "```\n\n"
            "*Yaxshi o'rganish uchun:*\n"
            "• VS Code + Python extension\n"
            "• PyCharm Community (bepul)\n"
            "• YouTube: \"Python darslari o'zbekcha\"\n\n"
            "Qanday savolingiz bor? Masalan:\n"
            "• Pythonni o'rnatish\n"
            "• Birinchi kod yozish\n"
            "• Telegram bot yaratish (Python bilan)\n"
            "• O'yin yoki veb-sayt yaratish"
        )

    # Ubuntu/Linux o'rnatish (oldingi batafsil javob)
    elif any(word in lower_text for word in ["linux", "ubuntu", "ikkita os", "dual boot"]):
        response = (
            "🐧 *Notebookga Ubuntu Linux o'rnatish (Windows bilan birga — Dual Boot)*\n\n"
            "Ehtiyot bo'ling — ma'lumotlar zaxirasini oling!\n\n"
            "1. ubuntu.com dan ISO yuklang\n"
            "2. Rufus bilan bootable USB yarating\n"
            "3. BIOSda USBni birinchi qilib qo'ying\n"
            "4. 'Install Ubuntu' → 'Something else' → bo'sh joy ajrating\n"
            "5. ext4 va swap bo'limlari yarating\n"
            "6. GRUB o'rnatiladi → qayta yuklang\n\n"
            "Endi Windows yoki Ubuntu tanlaysiz!\n\n"
            "Muammo chiqsa — aniq yozing, yordam beraman!\n"
            "📞 +998 94 256 15 86"
        )

    # Windows o'rnatish
    elif "windows" in lower_text and "o'rnat" in lower_text:
        response = "🖥️ Windows o'rnatish → ISO + Rufus + BIOSda USB → Disk format → O'rnatish"

    # Office
    elif any(word in lower_text for word in ["excel", "word", "office"]):
        response = "📊 Excel yoki 📝 Word bo'yicha savolingizni aniqroq yozing — formula, sahifa raqami, mundarija va h.k. bo'yicha yordam beraman!"

    # Kompaniya va aloqa
    elif any(word in lower_text for word in ["kompaniya", "smartxizmat"]):
        response = "*SmartXizmat* — IT va raqamli xizmatlar bo'yicha professional jamoa."

    elif any(word in lower_text for word in ["telefon", "aloqa"]):
        response = "📞 +998 94 256 15 86\n+998 20 023 84 86"

    # Umumiy javob (faqat kerak bo'lmaganda)
    else:
        response = (
            f"*Savolingiz:* `{message.text}`\n\n"
            "Rahmat! IT va dasturlash bo'yicha batafsil javob beraman.\n\n"
            "Misollar:\n"
            "• Python o'rnatish va dastur yozish\n"
            "• Ubuntu/Windows o'rnatish\n"
            "• Excel formulalari\n"
            "• Bot yaratish\n"
            "• Kompyuterni tezlashtirish\n\n"
            "Aniqroq yozing — bosqichma-bosqich yordam beraman!\n"
            "📞 Tez yordam: +998 94 256 15 86"
        )

    bot.reply_to(message, response, parse_mode='Markdown', reply_markup=get_main_menu())

print("Bot ishga tushdi! Python bo'limi qo'shildi — endi 'python' deb yozganda batafsil javob beradi.")
bot.infinity_polling()