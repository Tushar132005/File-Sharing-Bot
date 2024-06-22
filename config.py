#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24798261"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fef280037f5759eccc540c6d7a279a14")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002227081660"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6155478725"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://successspark09:tushar@filestore12.dnbo7vb.mongodb.net/?retryWrites=true&w=majority&appName=filestore12")
DB_NAME = os.environ.get("DATABASE_NAME", "filestore12")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001678918073"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Am 𝗛𝗞 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟™ store bot You will get here Study Material by links which will be provided in channels.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6155478725").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You need to join in my official channel to get lectures\n\nKindly Please join Channel\n\n And Click on try again or go on post link again\n\nThankyou\n\n𝗛𝗞 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟™~</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Bhratashree!!\n\nAap humare owner nahi hai kripya yaha msg naa kre ye bot sirf owner ki sunta hai kuch puchna hai to iss username pe msg kre @THEHEATHERS_BOT\n\nDhanyawad!"

ADMINS.append(OWNER_ID)
ADMINS.append(6155478725)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
