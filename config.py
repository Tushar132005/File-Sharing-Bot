#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23475322"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e00e5cebf073df8baba7db34ea0ebdc9")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002187391758"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6170050819"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Umar:cappuccino@cluster0.nqpyr3r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002234404301"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello👋🏻 {mention}\n\nI am YOUTUBER KING 👑 Here to provide you the file for which you are here\n\nOUR OFFICIAL SITE:- studyocean.xyz")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6155478725 6170050819 5183776660 6928637808").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello👋🏻 {mention}\n\n<b>⚠️You need to join in my official channel😊 to get data\n\n➡️Kindly Please join Channel✅‼️\n\n⭕️And Click on try again or go on post link again✅⭐️\n\nThankyou😊\n\n⭐️YOUTUBE KING™~</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "False" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

from os import environ

API = environ.get("API", "5a46477839bb186f9d168d34295a0db50eae2f05") # shortlink api
URL = environ.get("URL", "Vipurl.in") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "") # bot username without @
VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Bhratashree 😊!!\n\n➡️Aap humare owner nahi hai kripya yaha msg naa kre ye bot sirf owner ki sunta hai kuch puchna hai to iss username pe msg kre @YOUTUBER_KING 🙏\n\nDhanyawad!"

ADMINS.append(OWNER_ID)
ADMINS.append(6170050819)

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
