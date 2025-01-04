from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from ciraag.classes.chat_fight import Opponent

@Ciraag(rf"\{handler}cbomb")
async def custom_bomb(event):
    await event.delete()
    genie = Opponent()
    await genie.bomber_genie(event)