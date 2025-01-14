from ciraag.core.module_injector import *
from ciraag import __version__
from telethon import version
from platform import python_version
from ciraag.utils import get_uptime

class CiraagFetch:
    async def ciraag_fetch(self, event):
        self.chat = event.to_id
        self.ciraag_uptime = get_uptime()
        await ciraag.send_message(self.chat, f"Ciraag Version: {__version__}\nPython Version: {python_version()}\nTelethon Version: {version.__version__}\nUptime: {self.ciraag_uptime}")