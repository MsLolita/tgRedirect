import datetime, time

import tgcrypto
from pyrogram import Client, filters

privateTrash = -1001656259847
privateCryptoHan = -1001669121688
floodCryptohan = -1001668134966

solyanka = -1001679804682
privateBoys = -1001547629672

PHONE_NUMBER = "+6281338436161"

app = Client("privateRedirect", phone_number = PHONE_NUMBER)

@app.on_message(filters.chat(privateTrash, privateCryptoHan))
def takeSignal(client, message):
    time.sleep(59)
    postText = message["text"]
    message.copy(privateBoys)
    
@app.on_message(filters.chat(floodCryptohan))
def takeSignal(client, message):
    time.sleep(59)
    postText = message["text"]
    message.copy(solyanka)

if __name__ == "__main__":
    print("Start!")
    
    app.run()
