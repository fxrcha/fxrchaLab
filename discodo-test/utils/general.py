import asyncio
from log import Logger
from config import SPOTIFY_SECRET, SPOTIFY_ID


class General:
    def __init__(self) -> None:
        self.logger = Logger.basicLogger(self)
