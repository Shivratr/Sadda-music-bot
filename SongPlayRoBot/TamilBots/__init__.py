import logging
from pyrogram import Sadda_music_bot 
from config import API_HASH, API_ID, BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

app = Client("SongPlayRoBot", bot_token=1817100318:AAEVboRpBFc_MhCK0iUtmkknZbNBdDAi424, api_hash=b1d3a5bed5d00b6c37993e168242d184, api_id=6381747)
