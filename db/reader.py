__author__ = 'phate'

from conn import DBConnection

class DBReader(DBConnection):
    def __init__(self,ip='localhost',port=27017):
        super(DBReader,self).__init__(ip,port)

    def get_all_rules(self):
        """

        :rtype : List of RequestPacket
        """
        return self.con.find()

    #def get_rules_from_time_range(self,start,end):




