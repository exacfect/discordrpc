import psutil
import os
from pypresence import Presence
import time
import sys
tg = time.ctime()
def is_discord_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'Discord.exe':
            return True
    return False

def close_program():
    sys.exit()

if __name__ == "__main__":
    client_id = '1122470928614424626'
    RPC = Presence(client_id)
    RPC.connect()
    RPC.update(
        details="I wish that day you didn't come.",
        state="13/04/2022",
        timestamp = tg,
        large_image="icon",
        large_text="Exacfect Logo",
        small_image="discord",
        small_text="Discord Logo",
        buttons=[
            {"label": "No Hello", "url": "https://nohello.net/"},
            {"label": "Don't Ask To Ask", "url": "https://dontasktoask.com/"}
        ]
    )
    
    while True:
        if not is_discord_running():
            close_program()
            break
        time.sleep(60)
