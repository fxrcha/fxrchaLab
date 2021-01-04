import asyncio
from log import Logger
from config import SPOTIFY_SECRET, SPOTIFY_ID


class General:
    def __init__(self) -> None:
        self.logger = Logger.basicLogger(self)

    @staticmethod
    async def startDiscodo():
        cmd = "python3 -m discodo --port 6974 --auth SEXSEXSEX"
        return await asyncio.create_subprocess_shell(cmd)