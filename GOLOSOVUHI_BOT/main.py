import telebot

import speech_recognition as sr
import soundfile as sf

language='ru_RU'
TOKEN='5698628232:AAHE0iZ5KDxNq6IkHXFqUHB-1seAtTqmj5M'
bot = telebot.TeleBot(TOKEN)
r = sr.Recognizer()
id = -1001423575845


names = {"Илья": "@JestkiyPoc", "Лось": "@biboniy", "Лакай": "@MakeMeFlySoHigh"}


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


@bot.message_handler(content_types=["voice"])
def text(message):

    filename = "voice" + ".ogg"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(filename, 'wb') as new_file:
        new_file.write(downloaded_file)

    data, samplerate = sf.read(filename)
    sf.write('new_file.wav', data, samplerate)
    text = recognise('new_file.wav')
    count = 0

    try:
        text = "".join([i.lower() for i in text])

        for i, j in names.items():
            if i.lower() in text:
                bot.send_message(message.chat.id, f"{j} {text}")
                count += 1
        if count == 0:
            bot.send_message(message.chat.id, text)
    except Exception:
        bot.send_message(message.chat.id, "Не могу перевести, сорян")



bot.polling()


