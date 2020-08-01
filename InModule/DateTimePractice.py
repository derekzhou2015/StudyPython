#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
import re
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print("----------------------------------")
dt = datetime(2020, 2, 25, 23, 23, 59, 144433)
ts = dt.timestamp()
dt = datetime.utcfromtimestamp(ts)
print(dt, dt.timestamp())
print("----------------------------------")
# Str to Datetime
dt = datetime.strptime('2020-01-01 23:59:59.001929', '%Y-%m-%d %H:%M:%S.%f')
sdt = dt.strftime('%a,%b %d %H:%M')
print(dt, sdt)
print("----------------------------------")

now = datetime.now()
now = now + timedelta(hours=10)
print(now)
now = now - timedelta(hours=10, days=1)
print(now)
print("----------------------------------")
# UTC Time
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
print(dt)
print("----------------------------------")
utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_now.astimezone(timezone(timedelta(hours=8)))
tokyo_dt = utc_now.astimezone(timezone(timedelta(hours=9)))
print('utc:', utc_now)
print('bj:', bj_dt)
print('tokyo:', tokyo_dt)

print("----------------------------------")


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    zone = int(re.match(r'UTC(?P<zone>[\+-]\d+)', tz_str, re.I).group('zone'))
    result = dt.replace(tzinfo=timezone(timedelta(hours=zone)))
    return result.timestamp()


# test:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
print("----------------------------------")
