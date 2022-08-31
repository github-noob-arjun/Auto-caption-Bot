import os
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", 12345678))
API_HASH = os.environ.get("API_HASH", "")
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in os.environ.get('AUTH_CHANNEL', '0').split()]
ANIME_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in os.environ.get('ANIME_CHANNEL', '0').split()]
FILIM_GPY_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in os.environ.get('FILIM_GPY_CHANNEL', '0').split()]
