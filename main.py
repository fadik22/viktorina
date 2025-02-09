import telebot
from config import token
from collections import defaultdict
from logic import quiz_questions

# Словарь для хранения ответов пользователей (номер текущего вопроса)
user_responses = defaultdict(int)

# Словарь для хранения очков пользователей
points = defaultdict(int)

bot = telebot.TeleBot(token)

def send_question(chat_id):
    question = quiz_questions[user_responses[chat_id]]
    bot.send_message(chat_id, question.text, reply_markup=question.gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    # Проверяем, правильный ли ответ
    if call.data == "correct":
        bot.answer_callback_query(call.id, "Правильно ✅")
        points[chat_id] += 1  # Начисляем очки за правильный ответ
    else:
        bot.answer_callback_query(call.id, "Неправильно ❌")

    # Переход к следующему вопросу
    user_responses[chat_id] += 1  

    # Проверяем, закончились ли вопросы
    if user_responses[chat_id] >= len(quiz_questions):
        bot.send_message(chat_id, f"Правильно ответил! 🎉\nТвои очки: {points[chat_id]} / {len(quiz_questions)}")
        # Можно очистить данные пользователя (если надо)
        del user_responses[chat_id]
        del points[chat_id]
    else:
        send_question(chat_id)  # Отправляем следующий вопрос

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id not in user_responses:
        user_responses[chat_id] = 0
        send_question(chat_id)

bot.infinity_polling()
