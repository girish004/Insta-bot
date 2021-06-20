import os
import time
import sys
from tqdm import tqdm
sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot
bot=Bot()
bot.login(username="",password="")
print(bot.api.get_inbox_v2())
os.system("rmdir /s config")