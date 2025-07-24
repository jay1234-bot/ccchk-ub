import logging
from telethon import TelegramClient
from telethon.sessions import StringSession

# Logging setup
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

# 🔐 Hardcoded Config — yahan apne credentials daal de
API_ID = 26237149
API_HASH = '9aa3a717824271eb02b6ee5961c38bda'
DUMP_ID = -1002780220931  # Optional: if used somewhere later
STRING_SESSION = 'BQFNtIsAYHrVyWXpnjA2CIspiEFISu0Uy62yyk0ffjSHZJN60gmtodadqlaaREAOjZ8nn9xTUMe24JKmfMo-lbd_9v7gCJkCvJNhFskmwQFpaXhrYlsP_xSbZmP1k6VEwnKVElsLjVp51sv41ZKcNgPf8RCtVtQ7F7wkZqnNvT6649qYiuW0WupkQD9T-oDKamdePfYYwvnTiaBrx9geCtfpbtBzgFcU5-CqiL9IQGjEsrq-Zb2V_5NJBgvgixQt7hOl8YtkXt6OwrLlgtmkuKJ2jGChcwqC5gCJrruVhX7HOjiFNAdYR1h3IeawjNQ6x7cg0wZT3wN7LkxgR9fg7bJlDXnejwAAAAHQY_3eAA'
# 🔍 Debug session string (optional)
print("Using session:", repr(STRING_SESSION))

# 🚀 Initialize bot
Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')

LOGS.info("Telegram bot started successfully.")
