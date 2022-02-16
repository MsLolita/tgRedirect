import datetime, time

import tgcrypto
from pyrogram import Client, filters

chatIdDonor = [-1001669121688, -1001656259847]
to = -1001547629672

PHONE_NUMBER = "+6281338436161"

app = Client("privateRedirect", phone_number = PHONE_NUMBER)

@app.on_message(filters.chat(chatIdDonor))
def takeSignal(client, message):
    time.sleep(59)
    postText = message["text"]
    a = message.copy(to)
    print(a["text"])

if __name__ == "__main__":
    print("Start!")
    
    app.run()
