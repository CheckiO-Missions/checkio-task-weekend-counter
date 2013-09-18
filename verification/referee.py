from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS

date_cover = """

def cover(func, in_data):
    from datetime import date
    return func(date(*in_data[0]), date(*in_data[1]))

"""


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': date_cover,
            'python-3': date_cover
        }).on_ready)
