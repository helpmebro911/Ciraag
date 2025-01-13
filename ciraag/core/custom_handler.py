from os import environ
from dotenv import load_dotenv

load_dotenv()

try:
    handler = environ["command_handler"]
    if handler == "":
        handler = "."
except KeyError:
    handler = "."
