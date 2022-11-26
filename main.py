import telebot
from telebot import types
import data_base

Bot = telebot.TeleBot('5838208558:AAG4KXDzmuLKe4Ew_wonP6qANFmDHMO_-po')
user_index = 0
data = [[1, 'Равиль', '89998887733', '1234123412341234', 10000, '1234', 'АКТИВНА', '05,29',[]],
        [2, 'Ксения', '87776665544', '5678567856785678', 10000, '1234', 'ЗАБЛОКИРОВАНА','07.29', []]]

@Bot.message_handler(commands=['start'])
def login_1(message, res=True):
    Bot.reply_to(message,
                 '🧐Здравствуйте, я помощник Flex! Введите ваш номер телефона для дальнейших действий')

    Bot.register_next_step_handler(message, login_2)
def login_2(message):
    login_check = 0
    user_index = 0
    for i in range(len(data)):
        if data[i][2] == message.text:
            login_check = 1
            user_index = i
            break
    if login_check == 1:
            Bot.reply_to(message, 'Введите PIN код для подтверждения, что вы владелец карты')
    # if message.text==data[user_index][5]:
    #         login_check = 2
    #if login_check==2:
    #        Bot.reply_to(message,'Добро пожаловать, ваш баланс равен '+data[user_index][5])
    else:
        Bot.send_message(message.chat.id,'Номер отсутствует в базе данных')
        login_1(message)
    if login_check==1:
        Bot.register_next_step_handler(message, login_3)
def login_3(message):
    login_check=False
    bal_check=0
    if message.text==data[user_index][5]:
            login_check = True
    if login_check:
        bal_check=1
        Bot.send_message(message.chat.id,'Добро пожаловать, ваш баланс равен '+str(data[user_index][4]))
        
        if bal_check==1:
            Bot.send_message(message.chat.id,'Как настроение?')
            Bot.register_next_step_handler(message,button_message)
        else:
            Bot.register_next_step_handler(message,button_message)
    else:
        Bot.reply_to(message,'PIN код неверный, попробуйте заново /start')



def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mk5 = types.KeyboardButton('Баланс')
    mk1 = types.KeyboardButton('О карте')
    mk2 = types.KeyboardButton('История')
    mk3 = types.KeyboardButton('Перевод')
    mk4 = types.KeyboardButton('Ещё')
    markup.add(mk1,mk2,mk3,mk4,mk5)
    Bot.send_message(message.chat.id, 'Что вы хотите сделать?', reply_markup=markup)


@Bot.message_handler()



def answer(message):
    if message.text == 'Ещё':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mr1 = types.KeyboardButton('Помощь')
        mr2 = types.KeyboardButton('Акции и предложения')
        mr3 = types.KeyboardButton('Открыть новый счёт или продукт')
        mr4 = types.KeyboardButton('Назад')
        mr5 = types.KeyboardButton('Предложить кредит')
        markup1.add(mr1,mr2,mr3,mr4,mr5)
        Bot.send_message(message.chat.id,'C чем вам помочь?',reply_markup=markup1)
    elif message.text.strip()=='Назад':
        button_message(message)
    elif message.text.strip()=='Предложить кредит':
        Bot.send_message(message.chat.id,'Вы ещё не совершеннолетний, я не могу предложить вам кредит')
    elif message.text.strip()=='Баланс' :
        Bot.send_message(message.chat.id,'Ваш баланс: '+str( data[user_index][4]))
    elif message.text.strip()=='О карте' :
        Bot.send_message(message.chat.id,'Номер: 1236456712347890\nСрок действия: 07/28\nСтатус: Активна')
    elif message.text.strip()=='История' :
        if len(data[user_index][-1])==0:
            Bot.send_message(message.chat.id,'За последнее время платежей и переводов небыло')
        else:
            Bot.send_message(message.chat.id,data[user_index][-1])
    elif message.text.strip()=='Перевод' :
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1 = types.KeyboardButton('По номеру карты')
        mar2 = types.KeyboardButton('По номеру телефона')
        mar3 = types.KeyboardButton('Назад')
        markup2.add(mar1,mar2,mar3)
        Bot.send_message(message.chat.id,'Каким способом вы хотите превести?', reply_markup=markup2)
    elif message.text.strip()=='Назад':
        button_message(message)
    elif message.text.strip()=='По номеру карты' :
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        m1 = types.KeyboardButton('Кристина-500')
        m2 = types.KeyboardButton('Андрей-1000')
        markup3.add(m1,m2)
        Bot.send_message(message.chat.id, 'Введите номер карты и сумму перевода или выберите самый из списка', reply_markup=markup3)
    elif message.text.strip()=='Кристина-500':
        data[user_index][4]-=500
        data[user_index][-1].append('Кристина-500')
        Bot.reply_to(message,'Перевод завершён\nВаш баланс: '+str(data[user_index][4]))
        button_message(message)
    elif message.text.strip()=='Андрей-1000':
        data[user_index][4]-=1000
        data[user_index][-1].append('Андрей-1000')
        Bot.reply_to(message,'Перевод завершён\nВаш баланс: '+str(data[user_index][4]))
        button_message(message)

Bot.polling(non_stop=True, interval=0)