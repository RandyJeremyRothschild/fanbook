from pymongo import MongoClient

client = MongoClient('mongodb+srv://RJTP:randy.kun06@cluster0.j79tyse.mongodb.net/?retryWrites=true&w=majority')

db = client.dbRJTP

db.book.delete_one({'rating': 10})