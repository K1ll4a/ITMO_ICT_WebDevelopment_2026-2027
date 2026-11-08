from datetime import datetime
from django.contrib import messages
from django.templatetags.static import static
from django.urls import reverse
from django.utils.formats import date_format
from django.utils import timezone
from jinja2 import Environment


def race_time(value):
    if value is None:
        return '—'
    milliseconds = round(value.total_seconds() * 1000)
    minutes, rest = divmod(milliseconds, 60000)
    seconds, ms = divmod(rest, 1000)
    return f'{minutes:02d}:{seconds:02d}.{ms:03d}'


def display_date(value, fmt='d.m.Y'):
    if isinstance(value, datetime) and timezone.is_aware(value):
        value = timezone.localtime(value)
    return date_format(value, fmt)


def environment(**options):
    env = Environment(**options)
    env.globals.update(static=static, url=reverse, get_messages=messages.get_messages)
    env.filters.update(date=display_date, race_time=race_time)
    return env
