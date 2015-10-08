__author__ = 'phate'

"""
we add the params to parser in this file

"""

def add_argument_for_database(parser):
    """

    :type parser: ArgumentParser
    """
    parser.add_argument("-db_ip", "--database_ip", help="specify the ip of database")
    parser.add_argument("-db_p", "--database_port", type=int,help="specify the database port")
    return parser

def add_argument_for_head(parser):
    """

    :type parser: ArgumentParser
    """
    parser.add_argument("-m", "--mac", help="specify the mac address of host")
    parser.add_argument("-i", "--ip", help="specify the ip address of host")
    parser.add_argument("-host", "--hostname", help="specify the hostname of the host")
    parser.add_argument("-t", "--timestamp", help="specify the timestamp of sending rule")
    parser.add_argument("-ot", "--timeout", help="specify the timeout")
    return parser


def add_argument_for_rule(parser):
    """

    :type parser: ArgumentParser
    """
    parser.add_argument("-in_p",      "--in_port", type = int, help = "specify the Switch input port")
    parser.add_argument("-in_phy_p",  "--in_phy_port", help="specify the Switch physical input port")
    parser.add_argument("-e_d",       "--eth_dst", help = "specify the Ethernet destination address")
    parser.add_argument("-e_s",       "--eth_src", help = "specify the Ethernet source address")
    parser.add_argument("-e_t",       "--eth_type",type = int, help="specify the Ethernet frame type")
    parser.add_argument("-ip_p",      "--ip_proto", type = int, help = "specify the IP protocol")
    parser.add_argument("-ip4_s",     "--ipv4_src", help = "specify the IPv4 source address")
    parser.add_argument("-ip4_d",     "--ipv4_dst", help = "specify the IPv4 destination address")
    parser.add_argument("-t_s",       "--tcp_src", type = int,  help = "specify the TCP source port")
    parser.add_argument("-t_d",       "--tcp_dst", type = int,  help = "specify the TCP destination port")
    parser.add_argument("-u_s",       "--udp_src", type = int,  help = "specify the UDP source port")
    parser.add_argument("-u_d",       "--udp_dst", type = int,  help = "specify the UDP destination port")
    parser.add_argument("-ic_t",      "--icmpv4_type", type = int,  help = "specify the ICMP type")
    parser.add_argument("-ic_c",      "--icmpv4_code", type = int,  help = "specify the ICMP code")
    return parser

def add_argument_for_attach_field(parser):
    """

    :type parser: ArgumentParser
    """
    parser.add_argument("-pri", "--priority", help = "specify the priority for this packet")
    parser.add_argument("-en", "--enable", action="store_true", help="specify if  this rule can be applied")
    return parser


