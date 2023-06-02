# Получение токена бота из BotFather
TOKEN = 'your_token'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Сообщение приветствия
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я твой новый телеграм-бот :)")

# Ответ на вопрос "как дела?"
@bot.message_handler(func=lambda message: message.text == 'как дела?')
def how_are_you(message):
    answers = ['Отлично, спасибо!', 'Неплохо, а у тебя?', 'Бывало и лучше, но пока неплохо :)']
    bot.send_message(message.chat.id, random.choice(answers))

# Запуск бота
bot.polling()
