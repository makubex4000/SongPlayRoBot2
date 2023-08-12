import os
import re
from yt_dlp import YoutubeDL

class Config:
    API_ID = "2710398"
    API_HASH = "e64c45a8f94ae642c090404e5f81f196"
    BOT_TOKEN = "1800777638:AAGMKMECKMCVolKCFkC5T-3SkudIjsFtYTE"
    START_MSG = "<b>嗨! {}, 我是 🎸歌曲播放機器人，</b>發送你想要的歌名或網址... 😍🥰🤗例如:/s 南拳媽媽-下雨天"
    START_IMG = "https://telegra.ph/file/d0cdeca30d2082b437645.jpg"
    OWNER = "Kevin_RX"
    DOWNLOAD_LOCATION = "DOWNLOAD_LOCATION", "./DOWNLOADS/"
    msg = {}
