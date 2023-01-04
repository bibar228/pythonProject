import time
import telebot
from auth_data import token
import os.path

bot = telebot.TeleBot(token)
id_channel = "@PRONLIFE1"


@bot.message_handler(content_types=["text"])
def commands(message):
    while True:
        if message.text == "start":
            with open("videos.txt", "r", encoding="UTF-8") as file:
                for i in file.readlines():
                    with open("zapis.txt", "r", encoding="UTF-8") as d:
                        if i not in d.readlines():
                            try:
                                if os.path.getsize(f"D:\\видос\\{i[:-1]}") < 52428700:
                                    bot.send_video(id_channel, open(f"D:\\видос\\{i[:-1]}", "rb"))

                                    with open("zapis.txt", "a+", encoding="UTF-8") as mobi:
                                        mobi.write(i)
                                    time.sleep(5)
                                    print("all good")
                                    print(i, os.path.getsize(f"D:\\видос\\{i[:-1]}"))
                                    print("all good")
                            except Exception as e:
                                print(e)
                                print(i, os.path.getsize(f"D:\\видос\\{i[:-1]}"))
                                print(e)



bot.polling(none_stop=True, timeout=2)
