import pymongo
class DB(object):
    host = "localhost"
    port = 27017
    db = pymongo.MongoClient(host,port)
    client=pymongo.MongoClient(host,port)
    db=client['alert']
    
    @staticmethod
    def insert(c,d):
        DB.db[c].insert(d)

    @staticmethod
    def find(c,d):
        return DB.db[c].find(d)
    
    @staticmethod
    def find_one(c,d):
        return DB.db[c].find_one(d)

    @staticmethod
    def update(c,q,d):
        DB.db[c].update(q,d,upsert=True)

        
    @staticmethod
    def remove(c,d):
        DB.db[c].remove(d)