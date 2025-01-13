from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from ciraag.classes.plugins import PluginManager

async def load_plugin(client):
    @Ciraag(pattern=rf"\{handler}install")
    async def plugin_installer(event):
        plugin = PluginManager()
        await plugin.install_plugin(event)