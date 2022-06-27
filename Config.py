import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCaSD6z-oVbzRv1P6-vWjag7XTmgOkqxZtVvNstFyGUFDBA3HXOTPiJeE4Cs0q09OEFCstHgjWKpSq4Ux2hcMZOq48ET3YtZQXLEFY8tbLK6a_rfY1-wzBPYIErTzN7jWXu5CnInAmc54Kqx18gRlDn6XN1plYAVjzkySo5TcwrReF8CBQBQf8UNUzWfz3HLsEnErXk3QMgCiOpgwTNVpLx1BHHgHaoFLon6pcfd8cVjVM1H3iejEQVZh_LI7LVFOSTRJXtzTd7a9_A5D1ffakZhEAds5VB9x989C1Jp8F_u-nIKslQy2KuaOMqwPHzYBZs8oeNNSr1A_iVPhALAf84AAAAATmE0UUArQvoAJc3md9JA8Jcu8gXA2YWIq-WymfJaXbzpk_dZX88Ctq74u-5dOi-CVrht7MW1lqld0Zeh3ZeaXDJ6hIDxOOVo7V0PKLimRhjviCm5LfJi7ePF_dVKAGV4jWHpSeZw_3mz4QCIoTaQJcSErdAX1aiQGe3BunmD4HBwPsdbdGVpjLTisdfpOL63u5l_W8RHAAAAATmE0UUA")
BOT_TOKEN = getenv("BOT_TOKEN", "2003043761:AAENygNigPbaFxmcL4O67LyGNESBzvjSZ1M")
BOT_NAME = getenv("BOT_NAME", "chucky_music")
API_ID = int(getenv("API_ID", "7648375"))
API_HASH = getenv("API_HASH", "c7faa5774e20217bdef0f56f339152a4")
OWNER_NAME = getenv("OWNER_NAME", "kittu")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Kittu_the_criminalll")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐂𝐇𝐔𝐂𝐊𝐘 𝐌𝐔𝐒𝐈𝐂")
BOT_USERNAME = getenv("BOT_USERNAME", "Chuckymusic_bot")
OWNER_ID = getenv("OWNER_ID", "5409267519")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "🇨ԋυƈƙყ 🇲☋ⓢ☿☾")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Tamilchat_teashop")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Tamilchat_teashop")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5409267519").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/78d17df4c6b89b20bd735.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/8175abf1f4b2efd119043.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/196df11d25b44b94069d6.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/196df11d25b44b94069d6.jpg")
