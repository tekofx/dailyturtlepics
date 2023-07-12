import os
import logging
from dotenv import load_dotenv
import sys
from bot import Bot
log = logging.getLogger(__name__)

# Set workdir
path = os.path.dirname(os.path.abspath(__file__))
working_dir = os.path.dirname(path)
os.chdir(working_dir)


if "-t" in sys.argv:
    log.info("Executing in TEST mode")
    load_dotenv("dev.env")
else:
    log.info("Executing in NORMAL mode")
    
    
bot=Bot()
bot.run()