import logging


def safe_dict_access(dictinory, keys, exception_method):
    try:
        value = dictinory
        for key in keys:
            value = value[key]
    except KeyError as exception:
        exception_method(exception)
        return None

    return value
