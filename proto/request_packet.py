__author__ = 'lenovo'

"""
This is the class we send it to database

- consist by three parts
- header_id,attach_field,match_rule
- it can consist many match_rules

"""

class RequestPacket(object):
    def __init__(self, header_id, match_rules=None, attach_field=None):
        self.header_id = header_id
        self.match_rules = match_rules
        self.attach_field = attach_field

    def __str__(self):
        my_str = str(self.header_id)
        for match_rule in self.match_rules:
            my_str+=str(match_rule)+'\n'
        my_str+=str(self.attach_field)
        return my_str

    def to_dict(self):
        rules_list = []
        for r in self.match_rules:
            rules_list.append(r.to_dict())
        rules = [("rules",rules_list)]
        my_dict = dict(self.header_id.to_dict().items()+self.attach_field.to_dict().items()+rules)
        return my_dict






