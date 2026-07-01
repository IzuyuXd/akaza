import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/Senku/{config}", "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    # REQUIRED
    API_ID = 16136051
    API_HASH = "0f558cfd8541ededbd14e0b22768af5d"
    BOT_TOKEN = "8692160358:AAGhX1lZIEHwi7eYNMIBRDNBPx57kPe6bN4"
    OWNER_ID = 7200052671
    OWNER_USERNAME = "Izuyw"
    SUPPORT_CHAT = "BotSupportGc"
    LOG_CHANNEL = -1004424123752

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    SPAMWATCH_SUPPORT_CHAT = "@BotSupportGc"

    # OPTIONAL
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 8
    ALLOW_EXCL = True

    CASH_API_KEY = "awoo"
    TIME_API_KEY = "awoo"
    WALL_API = "awoo"
    AI_API_KEY = "awoo"

    BL_CHATS = []
    SPAMMERS = None
    ERROR_LOG_CHANNEL = -1001501815938

    # VPS Version (Heroku & Redis Removed)
    ARQ_API = "awoo"
    APOD_API_KEY = "awoo"

    ANIME_NAME = "Demon Slayer"
    START_MEDIA = "https://i.ibb.co/Sjj4Jw5/tmpzyrteemm.jpg"

    BOT_USERNAME = "AkazaProbot"
    UPDATE_CHANNEL = "BotLogsX"
    ALIVE_MEDIA = "https://i.ibb.co/tTPyXKYf/tmpm84g0mdh.jpg"
    BOT_ID = 5169508699

    STATS_IMG = "https://i.ibb.co/mjV4LY7/tmpzssniy4z.jpg"
    NETWORK_USERNAME = "TeamXAssociation"
    NETWORK = "T-X"

    INLINE_IMG = "https://i.ibb.co/mjV4LY7/tmpzssniy4z.jpg"
    API_WEATHER = "awoo"

    OWNER_WELCOME_MEDIA = "https://i.ibb.co/mjV4LY7/tmpzssniy4z.jpg"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True