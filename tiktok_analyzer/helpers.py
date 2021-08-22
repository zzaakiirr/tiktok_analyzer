import logging


def safe_dict_access(dictinory, keys, exception_method = None):
    try:
        value = dictinory
        for key in keys:
            value = value[key]
    except KeyError as exception:
        if exception_method:
            exception_method(exception)
        return None

    return value
