from ciraag.core.module_injector import *
from ciraag.core.client import ciraag_bot
from ciraag.core.custom_handler import handler
from telethon import events
from ciraag.classes.repository import Repository

@Ciraag(rf"\{handler}repo")
async def repo_details(event):
    await event.delete()
    ciraag = Repository()
    await ciraag.show_repository(event)

@ciraag_bot.on(events.InlineQuery)
async def get_query(query):
    ciraag = Repository()
    await ciraag.repo_query(query)