import logging
import logging.handlers
import os
from datetime import datetime
import sys

log = logging.getLogger("script-logger")
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "game-log.log"))

handler.setFormatter(formatter)
sys_handler = logging.StreamHandler(stream=sys.stdout)
sys_handler.setFormatter(formatter)

log.setLevel(logging.INFO)
log.addHandler(handler)
log.addHandler(sys_handler)


