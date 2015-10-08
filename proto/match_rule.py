__author__ = 'phate'

"""
The content for a rule sent to sdn application

- a part of request_packet,the other part is rule
- can refer to ryu's match class
- it can be expanded

"""


class MatchRule(object):
    """
    Flow Match Structure

    This class is implementation of the flow match structure
    You can define the flow match by the keyword arguments.
    The following arguments are available and it can be expanded

    ================ =============== ==================================
    Argument         Value           Description
    ================ =============== ==================================
    in_port          Integer 32bit   Switch input port
    in_phy_port      Integer 32bit   Switch physical input port
    eth_dst          MAC address     Ethernet destination address
    eth_src          MAC address     Ethernet source address
    eth_type         Integer 16bit   Ethernet frame type
    ip_proto         Integer 8bit    IP protocol
    ipv4_src         IPv4 address    IPv4 source address
    ipv4_dst         IPv4 address    IPv4 destination address
    tcp_src          Integer 16bit   TCP source port
    tcp_dst          Integer 16bit   TCP destination port
    udp_src          Integer 16bit   UDP source port
    udp_dst          Integer 16bit   UDP destination port
    icmpv4_type      Integer 8bit    ICMP type
    icmpv4_code      Integer 8bit    ICMP code
    arp_op           Integer 16bit   ARP opcode
    arp_spa          IPv4 address    ARP source IPv4 address
    arp_tpa          IPv4 address    ARP target IPv4 address
    arp_sha          MAC address     ARP source hardware address
    arp_tha          MAC address     ARP target hardware address
    ================ =============== ==================================

    sometimes we actually do not have to specify all of them,what we need
    to is just specify what we need
    """
    def __init__(self,**kwargs):
        self.fields = kwargs

    def __str__(self):
        my_str = ""
        for k in self.fields:
            my_str+=str(k)+":"+str(self.fields[k])
        return my_str

    def to_dict(self):
        return self.fields














