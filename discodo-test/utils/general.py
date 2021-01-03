import asyncio
from log import Logger
from config import SPOTIFY_SECRET, SPOTIFY_ID


class General:
    def __init__(self) -> None:
        self.logger = Logger.basicLogger(self)

    @staticmethod
    async def RunDiscodoNode() -> None:
        return await asyncio.create_subprocess_shell(
            f"python3 -m discodo -P 6974 -A SEXSEXSEX!!"
        )