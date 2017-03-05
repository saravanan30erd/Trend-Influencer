from flask import Flask, render_template
from pymongo import MongoClient, DESCENDING
from pymongo.errors import ConnectionFailure
# -*- coding: utf-8 -*-

# Flask
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


# MongoDB connection
def connect_db():
    uri = 'mongodb://db/influencer'
    client = MongoClient(uri)
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure:
        print 'MongoDB server not available'
    else:
        return client

client = connect_db()
if client != None:
    db = client.get_default_database()


@app.route('/')
def index():
    results =  db['influencers'].find({}, {'_id':0, 'screen_name':1, 'Name':1, 'Description':1}).sort('Followers', DESCENDING).limit(50)
    chennai = db['trends'].find({'location': 'Chennai'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    India = db['trends'].find({'location': 'India'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Delhi = db['trends'].find({'location': 'Delhi'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Bangalore = db['trends'].find({'location': 'Bangalore'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Mumbai = db['trends'].find({'location': 'Mumbai'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Kolkata = db['trends'].find({'location': 'Kolkata'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Pune = db['trends'].find({'location': 'Pune'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Amritsar = db['trends'].find({'location': 'Amritsar'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Srinagar = db['trends'].find({'location': 'Srinagar'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Hyderabad = db['trends'].find({'location': 'Hyderabad'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Ranchi = db['trends'].find({'location': 'Ranchi'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    Jaipur = db['trends'].find({'location': 'Jaipur'}, {'_id': 0}).sort('Followers', DESCENDING).limit(10)
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
