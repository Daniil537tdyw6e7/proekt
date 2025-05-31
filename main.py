#!/usr/bin/python

from telebot import types
from datetime import datetime, timedelta
import threading
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import random
import os
import io
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
from PIL import Image
import io
import logging
from queue import Queue
import zipfile
from datetime import timedelta
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
import logging

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    image_paths = ["images/4.jpg", "images/24.jpg", "images/25.jpg", "images/26.jpg", "images/27.jpg"]  # список картинок
    selected_image = random.choice(image_paths)  # выбираем случайную картинку

    with open(selected_image, "rb") as f:
        bot.send_photo(
            message.chat.id, 
            f,
            caption= "Привет! Я бот.\
Я буду присылать тебе домашнее задание по твоей команде.\
если хочешь ознокомиться с моими командами напиши /help!"
        )           


@bot.message_handler(commands=['hello']) 
def send_bye(message):
    image_paths = ["images/1.jpg", "images/16.jpg", "images/17.jpg", "images/18.jpg", "images/19.jpg"]  # список картинок
    selected_image = random.choice(image_paths)  # выбираем случайную картинку

    with open(selected_image, "rb") as f:
        bot.send_photo(
            message.chat.id, 
            f,
            caption= "привет, как твои дела?"
        )           

@bot.message_handler(commands=['bye'])
def send_bye(message):
    image_paths = ["images/12.jpg", "images/2.jpg", "images/13.jpg"]  # список картинок
    selected_image = random.choice(image_paths)  # выбираем случайную картинку

    with open(selected_image, "rb") as f:
        bot.send_photo(
            message.chat.id, 
            f,
            caption="До скорой встречи!"
        )
        
@bot.message_handler(commands=['g'])
def send_welcome(message):
    bot.send_message(message.chat.id, message.text.replace('/g ', ''))
    bot.delete_message(message.chat.id, message.id)

    
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    if message.json['new_chat_participant']['id'] == 7742495416:
        bot.send_message(message.chat.id, "всем привет,\
я бот, который предоставляет вам дополнительные возможности в чате.\
чтобы получше о них узнать, заходите на сайт -     или напишите команду /help\
             ")

@bot.message_handler(commands=['help'])
def send_bye(message):
    image_paths = ["images/3.jpg", "images/20.jpg", "images/21.jpg", "images/22.jpg", "images/23.jpg"]  # список картинок
    selected_image = random.choice(image_paths)  # выбираем случайную картинку

    with open(selected_image, "rb") as f:
        bot.send_photo(
            message.chat.id, 
            f,
            caption= "мой функционал:\
\n\n /hello\
\n /bye\
\n     "
        ) 

@bot.message_handler(commands=['sayt'])
def send_bye(message):
    image_paths = ["images/28.png", "images/29.jpg", "images/30.jpg", "images/31.jpg", "images/5.jpg"]  # список картинок
    selected_image = random.choice(image_paths)  # выбираем случайную картинку

    with open(selected_image, "rb") as f:
        bot.send_photo(
            message.chat.id, 
            f,
            caption= "если хочешь записать свои мысли то тебе поможет мой сайт - http://127.0.0.1:5000"
        ) 


hug_images = [
    "images/6.jpg",
    "images/32.jpg",
    "images/33.jpg",
    "images/34.jpg",
    "images/35.jpg"
    # Добавьте или уберите пути по своему желанию
]

@bot.message_handler(func=lambda msg: msg.reply_to_message is not None and 'обнять' in msg.text.lower())
def hug_reply(message):
    replied_user = message.reply_to_message.from_user.first_name
    current_user = message.from_user.first_name
    
    # Текст ответа
    text_response = f"{current_user} обнял(-а) {replied_user} 🤗"
    
    try:
        # Случайный выбор изображения из заданного списка
        selected_image = random.choice(hug_images)
        
        with open(selected_image, "rb") as f:
            bot.send_photo(
                message.chat.id,
                telebot.types.InputFile(f),
                caption=text_response
            )
    except Exception as e:
        print(f"Ошибка при отправке изображения: {e}")
        bot.reply_to(message, text_response)

# Укажите здесь конкретные изображения, которые хотите использовать
rt_images = [
    "images/36.jpg",
    "images/37.jpg",
    "images/38.jpg",
    "images/39.jpg",
    "images/7.jpg"
    # Добавьте или уберите пути по своему желанию
]

