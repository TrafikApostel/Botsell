# -*- coding: utf-8 -*-
from time import sleep
import telebot
from telebot import types
import requests
import json
from random import randint
from datetime import datetime, timedelta

QIWI_TOKEN = 'c2d9cf8651842ddc82b772d3aecd46a3'
QIWI_ACCOUNT = '79650734771'

token = "c2d9cf8651842ddc82b772d3aecd46a3"  # https://qiwi.com/api
phone = "+79650734771"

CHANNEL_NAME = '@WorkSPB_REP'
token_tg = "1183659381:AAHknGE7IsIrusgZ5Gjf27oDYU4Osyavz_M"
bot = telebot.TeleBot(token_tg)

baza = dict()
work_ = dict()
geo_ = dict()
geo__ = dict()
time_ = dict()
price_ = dict()
info_ = dict()
contact_ = dict()
text_ = dict()
pay_ = dict()
dates_ = dict()


@bot.message_handler(commands=['start','admin1Q2W3E4Rqwer'])
def any_msg(message):
    if message.text == '/start':
        keyboardstart = types.InlineKeyboardMarkup()
        first_button = types.InlineKeyboardButton(text="Ссылка", url='http://u1143278.isp.regruhosting.ru')
        second_button = types.InlineKeyboardButton(text="Согласен", callback_data="start")
        keyboardstart.add(first_button)
        keyboardstart.add(second_button)
        bot.send_message(message.chat.id,
                         'Вас приветствует сервис публикации объявлений,\nобъявления публикуются на канале @WorkSPB_REP и в некоторые закрытые группы и чаты, стоимость публикаций:\n150₽ - один раз,\n250₽ - три раза,\n500₽ - семь раз,\nоплата картой через Qiwi,\nа ниже ссылка на договор-оферту, если он, конечно,есть.',
                         reply_markup=keyboardstart)
    elif message.text == '/admin1Q2W3E4Rqwer':
        admin_get = str(text_)
        bot.send_message(message.chat.id,admin_get)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # button
    keyboardstart = types.InlineKeyboardMarkup()
    first_button = types.InlineKeyboardButton(text="Ссылка", url='http://u1143278.isp.regruhosting.ru')
    second_button = types.InlineKeyboardButton(text="Согласен", callback_data="start")
    keyboardstart.add(first_button)
    keyboardstart.add(second_button)
    keyboard1 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Я физлицо", callback_data="Phys")
    btn2 = types.InlineKeyboardButton(text="Я юрлицо", callback_data="Legal")
    keyboard1.add(btn1, btn2)
    keyboard2 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Москва", callback_data="Москва")
    btn2 = types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="Санкт-Петербург")
    keyboard2.add(btn1, btn2)
    keyboard3 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Telegram", url='"PythononeloveSSS')
    btn2 = types.InlineKeyboardButton(text="WhatsApp", url='https://89650734771')
    keyboard3.add(btn1, btn2)
    keyboard4 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Да", callback_data="Да")
    btn2 = types.InlineKeyboardButton(text="Нет", callback_data="Нет")
    keyboard4.add(btn1, btn2)
    keyboard5 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Да", callback_data="Да")
    btn2 = types.InlineKeyboardButton(text="Нет", callback_data="Нет")
    keyboard5.add(btn1, btn2)
    keyboard6 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Бармен', callback_data='Бармен')
    btn2 = types.InlineKeyboardButton(text='Кондитер', callback_data='Кондитер')
    btn3 = types.InlineKeyboardButton(text='Котломойщик', callback_data='Котломойщик')
    btn4 = types.InlineKeyboardButton(text='Менеджр/Администратор', callback_data='Менеджр/Адмистратор')
    btn5 = types.InlineKeyboardButton(text='Официант', callback_data='Официант')
    btn6 = types.InlineKeyboardButton(text='Повар', callback_data='Повар')
    btn7 = types.InlineKeyboardButton(text='Су-шеф', callback_data='Су-шеф')
    btn8 = types.InlineKeyboardButton(text='Су-шеф-кондитер', callback_data='Су-шеф-кондитер')
    btn9 = types.InlineKeyboardButton(text='Уборщик', callback_data='Уборщик')
    keyboard6.add(btn1, btn2, btn3)
    keyboard6.add(btn4, btn5, btn6)
    keyboard6.add(btn7, btn8, btn9)
    keyboard7 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='5/2', callback_data='5/2')
    btn2 = types.InlineKeyboardButton(text='2/2', callback_data='2/2')
    keyboard7.add(btn1, btn2)
    keyboard8 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Да', callback_data='Да_контакты')
    btn2 = types.InlineKeyboardButton(text='Нет', callback_data='Нет_контакты')
    keyboard8.add(btn1, btn2)
    keyboard9 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Да', callback_data='Да_инфа_работа')
    btn2 = types.InlineKeyboardButton(text='Нет', callback_data='Нет_инфа_работа')
    keyboard9.add(btn1, btn2)
    keyboard10 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Публиковать', callback_data='Публиковать')
    btn2 = types.InlineKeyboardButton(text='Оставить', callback_data='Оставить')
    keyboard10.add(btn1, btn2)
    keyboard11 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Один Раз (150₽)", callback_data="ONE")
    btn2 = types.InlineKeyboardButton(text="Три Дня три раза(250₽)", callback_data="TWO")
    btn3 = types.InlineKeyboardButton(text="Неделя семь раз(500₽)", callback_data="THREE")
    keyboard11.add(btn1)
    keyboard11.add(btn2)
    keyboard11.add(btn3)
    keyboard12 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Залатить 150RUB", callback_data="price1")
    keyboard12.add(btn1)
    keyboard13 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Залатить 250RUB", callback_data="price2")
    keyboard13.add(btn1)
    keyboard14 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Залатить 500RUB", callback_data="price3")
    keyboard14.add(btn1)
    keyboard15 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Ссылка для оплаты!",
                                      url='https://qiwi.com/payment/form/99999?extra[%27accountType%27]=phone&extra%5B%27account%27%5D=79650734771')
    keyboard15.add(btn1)
    if call.data == "start":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Вас приветствует сервис публикации объявлений,\nобъявления публикуются на канале @WorkSPB_REP и в некоторые закрытые группы и чаты, стоимость публикаций:\n150₽ - один раз,\n250₽ - три раза,\n500₽ - семь раз,\nоплата картой через Qiwi\nа ниже ссылка на договор-оферту, если он, конечно,есть.')
        bot.send_message(call.message.chat.id,
                         "Смотрите, я могу:\n1. Опубликовать объявление для вас о поиске линейного персонала с оплатой по банковской карте физического лица;\n2. Предложить вам, как юрлицу, вариант публикации объявлений через договор и счёт",
                         reply_markup=keyboard1)
    # ------------------------------------------------------------------------------------------------------------------------
    if call.data == "Legal":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                            text="Смотрите, я могу:\n1. Опубликовать объявление для вас о поиске линейного персонала с оплатой по банковской карте физического лица;\n2. Предложить вам, как юрлицу, вариант публикации объявлений через договор и счёт. Подробнее +79650734771",reply_markup=keyboard1)
    if call.data == "Phys":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Смотрите, я могу:\n1. Опубликовать объявление для вас о поиске линейного персонала с оплатой по банковской карте физического лица;\n2. Предложить вам, как юрлицу, вариант публикации объявлений через договор и счёт. Подробнее +79650734771")
        bot.send_message(call.message.chat.id, "Выберите в каком месте будем искать сотрудников или введите ручками.",
                         reply_markup=keyboard2)
        status = 2
        data = {call.from_user.id: str(status)}
        baza.update(data)
    # ------------------------------------------------------------------------------------------------------------------------
    if call.data == "Москва":
        geo = call.data
        user_id = call.from_user.id
        geo_.update({user_id: geo})
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите в каком месте будем искать сотрудников или введите ручками.")
        bot.send_message(call.message.chat.id,
                         "Вы указали Москва, желаете указать местоположение чуть более подробнее?",
                         reply_markup=keyboard4)

    elif call.data == "Санкт-Петербург":
        user_id = call.from_user.id
        geo = call.data
        geo_.update({user_id: geo})
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите в каком месте будем искать сотрудников или введите ручками.")
        bot.send_message(call.message.chat.id,
                         "Вы указали Санкт-Петербург, желаете указать местоположение чуть более подробнее?",
                         reply_markup=keyboard5)
    # ------------------------------------------------------------------------------------------------------------------------
    if call.data == 'Да':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Желаете указать местоположение чуть более подробнее?")
        bot.send_message(call.message.chat.id,
                         "В таком случае отправьте мне геоточку или напишите словами где это именно")
        status = 1
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Нет':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Желаете указать местоположение чуть более подробнее?")
        bot.send_message(call.message.chat.id, "Пожалуйста, выберите вариант ниже либо введите свой:",
                         reply_markup=keyboard6)
        status = 3
        data = {call.from_user.id: str(status)}
        baza.update(data)
    # -----------------------------------------------------------------------------------------------------------------------
    if call.data == 'Бармен':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками", reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Кондитер':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками",
                         reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Котломойщик':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками",
                         reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Менеджр/Адмистратор':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками", reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Официант':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками", reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Повар':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками", reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Су-шеф':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками", reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Су-шеф-кондитер':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками", reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Уборщик':
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пожалуйста, выберите вариант ниже либо введите свой:")
        bot.send_message(call.message.chat.id, "Выберите смену или введите руками", reply_markup=keyboard7)
        work = call.data
        work_.update({user_id: work})
        status = 4
        data = {call.from_user.id: str(status)}
        baza.update(data)
    # обработчик времени
    if call.data == '5/2':
        user_id = call.from_user.id
        time = call.data
        time_.update({user_id: time})
        status = 5
        data = {call.from_user.id: str(status)}
        baza.update(data)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите смену или введите руками")
        bot.send_message(call.message.chat.id, "Окей, выбранная смена " + time + ". А по зарплате чё?")
    elif call.data == '2/2':
        user_id = call.from_user.id
        time = call.data
        time_.update({user_id: time})
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите смену или введите руками")
        bot.send_message(call.message.chat.id, "Окей, выбранная смена " + time + ". А по зарплате чё?")
        status = 5
        data = {call.from_user.id: str(status)}
        baza.update(data)
    # будем осталять контакты
    if call.data == 'Да_инфа_работа':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Какая-либо дополнительная информация о вакансии?")
        bot.send_message(call.message.chat.id, 'Оооок, ну вводите')
        status = 7
        data = {call.from_user.id: str(status)}
        baza.update(data)
    elif call.data == 'Нет_инфа_работа':
        user_id = call.from_user.id
        try:
            work = work_[user_id]
        except KeyError:
            work = ''
        try:
            geo = geo_[user_id]
        except KeyError:
            geo = ''
        try:
            geoplus = geo__[user_id]
        except KeyError:
            geoplus = ''
        try:
            time = time_[user_id]
        except KeyError:
            time = ''
        try:
            price = price_[user_id]
        except KeyError:
            price = ''
        try:
            info = info_[user_id]
        except KeyError:
            info = ''
        try:
            contact = contact_[user_id]
        except KeyError:
            contact = ''
        text = 'Вакансия: ' + str(work) + '\nМесто: ' + str(
            geo) + '\nТочная локация: ' + str(
            geoplus) + '\nСмена: ' + time + '\nЗарплата: ' + price + '\nДополнительная информация: ' + info + '\nСвязь: ' + contact
        user_id = call.from_user.id
        text_.update({user_id: text})
        bot.send_message(call.message.chat.id,
                         'Итак, вот что у нас получилось:\n\n⚡️⚡️\nВакансия: ' + str(work) + '\nМесто: ' + str(
                             geo) + '\nТочная локация: ' + str(
                             geoplus) + '\nСмена: ' + time + '\nЗарплата: ' + price + '\nДополнительная информация: ' + info + '\nСвязь: ' + contact,
                         reply_markup=keyboard10)
    if call.data == 'Публиковать':
        bot.send_message(call.message.chat.id, text='На сколько раз заряжаем?', reply_markup=keyboard11)
    elif call.data == 'Оставить':
        bot.send_message(call.message.chat.id,
                         'Вас приветствует сервис публикации объявлений,\nобъявления публикуются на канале @WorkSPB_REP и в некоторые закрытые группы и чаты, стоимость публикаций:\n150₽ - один раз,\n250₽ - три раза,\n500₽ - семь раз,\nоплата картой через Qiwi,\nа ниже ссылка на договор-оферту, если он, конечно,есть.',
                         reply_markup=keyboardstart)
    if call.data == 'ONE':
        status = 'pay'
        data = {call.from_user.id: str(status)}
        baza.update(data)
        user_id = call.from_user.id
        price = 150
        pay_.update({user_id: price})
        # Минимальное значение при котором счет будет считаться закрытым
        comment = str(randint(10000, 1000000))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Переведите %i рублей на Qiwi счет %s с комментарием '%s'\nУвас есть 20 минут иначе транзакция не зашитается..." % (
                              price, phone, comment))
        bot.send_message(call.message.chat.id, comment, reply_markup=keyboard15)
        test = 1
        text = text_[user_id]
        while True and baza[user_id] == 'pay' and test <= 1000:
            s = requests.Session()
            s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
            parameters = {'rows': '50'}

            h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments',
                      params=parameters, verify=False)
            req = json.loads(h.text)
            for i in range(len(req)):
                x = req['data'][i]['comment']
                z = req['data'][i]['status']
                y = req['data'][i]['sum']['amount']
                if comment == x and price == y and z == 'SUCCESS':
                    bot.send_message(CHANNEL_NAME, text)
                    bot.send_message(call.message.chat.id, 'Операция по оплате успешна завершенна!')
                    status = 'goodpay'
                    data = {call.from_user.id: str(status)}
                    baza.update(data)
                    break
            test += 1
            sleep(7)
    elif call.data == 'TWO':
        status = 'pay'
        data = {call.from_user.id: str(status)}
        baza.update(data)
        user_id = call.from_user.id
        day_2 = datetime.now() + timedelta(days=1)
        day_2 = str(day_2.month) + str(day_2.day) + str(day_2.hour)
        day_3 = datetime.now() + timedelta(days=2)
        day_3 = str(day_3.month) + str(day_3.day) + str(day_3.hour)
        price = 250
        pay_.update({user_id: price})
        # Минимальное значение при котором счет будет считаться закрытым
        comment = str(randint(10000, 1000000))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Переведите %i рублей на Qiwi счет %s с комментарием '%s'\nУвас есть 20 минут иначе транзакция не зашитается..." % (
                                  price, phone, comment))
        bot.send_message(call.message.chat.id, comment, reply_markup=keyboard15)
        test = 1
        try:
            text = text_[user_id]
        except KeyError:
            text = ''
        while True and baza[user_id] == 'pay' and test <= 1000:
            s = requests.Session()
            s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
            parameters = {'rows': '50'}

            h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments',
                      params=parameters, verify=False)
            req = json.loads(h.text)
            for i in range(len(req)):
                x = req['data'][i]['comment']
                z = req['data'][i]['status']
                y = req['data'][i]['sum']['amount']
                if comment == x and price == y and z == 'SUCCESS':
                    bot.send_message(CHANNEL_NAME, text)
                    bot.send_message(call.message.chat.id, 'Операция по оплате успешна завершенна!')
                    status = 'goodpay'
                    data = {call.from_user.id: str(status)}
                    baza.update(data)
                    break
            test += 1
            sleep(7)
        if status == 'goodpay':
            bot.send_message(CHANNEL_NAME, text)
            while True:
                day = datetime.now()
                day = str(day.month) + str(day.day) + str(day.hour)
                test_data = day
                if test_data == day_2:
                    bot.send_message(CHANNEL_NAME, text)
                    break
                sleep(1500)
            while True:
                day = datetime.now()
                day = str(day.month) + str(day.day) + str(day.hour)
                test_data = day
                if test_data == day_3:
                    bot.send_message(CHANNEL_NAME, text)
                    break
                sleep(1500)
    elif call.data == 'THREE':
        status = 'pay'
        data = {call.from_user.id: str(status)}
        baza.update(data)
        user_id = call.from_user.id
        day_2 = datetime.now() + timedelta(days=1)
        day_2 = str(day_2.month) + str(day_2.day) + str(day_2.hour)
        day_3 = datetime.now() + timedelta(days=2)
        day_3 = str(day_3.month) + str(day_3.day) + str(day_3.hour)
        day_4 = datetime.now() + timedelta(days=3)
        day_4 = str(day_4.month) + str(day_4.day) + str(day_4.hour)
        day_5 = datetime.now() + timedelta(days=4)
        day_5 = str(day_5.month) + str(day_5.day) + str(day_5.hour)
        day_6 = datetime.now() + timedelta(days=5)
        day_6 = str(day_6.month) + str(day_6.day) + str(day_6.hour)
        day_7 = datetime.now() + timedelta(days=6)
        day_7= str(day_7.month) + str(day_7.day) + str(day_7.hour)
        price = 500
        pay_.update({user_id: price})
        # Минимальное значение при котором счет будет считаться закрытым
        comment = str(randint(10000, 1000000))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Переведите %i рублей на Qiwi счет %s с комментарием '%s'\nУвас есть 20 минут иначе транзакция не зашитается..." % (
                                  price, phone, comment))
        bot.send_message(call.message.chat.id, comment, reply_markup=keyboard15)
        test = 1
        text = text_[user_id]
        while True and baza[user_id] == 'pay' and test <= 1000:
            s = requests.Session()
            s.headers['authorization'] = 'Bearer ' + QIWI_TOKEN
            parameters = {'rows': '50'}

            h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + QIWI_ACCOUNT + '/payments',
                      params=parameters, verify=False)
            req = json.loads(h.text)
            for i in range(len(req)):
                x = req['data'][i]['comment']
                z = req['data'][i]['status']
                y = req['data'][i]['sum']['amount']
                if comment == x and price == y and z == 'SUCCESS':
                    bot.send_message(CHANNEL_NAME, text)
                    bot.send_message(call.message.chat.id, 'Операция по оплате успешна завершенна!')
                    status = 'goodpay'
                    data = {call.from_user.id: str(status)}
                    baza.update(data)
                    break
            test += 1
            sleep(7)
        if status == 'goodpay':
            bot.send_message(CHANNEL_NAME, text)
            while True:
                day = datetime.now()
                day = str(day.month) + str(day.day) + str(day.hour)
                test_data = day
                if test_data == day_2:
                    bot.send_message(CHANNEL_NAME, text)
                    break
                sleep(1500)
            while True:
                day = datetime.now()
                day = str(day.month) + str(day.day) + str(day.hour)
                test_data = day
                if test_data == day_3:
                    bot.send_message(CHANNEL_NAME, text)
                    break
                sleep(1500)
            while True:
                day = datetime.now()
                day = str(day.month) + str(day.day) + str(day.hour)
                test_data = day
                if test_data == day_4:
                    bot.send_message(CHANNEL_NAME, text)
                    break
                sleep(1500)
            while True:
                day = datetime.now()
                day = str(day.month) + str(day.day) + str(day.hour)
                test_data = day
                if test_data == day_5:
                    bot.send_message(CHANNEL_NAME, text)
                    break
                sleep(1500)
            while True:
                day = datetime.now()
                day = str(day.month) + str(day.day) + str(day.hour)
                test_data = day
                if test_data == day_6:
                    bot.send_message(CHANNEL_NAME, text)
                    break
                sleep(1500)
            while True:
                day = datetime.now()
                day = str(day.month) + str(day.day) + str(day.hour)
                test_data = day
                if test_data == day_7:
                    bot.send_message(CHANNEL_NAME, text)
                    break
                sleep(1500)
