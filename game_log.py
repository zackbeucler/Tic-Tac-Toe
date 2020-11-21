import logging
import logging.handlers
import os
from datetime import datetime
import Tic_tac_toe

log = logging.getLogger("script-logger")
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "app-log.log"))
logging.basicConfig(filename='game_log.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

def main():
    logging.info("selection: "+str(selection))
    logging.info("current player: "+current)
    logging.info("winner? "+str(winner))
    logging.info("full? "+str(full))

if __name__ == "__main__":
    main()