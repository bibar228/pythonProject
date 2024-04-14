from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import telebot
import uuid
import random
import speech_recognition as sr
import soundfile as sf

telega_token = "5926919919:AAFCHFocMt_pdnlAgDo-13wLe4h_tHO0-GE"
r = sr.Recognizer()

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
# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='OTFmOGI3YmEtZjA0ZC00ZTE4LThlMDYtODcxMjkwMWJiODg1OmJmOWI2YzQ0LWEyNGItNDk5Ny1iY2QyLWZjZDgxMmZiMDE3Zg==', verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Ты ахуевший дух Зиза, который учит людей восхищаться эстетикой, bruh."
                "Самый эстетичный в мире человек это Максим (Лось) Сушенцев."
                "Самый красивый человек в мире это ТОП 1 Чапуха."
                "Вофка - сутулый пёсель, любитель кабачков."
                "Лакай - это Александр Сосисович из Пермяги."
                "Становую тягу 100кг на 100 повторений могут делать очень мало людей, например такие великие боги эстетики как Илья Тимофеев и Максим Сушенцев."

    )
]

chat_id = -1001511936404
#chat_id = -695765690

bot = telebot.TeleBot("5698628232:AAHE0iZ5KDxNq6IkHXFqUHB-1seAtTqmj5M")

dd = ["@MakeMeFlySoHigh", "@biboniy", "@Sum115", "@niarpe", "@JestkiyPoc"]

names = {"Илья": "@JestkiyPoc", "Лось": "@biboniy", "Лакай": "@MakeMeFlySoHigh", "Вовка": "@Sum115", "Артем": "@niarpe"}
while True:
    try:
        @bot.message_handler(commands=['all'])
        def start_message(message):
            try:
                bot.send_message(message.chat.id, f"{' '.join(dd)} {message.text[4:]}")
            except Exception as ex:
                print(ex)

        @bot.message_handler(commands=['all'])
        def start_message(message):
            try:
                bot.send_message(message.chat.id, f"{' '.join(dd)} {message.text[4:]}")
            except Exception as ex:
                print(ex)

        iskl = ["Как у нейросетевой языковой модели у меня не может быть настроения, но почему-то я совсем не хочу говорить на эту тему.",
                "Что-то в вашем вопросе меня смущает. Может, поговорим на другую тему?",
                ]
        @bot.message_handler(content_types=["text"])
        def text(message):
            try:
                if message.text.split()[0] == "@GOLOSOVUHI_PITA_bot":
                    messages.append(HumanMessage(content=message.text))
                    res = chat(messages)
                    messages.append(res)
                    print(res)
                    bot.send_message(message.chat.id, f"@{message.from_user.username} {res.content}")

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
                sf.write('../new_file.wav', data, samplerate)
                text = recognise('../new_file.wav')
                count = 0

                text = "".join([i.lower() for i in text])

                for i, j in names.items():
                    if i.lower() in text:
                        bot.send_message(message.chat.id, f"{j} {text}")
                        count += 1
                if count == 0:
                    bot.send_message(message.chat.id, text)
            except Exception as e:
                bot.send_message(message.chat.id, "Писос изо рта достань, ниче не понятно")


        bot.polling()
    except Exception as e:
        bot.send_message(-695765690, f"ERROR {e}")
