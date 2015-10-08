__author__ = 'lenovo'

"""
The attach field for a request_packet

- include priority and enable
- it help analysis the rule in database
- it can be also expanded

"""

class AttachField(object):
    """
    Header_ID

    It will be used as a part of request_packet sent to database

    ============= =========================================================
    Attribute     Description
    ============= =========================================================
    priority      specify the priority for a packet
    enable        whether enable a packet
    ============= =========================================================
    """
    def __init__(self,priority = 0,enable = False):
        self.priority = priority
        self.enable = enable

    def __str__(self):
        return "priority:{}\nenable:{}\n".format(self.priority,self.enable)

    # it will be used to insert in mongodb
    def to_dict(self):
        my_dict = {"priority": self.priority,"enable":self.enable}
        return my_dict


