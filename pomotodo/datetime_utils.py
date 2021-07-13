# coding=utf-8
import dateutil.parser


def from_iso8601(s):
    d = dateutil.parser.parse(s)
    return d


def to_iso8601(dt):
    return dt.strftime("%Y-%M-%DT%H:%M:%S.mmmmmmZ")


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
