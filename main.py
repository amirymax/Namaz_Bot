from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from tokenz import token
from Person import Person

bot = Bot(token=token)
dp = Dispatcher(bot)
user = Person()


@dp.message_handler(commands=['bqapen_hamat'])
async def send_all(message):
    user.send_to_all()
    for i in user.sending_list:
        await eval(i)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user.name = message.from_user.first_name
    user.username = message.from_user.username
    user.user_id = message.from_user.id
    start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tj = types.KeyboardButton('Тоҷикистон🇹🇯')
    ru = types.KeyboardButton('Россия🇷🇺')
    ind = types.KeyboardButton('Indonesia🇮🇩')
    kz = types.KeyboardButton('Қазақстан🇰🇿')
    uz = types.KeyboardButton('Oʻzbekiston🇺🇿')
    start_keyboard.add(tj, ru, ind, kz, uz)
    s = '''
        \tТоҷикистон🇹🇯
    Россия🇷🇺
    Indonesia🇮🇩
    Қазақстан🇰🇿
    Oʻzbekiston🇺🇿
        '''
    user.start_keyboard = start_keyboard
    await bot.send_message(message.chat.id, s, reply_markup=start_keyboard)


# Tojikiston

@dp.message_handler(lambda message: message.text == 'Тоҷикистон🇹🇯')
async def taj(message: types.Message):
    greetings = f'Салом <b>{message.from_user.first_name}!</b>\nБарои дидани вақти <b>намоз🕋</b> шаҳри худро интихоб кунед\n\n<i>Автор: Амирӣ</i>'
    user.country = 'tj'
    keys = list(user.taj_cities.keys())
    tj_cities_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('◀️')
    tj_cities_markup.add(back)
    for i in range(0, len(keys) - 1, 2):
        b1 = types.KeyboardButton(keys[i])
        b2 = types.KeyboardButton(keys[i + 1])
        tj_cities_markup.add(b1, b2)

    tj_cities_markup.add(back)

    await bot.send_message(message.chat.id, greetings, reply_markup=tj_cities_markup, parse_mode='html')


@dp.message_handler(lambda message: message.text in user.taj_cities.keys())
async def tj_cities(message: types.Message):
    user.city = message.text
    user.parse_tj()
    await bot.send_message(message.chat.id, user.message, parse_mode='html', disable_web_page_preview=True)
    user.to_db()


##########

# Russia

@dp.message_handler(lambda message: message.text == 'Россия🇷🇺')
async def rus(message: types.Message):
    greetings = f'Привет <b>{message.from_user.first_name}!</b>\nЧтобы посмотерть время <b>намаза🕋</b> выберите свой город.\n\n<i>Автор: Амири</i>'
    user.country = 'ru'
    keys = list(user.rus_cities.keys())
    ru_cities_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(keys) - 1, 2):
        b1 = types.KeyboardButton(keys[i])
        b2 = types.KeyboardButton(keys[i + 1])
        ru_cities_markup.add(b1, b2)
    back = types.KeyboardButton('◀️')
    ru_cities_markup.add(back)
    await bot.send_message(message.chat.id, greetings, reply_markup=ru_cities_markup, parse_mode='html')


@dp.message_handler(lambda message: message.text in user.rus_cities.keys())
async def ru_cities(message: types.Message):
    user.city = message.text
    user.parse_ru()
    await bot.send_message(message.chat.id, user.message, parse_mode='html', disable_web_page_preview=True)
    user.to_db()


##########

# Indonesia

@dp.message_handler(lambda message: message.text == 'Indonesia🇮🇩')
async def ind(message: types.Message):
    greetings = f'Salam <b>{message.from_user.first_name}!</b>\nBot telegram ini dibuat oleh Amiri untuk menunjukkan waktu shalat.🕋\n\n<i>Pengarang: Amiri</i>'
    user.country = 'ind'
    keys = list(user.ind_cities.keys())
    ind_cities_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('◀️')
    ind_cities_markup.add(back)
    for i in range(0, len(keys) - 1, 2):
        b1 = types.KeyboardButton(keys[i])
        b2 = types.KeyboardButton(keys[i + 1])
        ind_cities_markup.add(b1, b2)

    ind_cities_markup.add(back)
    await bot.send_message(message.chat.id, greetings, reply_markup=ind_cities_markup, parse_mode='html')


