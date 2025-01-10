from ciraag.core.module_injector import *
from os import kill, getpid, remove
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
   
    async def uninstall_plugin(self, event):
        await event.edit("Initiating plugin uninstallation process. Please allow sufficient time for completion.")
        sleep(3)
        self.get_plugin = await event.get_reply_message()
        try:
            self.file_name = self.get_plugin.media.document.attributes[0].file_name
            self.mime_type = self.get_plugin.media.document.mime_type
            if self.get_plugin.media and self.mime_type == "text/x-python":
                remove(f"ciraag/plugins/{self.file_name}")
                restart_script()
                await event.edit(f"Successfully uninstalled the {self.file_name} plugin. Rebooting the Ciraag userbot to ensure a clean unload. Please allow a few seconds for the process to complete.")
                kill(getpid(), SIGTERM)
        except:
            await event.edit("There might be an error with uninstalling the plugin.")