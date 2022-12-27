from pymongo import MongoClient

client = MongoClient('mongodb+srv://RJTP:randy.kun06@cluster0.j79tyse.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

db.books.update_one(
    {'title': 'The Fisherman and the Fish'}, 
    {'$set': {'author': 'Jimmy Kim'}}
)