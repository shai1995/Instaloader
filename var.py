# © Coded by @Dypixx
import os
from typing import List

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN = int(os.getenv("ADMIN", ""))

CHNL_LINK = os.getenv("CHNL_LINK", "https://t.me/MRADBOT_OFFICIALS")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002564857492"))
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002528883374"))

DB_URI = os.getenv("DB_URI", "") #MongoDB URL
DB_NAME = os.getenv("DB_NAME", "Cluster0")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001315120330").split())) # Add Multiple channel id

REEL_AUTO_DELETE = int(os.getenv("REEL_AUTO_DELETE", "600")) #10min

"""
This code is created and owned by @Dypixx. Do not remove or modify the credit.

Removing the credit does not make you a developer; it only shows a lack of respect for real developers.
  
Respect the work. Keep the credit.

"""
