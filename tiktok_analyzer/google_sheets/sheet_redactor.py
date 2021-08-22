import logging
from pathlib import Path

from gspread import service_account
from gspread.exceptions import APIError

from google_sheets.helpers import col_number
from google_sheets.sheet_config import (
    SERVICE_ACCOUNT_FILENAME,
    WORKBOOK_NAME,

    START_INDEX,
    USERNAMES_COL_NAME,
    FOLLOWERS_COUNT_COL_NAME,
    AVG_PLAY_COUNT_COL_NAME,
)


class TikTokSheetRedactor:

    # MARK: - Init

    def __init__(self,
                 service_account_filename=SERVICE_ACCOUNT_FILENAME,
                 workbook_name=WORKBOOK_NAME,
                 start_index=START_INDEX,
                 usernames_col=USERNAMES_COL_NAME,
                 followers_count_col=FOLLOWERS_COUNT_COL_NAME,
                 avg_play_count_col=AVG_PLAY_COUNT_COL_NAME):

        self.start_index = start_index
        self.usernames_col = usernames_col
        self.followers_count_col = followers_count_col
        self.avg_play_count_col = avg_play_count_col
        self.sheet = self.__get_sheet(service_account_filename, workbook_name)

    # MARK: - Public methods


    def get_usernames(self):
        logging.info("Parsing usernames from sheet")
        col_values = self.__safe_sheet_method(
            'col_values',
            col_number(self.usernames_col),
        )
        usernames = col_values[self.start_index - 1:]
        return usernames

    def update_followers_count(self, row_number, followers_count):
        logging.info("Updating followers count for row: <%s>", row_number)
        self.__safe_sheet_method(
            'update',
            f'{self.followers_count_col}{row_number}',
            followers_count,
        )

    def update_avg_play_count(self, row_number, avg_play_count):
        logging.info("Updating avg play count for row: <%s>", row_number)
        self.__safe_sheet_method(
            'update',
            f'{self.avg_play_count_col}{row_number}',
            avg_play_count,
        )

    # MARK: - Private methods

    def __get_sheet(self, service_account_filename, workbook_name):
        try:
            gc = service_account(
                filename=Path(__file__).with_name(service_account_filename),
            )
            sh = gc.open(workbook_name)
        except FileNotFoundError:
            logging.error(
                "Cannot find service account file with name: <%s>",
                service_account_filename,
            )
            return None

        return sh.sheet1

    def __safe_sheet_method(self, method_name, *args, **kwargs):
        try:
            result = getattr(self.sheet, method_name)(*args, **kwargs)
        except APIError as exception:
            logging.error("Error with Google sheet API: %s", exception)
            return None

        return result
