import logging


LOG_FILENAME = 'app.log'
LOG_FILEMODE = 'a'
LOG_FORMAT = '%(asctime)s:%(levelname)s - %(message)s'


def configure_logging(log_filename=LOG_FILENAME,
                      lof_filemode=LOG_FILEMODE,
                      log_format=LOG_FORMAT):
    logging.basicConfig(
        filename=log_filename,
        filemode=lof_filemode,
        format=log_format,
        level=logging.DEBUG,
    )
