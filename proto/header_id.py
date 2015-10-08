__author__ = 'phate'

"""
The header identification for a rule sent to sdn application

- a part of request_packet,the other part is rule
- it is a mark for a requet_packet sent to database
- can be expanded to add a hash to identify

"""

import re
import uuid
import socket
from datetime import *

class HeaderId(object):
    """
    Header_ID

    It will be used as a part of request_packet sent to database

    ============= =========================================================
    Attribute     Description
    ============= =========================================================
    mac           the mac address of machine which send a request_packet.
    ip            the ip address.
    hostname      the name of a host,can be default
    timeout       it specify the how long this packet will survive
                  after that,it will be removed from database
    timestamp     specify when to send the packet
    ============= =========================================================
    """
    def __init__(self, mac, ip, hostname="", timeout=5000, timestamp=datetime.now()):
        if check_mac(mac):
            self.mac = mac
        else:
            self.mac = '00:00:00:00:00:00'
        if check_ip(ip):
            self.ip = ip
        else:
            self.ip = '0.0.0.0'
        self.hostname = hostname
        self.timestamp = timestamp
        self.timeout = timeout

    def __str__(self):
        return 'mac:{}\nip:{}\nhostname:{}\ntimestamp:{}\ntimeout:{}ms\n'.format(self.mac,
                                                                                 self.ip,
                                                                                 self.hostname,
                                                                                 self.timestamp,
                                                                                 self.timeout)
    def to_dict(self):
        my_dict = {"mac": self.mac,
                  "ip": self.ip,
                  "hostname": self.hostname,
                  "timestamp": self.timestamp,
                  "timeout": self.timeout}
        return my_dict



# check if the ip given is available
def check_ip(ip):
    ip_pattern = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
    return ip_pattern.match(ip) is not None

# check if the mac given is available
def check_mac(mac):
    mac_pattern = re.compile(r'' '\n'
                             r'                      (^([0-9A-F]{1,2}[-]){5}([0-9A-F]{1,2})$' '\n'
                             r'                      |^([0-9A-F]{1,2}[:]){5}([0-9A-F]{1,2})$' '\n'
                             r'                      |^([0-9A-F]{1,2}[.]){5}([0-9A-F]{1,2})$)' '\n'
                             r'                      ',
                             re.VERBOSE | re.IGNORECASE)
    return mac_pattern.match(mac) is not None


def get_ip_address():
    my_name = get_hostname()
    my_addr = socket.gethostbyname(my_name)
    return my_addr


def get_hostname():
    my_name = socket.getfqdn(socket.gethostname())
    return my_name


def get_mac_address():
    mac=uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])


def get_default_identification():
    """

    :rtype : HeaderId
    """
    default_mac = get_mac_address()
    default_ip  = get_ip_address()
    default_hostname = get_hostname()
    default_id = HeaderId(mac = default_mac, ip = default_ip, hostname = default_hostname)
    return default_id





