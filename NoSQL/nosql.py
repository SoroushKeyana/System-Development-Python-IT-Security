import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client.get_database('school')

db.student.insert_one({"name": 'Qasem', "age": 31, "rank": 2})



