__author__ = 'phate'

"""
We define a event and a ryuapp here

- this event is to communicate with ryu app
- it will include the rules in database
- the ryuapp will send the rule
"""

import logging

from ryu.controller import event
from ryu.controller import handler
from ryu.base import app_manager

LOG = logging.getLogger('MyEvTrigger')


class EventGetRules(event.EventBase):
    def __init__(self, rps):
        super(EventGetRules, self).__init__()
        self.rps = rps


class MyEvTrigger(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(MyEvTrigger, self).__init__(*args, **kwargs)

    def build_event(self,reader):
        """

        :rtype : EventGetRules
        """
        ev = EventGetRules(reader.get_all_rules())
        return ev

    def send(self,name,reader):
        ev = self.build_event(reader)
        self.send_event(name,ev)


handler.register_service('MyEvTrigger')