from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from ciraag.classes.ciraag_sys import CiraagFetch

async def load_plugin(client):
    @Ciraag(pattern=rf"\{handler}fetch")
    async def ciraag_information(event):
        await event.delete()
        ciraag_system = CiraagFetch()
        await ciraag_system.ciraag_fetch(event)