from pymongo import MongoClient
from pymongo.errors import ConnectionFailure



def connect_db():
    uri = 'mongodb://db/influencer'
    client = MongoClient(uri)
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure:
        return 404
    else:
        return client

def update_document(collection, document, filters):
    client = connect_db()
    if client != 404:
        try:
            db = client.get_default_database()
            collection = db[collection]
            collection.replace_one(filters, document, upsert=True)
        except Exception, e:
            print str(e)
    else:
        print 'MongoDB server not available'
    
if __name__ == '__main__':
    update_document('test', {'test' : True}, {'_id' : 2})
