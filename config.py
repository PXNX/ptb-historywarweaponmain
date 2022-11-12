import os

# Railway and Heroku need that, to assign the proper webhook
PORT = os.getenv("PORT")

# This has to be the ID or public username of your channel
CHANNEL= -1001205641526

# Replace it with whatever footer you want to append to your messages
FOOTER="\n\n🪖Война История Оружие\n<a href='https://t.me/historywarweaponmain'>Подписаться на канал</a>"

# if you test it locally, you can just do something like TOKEN="123abc--replace-this-with-what-@botfather-sent-you!"
TOKEN= os.getenv("TOKEN")

# To let the bot run on your local machine, maybe in PyCharm, set to True.
TEST_MODE = True