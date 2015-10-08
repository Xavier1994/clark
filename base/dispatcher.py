__author__ = 'phate'

from get_rules import EventGetRules,MyEvTrigger
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls

class Dispatcher(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(Dispatcher, self).__init__(*args, **kwargs)
        self.dps = []

    @set_ev_cls(ofp_event.EventOFPPacketIn,MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        dp = msg.datapath
        if dp not in self.dps:
            self.dps.append(dp)

    @set_ev_cls(EventGetRules,MAIN_DISPATCHER)
    def get_rules_handler(self,ev):
        rps = ev.rps

