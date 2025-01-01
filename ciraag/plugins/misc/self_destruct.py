from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from ciraag.classes.timer import SelfDestruct

@Ciraag(rf"\{handler}tmd")
async def get_self_destructive_media(event):
    await event.delete()
    media = SelfDestruct()
    await media.save(event)