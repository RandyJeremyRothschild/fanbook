from pymongo import MongoClient

client = MongoClient('mongodb+srv://RJTP:randy.kun06@cluster0.j79tyse.mongodb.net/?retryWrites=true&w=majority')

db = client.dbRJTP

movie = db.movies.find_one({'movie': 'The Matrix'})

print(movie['rating'])