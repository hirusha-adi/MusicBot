import json

class BotInfo:
    with open("musicbot/database/settings/config.json", "r", encoding="utf-8") as file:
        data = json.loads(file.read())

    BOT_TOKEN = data["BOT_TOKEN"]
    BOT_PREFIX = data["BOT_PREFIX"]
    BOT_NAME = data["BOT_NAME"]
    BOT_AVATAR_URL = data["BOT_AVATAR_URL"]

    CREATOR_NAME = data["CREATOR_NAME"]

    RUN_FLASK_WEB_SERVER_DATA = data["RUN_FLASK_WEB_SERVER"]
    if str(RUN_FLASK_WEB_SERVER_DATA).lower().startswith('y'):
        RUN_FLASK_WEB_SERVER = True
    else:
        RUN_FLASK_WEB_SERVER = False


print(BotInfo.RUN_FLASK_WEB_SERVER)
