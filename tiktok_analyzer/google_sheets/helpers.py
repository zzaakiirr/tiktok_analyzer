def col_number(col_letter):
    try:
        return ord(col_letter.lower()) - 96
    except (TypeError, AttributeError):
        return None


# https://stackoverflow.com/a/18891054
def thousand_separated(number):
    try:
        return '{:,}'.format(number).replace(',', ' ')
    except TypeError:
        return None
