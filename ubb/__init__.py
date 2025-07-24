import os
import logging
import yaml

from telethon import TelegramClient
from telethon.sessions import StringSession

# Logging config
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

# Resolve config.yml path no matter where this file runs from
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yml')

# Load config
with open(config_path, 'r') as f:
    CONFIG = yaml.safe_load(f)

# Read variables from env or config
API_ID = int(os.getenv('API_ID', CONFIG['api_id']))
API_HASH = os.getenv('API_HASH', CONFIG['api_hash'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['dump_id'])
STRING_SESSION = os.getenv('STRING_SESSION', CONFIG['string_session'])

# Initialize client
Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')

LOGS.info("Telegram client initialized successfully.")