@bot.message_handler(func=lambda msg: msg.reply_to_message is not None and 'ударить' in msg.text.lower())
def hug_reply(message):
    replied_user = message.reply_to_message.from_user.first_name
    current_user = message.from_user.first_name
    
    # Текст ответа
    text_response = f"👊 {current_user} ударил(-а) {replied_user} "
    
    try:
        # Случайный выбор изображения из заданного списка
        selected_image = random.choice(rt_images)
        
        with open(selected_image, "rb") as f:
            bot.send_photo(
                message.chat.id,
                telebot.types.InputFile(f),
                caption=text_response
            )
    except Exception as e:
        print(f"Ошибка при отправке изображения: {e}")
        bot.reply_to(message, text_response)

# Укажите здесь конкретные изображения, которые хотите использовать
re_images = [
    "images/11.jpg",
    "images/52.jpg",
    "images/53.jpg",
    "images/54.jpg",
    "images/55.jpg"
    # Добавьте или уберите пути по своему желанию
]

@bot.message_handler(func=lambda msg: msg.reply_to_message is not None and 'убить' in msg.text.lower())
def hug_reply(message):
    replied_user = message.reply_to_message.from_user.first_name
    current_user = message.from_user.first_name
    
    # Текст ответа
    text_response = f"🔪 {current_user} убил(-а) {replied_user}"
    
    try:
        # Случайный выбор изображения из заданного списка
        selected_image = random.choice(re_images)
        
        with open(selected_image, "rb") as f:
            bot.send_photo(
                message.chat.id,
                telebot.types.InputFile(f),
                caption=text_response
            )
    except Exception as e:
        print(f"Ошибка при отправке изображения: {e}")
        bot.reply_to(message, text_response)

# Укажите здесь конкретные изображения, которые хотите использовать
oi_images = [
    "images/10.jpg",
    "images/48.jpg",
    "images/49.jpg",
    "images/50.jpg",
    "images/51.jpg"
    # Добавьте или уберите пути по своему желанию
]

@bot.message_handler(func=lambda msg: msg.reply_to_message is not None and 'тыкнуть' in msg.text.lower())
def hug_reply(message):
    replied_user = message.reply_to_message.from_user.first_name
    current_user = message.from_user.first_name
    
    # Текст ответа
    text_response = f"🥢 {current_user} тыкнул(-а) {replied_user} "
    
    try:
        # Случайный выбор изображения из заданного списка
        selected_image = random.choice(oi_images)
        
        with open(selected_image, "rb") as f:
            bot.send_photo(
                message.chat.id,
                telebot.types.InputFile(f),
                caption=text_response
            )
    except Exception as e:
        print(f"Ошибка при отправке изображения: {e}")
        bot.reply_to(message, text_response)

# Укажите здесь конкретные изображения, которые хотите использовать
gh_images = [
    "images/9.jpg",
    "images/44.jpg",
    "images/45.jpg",
    "images/46.jpg",
    "images/47.jpg"
    # Добавьте или уберите пути по своему желанию
]

@bot.message_handler(func=lambda msg: msg.reply_to_message is not None and 'взорвать' in msg.text.lower())
def hug_reply(message):
    replied_user = message.reply_to_message.from_user.first_name
    current_user = message.from_user.first_name
    
    # Текст ответа
    text_response = f"🧨 {current_user} взорвал(-а) {replied_user} "
    
    try:
        # Случайный выбор изображения из заданного списка
        selected_image = random.choice(gh_images)
        
        with open(selected_image, "rb") as f:
            bot.send_photo(
                message.chat.id,
                telebot.types.InputFile(f),
                caption=text_response
            )
    except Exception as e:
        print(f"Ошибка при отправке изображения: {e}")
        bot.reply_to(message, text_response)


# Укажите здесь конкретные изображения, которые хотите использовать
ty_images = [
    "images/8.jpg",
    "images/40.jpg",
    "images/41.jpg",
    "images/42.jpg",
    "images/43.jpg"
    # Добавьте или уберите пути по своему желанию
]

