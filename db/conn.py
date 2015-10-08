__author__ = 'phate'

"""
This class handle the connection with mongodb


"""

from pymongo import MongoClient

class DBConnection(object):
    def __init__(self, ip,port,name = 'test',table = 'rule'):
        self.client = MongoClient(ip, port)
        self.db = self.client[name]
        self.con = self.db[table]

    def get_default_database(self):
        self.db = self.client['test']
        return self.db

    def get_new_database(self,name):
        self.db = self.client[name]
        return self.db






