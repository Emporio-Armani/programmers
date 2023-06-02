# получение токена бота из BotFather
TOKEN = 'your_token'

# создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# сообщение приветствия
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я твой новый телеграм-бот :)")
