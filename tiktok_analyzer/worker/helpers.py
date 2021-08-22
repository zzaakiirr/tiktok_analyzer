import logging

from tiktok_analyzer.helpers import safe_dict_access


def get_avg_posts_count(posts):
    valid_posts_count = posts.count
    total_play_count = 0

    for post in posts:
        play_count = safe_dict_access(
            post, ['stats', 'playCount'],
            lambda exception: logging.error(
                'Cannot get play count for post %s. KeyError: %s',
                post,
                exception
            )
        )
        if not play_count:
            valid_posts_count -= 1
            continue

        total_play_count += int(play_count)

    int(total_play_count / valid_posts_count)
