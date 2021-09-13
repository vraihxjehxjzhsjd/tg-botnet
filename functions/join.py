from telethon import functions
from alive_progress import alive_bar
import time

class group:
    def __init__(self, clients):
        self.clients = clients
    def join(self):
        chat_id = 0
        link = input("\033[91mgroup\033[39m: ")
        delay = float(input("\033[91mdelay\033[39m: "))
        with alive_bar(len(self.clients), title = "Bots joining"):
            for client in self.clients:
                try:
                    client.connect()
                    if link[:1] == "@":
                        chat = client.get_entity(link[1:])
                        client(functions.channels.JoinChannelRequest(chat.id))
                        chat_id = (1000000000000 + chat.id) * -1
                    try:
                        if link[:13] == "https://t.me/":
                            chat = client.get_entity(link[13:])
                            client(functions.channels.JoinChannelRequest(chat.id))
                            chat_id = (1000000000000 + chat.id) * -1
                    except:
                        pass
                    if link[13:22] == "joinchat/":
                        chat = client(functions.messages.ImportChatInviteRequest(link[:22])
                        chat_id = -1 * chat.updates[1].participants.chat_id
                    del client
                except:
                    pass
                bar()
                time.sleep(delay)
                
