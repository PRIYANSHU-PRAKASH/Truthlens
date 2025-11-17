"""
A set of functions commonly used in the Newscrape project.
"""

from datetime import timezone, timedelta
from bs4 import NavigableString, Comment


def str_is_set(string):
    """
    Return False if string is empty True otherwise.
    """
    return string


def is_string(obj):
    """
    Returns True if obj is string False if not.
    """
    return not isinstance(obj, Comment) and isinstance(obj, NavigableString)


def to_utc(timestamp):
    return timestamp.astimezone(tz=timezone.utc)


def set_ist_zone(timestamp):
    timestamp.replace(
        tzinfo=timezone(timedelta(hours=5, minutes=30))
    )


def ist_to_utc(timestamp):
    set_ist_zone(timestamp)
    return to_utc(timestamp)


