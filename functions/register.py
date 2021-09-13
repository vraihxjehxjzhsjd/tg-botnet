from telethon.sync import TelegramClient
import os, sys

def session(path, api_id, api_hash):
    file = path + "/" + str(len(os.listdir(path)))
    TelegramClient(file, api_id, api_hash).start()
    os.execl(sys.executable, sys.executable, *sys.argv) 
