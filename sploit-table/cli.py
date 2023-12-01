import os
import time
import asyncio
from main import log, colors, miprnox, miprnox1, clear_screen, getcrit, getwarn



try:
    log.status("Importing dependencies")
    import colorama
    import pyfiglet
except ImportError:
    log.error("ImportError, installing dependencies, no need to worry")
    os.system("pip install colorama")
    os.system("pip install pyfiglet")
    time.sleep(2)
    log.success("Installed dependencies")
    time.sleep(1)
    import colorama
    import pyfiglet
finally:
   log.status("Import dependencies has passed, assuming success")



class cli:
    def command():
        current_dir = os.getcwd()
        ucommand = input(f"[{current_dir} - Sploit-Tables] -$")
        return ucommand
    


def update():
    global criterr
    criterr = getcrit()
    global warnerr
    warnerr = getwarn()

asyncio.run(update())

while criterr == 0:
    cli.command()

