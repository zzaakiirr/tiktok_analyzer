import logging

import log
from tiktok.tiktok_parser import TikTokParser
from google_sheets.sheet_redactor import TikTokSheetRedactor
from worker.worker import Worker


def run_worker():
    log.configure_logging()

    parser = TikTokParser()
    sheet_redactor = TikTokSheetRedactor()
    worker = Worker(parser, sheet_redactor)

    worker.go()


if __name__ == '__main__':
    run_worker()
