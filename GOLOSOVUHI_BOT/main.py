import telebot
import uuid
import speech_recognition as sr
import soundfile as sf
import pymysql
import random
from bot import TOKEN
import openai
from openai_key import key

language='ru_RU'
bot = telebot.TeleBot(TOKEN)
r = sr.Recognizer()
openai.api_key = key

names = {"Илья": "@JestkiyPoc", "Лось": "@biboniy", "Лакай": "@MakeMeFlySoHigh", "Вовка": "@Sum115", "Артем": "@niarpe"}


def recognise(filename):
    with sr.WavFile(filename) as source:
        recorded_audio = r.listen(source)
        print("Done recording")

    ''' Recorgnizing the Audio '''
    try:
        text = r.recognize_google(recorded_audio, language="ru-RU")
        return text

    except Exception as ex:
        return ex




dd = ["@MakeMeFlySoHigh", "@biboniy", "@Sum115", "@niarpe", "@JestkiyPoc"]

@bot.message_handler(commands=['all'])
def start_message(message):
    try:
        bot.send_message(message.chat.id, f"{' '.join(dd)} {message.text[4:]}")
    except Exception as ex:
        print(ex)

@bot.message_handler(content_types=["text"])
def text(message):
    mama = ["матухи", "мамашу", "маму", "матуху", "мамашку", "маме", "мaмe", "мама", "мамку", "mamy", "mamky", "mamku", "мамаша",
            "мother", "mama", "мaть", "мать", "мамаше", "матухе", "мамашке", "мамке", "маме", 'мaмa', 'маma', 'мamа', 'mаma', 'mamа', 'mama', 'maмa', 'mамa', 'мамa', 'мaма', 'mама', 'мama', 'маmа', 'maма', 'mаmа']
    no_mama = ["Мама это святое!", "Не трогай маму, паскуда!", "Not trogat` mother plz", "Надеюсь ты подумаешь над своим поведеним и больше не будешь упоминать мамулечку в суе, паскуда тварь!", "ЕБАЛО НА НОЛЬ, ПАДЛА, ЗА МАМУ ВИЕБУ", "Еще раз про маму и пиздец тебе, понял?"]
    check = ['маме', 'mаме', 'мamе', 'mамe', 'maме', 'мамe', 'маmе', 'mame', 'mаme', 'мaмe', 'маme', 'мame', 'mаmе', 'maмe', 'мaме', 'mamе', 'мамk', 'мamк', 'maмk', 'maмк', 'маmк', 'мамк', 'маmk', 'мaмk', 'mаmк', 'мamk', 'mаmk', 'mамк', 'mamk', 'мaмк', 'mамk', 'mamк', 'mатy', 'мaту', 'mату', 'мaтy', 'мату', 'матy', 'maту', 'maтy', 'мaма', 'mаmа', 'maма', 'маmа', 'мamа', 'mama', 'mамa', 'мaмa', 'mamа', 'мамa', 'мама', 'маma', 'maмa', 'mаma', 'мama', 'mама']
    try:
        text = "".join([i.lower() for i in message.text])

        for i in text.split():
            if i in mama or i[:4] in check:
                if message.from_user.username == "niarpe":
                    bot.send_message(message.chat.id, f"@niarpe {random.choice(no_mama)}")
                elif message.from_user.username == "Sum115":
                    bot.send_message(message.chat.id, f"@Sum115 {random.choice(no_mama)}")
                elif message.from_user.username == "MakeMeFlySoHigh":
                    bot.send_message(message.chat.id, f"@MakeMeFlySoHigh {random.choice(no_mama)}")

        mess = message.text.split()

        if mess[0] == "@GOLOSOVUHI_PITA_bot":
            if mess[1] in ["скажи", "Скажи", "Передай", "передай"]:
                if mess[2] in ["Вовке", "вовке", "вове", "Вове", "Вофке", "вофке", "Вовке,", "вовке,", "вове,",
                                   "Вове,", "Вофке,", "вофке,"]:
                    bot.send_message(message.chat.id,
                                         f"@Sum115 вам просили передать, что вы {' '.join(message.text.split()[5:])}")
                elif mess[2] in ["Лосю", "Лосю,", "лосю", "лосю,"]:
                    bot.send_message(message.chat.id,
                                         f"@bibak228 вам просили передать, что вы {' '.join(message.text.split()[5:])}")
                elif mess[2] in ["Илье", "Илье,", "илье", "илье,", "Ексиже", "ексиже", "ексиже,", "Ексиже,"]:
                    bot.send_message(message.chat.id,
                                         f"@JestkiyPoc вам просили передать, что вы {' '.join(message.text.split()[5:])}")
                elif mess[2] in ["Лакаю", "Лакаю,", "лакаю", "лакаю,", "Сосиске", "Сосиске,", "сосиске",
                                     "сосиске,"]:
                    bot.send_message(message.chat.id,
                                         f"@MakeMeFlySoHigh вам просили передать, что вы {' '.join(message.text.split()[5:])}")
                elif mess[2] in ["Питу", "Питу,", "питу", "питу,", "Артему", "Артему,", "артему", "артему,"]:
                    bot.send_message(message.chat.id,
                                         f"@niarpe вам просили передать, что вы {' '.join(message.text.split()[5:])}")
                else:
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=message.text,
                        temperature=0.9,
                        max_tokens=1000,
                        top_p=1.0,
                        frequency_penalty=0.0,
                        presence_penalty=0.6,
                        stop=["You:"]
                    )
                    bot.send_message(message.chat.id,
                                         f"@{message.from_user.username} {response['choices'][0]['text']}")
            else:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=message.text,
                    temperature=0.9,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.6,
                    stop=["You:"]
                )
                bot.send_message(message.chat.id, f"@{message.from_user.username} {response['choices'][0]['text']}")

    except Exception as ex:
        print(ex)



    with open("chat.txt", "a+", encoding="UTF-8") as file:
        chat_info = bot.get_chat(message.chat.id).title
        file.write(f"{chat_info} --- {message.from_user.first_name}: {message.text}")
        file.write("\n")
        try:
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='warlight123',
                                         database='telega_db',
                                         cursorclass=pymysql.cursors.DictCursor)
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM `group_table`")
                    d = cursor.fetchall()
                    if chat_info not in [i["group_name"] for i in d]:
                        insert_query = "INSERT INTO `group_table` (group_name) VALUES (%s)"
                        cursor.execute(insert_query, (chat_info))
                        connection.commit()

                    cursor.execute("SELECT * FROM `nick_name`")
                    names = cursor.fetchall()
                    if message.from_user.first_name not in [i["nick_name"] for i in names]:
                        insert_query = "INSERT INTO `nick_name` (nick_name) VALUES (%s)"
                        cursor.execute(insert_query, (message.from_user.first_name))
                        connection.commit()

                    cursor.execute("SELECT * FROM `group_table`")
                    d = [i["group_name"] for i in cursor.fetchall()]
                    cursor.execute("SELECT * FROM `nick_name` ORDER BY nick_name_id")
                    names = [i["nick_name"] for i in cursor.fetchall()]
                    val = ((d.index(chat_info) + 1, names.index(message.from_user.first_name) + 1, message.text))

                    insert_query = "INSERT INTO `osnova` (group_id, nick_name_id, message_text) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, val)
                    connection.commit()
            finally:
                connection.close()
        except Exception as ex:
            print(ex)

