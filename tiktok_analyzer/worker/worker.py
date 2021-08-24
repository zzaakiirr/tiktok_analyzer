import worker.helpers as worker_helpers
import time


USER_POSTS_COUNT = 12


class Worker:
    def __init__(self, parser, sheet_redactor):
        self.parser = parser
        self.sheet_redactor = sheet_redactor

    def go(self, posts_count = USER_POSTS_COUNT):
        self.sheet_redactor.set_initial_formatting()
        current_row_index = self.sheet_redactor.start_index

        for username in self.sheet_redactor.get_usernames():
            user = self.parser.get_user(username)
            if user:
                self.__update_followers_count(user, current_row_index)
                self.__update_avg_play_count(
                    user,
                    posts_count,
                    current_row_index
                )
            else:
                self.sheet_redactor.format_error(
                    self.sheet_redactor.usernames_col,
                    current_row_index,
                )
            # Escape Google Sheets write requests per minute quota
            time.sleep(1)
            current_row_index += 1

    # MARK: - Private methods

    def __update_followers_count(self, user, current_row_index):
        followers_count = self.parser.get_followers_count(user)
        if followers_count:
            self.sheet_redactor.update_followers_count(
                current_row_index,
                followers_count,
            )
        else:
            self.sheet_redactor.format_error(
                self.sheet_redactor.followers_count_col,
                current_row_index,
            )

    def __update_avg_play_count(self, user, posts_count, current_row_index):
        posts = self.parser.get_user_posts(user, posts_count)
        avg_play_count = worker_helpers.get_avg_posts_count(posts)
        if avg_play_count:
            self.sheet_redactor.update_avg_play_count(
                current_row_index,
                avg_play_count,
            )
        else:
            self.sheet_redactor.format_error(
                self.sheet_redactor.avg_play_count_col,
                current_row_index,
            )