@bot.message_handler(content_types=['text'])
def text_msg(message):
    ud = message.from_user.id
    try:
        status = baza[ud]
    except KeyError:
        status = None
    keyboard4 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Да", callback_data="Да")
    btn2 = types.InlineKeyboardButton(text="Нет", callback_data="Нет")
    keyboard4.add(btn1, btn2)
    keyboard6 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Бармен', callback_data='Бармен')
    btn2 = types.InlineKeyboardButton(text='Кондитер', callback_data='Кондитер')
    btn3 = types.InlineKeyboardButton(text='Котломойщик', callback_data='Котломойщик')
    btn4 = types.InlineKeyboardButton(text='Менеджр/Адми...', callback_data='Менеджр/Адмистратор')
    btn5 = types.InlineKeyboardButton(text='Официант', callback_data='Официант')
    btn6 = types.InlineKeyboardButton(text='Повар', callback_data='Повар')
    btn7 = types.InlineKeyboardButton(text='Су-шеф', callback_data='Су-шеф')
    btn8 = types.InlineKeyboardButton(text='Су-шеф-кондитер', callback_data='Су-шеф-кондитер')
    btn9 = types.InlineKeyboardButton(text='Уборщик', callback_data='Уборщик')
    keyboard6.add(btn1, btn2, btn3)
    keyboard6.add(btn4, btn5, btn6)
    keyboard6.add(btn7, btn8, btn9)
    keyboard7 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='5/2', callback_data='5/2')
    btn2 = types.InlineKeyboardButton(text='2/2', callback_data='2/2')
    keyboard7.add(btn1, btn2)
    keyboard9 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Да', callback_data='Да_инфа_работа')
    btn2 = types.InlineKeyboardButton(text='Нет', callback_data='Нет_инфа_работа')
    keyboard9.add(btn1, btn2)
    keyboard10 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Публиковать', callback_data='Публиковать')
    btn2 = types.InlineKeyboardButton(text='Оставить', callback_data='Оставить')
    keyboard10.add(btn1, btn2)
    if status == '1':
        user_id = message.from_user.id
        geoplus = message.text
        geo__.update({user_id: geoplus})
        status = 3
        data = {message.from_user.id: str(status)}
        baza.update(data)
        bot.send_message(message.chat.id, text="Пожалуйста, выберите вариант ниже либо введите свой:",
                         reply_markup=keyboard6)
    elif status == '2':
        user_id = message.from_user.id
        geo = message.text
        geo_.update({user_id: geo})
        status = 3
        data = {message.from_user.id: str(status)}
        baza.update(data)
        bot.send_message(message.chat.id, text="Желаете указать местоположение чуть более подробнее?",
                         reply_markup=keyboard4)
    elif status == '3':
        user_id = message.from_user.id
        work = message.text
        work_.update({user_id: work})
        status = 4
        data = {message.from_user.id: str(status)}
        baza.update(data)
        bot.send_message(message.chat.id, "Выберите смену или введите руками", reply_markup=keyboard7)
    elif status == '4':
        user_id = message.from_user.id
        time = message.text
        time_.update({user_id: time})
        status = 5
        data = {message.from_user.id: str(status)}
        baza.update(data)
        bot.send_message(message.chat.id, "Окей, выбранная смена " + time + ". А по зарплате чё?")
    elif status == '5':
        user_id = message.from_user.id
        price = message.text
        price_.update({user_id: price})
        status = 6
        data = {message.from_user.id: str(status)}
        baza.update(data)
        bot.send_message(message.chat.id, 'Вводите же свои контакты поскорее')
    elif status == '6':
        user_id = message.from_user.id
        contact = message.text
        contact_.update({user_id: contact})
        bot.send_message(message.chat.id, 'Какая-либо дополнительная информация о вакансии?', reply_markup=keyboard9)
    elif status == '7':
        user_id = message.from_user.id
        work_info = message.text
        info_.update({user_id: work_info})
        try:
            work = work_[user_id]
        except KeyError:
            work = ''
        try:
            geo = geo_[user_id]
        except KeyError:
            geo = ''
        try:
            geoplus = geo__[user_id]
        except KeyError:
            geoplus = ''
        try:
            time = time_[user_id]
        except KeyError:
            time = ''
        try:
            price = price_[user_id]
        except KeyError:
            price = ''
        try:
            info = info_[user_id]
        except KeyError:
            info = ''
        try:
            contact = contact_[user_id]
        except KeyError:
            contact = ''
        text = 'Вакансия: ' + str(work) + '\nМесто: ' + str(
            geo) + '\nТочная локация: ' + str(
            geoplus) + '\nСмена: ' + time + '\nЗарплата: ' + price + '\nДополнительная информация: ' + info + '\nСвязь: ' + contact
        user_id = message.from_user.id
        text_.update({user_id: text})
        bot.send_message(message.chat.id,
                         'Итак, вот что у нас получилось:\n\n⚡️⚡️\nВакансия: ' + str(work) + '\nМесто: ' + str(
                             geo) + '\nТочная локация: ' + str(
                             geoplus) + '\nСмена: ' + time + '\nЗарплата: ' + price + '\nДополнительная информация: ' + info + '\nСвязь: ' + contact,
                         reply_markup=keyboard10)
    else:
        pass


if __name__ == "__main__":
    bot.polling(none_stop=True)