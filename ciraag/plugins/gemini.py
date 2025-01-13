from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from ciraag.classes.ai import Gemini

async def load_plugin(client):
    @Ciraag(pattern=rf"\{handler}gemini")
    async def gemini_ai(event):
        await event.delete()
        ai = Gemini()
        await ai.google_gemini(event)