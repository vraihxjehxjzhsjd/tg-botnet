from telethon.sync import TelegramClient
import os, sys

def update():
    vote = input("\033[91mupdate sessions? \033[35m[y/n] \033[36m(n) \033[39m: ")
    if vote.lower() in ["y", "ye", "yes"]
        return True
    return False

def sessions(path="sessions", api_id, api_hash):
    files, clients = os.listdir(path), []
    for file in files:
        if file.endswith(".session-journal"):
            os.remove(os.path.join(path, file))
    files = os.listdir(path)
    for file in files:
        name = "sessions/" + file.split(".", maxsplit=1)[0]
        clients.append(TelegramClient(name, api_id, api_hash))
    #update = input("<red>update sessions?</red> <yellow>[y/n]</yellow> <cyan>(n)</cyan>: ")
    return clients
