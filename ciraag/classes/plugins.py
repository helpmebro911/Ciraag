from ciraag.core.module_injector import *
from os import kill, getpid
from signal import SIGTERM
from subprocess import Popen
from time import sleep

def restart_script():
  bash_command = ["bash", "start.sh"]
  Popen(bash_command)

class PluginManager:
    async def install_plugin(self, event):
        await event.edit("Plugin download in progress. Please allow sufficient time for completion.")
        sleep(3)
        self.get_plugin = await event.get_reply_message()
        try:
            self.mime_type = self.get_plugin.media.document.mime_type
            if self.get_plugin.media and self.mime_type == "text/x-python":
                await self.get_plugin.download_media(file="ciraag/plugins")
                await event.edit("Plugin download and installation completed.")
                sleep(3)
                restart_script()
                await event.edit("Great news! The plugin installation is complete. To ensure optimal performance, Ciraag is undergoing a reboot. You should be able to start using the new features shortly.")
                kill(getpid(), SIGTERM)
        except:
            await event.edit("Oops, something went wrong during the plugin installation. It looks like the plugin might not be the right fit for Ciraag, or there could be a small hiccup in the process. Let's try checking the plugin's compatibility and following the installation steps again.")