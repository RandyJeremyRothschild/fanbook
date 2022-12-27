from pymongo import MongoClient

client = MongoClient('mongodb+srv://RJTP:randy.kun06@cluster0.j79tyse.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

doc = {
    'name': 'bob',
    'age': 27
}

db.users.insert_one(doc)