# coding=UTF-8
from pytz import timezone
from datetime import datetime, timedelta
from unittest import TestCase

shanghai_zone = timezone('Asia/Shanghai')
brisbane_zone = timezone('Australia/Brisbane')
los_angeles_zone = timezone('America/Los_Angeles')


class TimeSample(TestCase):
    def setUp(self):
        self.now = datetime.now()

    def test_now(self):
        naive_now = self.now
        shanghai_now = self.now.replace(tzinfo=shanghai_zone)
        brisbane_now = shanghai_now.astimezone(tz=brisbane_zone)
        la_now = shanghai_now.astimezone(tz=los_angeles_zone)
        print('naive_now: %s' % naive_now)
        print('shanghai_now: %s' % shanghai_now)
        print('brisbane_now: %s' % brisbane_now)
        print('los_angeles_now: %s' % la_now)

    def test_duration(self):
        later = timedelta(hours=1)
        one_hour_later = self.now + later
        print('naive_now: %s' % self.now)
        print('one hour later: %s' % one_hour_later)

    def test_time_compare(self):
        one_hour = timedelta(hours=1)
        today = self.now
        tomorrow = self.now + timedelta(days=1)
        time_diff = tomorrow - today
        print('tomorrow - today: %s' % time_diff)
        assert (tomorrow > today)
        assert (time_diff > one_hour)
