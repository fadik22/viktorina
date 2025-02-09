import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Геттер для текста вопроса
    @property
    def text(self):
        return self.__text

    # Метод для генерации Inline-клавиатуры
    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        for i, option in enumerate(self.options):
            callback_data = 'correct' if i == self.__answer_id else 'wrong'
            markup.add(InlineKeyboardButton(option, callback_data=callback_data))
        return markup


# Список вопросов для викторины
quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 0, "Спят", "Пишут мемы"),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, 
             "Обретение вашего внутреннего урр-мирения", 
             "Тайм-менеджмент или как выделить 18 часов в день для сна", 
             "101 способ уснуть на 5 минут раньше, чем хозяин", 
             "Пособие по управлению людьми")
]
