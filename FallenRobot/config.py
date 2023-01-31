class Config(object):
    LOGGER = True

    API_ID = "23890262"
    API_HASH = "da7e86cf57b0e6220b8a9e0aed228a68"
    TOKEN = "5841568185:AAFODqetoPeeBhBsXDyRVT7KIniZDnpWOY8"
    OWNER_ID = "1488316798"
    OWNER_USERNAME = "miyuki_senpai"
    SUPPORT_CHAT = "devils_chats"
    JOIN_LOGGER = (-1001868871195)
    EVENT_LOGS = (-1001868871195)

    SQLALCHEMY_DATABASE_URI = "postgres://oczrqkvk:p11ua8LdXcupAcFLF-ZjB3uBXVDdYhu4@suleiman.db.elephantsql.com/oczrqkvk"
    MONGO_DB_URI = "mongodb+srv://Hetal:HetalShah@cluster0.g8xrb.mongodb.net/?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = 
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = 
    WOLVES = 

    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = ""
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
