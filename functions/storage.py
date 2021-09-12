from telethon.sync import TelegramClient
import os, sys

def sessions(path="sessions", api_id, api_hash):
    files, clients = os.listdir(path), []
    for file in files:
        if file.endswith(".session-journal"):
            os.remove(os.path.join(path, file))
    files = os.listdir(path)
    for file in files:
        _file = "sessions/" + file
        clients.append(TelegramClient(_file, api_id, api_hash))
    return clients
