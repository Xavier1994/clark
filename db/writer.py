__author__ = 'phate'

from conn import DBConnection

class DBWriter(DBConnection):
    def __init__(self,ip='localhost',port=27017):
        super(DBWriter,self).__init__(ip,port)

    def insert_rule(self, rule):
        rule_id = self.con.insert_one(rule.to_dict()).inserted_id
        return rule_id

    def insert_many_rules(self,rules):
        rules_dict = []
        for rule in rules:
            rules_dict.append(rule.to_dict())
            result_ids = self.dbcon.con.insert_many(rules_dict).inserted_ids
        return result_ids











