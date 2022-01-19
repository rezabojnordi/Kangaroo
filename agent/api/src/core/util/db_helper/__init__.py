import pymongo
import os


class Database:
    """A wrapper class of pymongo to ease things and hide the implementation
    dependencies from developer"""

    def __init__(self, db_name="mydatabase", col="mycol", host="127.0.0.1", port=27017, username='', password='', auth_src=''):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.m = pymongo.MongoClient(
            "mongodb://{username}:{password}@{host}:{port}/?authSource={auth_src}"
            .format(username=self.username, password=self.password, host=self.host, port=self.port, auth_src=auth_src))
        self.db_name = self.m[db_name]
        self.col = self.db_name[col]

    def insert_one(self, obj_data):
        r = self.col.insert_one(obj_data)
        return r.inserted_id

    def insert_many(self, obj_data):
        r = self.col.insert_many(obj_data)
        return r.inserted_ids

    def find_one_params(self, one_obj):
        r = self.col.find_one(one_obj)
        return r

    def find(self, limit=0):
        r = self.col.find().limit(limit)
        data = []
        for i in r:
            data.append(i)
        return data

    def find_many_params(self, one_obj):
        r = self.col.find(one_obj)
        data = []
        for i in r:
            data.append(i)
        return data

    def find_filter(self, query):
        """When finding documents in a collection,
        you can filter the result by using a query object.
        """
        r = self.col.find(query)
        data = []
        for i in r:
            data.append(i)
        return data

    def sort(self, key, gradient=1):
        """
        sort("name", 1) #ascending
        sort("name", -1) #descending
        """
        r = self.col.find().sort(key, gradient)
        data = []
        for i in r:
            data.append(i)
        return data

    def delete_one(self, query):
        data = []
        find = self.col.find()
        r = self.col.delete_one(query)
        for i in find:
            data.append(i)
        return data

    def delete_many(self, query={}):
        r = self.col.delete_many(query)
        return r.deleted_count

    def drop(self):
        """The drop() method returns true if the collection was dropped successfully,
        and false if the collection does not exist.
        """
        r = self.col.drop()
        return r

    def update_one(self, query, new_value):
        data = []
        find = self.col.find()
        values = {"$set": new_value}
        r = self.col.update_one(query, values, upsert=True)
        for i in find:
            data.append(i)
        return data

    def update_many(self, query, new_value):
        values = {"$set": new_value}
        r = self.col.update_one(query, values)
        return r.modified_count


db_helper_obj = Database(
    username=os.getenv('MONGO_USERNAME'),
    password=os.getenv('MONGO_PASSWORD'),
    host=os.getenv('MONGO_HOST'),
    port=int(os.getenv('MONGO_PORT')),
    db_name=os.getenv('MONGO_DBNAME'),
    auth_src=os.getenv('MONGO_AUTH_SOURCE'),
    col=os.getenv('MONGO_COLLECTION'),
)

# TODO: Change how the Database object is created with a if __name__ == "__main__";
# Otherwise it should be created where it's needed not here in this module
