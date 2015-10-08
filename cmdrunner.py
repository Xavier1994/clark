__author__ = 'phate'

"""
This is the cmd runner to send the request_packet to database
we can directly run this file

- divide its cmd into four parts
- one is about db
- tow is about header_id
- three is about rule
- four is attach_field

"""
import argparse
from cmd import add_params,check_params
from proto.request_packet import RequestPacket

def main():
    parser = argparse.ArgumentParser()
    add_params.add_argument_for_head(add_params.add_argument_for_database(parser))
    add_params.add_argument_for_rule(add_params.add_argument_for_attach_field(parser))
    args = parser.parse_args()
    db_writer = check_params.check_and_return_db(args)
    request_packet = RequestPacket(check_params.check_and_return_header(args),
                                   check_params.check_and_return_rule(args),
                                   check_params.check_and_return_attach_field(args))

    #before we write it in db,we should check it
    request_id = db_writer.insert_rule(request_packet)
    print("successfully insert the requests, its inserted id is {}\n\nand the request is:".format(request_id))
    print(request_packet)




if __name__ == '__main__':

    """
    Cmdline choices

    The below is the current cmdline choice,we can expande it to
    support more

    ================ ================== ================ ==================================
    Argument         FullArgument       Value            Description
    ================ ================== ================ ==================================
    -db_ip           --database_ip      IP address       The ip of database
    -db_p            --database_port    Integer 32bit    The port of database
    -m               --mac              MAC address      The mac address of own machine
    -i               --ip               IP address       The ip address of own machine
    -host            --hostname         Host Name        the name of own host
    -t               --timestamp        Time             the timestamp of request packet
    -ot              --timeout          Time range       How long the request can survive
    -in_p            --in_port          Integer 32bit    Switch input port
    -in_phy_p        --in_phy_port      Integer 32bit    Switch physical input port
    -e_d             --eth_dst          MAC address      Ethernet destination address
    -e_s             --eth_src          MAC address      Ethernet source address
    -e_t             --eth_type         Integer 16bit    Ethernet frame type
    -ip_p            --ip_proto         Integer 8bit     IP protocol
    -ip4_s           --ipv4_src         IPv4 address     IPv4 source address
    -ip4_d           --ipv4_dst         IPv4 address     IPv4 destination address
    -t_s             --tcp_src          Integer 16bit    TCP source port
    -t_d             --tcp_dst          Integer 16bit    TCP destination port
    -u_s             --udp_src          Integer 16bit    UDP source port
    -u_d             --udp_dst          Integer 16bit    UDP destination port
    -ic_t            --icmpv4_type      Integer 8bit     ICMP type
    -ic_c            --icmpv4_code      Integer 8bit     ICMP code
    -pri             --priority          Integer 32bit    The priority of packet
    -en              --enable           Bool             If the packet can be handled
    ================ =============== ==================================

    sometimes we actually do not have to specify all of them,what we need
    to is just specify what we need
    """
    main()