@bot.message_handler(func=lambda msg: msg.reply_to_message is not None and 'улететь' in msg.text.lower())
def hug_reply(message):
    replied_user = message.reply_to_message.from_user.first_name
    current_user = message.from_user.first_name
    
    # Текст ответа
    text_response = f"🛬 {current_user} улетел(-а) без {replied_user} "
    
    try:
        # Случайный выбор изображения из заданного списка
        selected_image = random.choice(ty_images)
        
        with open(selected_image, "rb") as f:
            bot.send_photo(
                message.chat.id,
                telebot.types.InputFile(f),
                caption=text_response
            )
    except Exception as e:
        print(f"Ошибка при отправке изображения: {e}")
        bot.reply_to(message, text_response)

marriages = {}  # user_id: spouse_id
pending_proposals = {}  # target_id: (proposer_id, message_info)


@bot.message_handler(func=lambda msg: msg.reply_to_message is not None and 'брак' in msg.text.lower())
def marry(message):
    proposer_id = message.from_user.id

    if not message.reply_to_message:
        bot.reply_to(message, "💬 Используй брак в ответ на сообщение пользователя.")
        return

    target = message.reply_to_message.from_user
    target_id = target.id

    if proposer_id == target_id:
        bot.reply_to(message, "🤨 Ты не можешь пожениться с самим собой.")
        return

    if proposer_id in marriages:
        bot.reply_to(message, "❗ Ты уже в браке.")
        return

    if target_id in marriages:
        bot.reply_to(message, "❗ Этот пользователь уже в браке.")
        return

    if target_id in pending_proposals:
        bot.reply_to(message, "❗ Этому пользователю уже сделали предложение.")
        return

    # Создание кнопок
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("♥️", callback_data=f"accept_{target_id}"),
        InlineKeyboardButton("💔", callback_data=f"decline_{target_id}")
    )

    sent = bot.send_message(
        message.chat.id,
        f"💍 {message.from_user.first_name} сделал(а) предложение руки и сердца {target.first_name}!\
\n• согласиться - ❤️\
\n• отказаться - 💔",
        reply_markup=markup
    )

    # Сохраняем предложение и запускаем таймер на автоотказ
    pending_proposals[target_id] = (proposer_id, (sent.chat.id, sent.message_id))
    threading.Thread(target=auto_decline, args=(target_id,), daemon=True).start()


def auto_decline(target_id):
    time.sleep(3600)  # 1 час = 3600 секунд
    if target_id in pending_proposals:
        proposer_id, (chat_id, msg_id) = pending_proposals.pop(target_id)
        bot.edit_message_text(
            f"⌛ Предложение истекло. Пользователь <a href='tg://user?id={target_id}'>не ответил</a>.",
            chat_id=chat_id,
            message_id=msg_id,
            parse_mode='HTML'
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith('accept_') or call.data.startswith('decline_'))
def handle_proposal_response(call):
    action, target_id_str = call.data.split("_", 1)
    target_id = int(target_id_str)

    if call.from_user.id != target_id:
        bot.answer_callback_query(call.id, "❌ Это предложение не для тебя.")
        return

    if target_id not in pending_proposals:
        bot.answer_callback_query(call.id, "❗ Предложение уже обработано.")
        return

    proposer_id, (chat_id, msg_id) = pending_proposals.pop(target_id)

    if action == "accept":
        marriages[proposer_id] = target_id
        marriages[target_id] = proposer_id

        bot.edit_message_text(
            f"🎉 <a href='tg://user?id={target_id}'>пользователь</a> и <a href='tg://user?id={proposer_id}'>пользователь</a> теперь в браке!",
            chat_id=chat_id,
            message_id=msg_id,
            parse_mode='HTML'
        )
    elif action == "decline":
        bot.edit_message_text(
            f"💔 <a href='tg://user?id={target_id}'>пользователь</a> отказал(а) <a href='tg://user?id={proposer_id}'>пользователю</a> в браке.",
            chat_id=chat_id,
            message_id=msg_id,
            parse_mode='HTML'
        )


@bot.message_handler(func=lambda msg: msg.reply_to_message is not None and 'ра' in msg.text.lower())
def handle_divorce(message):
    user_id = message.from_user.id

    if user_id not in marriages:
        bot.reply_to(message, "❗ Ты не в браке.")
        return

    spouse_id = marriages.pop(user_id)
    marriages.pop(spouse_id, None)

    try:
        user_info = bot.get_chat(user_id)
        spouse_info = bot.get_chat(spouse_id)

        user_tag = f"<a href='tg://user?id={user_id}'>@{user_info.username}</a>" if user_info.username else f"<a href='tg://user?id={user_id}'>{user_info.first_name}</a>"
        spouse_tag = f"<a href='tg://user?id={spouse_id}'>@{spouse_info.username}</a>" if spouse_info.username else f"<a href='tg://user?id={spouse_id}'>{spouse_info.first_name}</a>"

        text = f"💔 {user_tag} развёлся(лась) с {spouse_tag}."
    except:
        text = f"💔 <a href='tg://user?id={user_id}'>Пользователь</a> развёлся(лась) с <a href='tg://user?id={spouse_id}'>пользователем</a>."

    bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(commands=['браки'])
