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
STRING_SESSION = 'BQFNtIsAgbVdHxKkMVUPkUzDLmSEiRdciLQ4pLxz7R7JqthqAaIP5H4t6YDOMUTcdgKLO8w3cejCFrOrbADsxIBvsD7kVGTwT9qg1xakvmRZFDTF4Ud4MMvZOK4jHXlF3qkzQ8fZl0xyLt063xqFfpiSCx962iqmda7BFzD8vUbGob1T-OrMRklQtuOV9o15q2UjC4Nsy6wIJISTcU9PU8leINJWWVbDykHuqoB_40g3FOltD0Yq85SPw0EMB0EQl52FcpiTZLCd4GxE0mVI0CZYiEPDyLBcOjE5H_2wuGiDsF5GG6p4JcsgGGqiLgSPay2bghiUDxMs8YvNMD6T9j7rJ42XuQAAAAHcRIKaAA'

# 🔍 Debug session string (optional)
print("Using session:", repr(STRING_SESSION))

# 🚀 Initialize bot
Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')

LOGS.info("Telegram bot started successfully.")
