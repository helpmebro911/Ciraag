from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from ciraag.classes.plugins import PluginManager

async def load_plugin(client):
    @client.on(events.NewMessage(outgoing=True, pattern=rf"\{handler}uninstall"))
    async def plugin_uninstaller(event):
        plugin = PluginManager()
        await plugin.uninstall_plugin(event)