def list_marriages(message):
    if not marriages:
        bot.reply_to(message, "📭 Пока нет ни одного брака.")
        return

    @bot.message_handler(commands=['marriages'])
    def handle_marriages(message):
        if not marriages:
            bot.send_message(message.chat.id, "📭 Пока нет ни одного брака.")
        return

    listed = set()
    result = "💖 <b>Список браков:</b>\n"

    for user_id, spouse_id in marriages.items():
        if user_id in listed or spouse_id in listed:
            continue

        try:
            user = bot.get_chat(user_id)
            spouse = bot.get_chat(spouse_id)

            user_name = user.first_name
            spouse_name = spouse.first_name

            result += (
                f"• <a href='tg://user?id={user_id}'>{user_name}</a> ❤️ "
                f"<a href='tg://user?id={spouse_id}'>{spouse_name}</a>\n"
            )

        except Exception:
            # если не удалось получить имя (например, пользователь заблокировал бота)
            result += (
                f"• <a href='tg://user?id={user_id}'>пользователь</a> ❤️ "
                f"<a href='tg://user?id={spouse_id}'>пользователь</a>\n"
            )

        listed.add(user_id)
        listed.add(spouse_id)

    bot.send_message(
        message.chat.id,
        result,
        parse_mode='HTML'
    )

# Загрузка модели
model = tf.keras.models.load_model("C:/Users/snv-a/Desktop/проект/keras_model.h5", compile=False)

# Загрузка меток классов
class_names = open("labels.txt", "r", -1, 'utf-8').readlines()
print(class_names)

def predict_image(image_data):
    # Преобразование байтового массива в изображение
    image = Image.open(io.BytesIO(image_data)).convert("RGB")

    # Масштабирование изображения до 224x224
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Преобразование изображения в массив NumPy
    image_array = np.asarray(image)

    # Нормализация изображения
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Создание массива для подачи в модель
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Прогнозирование модели
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:], confidence_score

@bot.message_handler(content_types=['photo','text'])
def process_photo(message):
    if message.caption == "фото":
        # Получаем последнее отправленное изображение
        file_info = bot.get_file(message.photo[0].file_id)
        img_bytes = bot.download_file(file_info.file_path)

        # Прогнозируем класс изображения
        class_name, confidence_score = predict_image(img_bytes)

        # Формируем ответное сообщение
        response = f"Class: {class_name}\nConfidence Score: {confidence_score:.2f}"
        # Отправляем ответ пользователю
        if confidence_score > 0.70 and class_name != None:
            bot.reply_to(message, "Это " + class_name + response)
        else:
            bot.reply_to(message, "Не удалось распознать объект на изображении либо я его не знаю. Попробуйте прислать другой снимок.")

# Словарь для хранения замученных пользователей
muted_users = {}  # chat_id: {user_id: (until_datetime, username)}

# ✅ /mute — замутить пользователя
@bot.message_handler(commands=['mute'])
def mute_user(message):
    if not message.reply_to_message:
        bot.reply_to(message, "❗ Используй /mute в ответ на сообщение.")
        return

    try:
        args = message.text.split()
        mute_minutes = int(args[1]) if len(args) > 1 else 5
    except:
        bot.reply_to(message, "⚠️ Укажи время в минутах. Пример: /mute 10", parse_mode="Markdown")
        return

    user = message.reply_to_message.from_user
    chat_id = message.chat.id
    until_date = datetime.now() + timedelta(minutes=mute_minutes)

    try:
        bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user.id,
            permissions=types.ChatPermissions(can_send_messages=False),
            until_date=until_date
        )

        if chat_id not in muted_users:
            muted_users[chat_id] = {}
        muted_users[chat_id][user.id] = (until_date, user.full_name)

        bot.reply_to(message, f"🔇 {user.full_name} замучен на {mute_minutes} мин.")
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {e}")