@bot.message_handler(content_types=["photo"])
def photo(message):
    try:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        filename = str(uuid.uuid4()) + ".jpg"
        with open(filename, 'wb') as new_file:
            new_file.write(downloaded_file)
        print("get photo")

        chat_info = bot.get_chat(message.chat.id).title

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='warlight123',
                                     database='telega_db',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM `group_table`")
                d = cursor.fetchall()
                if chat_info not in [i["group_name"] for i in d]:
                    insert_query = "INSERT INTO `group_table` (group_name) VALUES (%s)"
                    cursor.execute(insert_query, (chat_info))
                    connection.commit()

                cursor.execute("SELECT * FROM `nick_name`")
                names = cursor.fetchall()
                if message.from_user.first_name not in [i["nick_name"] for i in names]:
                    insert_query = "INSERT INTO `nick_name` (nick_name) VALUES (%s)"
                    cursor.execute(insert_query, (message.from_user.first_name))
                    connection.commit()

                cursor.execute("SELECT * FROM `group_table`")
                d = [i["group_name"] for i in cursor.fetchall()]
                cursor.execute("SELECT * FROM `nick_name` ORDER BY nick_name_id")
                names = [i["nick_name"] for i in cursor.fetchall()]
                val = ((d.index(chat_info) + 1, names.index(message.from_user.first_name) + 1, filename))

                insert_query = "INSERT INTO `osnova` (group_id, nick_name_id, photo) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, val)
                connection.commit()

        finally:
            connection.close()
    except Exception as ex:
        print(ex)


