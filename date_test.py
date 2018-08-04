#!/usr/bin/env python3

import time
import datetime


def test_time():
    ts = time.time()
    st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    dt = time.strptime("2018-08-05 01:08:47", "%Y-%m-%d %H:%M:%S")
    print("time: ", ts, st, dt)


def test_datetime():
    # timestamp <=> datetime
    dt = datetime.datetime.fromtimestamp(1533402335)
    ts = dt.timestamp()
    print("timestamp <=> datetime: ", dt, ts)

    # datetime <=> str
    dt = datetime.datetime.strptime("2018-08-05 01:08:47", "%Y-%m-%d %H:%M:%S")
    st = dt.strftime("%Y-%m-%d %H:%M:%S")
    print("datetime <=> str: ", dt, st)

    # datetime <=> timedelta
    t1 = datetime.datetime.now()
    t2 = t1 + datetime.timedelta(seconds=3600)
    print("datetime <=> timedelta: ", t1, t2)


def main():
    test_time()
    test_datetime()


if __name__ == "__main__":
    main()
