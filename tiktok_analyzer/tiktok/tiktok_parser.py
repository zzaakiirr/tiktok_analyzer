import logging

from TikTokApi import TikTokApi as tiktok_api

from tiktok_analyzer.helpers import safe_dict_access


class TikTokParser:
    def __init__(self):
        self.api = tiktok_api.get_instance()

    def get_user(self, username):
        logging.info("TikTokApi: fetching user by username <%s>", username)
        user = self.__safe_api_call(
            'get_user',
            username,
            error_handler = lambda exception: logging.error(
                'Cannot get user by username <%s>. Exception: %s',
                username,
                exception
            )
        )
        return user

    def get_followers_count(self, user):
        return safe_dict_access(
            user, ['userInfo', 'stats', 'followerCount'],
            lambda exception: logging.error(
                'Cannot get followers count for user: %s. Key error: %s',
                user,
                exception,
            )
        )

    def get_user_posts(self, user, count):
        user_info = safe_dict_access(
            user, ['userInfo', 'user'],
            lambda exception: logging.error(
                'Cannot get user_info for user: %s. KeyError: %s',
                user,
                exception
            )
        )
        if user_info is None:
            return

        user_id = user_info.get('id')
        sec_uid = user_info.get('secUid')

        return self.__safe_api_call(
            'user_posts', user_id, sec_uid, count,
            error_handler = lambda exception: logging.error(
                'Cannot get user posts for user info: %s. Exception: %s',
                user_info,
                exception,
            )
        )

    # MARK: - Private methods

    def __safe_api_call(self, method_name, *args, **kwargs):
        try:
            result = getattr(self.api, method_name)(*args)
        except Exception as exception:
            error_handler = kwargs.get('error_handler')
            if error_handler:
                error_handler(exception)
            return None

        return result