@bot.message_handler(content_types=["video"])
def photo(message):
    try:
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        filename = str(uuid.uuid4()) + ".mp4"
        with open(filename, 'wb') as new_file:
            new_file.write(downloaded_file)
        print("get video")

        chat_info = bot.get_chat(message.chat.id).title

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='warlight123',
                                     database='telega_db',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM `group_table`")
                d = cursor.fetchall()
                if chat_info not in [i["group_name"] for i in d]:
                    insert_query = "INSERT INTO `group_table` (group_name) VALUES (%s)"
                    cursor.execute(insert_query, (chat_info))
                    connection.commit()

                cursor.execute("SELECT * FROM `nick_name`")
                names = cursor.fetchall()
                if message.from_user.first_name not in [i["nick_name"] for i in names]:
                    insert_query = "INSERT INTO `nick_name` (nick_name) VALUES (%s)"
                    cursor.execute(insert_query, (message.from_user.first_name))
                    connection.commit()

                cursor.execute("SELECT * FROM `group_table`")
                d = [i["group_name"] for i in cursor.fetchall()]
                cursor.execute("SELECT * FROM `nick_name` ORDER BY nick_name_id")
                names = [i["nick_name"] for i in cursor.fetchall()]
                val = ((d.index(chat_info) + 1, names.index(message.from_user.first_name) + 1, filename))

                insert_query = "INSERT INTO `osnova` (group_id, nick_name_id, video) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, val)
                connection.commit()

        finally:
            connection.close()
    except Exception as ex:
        print(ex)


@bot.message_handler(content_types=['video_note'])
def photo(message):
    try:
        file_info = bot.get_file(message.video_note.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        filename = str(uuid.uuid4()) + ".mp4"
        with open(filename, 'wb') as new_file:
            new_file.write(downloaded_file)
        print("get circle")

        chat_info = bot.get_chat(message.chat.id).title

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='warlight123',
                                     database='telega_db',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM `group_table`")
                d = cursor.fetchall()
                if chat_info not in [i["group_name"] for i in d]:
                    insert_query = "INSERT INTO `group_table` (group_name) VALUES (%s)"
                    cursor.execute(insert_query, (chat_info))
                    connection.commit()

                cursor.execute("SELECT * FROM `nick_name`")
                names = cursor.fetchall()
                if message.from_user.first_name not in [i["nick_name"] for i in names]:
                    insert_query = "INSERT INTO `nick_name` (nick_name) VALUES (%s)"
                    cursor.execute(insert_query, (message.from_user.first_name))
                    connection.commit()

                cursor.execute("SELECT * FROM `group_table`")
                d = [i["group_name"] for i in cursor.fetchall()]
                cursor.execute("SELECT * FROM `nick_name` ORDER BY nick_name_id")
                names = [i["nick_name"] for i in cursor.fetchall()]
                val = ((d.index(chat_info) + 1, names.index(message.from_user.first_name) + 1, filename))

                insert_query = "INSERT INTO `osnova` (group_id, nick_name_id, video) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, val)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)


@bot.message_handler(content_types=["voice"])
def text(message):
    try:
        filename = str(uuid.uuid4()) + ".ogg"
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(filename, 'wb') as new_file:
            new_file.write(downloaded_file)

        data, samplerate = sf.read(filename)
        sf.write('new_file.wav', data, samplerate)
        text = recognise('new_file.wav')
        count = 0

        text = "".join([i.lower() for i in text])

        for i, j in names.items():
            if i.lower() in text:
                bot.send_message(message.chat.id, f"{j} {text}")
                count += 1
        if count == 0:
            bot.send_message(message.chat.id, text)
    except Exception as e:
        bot.send_message(message.chat.id, "Что-то непереводимое")




bot.polling()