@dp.message_handler(lambda message: message.text in user.ind_cities.keys())
async def ind_cities(message: types.Message):
    user.city = message.text
    user.parse_ind()
    await bot.send_message(message.chat.id, user.message, parse_mode='html', disable_web_page_preview=True)
    user.to_db()


##########

# Kazakhstan

@dp.message_handler(lambda message: message.text == 'Қазақстан🇰🇿')
async def kaz(message: types.Message):
    greetings = f'Привет <b>{message.from_user.first_name}!</b>\nЧтобы посмотерть время <b>намаза🕋</b> выберите свой город.\n\n<i>Автор: Амири</i>'
    user.country = 'kz'
    keys = list(user.kaz_cities.keys())
    kz_cities_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(keys) - 1, 2):
        b1 = types.KeyboardButton(keys[i])
        b2 = types.KeyboardButton(keys[i + 1])
        kz_cities_markup.add(b1, b2)
    back = types.KeyboardButton('◀️')
    kz_cities_markup.add(back)
    await bot.send_message(message.chat.id, greetings, reply_markup=kz_cities_markup, parse_mode='html')


@dp.message_handler(lambda message: message.text in user.kaz_cities.keys())
async def kaz_cities(message: types.Message):
    user.city = message.text
    user.parse_kz()
    await bot.send_message(message.chat.id, user.message, parse_mode='html', disable_web_page_preview=True)
    user.to_db()


##########


# Uzbekistan

@dp.message_handler(lambda message: message.text == 'Oʻzbekiston🇺🇿')
async def uzb(message: types.Message):
    greetings = f'Привет <b>{message.from_user.first_name}!</b>\nЧтобы посмотерть время <b>намаза🕋</b> выберите свой город.\n\n<i>Автор: Амири</i>'
    user.country = 'uz'
    keys = list(user.uzb_cities.keys())
    uz_cities_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(keys) - 1, 2):
        b1 = types.KeyboardButton(keys[i])
        b2 = types.KeyboardButton(keys[i + 1])
        uz_cities_markup.add(b1, b2)
    back = types.KeyboardButton('◀️')
    uz_cities_markup.add(back)
    await bot.send_message(message.chat.id, greetings, reply_markup=uz_cities_markup, parse_mode='html')


@dp.message_handler(lambda message: message.text in user.uzb_cities.keys())
async def uzb_cities(message: types.Message):
    user.city = message.text
    user.parse_uz()
    await bot.send_message(message.chat.id, user.message, parse_mode='html', disable_web_page_preview=True)
    user.to_db()


##########


@dp.message_handler(lambda message: message.text == '◀️')
async def go_back(message: types.Message):
    if user.start_keyboard is None:
        start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tj = types.KeyboardButton('Тоҷикистон🇹🇯')
        ru = types.KeyboardButton('Россия🇷🇺')
        ind = types.KeyboardButton('Indonesia🇮🇩')
        kz = types.KeyboardButton('Қазақстан🇰🇿')
        uz = types.KeyboardButton('Oʻzbekiston🇺🇿')
        start_keyboard.add(tj, ru, ind, kz, uz)
        s = '''
                \tТоҷикистон🇹🇯
            Россия🇷🇺
            Indonesia🇮🇩
            Қазақстан🇰🇿
            Oʻzbekiston🇺🇿
                '''
        user.start_keyboard = start_keyboard

    await bot.send_message(message.chat.id, '◀️', reply_markup=user.start_keyboard)


executor.start_polling(dp, skip_updates=True)
