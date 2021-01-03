import asyncio
from log import Logger
from config import SPOTIFY_SECRET, SPOTIFY_ID


class General:
    def __init__(self) -> None:
        self.logger = Logger.basicLogger()


    def RunDiscodoNode(self) -> None:
        asyncio.create_subprocess_shell(
            f"python3 -m discodo -P 6974 -A SEXSEXSEX!! --spotify-id {SPOTIFY_ID} --spotify-secret {SPOTIFY_SECRET}"
        )
        self.logger.info("Discodo node started.")