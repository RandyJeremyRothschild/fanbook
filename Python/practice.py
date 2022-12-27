from pymongo import MongoClient

client = MongoClient('mongodb+srv://RJTP:randy.kun06@cluster0.j79tyse.mongodb.net/?retryWrites=true&w=majority')

db = client.dbRJTP

user = db.users.find_one({'name': 'bobby'})
print(user)