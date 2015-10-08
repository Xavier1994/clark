__author__ = 'phate'

from datetime import datetime, timedelta
from base.get_rules import EventGetRules, MyEvTrigger
from base.simple_switch_l3 import SimpleSwitch13


def work():
    event = EventGetRules("Hello")
    app = MyEvTrigger()
    app.send_event(SimpleSwitch13,event)


def run_task(func, day=0, hour=0, min=0, second=0):
    # Init time
    now = datetime.now()
    str_now = now.strftime('%Y-%m-%d %H:%M:%S')
    print "now:",str_now
    # First next run time
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period
    str_next_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print "next run:",str_next_time
    while True:
        # Get system current time
        iter_now = datetime.now()
        iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(iter_now_time) == str(str_next_time):
            # Get every start work time
            print "start work: %s" % iter_now_time
            # Call task func
            func()
            print "task done."
            # Get next iteration time
            iter_time = iter_now + period
            str_next_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print "next_iter: %s" % str_next_time
            # Continue next iteration
            continue

run_task(work, day=0, hour=0, min=0,second=3)
