__author__ = 'phate'

"""
This is used to check the params and return responsive object

"""
from proto.header_id import HeaderId
from db.writer import DBWriter
from proto.match_rule import MatchRule
from proto.attach_field import AttachField


def check_and_return_db(args):
    """

    :rtype : DBWriter
    """
    if (args.database_ip is None) or (args.database_port is None):
        return DBWriter()
    else:
        return DBWriter(args.database_ip,args.database_port)

def check_and_return_header(args):
    """

    :rtype : HeaderId
    """
    if (args.ip is None) or (args.mac is None):
        return check_and_return_header()
    else:
        header_id = HeaderId(mac = args.mac,
                             ip = args.ip,
                             hostname = args.hostname,
                             timeout = args.timeout)
        return header_id

def check_and_return_rule(args):
    """

    :rtype : MatchRule
    """
    kwargs = {"in_port": args.in_port,
             "in_phy_port:": args.in_phy_port,
             "eth_dst": args.eth_dst,
             "eth_src": args.eth_src,
             "eth_type": args.eth_type,
             "ip_proto": args.ip_proto,
             "ipv4_src": args.ipv4_src,
             "ipv4_dst": args.ipv4_dst,
             "tcp_src": args.tcp_src,
             "tcp_dst": args.tcp_dst,
             "udp_src": args.udp_src,
             "udp_dst": args.udp_dst,
             "icmpv4_type": args.icmpv4_type,
             "icmpv4_code": args.icmpv4_code}

    rule = MatchRule(kwargs)
    return rule

def check_and_return_attach_field(args):
    """

    :rtype : AttachField
    """
    if args.priority is None:
        return AttachField()
    else:
        return AttachField(args.priority,args.enable)