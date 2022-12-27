from pymongo import MongoClient

client = MongoClient('mongodb+srv://RJTP:randy.kun06@cluster0.j79tyse.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

db.books.insert_one({
    'title': 'Harry Potter', 
    'author': 'J.K Rowling', 
    'rating': 90
})

db.books.insert_one({
    'title': 'The Fisherman and the Fish',
    'author': 'Joseph Choi', 
    'rating': 10
})

db.books.insert_one({
    'title': 'Fire in the Water',
    'author': 'Some Dude', 
    'rating': 57
})