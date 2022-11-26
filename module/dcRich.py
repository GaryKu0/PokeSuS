from pypresence import Presence 
import time
import threading
from module.var import *
start = int(time.time())
client_id = "695279575143546900"
RPC = Presence(client_id)
RPC.connect()

def DiscordRichPresence():
    print("[INFO] 📢 Discord Rich Presence is running")
    global game_running
    while game_running: 
        print("Game Running",game_running)
        RPC.update(
            large_image = "pokesus", #name of your asset
            large_text = "Game created by: @Albus Dumbledore#0301",
            details = "Exploring the world of Pokesus",
            #state = "",
            start = start,
            buttons = [{"label": "View it on Github!", "url": "https://github.com/GaryKu0/NKUST/tree/main/2022/code/2022MidTerm"}, {"label": "🥑 Avocado CSS", "url": "https://id0x.ga"}] #up to 2 buttons
        )
        time.sleep(1)

