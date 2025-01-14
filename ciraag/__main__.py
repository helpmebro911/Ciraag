from ciraag.core.module_injector import *
from glob import glob
from asyncio import sleep, run
from signal import signal, SIGINT
from ciraag.utils.uptime import Ciraag_Uptime
from os import remove
from telethon.tl.functions.channels import JoinChannelRequest

ciraag_channel = "@ciraag"
ciraag_chat = "@ciraag_chat"
ciraag_plugins = "@ciraag_plugins"
ciraag_developer = "@iniridwanul_timeline"

def signal_handler(sig, frame):
    print("\nReceived signal:", sig)
    print("Stopping Ciraag gracefully...")
    ciraag.disconnect()
    remove("uptime.txt")
    exit(0)

signal(SIGINT, signal_handler)

async def main():
    for plugin in glob("ciraag/plugins/*.py"):
        plugin_name = plugin.replace(".py", "").replace("ciraag/plugins/", "")
        module = __import__(f"ciraag.plugins.{plugin_name}", fromlist=[plugin_name])
        if hasattr(module, "load_plugin"):
            await module.load_plugin(ciraag)
            print(f"{plugin_name} plugin loaded successfully")
    try:
        await ciraag.start()
        iniuptime = Ciraag_Uptime()
        iniuptime.uptime()
        print("Ciraag Started")
        boot = open("ciraag/utils/boot.txt", "r")
        data = boot.read()
        size = len(data)
        boot.close()
        if size == 0:
            boot_file = open("ciraag/utils/boot.txt", "w")
            boot_file.write("Success")
            boot_file.close()
            await ciraag(JoinChannelRequest(channel=f"{ciraag_channel}"))
            await ciraag(JoinChannelRequest(channel=f"{ciraag_chat}"))
            await ciraag(JoinChannelRequest(channel=f"{ciraag_plugins}"))
            await ciraag(JoinChannelRequest(channel=f"{ciraag_developer}"))
        else:
            pass
        await sleep(float("inf")) 
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Stopping Ciraag gracefully...")
        await ciraag.disconnect()

run(main())