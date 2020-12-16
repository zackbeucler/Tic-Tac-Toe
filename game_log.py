import logging
import logging.handlers
import os
from datetime import datetime

log = logging.getLogger("script-logger")
log.setLevel(logging.INFO)
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "game-log.log"))
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s","%Y:%m:%d:%H:%M:%S")
handler.setFormatter(formatter)
log.addHandler(handler)