# ✅ /unmute — размутить пользователя
@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    if not message.reply_to_message:
        bot.reply_to(message, "❗ Используй /unmute в ответ на сообщение.")
        return

    user = message.reply_to_message.from_user
    chat_id = message.chat.id

    try:
        bot.restrict_chat_member(
            chat_id=chat_id,
            user_id=user.id,
            permissions=types.ChatPermissions(can_send_messages=True)
        )

        if chat_id in muted_users and user.id in muted_users[chat_id]:
            muted_users[chat_id].pop(user.id)

        bot.reply_to(message, f"🔈 {user.full_name} размучен.")
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {e}")

# ✅ /mutelist — показать всех замученных
@bot.message_handler(commands=['mutelist'])
def show_muted_list(message):
    chat_id = message.chat.id
    now = datetime.now()

    if chat_id not in muted_users or not muted_users[chat_id]:
        bot.reply_to(message, "📭 Нет замученных пользователей.")
        return

    text = "📃 Замученные пользователи:\n\n"
    for user_id, (until, name) in muted_users[chat_id].items():
        remaining = until - now
        if remaining.total_seconds() <= 0:
            continue
        minutes = int(remaining.total_seconds() / 60)
        text += f"• {name} — до {until.strftime('%H:%M:%S')} ({minutes} мин)\n"

    bot.send_message(chat_id, text)

# Структура хранения: {chat_id: {user_id: уровень}}
moderators = {}

# Проверка, является ли пользователь админом
def is_admin(chat_id, user_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ['administrator', 'creator']
    except:
        return False

# Проверка уровня модерации
def get_mod_level(chat_id, user_id):
    return moderators.get(chat_id, {}).get(user_id)

# Проверка, является ли пользователь модератором с уровнем 1 или выше
def is_mod(chat_id, user_id, level=1):
    return get_mod_level(chat_id, user_id) is not None and get_mod_level(chat_id, user_id) >= level

# ✅ Команда +модер1 или +модер2 — назначение модератора с уровнем
@bot.message_handler(func=lambda msg: msg.text.lower() in ['+модер1', '+модер2'])
def assign_mod(message):
    if not message.reply_to_message:
        bot.reply_to(message, "⛔ Используй команду в ответ на сообщение пользователя.")
        return

    chat_id = message.chat.id
    from_id = message.from_user.id

    if not is_admin(chat_id, from_id):
        bot.reply_to(message, "⛔ Только администратор может назначать модераторов.")
        return

    level = 2 if message.text.lower() == '+модер2' else 1
    target = message.reply_to_message.from_user

    if chat_id not in moderators:
        moderators[chat_id] = {}

    moderators[chat_id][target.id] = level
    bot.reply_to(message, f"✅ {target.first_name} назначен модератором уровня {level}.")

# ❌ Снять модератора
@bot.message_handler(func=lambda msg: msg.text.lower() == '-модер')
def remove_mod(message):
    if not message.reply_to_message:
        bot.reply_to(message, "⛔ Используй -модер в ответ на сообщение пользователя.")
        return

    chat_id = message.chat.id
    from_id = message.from_user.id

    if not is_admin(chat_id, from_id):
        bot.reply_to(message, "⛔ Только администратор может снять модератора.")
        return

    target = message.reply_to_message.from_user

    if chat_id in moderators and target.id in moderators[chat_id]:
        del moderators[chat_id][target.id]
        bot.reply_to(message, f"❌ {target.first_name} больше не модератор.")
    else:
        bot.reply_to(message, "ℹ️ Этот пользователь не является модератором.")

# 📋 Список модераторов
@bot.message_handler(commands=['modlist'])
def list_mods(message):
    chat_id = message.chat.id
    if chat_id not in moderators or not moderators[chat_id]:
        bot.reply_to(message, "📭 Модераторы не назначены.")
        return

    mod_text = "📋 *Список модераторов:*\n"
    for user_id, level in moderators[chat_id].items():
        try:
            user = bot.get_chat_member(chat_id, user_id).user
            mod_text += f"• {user.first_name} — уровень {level}\n"
        except:
            mod_text += f"• [неизвестный пользователь] — уровень {level}\n"

    bot.send_message(chat_id, mod_text, parse_mode='Markdown')

try:
    bot.polling()
except Exception as e:
    print (e)
