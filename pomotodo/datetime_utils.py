# coding=utf-8
from datetime import timedelta

import dateutil.parser


def from_iso8601(s):
    d = dateutil.parser.parse(s)
    return d


def to_iso8601(dt):
    """
    different between python 2.x and python 3.x?
    suggest to local tz than datetime.isoformat()
    like this:

    now = datetime_utils.to_local(datetime.now())
    print(now.isoformat())

    :param dt:
    :return:
    """
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f%z")


def convert_tz(dt, to_tz):
    return dt.astimezone(to_tz)


def to_local(dt):
    from dateutil import tz
    local_tz = tz.tzlocal()
    return dt.astimezone(local_tz)


def to_utc(dt):
    from dateutil import tz
    utc_tz = tz.gettz('UTC')
    return dt.astimezone(utc_tz)


def local_today():
    from datetime import date
    naive_today = date.today()

    from datetime import datetime
    from dateutil import tz
    today_dt = datetime(naive_today.year, naive_today.month, naive_today.day, tzinfo=tz.tzlocal())

    return today_dt


def utc_today():
    return to_utc(local_today())


def local_yesterday():
    return local_today() - timedelta(days=1)


def utc_yesterday():
    return to_utc(local_yesterday())
