from ciraag.core.module_injector import *
from glob import glob
from asyncio import sleep, run
from signal import signal, SIGINT
from os import remove

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
        print("Ciraag Started")
        await sleep(float("inf")) 
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Stopping Ciraag gracefully...")
        await ciraag.disconnect()

run(main())