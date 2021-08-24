import logging
from datetime import datetime
from pathlib import Path

LOG_FOLDER_PATH = 'logs'
LOG_FILENAME = datetime.now().strftime('%Y_%m_%d_%H:%M:%S.log')
LOG_FILEPATH = f'{LOG_FOLDER_PATH}/{LOG_FILENAME}'

LOG_FILEMODE = 'w'
LOG_FORMAT = '%(asctime)s:%(levelname)s - %(message)s'


def configure_logging(log_filename=LOG_FILEPATH,
                      lof_filemode=LOG_FILEMODE,
                      log_format=LOG_FORMAT):
    Path(LOG_FOLDER_PATH).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_filename,
        filemode=lof_filemode,
        format=log_format,
        level=logging.ERROR,
    )
