from ciraag.core.module_injector import *
from glob import glob
from asyncio import sleep, run

async def main():
    for plugin in glob("ciraag/plugins/*.py"):
        plugin_name = plugin.replace(".py", "").replace("ciraag/plugins/", "")
        module = __import__(f"ciraag.plugins.{plugin_name}", fromlist=[plugin_name])
        if hasattr(module, "load_plugin"):
            await module.load_plugin(ciraag)
            print(f"{plugin_name} plugin loaded successfully")
    await ciraag.start()
    print("Ciraag Started")
    await sleep(float("inf"))

run(main())