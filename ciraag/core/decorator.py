from telethon import events
from ciraag.core.module_injector import *

class CiraagUserbot:
    def __init__(self, client):
        self.client = client
    def __call__(self, pattern):
        def decorator(func):
            @self.client.on(events.NewMessage(outgoing=True, pattern=pattern))
            async def wrapper(event):
                await func(event)
            return wrapper
        return decorator

Ciraag = CiraagUserbot(ciraag)